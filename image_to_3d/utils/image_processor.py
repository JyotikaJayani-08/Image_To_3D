import cv2
import numpy as np
from PIL import Image
import torch
from torchvision import transforms

class ImageProcessor:
    def __init__(self):
        # Initialize any models needed for image processing
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        # For background removal, we could use more sophisticated models like U2Net
        # but for simplicity let's use basic OpenCV techniques
        
    def preprocess_image(self, image_path):
        """Preprocess the input image for 3D generation."""
        image = cv2.imread(image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        # Resize for model input
        image = cv2.resize(image, (224, 224))
        
        # Basic normalization
        image = image / 255.0
        
        return image
    
    def remove_background(self, image_path):
        """Simple background removal using GrabCut algorithm."""
        img = cv2.imread(image_path)
        mask = np.zeros(img.shape[:2], np.uint8)
        
        # Use a rectangle to initialize GrabCut
        bgdModel = np.zeros((1, 65), np.float64)
        fgdModel = np.zeros((1, 65), np.float64)
        
        # Set rectangle (start_x, start_y, width, height)
        rect = (50, 50, img.shape[1] - 100, img.shape[0] - 100)
        
        # Apply GrabCut
        cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
        
        # Create mask where sure and likely backgrounds are 0, otherwise 1
        mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
        
        # Multiply image with the mask to get foreground
        img_fg = img * mask2[:, :, np.newaxis]
        
        # Convert to PIL Image for further processing
        pil_img = Image.fromarray(cv2.cvtColor(img_fg, cv2.COLOR_BGR2RGB))
        
        return pil_img