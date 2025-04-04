# Medical Data Extraction - Setup Guide

This guide will help you set up and run the Medical Data Extraction project using a virtual environment.

## Prerequisites

- Python 3.8 or higher
- Windows, macOS, or Linux operating system
- Internet connection for downloading dependencies

## Setup Instructions

### 1. Create and Activate Virtual Environment

First, create a virtual environment to isolate the project dependencies:

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 2. Install Python Dependencies

With the virtual environment activated, install the required Python packages:

```bash
pip install -r requirements.txt
```

### 3. Install External Dependencies

This project requires Tesseract OCR for text recognition:

#### Tesseract OCR
Tesseract is required for OCR functionality. You can:
- Use the provided `setup_dependencies.bat` script on Windows
- Or download and install manually:
  - Windows: Download from [UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki)
  - macOS: `brew install tesseract`
  - Linux: `sudo apt-get install tesseract-ocr`

### 4. Set Environment Variables

Set the following environment variable to point to your Tesseract installation:

```bash
# Windows
set TESSERACT_PATH=C:\Program Files\Tesseract-OCR\tesseract.exe

# macOS/Linux
export TESSERACT_PATH=/usr/bin/tesseract
```

## Running the Application

### Using Batch Files (Windows)

We've provided batch files to simplify running the application:

1. Start the backend server:
   ```
   run_backend.bat
   ```

2. In a new terminal, start the frontend:
   ```
   run_frontend.bat
   ```

### Manual Execution

1. Activate the virtual environment:
   ```bash
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

2. Start the backend server:
   ```bash
   python backend/src/main.py
   ```

3. In a new terminal with the virtual environment activated, start the frontend:
   ```bash
   streamlit run frontend/app.py
   ```

## Troubleshooting

### Common Issues

1. **OCR Error**:
   - Ensure Tesseract is installed correctly
   - Verify the TESSERACT_PATH environment variable is set correctly

2. **Package Import Errors**:
   - Ensure you're running the application from the activated virtual environment
   - Try reinstalling the dependencies: `pip install -r requirements.txt`

3. **Backend Connection Error**:
   - Ensure the backend server is running on http://127.0.0.1:8000
   - Check for any firewall or network issues

### Getting Help

If you encounter issues not covered here, please check the original project documentation or create an issue on the project repository.
