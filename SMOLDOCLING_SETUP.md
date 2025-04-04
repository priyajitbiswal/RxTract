# 🩺📄 Medical Data Extraction with SmolDocling AI

This guide will help you set up the enhanced Medical Data Extraction system with SmolDocling AI integration for advanced analysis of medical documents.

## 🧰 Prerequisites

1. Python 3.8+ installed
2. Tesseract OCR 5.5.0 installed
3. Git (optional, for cloning the repository)

## 🔧 Installation Steps

### 1. Set Up Environment

```bash
# Create and activate a virtual environment (recommended)
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/Mac:
# source venv/bin/activate
```

### 2. Install Dependencies

```bash
# Install all required packages
pip install -r requirements.txt
```

### 3. Install Tesseract OCR (if not already installed)

#### Windows:
- Run the `install_tesseract.bat` script included in this repository
- Or download from: https://github.com/UB-Mannheim/tesseract/wiki
- Add Tesseract to your system PATH (e.g., `C:\Program Files\Tesseract-OCR`)

#### Mac:
```bash
brew install tesseract
```

#### Linux:
```bash
sudo apt install tesseract-ocr
```

### 4. Verify Tesseract Installation

```bash
tesseract --version
```

This should display the Tesseract version (5.5.0 or later recommended).

## 🚀 Running the Application

### 1. Start the Backend Server

```bash
# Run the backend server
.\run_backend.bat
# Or manually:
# cd backend
# uvicorn src.main:app --reload
```

### 2. Start the Frontend Application

```bash
# In a new terminal window, run the frontend
.\run_frontend.bat
# Or manually:
# cd frontend
# streamlit run app.py
```

### 3. Access the Application

Open your web browser and navigate to:
- http://localhost:8503

## 🧠 SmolDocling AI Features

The SmolDocling integration adds the following AI-powered analysis to your medical documents:

1. **Likely Diagnosis**: AI-suggested potential diagnoses based on prescription content
2. **Recommended Daily Routine**: Personalized activity suggestions based on the medical context
3. **Dietary Recommendations**: Food and nutrition advice aligned with the medical condition
4. **Warnings & Side Effects**: Potential medication side effects and precautions

## 🔍 Testing the AI Features

1. Upload a medical document (prescription or patient details)
2. Select the document type
3. Click "Process Document"
4. View the extracted information alongside AI-powered analysis

## 📋 Troubleshooting

If the AI analysis is not appearing:
1. Check that all dependencies are installed correctly
2. Ensure you have an internet connection (required for the first run to download the model)
3. Look for error messages in the terminal running the backend server
4. Check the debug folder for extracted text and processing information

## 📝 Notes

- The first time you run the application with SmolDocling, it will download the model (approximately 500MB)
- Processing time may be longer for the first few documents as the model loads
- For optimal results, ensure your documents are clear and well-lit

## 🔄 Updates and Maintenance

To update the application:
1. Pull the latest changes from the repository
2. Install any new dependencies: `pip install -r requirements.txt`
3. Restart both the backend and frontend servers

## 📚 Additional Resources

- [Tesseract Documentation](https://tesseract-ocr.github.io/)
- [SmolDocling Model Information](https://huggingface.co/ds4sd/SmolDocling-256M-preview)
- [Transformers Library Documentation](https://huggingface.co/docs/transformers/index)
