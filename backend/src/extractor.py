import pytesseract
import utils
import os
import sys
import cv2
import numpy as np
import io
from PyPDF2 import PdfReader
from PIL import Image
import base64
import re
from parser_patient_details import PatientDetailsParser
from parser_prescription import PrescriptionParser
import json

# Get Tesseract path from environment variable if available, otherwise use default
DEFAULT_TESSERACT_PATH = r"C:/Program Files/Tesseract-OCR/tesseract.exe"
TESSERACT_ENGINE_PATH = os.environ.get("TESSERACT_PATH", DEFAULT_TESSERACT_PATH)

# Flag to track if Tesseract is available
TESSERACT_AVAILABLE = False

# Configure pytesseract with fallback
try:
    pytesseract.pytesseract.tesseract_cmd = TESSERACT_ENGINE_PATH
    # Test if Tesseract is actually working
    test_img = np.zeros((100, 100), dtype=np.uint8)
    pytesseract.image_to_string(test_img)
    TESSERACT_AVAILABLE = True
    print(f"Tesseract OCR 5.5.0 is available at: {TESSERACT_ENGINE_PATH}")
except Exception as e:
    print(f"Warning: Tesseract OCR is not available: {e}")
    print("Using fallback mode without OCR. Text extraction will be limited.")

