import streamlit as st
import os
import tempfile
from utils.model_generator import ModelGenerator

def main():
    st.title("Photo/Text to 3D Model Generator")
    st.write("Upload an image or enter a text prompt to generate a 3D model")
    
    # Create tabs for different input types
    tab1, tab2 = st.tabs(["Photo Input", "Text Input"])
    
    model_generator = ModelGenerator()
    output_dir = os.path.join(os.getcwd(), "output")
    os.makedirs(output_dir, exist_ok=True)
    
    with tab1:
        st.header("Generate 3D Model from Photo")
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
        
        if uploaded_file is not None:
            # Display the uploaded image
            st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
            
            # Process when button is clicked
            if st.button("Generate 3D Model from Image"):
                with st.spinner("Generating 3D model..."):
                    # Save uploaded file to temp location
                    with tempfile.NamedTemporaryFile(delete=False, suffix='.jpg') as tmp_file:
                        tmp_file.write(uploaded_file.getvalue())
                        img_path = tmp_file.name
                    
                    # Generate output path
                    output_path = os.path.join(output_dir, "image_model.obj")
                    
                    # Generate the model
                    try:
                        mesh = model_generator.generate_from_image(img_path, output_path)
                        
                        # Display the visualization
                        fig = model_generator.visualize_mesh(mesh)
                        st.pyplot(fig)
                        
                        # Provide download link
                        with open(output_path, 'rb') as file:
                            st.download_button(
                                label="Download 3D Model (.obj)",
                                data=file,
                                file_name="image_model.obj",
                                mime="model/obj"
                            )
                        
                        st.success("3D model generated successfully!")
                    except Exception as e:
                        st.error(f"Error generating model: {str(e)}")
                    
                    # Clean up
                    os.unlink(img_path)
    
    with tab2:
        st.header("Generate 3D Model from Text")
        text_prompt = st.text_input("Enter a description:", placeholder="Example: A small toy car")
        
        if st.button("Generate 3D Model from Text") and text_prompt:
            with st.spinner("Generating 3D model..."):
                # Generate output path
                output_path = os.path.join(output_dir, "text_model.obj")
                
                # Generate the model
                try:
                    mesh = model_generator.generate_from_text(text_prompt, output_path)
                    
                    # Display the visualization
                    fig = model_generator.visualize_mesh(mesh)
                    st.pyplot(fig)
                    
                    # Provide download link
                    with open(output_path, 'rb') as file:
                        st.download_button(
                            label="Download 3D Model (.obj)",
                            data=file,
                            file_name="text_model.obj",
                            mime="model/obj"
                        )
                    
                    st.success("3D model generated successfully!")
                except Exception as e:
                    st.error(f"Error generating model: {str(e)}")

if __name__ == "__main__":
    main()