import streamlit as st
import requests
import json
import os
import sys
import io
from PIL import Image
import numpy as np
from PyPDF2 import PdfReader
import base64
import time

# Set page config must be the first Streamlit command
st.set_page_config(
    page_title="Medical Data Extraction",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Backend URL
BACKEND_URL = "http://127.0.0.1:8000/extract_from_doc"

def is_venv():
    """Check if running in a virtual environment"""
    return (hasattr(sys, 'real_prefix') or
            (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix))

def convert_pdf_to_image(pdf_bytes):
    """Convert PDF bytes to image using PyPDF2 instead of pdf2image"""
    try:
        # Read PDF from bytes
        pdf = PdfReader(io.BytesIO(pdf_bytes))
        
        if len(pdf.pages) == 0:
            st.error("The PDF file appears to be empty.")
            return None
        
        # Try to extract image from the first page
        page = pdf.pages[0]
        
        # Check if the page has images
        if page.images:
            # Get the first image
            image = page.images[0]
            img = Image.open(io.BytesIO(image.data))
            return img
        else:
            # If no images found, try to extract from XObject
            xObject = page['/Resources']['/XObject'].get_object() if '/XObject' in page['/Resources'] else {}
            for obj in xObject:
                if xObject[obj]['/Subtype'] == '/Image':
                    data = xObject[obj].get_data()
                    img = Image.open(io.BytesIO(data))
                    return img
        
        # If we couldn't extract an image, create a blank one with a message
        st.warning("Could not extract image from PDF. Using a placeholder image.")
        img = Image.new('RGB', (800, 600), color='white')
        return img
        
    except Exception as e:
        st.error(f"Error converting PDF: {str(e)}")
        st.info("If you're seeing this error, the PDF might be in a format that's difficult to process.")
        return None

def check_tesseract():
    """Check if Tesseract is available and return its path"""
    tesseract_path = os.environ.get("TESSERACT_PATH", "C:/Program Files/Tesseract-OCR/tesseract.exe")
    if os.path.exists(tesseract_path):
        return True, tesseract_path
    return False, tesseract_path

def display_prescription_data(data):
    st.subheader("Extracted Prescription Information")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Patient Information")
        st.write(f"**Name:** {data.get('patient_name', 'Not found')}")
        st.write(f"**Address:** {data.get('patient_address', 'Not found')}")
        
        st.markdown("#### Medication")
        st.write(f"**Medicines:** {data.get('medicines', 'Not found')}")
        st.write(f"**Directions:** {data.get('directions', 'Not found')}")
        st.write(f"**Refill:** {data.get('refill', 'Not found')}")
    
    # Display AI analysis if available
    if 'ai_analysis' in data:
        with col2:
            st.markdown("#### 🧠 AI Analysis")
            analysis = data['ai_analysis']
            
            with st.container(border=True):
                st.markdown("##### 🔍 Likely Diagnosis")
                st.write(analysis.get('diagnosis', 'Not available'))
                
                st.markdown("##### 📅 Recommended Routine")
                st.write(analysis.get('routine', 'Not available'))
                
                st.markdown("##### 🍎 Dietary Recommendations")
                st.write(analysis.get('diet', 'Not available'))
                
                st.markdown("##### ⚠️ Warnings & Side Effects")
                st.write(analysis.get('warnings', 'Not available'))

def display_patient_details(data):
    st.subheader("Extracted Patient Details")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Patient Information")
        st.write(f"**Name:** {data.get('patient_name', 'Not found')}")
        st.write(f"**Phone:** {data.get('phone_no', 'Not found')}")
        st.write(f"**Vaccination Status:** {data.get('vaccination_status', 'Not found')}")
        st.write(f"**Insurance:** {data.get('has_insurance', 'Not found')}")
        
        st.markdown("#### Medical Information")
        st.write(f"**Medical Problems:** {data.get('medical_problems', 'Not found')}")
    
    # Display AI analysis if available
    if 'ai_analysis' in data:
        with col2:
            st.markdown("#### 🧠 AI Analysis")
            analysis = data['ai_analysis']
            
            with st.container(border=True):
                st.markdown("##### 🔍 Likely Diagnosis")
                st.write(analysis.get('diagnosis', 'Not available'))
                
                st.markdown("##### 📅 Recommended Routine")
                st.write(analysis.get('routine', 'Not available'))
                
                st.markdown("##### 🍎 Dietary Recommendations")
                st.write(analysis.get('diet', 'Not available'))
                
                st.markdown("##### ⚠️ Warnings & Side Effects")
                st.write(analysis.get('warnings', 'Not available'))

def main():
    st.title("Medical Data Extraction 🏥")
    st.markdown("### Extract information from medical documents using OCR technology")
    
    # Sidebar with environment information
    st.sidebar.title("About")
    st.sidebar.info("This application extracts information from medical documents using OCR technology.")
    
    # Check Tesseract availability
    tesseract_available, tesseract_path = check_tesseract()
    
    # Display Tesseract status prominently
    if tesseract_available:
        st.sidebar.success(f"✅ Tesseract OCR 5.5.0 is available")
    else:
        st.sidebar.error(f"❌ Tesseract OCR 5.5.0 is not found")
        st.sidebar.warning(f"Expected path: {tesseract_path}")
        st.sidebar.info("Please install Tesseract 5.5.0 for full OCR functionality")
    
    show_env_info = st.sidebar.checkbox("Show Environment Info")
    if show_env_info:
        st.sidebar.subheader("Environment")
        st.sidebar.write(f"Running in virtual environment: {is_venv()}")
        st.sidebar.write(f"Python version: {sys.version}")
        st.sidebar.write(f"Working directory: {os.getcwd()}")
        
        if tesseract_available:
            st.sidebar.write(f"Tesseract path: {tesseract_path}")
    
    # Setup instructions in sidebar
    with st.sidebar.expander("Setup Instructions"):
        st.markdown("""
        ### Requirements
        - Python 3.8+
        - Tesseract OCR 5.5.0 installed
        
        ### Environment Setup
        1. Create a virtual environment:
           ```
           python -m venv venv
           ```
        2. Activate the virtual environment:
           ```
           venv\\Scripts\\activate  # Windows
           source venv/bin/activate  # macOS/Linux
           ```
        3. Install dependencies:
           ```
           pip install -r requirements.txt
           ```
        4. Set environment variables:
           ```
           set TESSERACT_PATH=C:\\Program Files\\Tesseract-OCR\\tesseract.exe  # Windows
           export TESSERACT_PATH=/path/to/tesseract  # macOS/Linux
           ```
        """)
    
    # File upload
    st.subheader("Upload Document")
    
    # Create columns for better layout
    col1, col2 = st.columns([2, 1])
    
    with col1:
        file = st.file_uploader("Choose a file", type=["pdf", "jpg", "jpeg", "png"])
    
    with col2:
        # Document type selection
        doc_type = st.selectbox(
            "Select Document Type",
            ["prescription", "patient_details"]
        )
    
    if file:
        try:
            # Display the uploaded file
            col_preview, col_results = st.columns(2)
            
            with col_preview:
                st.subheader("Document Preview")
                
                # Handle different file types
                file_ext = os.path.splitext(file.name)[1].lower()
                
                if file_ext == '.pdf':
                    # For PDFs, try to convert to image for display
                    image = convert_pdf_to_image(file.getvalue())
                    if image:
                        st.image(image, use_container_width=True)
                    else:
                        st.info("PDF preview not available. You can still process the document.")
                else:
                    # For images, display directly
                    image = Image.open(file)
                    st.image(image, use_container_width=True)
            
            # Process document button
            process_button = st.button("Process Document", type="primary")
            
            if process_button:
                with st.spinner("Processing document..."):
                    # Show progress
                    progress_bar = st.progress(0)
                    for i in range(100):
                        # Update progress bar
                        progress_bar.progress(i + 1)
                        time.sleep(0.01)
                    
                    # Prepare the file for the API request
                    files = {"file": (file.name, file.getvalue(), f"application/{file_ext[1:]}" if file_ext == '.pdf' else f"image/{file_ext[1:]}")}
                    form_data = {"file_format": doc_type}
                    
                    try:
                        # Make API request to backend
                        response = requests.post(BACKEND_URL, files=files, data=form_data)
                        
                        # Handle response
                        if response.status_code == 200:
                            with col_results:
                                extracted_data = response.json()
                                if doc_type == "prescription":
                                    display_prescription_data(extracted_data)
                                elif doc_type == "patient_details":
                                    display_patient_details(extracted_data)
                                st.success("✅ Document processed successfully!")
                        else:
                            error_msg = f"Server returned status code {response.status_code}"
                            try:
                                error_detail = response.json().get("detail", "Unknown error")
                                error_msg += f" - {error_detail}"
                            except:
                                pass
                            st.error(error_msg)
                            
                            # Provide helpful guidance for common errors
                            if "Tesseract" in error_msg:
                                st.warning("This error is related to Tesseract OCR.")
                                st.info("Please make sure Tesseract 5.5.0 is installed and the TESSERACT_PATH environment variable is set correctly.")
                    except requests.exceptions.ConnectionError:
                        st.error("Could not connect to the backend server. Please make sure it's running.")
                        st.info("Run the backend server with: `python backend/src/main.py`")
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
        except Exception as e:
            st.error(f"Error: {str(e)}")
            st.info("Please make sure you've uploaded a valid file.")

# Add information about the project
with st.expander("About this application"):
    st.markdown("""
    This application extracts information from medical documents using OCR technology.
    
    **Supported document types:**
    - Prescriptions
    - Patient Details
    
    **Supported file formats:**
    - PDF files
    - Image files (JPG, PNG)
    
    **Requirements:**
    - PyPDF2 (for PDF processing)
    - Tesseract OCR 5.5.0 (required for text extraction)
    
    For more information, check the [GitHub repository](https://github.com/abhijeetk597/medical-data-extraction).
    """)

# Add environment setup instructions
with st.expander("Environment Setup"):
    st.markdown("""
    ### Setting up the environment
    
    1. Create a virtual environment:
       ```
       python -m venv venv
       ```
    
    2. Activate the virtual environment:
       - Windows: `venv\\Scripts\\activate`
       - Linux/Mac: `source venv/bin/activate`
    
    3. Install dependencies:
       ```
       pip install -r requirements.txt
       ```
    
    4. Install Tesseract OCR 5.5.0:
       - Download from: [Tesseract GitHub](https://github.com/UB-Mannheim/tesseract/wiki)
       - Install to the default location: `C:\\Program Files\\Tesseract-OCR`
    
    5. Set environment variables for Tesseract path:
       - Windows: 
         ```
         set TESSERACT_PATH=C:\\Program Files\\Tesseract-OCR\\tesseract.exe
         ```
       - Linux/Mac:
         ```
         export TESSERACT_PATH=/path/to/tesseract
         ```
    
    6. Run the backend server:
       ```
       python backend/src/main.py
       ```
    
    7. Run the frontend app:
       ```
       streamlit run frontend/app.py
       """
    )

if __name__ == "__main__":
    main()