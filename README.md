# Photo/Text to 3D Model Generator

This prototype accepts either a **photo** or **text prompt** and generates a simple **3D model (.obj format)** that can be visualized and downloaded.



## 🚀 Features

- **Dual Input**: Supports both photo and text inputs
- **Image Processing**: Background removal and preprocessing for uploaded photos
- **Text Processing**: Enhances text prompts to generate suitable 3D representations
- **3D Generation**: Produces basic 3D shapes based on input
- **Visualization**: Displays an interactive 3D preview
- **Export**: Download 3D models in `.obj` format for printing or editing



## 🛠 Installation

1. **Clone the repository**:
 
   git clone https://github.com/JyotikaJayani-08/Image_To_3D.git
   cd Image-To-3D


2. **Create and activate a virtual environment**:

   ```bash
    python -m venv venv
    source venv/bin/activate        # On Windows: venv\Scripts\activate
   ```

3. **Upgrade pip and tools**:

   ```bash
   pip install --upgrade pip setuptools wheel
   ```

4. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

   If you face installation issues:

   ```bash
   pip install --no-cache-dir -r requirements.txt
   ```

---

## 💡 Usage

1. **Run the app**:

   ```bash
   streamlit run app.py
   ```

2. **Open your browser** at the address shown in the terminal (typically [http://localhost:8501](http://localhost:8501)).

3. **Choose input mode**:

   * **Photo Input**: Upload a `.jpg` or `.png` image.
   * **Text Input**: Enter a description (e.g., `"A small sphere"`).

4. **Generate and Download**:

   * Click **Generate 3D Model**
   * Wait for processing
   * View the result and download the `.obj` file
  
 ## 📸 Demo Screenshots & Video
 
## 🔘 Text-to-3D Example



Input: "A sphere"


Output:


<img width="620" alt="image" src="https://github.com/user-attachments/assets/0426f735-4e1d-4c27-83bb-916be24dad04" />

Input : "A cylinder "

Output :

<img width="588" alt="image" src="https://github.com/user-attachments/assets/f7499dd8-d71e-4867-927a-5202843d3a25" />



## 🔘 Photo-to-3D Example


Input: Uploaded image

<img width="652" alt="image" src="https://github.com/user-attachments/assets/3616cdc4-226a-4b58-ac1e-e71532cc4e90" />



Output: 

<img width="602" alt="image" src="https://github.com/user-attachments/assets/f1a51969-0522-4d09-afcd-0d3c85bfab64" />


  ## ▶ Demo Video


https://github.com/user-attachments/assets/eb2997ee-96ed-4ae3-9ac0-8378043ad4aa







## 📚 Libraries Used

* [**Streamlit**](https://streamlit.io/) – Web UI framework
* [**OpenCV**](https://opencv.org/) & [**PIL**](https://pillow.readthedocs.io/) – Image handling
* [**Trimesh**](https://trimsh.org/) – 3D mesh generation and export
* [**NumPy**](https://numpy.org/) – Numerical computing
* [**Matplotlib**](https://matplotlib.org/) – 3D plotting
* [**PyTorch**](https://pytorch.org/) & [**TorchVision**](https://pytorch.org/vision/stable/index.html) – Deep learning (optional)



## 🧠 Thought Process

### Approach

1. **Dual Input Handling**:

   * Developed separate pipelines for text and image processing.

2. **Image Processing**:

   * Basic background removal using OpenCV’s GrabCut (U2Net suggested for real-world use).
   * Resized and normalized inputs.

3. **Text Prompt Parsing**:

   * Enhanced prompts and mapped to simple 3D shapes.
   * Special case recognition (e.g., "car", "cube", "ball").

4. **3D Shape Generation**:

   * Used Trimesh to build primitive shapes based on input.
   * Placeholder logic for more complex future integrations (e.g., Point-E, Shape-E).

5. **Visualization & Export**:

   * Displayed using Matplotlib 3D tools.
   * .obj export enabled via Trimesh and Streamlit download button.



## ⚠ Limitations & Future Work

* **Current Output**: Only basic 3D shapes (cube, sphere, etc.)
* **Speed**: Optimized for simplicity, not real-time performance
* **Enhancements**:

  * Texture and color mapping
  * Advanced shape synthesis using deep models
  * Output in other formats (.stl, .glb, .fbx)
  * Better 3D interactivity (e.g., rotation, lighting controls)



## 📌 Notes

This prototype is a demonstration of the **workflow and architecture** for a future AI-powered 3D model generator. For production-grade usage, integration with advanced models like **Point-E**, **Shap-E**, or **DreamFusion** is recommended.



## 📷 Example Use Case

> Enter: `"A small tree"` → Output: A basic 3D cylinder with branches approximation
> Upload: `tree.jpg` → Output: Preprocessed silhouette converted to primitive shape





