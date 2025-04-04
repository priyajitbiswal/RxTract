import numpy as np
import cv2

def preprocess_image(img):
    """
    Enhanced image preprocessing for Tesseract 5.5.0
    This function applies several image processing techniques to improve OCR accuracy
    """
    # Convert to grayscale if needed
    if len(img.shape) == 3:
        gray = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2GRAY)
    else:
        gray = img
    
    # Resize the image (larger images generally give better OCR results)
    resized = cv2.resize(gray, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR)
    
    # Apply bilateral filter to remove noise while preserving edges
    denoised = cv2.bilateralFilter(resized, 9, 75, 75)
    
    # Apply adaptive thresholding to handle different lighting conditions
    processed_image = cv2.adaptiveThreshold(
        denoised,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        65,  # block size (optimized for medical documents)
        13   # constant (optimized for medical documents)
    )
    
    # Apply morphological operations to remove small noise
    kernel = np.ones((1, 1), np.uint8)
    processed_image = cv2.morphologyEx(processed_image, cv2.MORPH_CLOSE, kernel)
    
    return processed_image

def enhance_image_for_display(img):
    """
    Enhance image for display purposes (not for OCR)
    """
    # Convert to grayscale if needed
    if len(img.shape) == 3:
        gray = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2GRAY)
    else:
        gray = img
    
    # Apply CLAHE (Contrast Limited Adaptive Histogram Equalization)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    enhanced = clahe.apply(gray)
    
    return enhanced