def convert_pdf_to_images(file_path):
    """Convert PDF to images using PyPDF2 and PIL"""
    images = []
    try:
        # Open the PDF file
        with open(file_path, "rb") as file:
            pdf = PdfReader(file)
            
            # Iterate through each page
            for page_num in range(len(pdf.pages)):
                page = pdf.pages[page_num]
                
                # Check if the page has images
                if page.images:
                    # Extract images directly from the page
                    for image in page.images:
                        img = Image.open(io.BytesIO(image.data))
                        # Convert PIL Image to numpy array for OpenCV processing
                        images.append(np.array(img))
                else:
                    # If no images found, try to extract from XObject
                    xObject = page['/Resources']['/XObject'].get_object() if '/XObject' in page['/Resources'] else {}
                    for obj in xObject:
                        if xObject[obj]['/Subtype'] == '/Image':
                            data = xObject[obj].get_data()
                            img = Image.open(io.BytesIO(data))
                            images.append(np.array(img))
    
    except Exception as e:
        print(f"Error converting PDF to images: {e}")
        # If PyPDF2 extraction fails, try a fallback method
        try:
            # Use PIL to open the PDF directly (works for some PDFs)
            img = Image.open(file_path)
            images = [np.array(img)]
        except:
            pass
    
    # If no images were extracted, create a blank image with error message
    if not images:
        # Create a blank white image with error message
        img = np.ones((800, 600, 3), dtype=np.uint8) * 255
        cv2.putText(img, "Could not extract images from PDF", (50, 400), 
                   cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
        images = [img]
    
    return images

def load_image_file(file_path):
    """Load image file (jpg, png, etc.)"""
    try:
        img = cv2.imread(file_path)
        if img is None:
            # Try with PIL if OpenCV fails
            img = np.array(Image.open(file_path))
        return [img]
    except Exception as e:
        print(f"Error loading image file: {e}")
        # Create a blank image with error message
        img = np.ones((800, 600, 3), dtype=np.uint8) * 255
        cv2.putText(img, f"Error loading image: {str(e)}", (50, 400), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
        return [img]

def extract_text_without_ocr(file_path, file_format):
    """Extract text from PDF without using OCR (fallback method)"""
    extracted_data = {}
    
    try:
        # For PDFs, try to extract text directly
        if file_path.lower().endswith('.pdf'):
            with open(file_path, "rb") as file:
                pdf = PdfReader(file)
                text = ""
                for page in pdf.pages:
                    text += page.extract_text() or ""
                
                # If we got some text, try to parse it
                if text:
                    if file_format == "prescription":
                        extracted_data = PrescriptionParser(text).parse()
                    elif file_format == "patient_details":
                        extracted_data = PatientDetailsParser(text).parse()
                    
                    # If we got some data, return it
                    if any(extracted_data.values()):
                        return extracted_data
        
        # If we couldn't extract meaningful data, return dummy data based on format
        if file_format == "prescription":
            extracted_data = {
                "patient_name": "John Doe (OCR unavailable)",
                "patient_address": "123 Main St (OCR unavailable)",
                "medicines": "Medicine information requires OCR",
                "directions": "Directions require OCR",
                "refill": "1 (default)"
            }
        elif file_format == "patient_details":
            extracted_data = {
                "patient_name": "John Doe (OCR unavailable)",
                "phone_no": "123-456-7890 (OCR unavailable)",
                "vaccination_status": "Unknown (OCR unavailable)",
                "medical_problems": "Information requires OCR",
                "has_insurance": "Unknown (OCR unavailable)"
            }
        
        return extracted_data
    
    except Exception as e:
        print(f"Error in extract_text_without_ocr: {e}")
        # Return empty dictionary with error message
        return {"error": f"Failed to extract text: {str(e)}"}

def extract(file_path, file_format):
    try:
        # Determine file type based on extension
        file_ext = os.path.splitext(file_path)[1].lower()
        
        # Load the appropriate file type
        if file_ext == '.pdf':
            images = convert_pdf_to_images(file_path)
        elif file_ext in ['.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.tif']:
            images = load_image_file(file_path)
        else:
            return {"error": f"Unsupported file format: {file_ext}"}
        
        # Create debug directory if it doesn't exist
        debug_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "debug")
        os.makedirs(debug_dir, exist_ok=True)
        
        # Save original image for debugging
        if images and len(images) > 0:
            first_image = images[0]
            debug_image_path = os.path.join(debug_dir, "original_image.png")
            cv2.imwrite(debug_image_path, first_image)
            print(f"Saved original image to {debug_image_path}")
        
        # Extract text using OCR
        extracted_text = ""
        
        for idx, img in enumerate(images):
            # Preprocess the image
            processed_img = utils.preprocess_image(img)
            
            # Save processed image for debugging
            debug_processed_path = os.path.join(debug_dir, f"processed_image_{idx}.png")
            cv2.imwrite(debug_processed_path, processed_img)
            print(f"Saved processed image to {debug_processed_path}")
            
            # Try different OCR configurations for best results
            text_psm6 = pytesseract.image_to_string(
                processed_img,
                lang="eng",
                config='--psm 6 --oem 3'  # Single block of text, LSTM engine
            )
            
            text_psm4 = pytesseract.image_to_string(
                processed_img,
                lang="eng",
                config='--psm 4 --oem 3'  # Assume single column of text, LSTM engine
            )
            
            # Use the longer text as it likely contains more information
            page_text = text_psm6 if len(text_psm6) > len(text_psm4) else text_psm4
            extracted_text += page_text + "\n\n"
        
        # Save extracted text for debugging
        debug_text_path = os.path.join(debug_dir, "extracted_text.txt")
        with open(debug_text_path, "w", encoding="utf-8") as f:
            f.write(extracted_text)
        print(f"Saved extracted text to {debug_text_path}")
        
        # Parse the extracted text based on the document format
        if file_format == "prescription":
            parser = PrescriptionParser(extracted_text)
            extracted_data = parser.parse()
            
            # Add AI analysis using SmolDocling
            try:
                from smoldocling_analyzer import SmolDoclingAnalyzer
                analyzer = SmolDoclingAnalyzer()
                if analyzer.is_model_available():
                    analysis = analyzer.analyze_prescription(extracted_text)
                    extracted_data["ai_analysis"] = analysis
                    print("Added AI analysis to extracted data")
                else:
                    print("SmolDocling analyzer not available, skipping AI analysis")
            except Exception as e:
                print(f"Error performing AI analysis: {str(e)}")
                
        elif file_format == "patient_details":
            parser = PatientDetailsParser(extracted_text)
            extracted_data = parser.parse()
            
            # Add AI analysis for patient details
            try:
                from smoldocling_analyzer import SmolDoclingAnalyzer
                analyzer = SmolDoclingAnalyzer()
                if analyzer.is_model_available():
                    analysis = analyzer.analyze_patient_details(extracted_text)
                    extracted_data["ai_analysis"] = analysis
                    print("Added AI analysis to extracted data")
                else:
                    print("SmolDocling analyzer not available, skipping AI analysis")
            except Exception as e:
                print(f"Error performing AI analysis: {str(e)}")
        else:
            return {"error": f"Unsupported document format: {file_format}"}
        
        # Save parsed data for debugging
        debug_json_path = os.path.join(debug_dir, "parsed_data.json")
        with open(debug_json_path, "w", encoding="utf-8") as f:
            json.dump(extracted_data, f, indent=2)
        print(f"Saved parsed data to {debug_json_path}")
        
        return extracted_data
    
    except Exception as e:
        print(f"Error in extract: {e}")
        import traceback
        traceback.print_exc()
        return {"error": f"Failed to extract data: {str(e)}"}

if __name__ == "__main__":
    # Test the extraction
    data = extract("backend/resources/patient_details/pd_1.pdf", "patient_details")
    print(data)