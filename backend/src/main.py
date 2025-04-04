from fastapi import FastAPI, Form, UploadFile, File, HTTPException
import uvicorn
from extractor import extract
import uuid
import os
import shutil

app = FastAPI()

# Ensure uploads directory exists
UPLOAD_DIR = "backend/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/extract_from_doc")
def extract_from_doc(
    file: UploadFile = File(...),
    file_format: str = Form(...)
):
    # Validate file format
    if file_format not in ["prescription", "patient_details"]:
        raise HTTPException(status_code=400, detail=f"Invalid file format: {file_format}. Must be 'prescription' or 'patient_details'")
    
    # Validate file type
    file_extension = os.path.splitext(file.filename)[1].lower()
    supported_extensions = ['.pdf', '.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.tif']
    
    if file_extension not in supported_extensions:
        raise HTTPException(
            status_code=400, 
            detail=f"Unsupported file type: {file_extension}. Supported types: {', '.join(supported_extensions)}"
        )
    
    # Read file content
    try:
        content = file.file.read()
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error reading file: {str(e)}")
    
    # Generate unique filename
    unique_filename = str(uuid.uuid4())
    FILE_PATH = os.path.join(UPLOAD_DIR, f"{unique_filename}{file_extension}")
    
    # Write file to disk
    try:
        with open(FILE_PATH, "wb") as f:
            f.write(content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error saving file: {str(e)}")

    # Process file
    try:
        # Check if Tesseract is available
        tesseract_path = os.environ.get("TESSERACT_PATH", "C:/Program Files/Tesseract-OCR/tesseract.exe")
        if not os.path.exists(tesseract_path):
            raise HTTPException(
                status_code=500,
                detail=f"Tesseract OCR not found at {tesseract_path}. Please ensure Tesseract 5.5.0 is installed."
            )
            
        data = extract(FILE_PATH, file_format)
    except Exception as e:
        # Clean up file
        if os.path.exists(FILE_PATH):
            os.remove(FILE_PATH)
        
        # Provide more helpful error message for common issues
        error_message = str(e)
        if "tesseract" in error_message.lower():
            error_message = "Tesseract OCR 5.5.0 is not installed or it's not in your PATH. Please ensure it's installed at C:/Program Files/Tesseract-OCR/tesseract.exe or set the TESSERACT_PATH environment variable."
        
        raise HTTPException(status_code=500, detail=f"Error processing file: {error_message}")

    # Clean up file
    if os.path.exists(FILE_PATH):
        os.remove(FILE_PATH)

    return data

@app.get("/")
def read_root():
    return {"message": "Medical Data Extraction API is running. Use POST /extract_from_doc to process documents."}

@app.get("/health")
def health_check():
    """Health check endpoint"""
    tesseract_path = os.environ.get("TESSERACT_PATH", "C:/Program Files/Tesseract-OCR/tesseract.exe")
    tesseract_available = os.path.exists(tesseract_path)
    
    return {
        "status": "healthy",
        "tesseract_available": tesseract_available,
        "tesseract_path": tesseract_path
    }

if __name__ == "__main__":
    print("Starting Medical Data Extraction Backend...")
    print("API will be available at http://127.0.0.1:8000")
    print("Supported file formats: PDF, JPG, PNG, and other image formats")
    print("Supported document types: prescription, patient_details")
    
    # Check Tesseract availability
    tesseract_path = os.environ.get("TESSERACT_PATH", "C:/Program Files/Tesseract-OCR/tesseract.exe")
    if os.path.exists(tesseract_path):
        print(f" Tesseract OCR 5.5.0 found at: {tesseract_path}")
    else:
        print(f" Warning: Tesseract OCR not found at {tesseract_path}")
        print("Please ensure Tesseract 5.5.0 is installed for full OCR functionality.")
    
    uvicorn.run(app, host="127.0.0.1", port=8000)