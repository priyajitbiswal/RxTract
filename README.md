# RxTract - AI-Powered Medical Data Extractor

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-green.svg)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28.1-red.svg)](https://streamlit.io/)
[![Tesseract](https://img.shields.io/badge/Tesseract-5.5.0-orange.svg)](https://github.com/tesseract-ocr/tesseract)
[![SmolDocling](https://img.shields.io/badge/SmolDocling-AI%20Enhanced-purple.svg)](https://huggingface.co/docs/transformers)

> **🏆 Spectrum'25 VIT Hackathon Winner Project**

An intelligent OCR-powered medical document processing system enhanced with AI analysis capabilities. RxTract transforms unstructured medical documents (prescriptions and patient records) into structured, actionable data using advanced computer vision, natural language processing, and AI-driven insights.

## 🚀 Demo

### Application Interface

![Medical Data Extraction Interface](4.png)
_Interactive Streamlit frontend with document upload, real-time processing, and AI-enhanced analysis_

### AI-Enhanced Results

![Extraction Results with AI Analysis](5.png)
_Complete medical data extraction with structured output and AI-powered insights including diagnosis suggestions, dietary recommendations, and treatment guidance_

## 📋 Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [AI Integration](#ai-integration)
- [Technology Stack](#technology-stack)
- [System Architecture](#system-architecture)
- [Installation & Setup](#installation--setup)
- [Usage Guide](#usage-guide)
- [API Documentation](#api-documentation)
- [Project Structure](#project-structure)
- [Development](#development)
- [Contributing](#contributing)
- [Troubleshooting](#troubleshooting)

## 🔍 Overview

RxTract addresses the critical need for automated medical document processing in healthcare institutions, insurance companies, and medical practices. By combining traditional OCR with cutting-edge AI analysis, it provides comprehensive document understanding beyond simple text extraction.

### The Problem

- **Manual Processing**: Healthcare workers spend hours manually extracting data from medical documents
- **Error-Prone**: Human data entry introduces inconsistencies and mistakes
- **Lack of Insights**: Traditional OCR only extracts text without understanding medical context
- **Scalability Issues**: Cannot handle large volumes of documents efficiently

### Our Solution

- **Intelligent OCR**: Tesseract 5.5.0 with custom preprocessing for medical documents
- **AI-Powered Analysis**: SmolDocling integration for medical context understanding
- **Structured Output**: JSON-formatted data ready for healthcare systems integration
- **Real-time Processing**: FastAPI backend with Streamlit frontend for immediate results
- **Multi-format Support**: PDF, PNG, JPG, and other common medical document formats

## ✨ Key Features

### Core Capabilities

- **📄 Multi-Document Support**: Prescriptions and patient medical records
- **🔄 Format Flexibility**: PDF, PNG, JPG, JPEG, BMP, TIFF support
- **🧠 AI-Enhanced Analysis**: Medical insights beyond text extraction
- **⚡ Real-time Processing**: Sub-5 second processing for most documents
- **🛡️ Error Recovery**: Robust fallback mechanisms for challenging documents
- **🔍 Debug Mode**: Complete processing pipeline visibility

### Advanced Features

- **📊 Structured Data Output**: Standardized JSON format for system integration
- **🔄 Batch Processing**: Handle multiple documents simultaneously
- **🌐 Cross-Platform**: Windows, Linux, and macOS support
- **🏥 Medical Context**: Understanding of medication interactions and recommendations
- **📈 Confidence Scoring**: Reliability metrics for extracted data

### Supported Document Types

#### 1. Prescription Documents

- **Extracted Fields**: Patient name, address, medications, dosages, directions, refill information
- **AI Analysis**: Drug interactions, side effects, dietary recommendations, treatment adherence tips

#### 2. Patient Medical Records

- **Extracted Fields**: Personal information, medical history, contact details, treatment records
- **AI Analysis**: Risk factors, care recommendations, follow-up suggestions, health insights

## 🧠 AI Integration

RxTract incorporates advanced AI capabilities through SmolDocling integration:

### Medical Intelligence Features

- **🩺 Likely Diagnosis**: AI-suggested potential diagnoses based on prescription patterns
- **💊 Drug Analysis**: Medication interaction warnings and side effect alerts
- **🥗 Dietary Guidance**: Nutrition recommendations aligned with medical conditions
- **📅 Treatment Plans**: Personalized daily routines and care instructions
- **⚠️ Risk Assessment**: Health risk identification and preventive measures

### Implementation

- **Rule-Based Fallback**: Continues operation even without model availability
- **Medical Knowledge Base**: Comprehensive medication database with 50+ common drugs
- **Contextual Processing**: Document type-specific analysis algorithms
- **Confidence Metrics**: Reliability scoring for AI-generated insights

## 🛠️ Technology Stack

### Backend Infrastructure

- **FastAPI 0.104.1**: High-performance async web framework
- **Python 3.8+**: Core programming language with type hints
- **Uvicorn 0.23.2**: ASGI server for production deployment

### OCR & Image Processing

- **Tesseract OCR 5.5.0**: Google's state-of-the-art OCR engine
- **pytesseract 0.3.10**: Python wrapper for Tesseract
- **OpenCV 4.8.1.78**: Computer vision and image preprocessing
- **PIL/Pillow 10.1.0**: Image manipulation and format support
- **pdf2image 1.16.3**: PDF to image conversion

### AI & Machine Learning

- **SmolDocling**: Document understanding transformer model
- **Transformers**: Hugging Face NLP library
- **PyTorch**: Deep learning framework support

### Frontend & Interface

- **Streamlit 1.28.1**: Interactive web application framework
- **Requests 2.31.0**: HTTP client for API communication
- **PyPDF2**: PDF processing and text extraction fallback

### Development Tools

- **pytest**: Comprehensive testing framework
- **python-dotenv**: Environment variable management
- **NumPy 1.26.1**: Numerical computing support

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    RxTract Medical Data Extractor               │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Streamlit     │    │   FastAPI       │    │   Tesseract     │
│   Frontend      │◄──►│   Backend       │◄──►│   OCR Engine    │
│   (Port 8501)   │    │   (Port 8000)   │    │   (5.5.0)       │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         │                       ▼                       │
         │              ┌─────────────────┐              │
         │              │ SmolDocling AI  │              │
         │              │   Analyzer      │              │
         │              └─────────────────┘              │
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│  File Upload    │    │  Image          │    │  Text           │
│  Interface      │    │  Preprocessing  │    │  Extraction     │
│  • Drag & Drop  │    │  • Thresholding │    │  • OCR Engine   │
│  • Multi-format │    │  • Noise Remove │    │  • Fallback     │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                │
                                ▼
                       ┌───────────────────┐
                       │  Medical AI       │
                       │  Analysis         │
                       │  • Diagnosis      │ 
                       │  • Interactions   │
                       │  • Recommendations│
                       └───────────────────┘
                                │
                                ▼
                       ┌─────────────────┐
                       │  Regex Parsing  │
                       │  & Structuring  │
                       │  • Field Extract│
                       │  • Validation   │
                       └─────────────────┘
                                │
                                ▼
                       ┌─────────────────┐
                       │  Enhanced JSON  │
                       │  Output + AI    │
                       │  Insights       │
                       └─────────────────┘
```

### Processing Pipeline

1. **Document Upload** → Streamlit interface with drag-and-drop support
2. **Format Validation** → Automatic file type detection and validation
3. **Image Conversion** → PDF to image conversion using pdf2image/PyPDF2
4. **Preprocessing** → OpenCV adaptive thresholding and noise reduction
5. **OCR Extraction** → Tesseract text extraction with confidence scoring
6. **AI Analysis** → SmolDocling medical context analysis and recommendations
7. **Structured Parsing** → Regex-based field extraction using document-specific patterns
8. **Output Generation** → Combined traditional + AI data in JSON format
9. **Debug Logging** → Complete pipeline visibility for troubleshooting

## 🔧 Installation & Setup

### Prerequisites

- **Python 3.8+** with pip package manager
- **Git** for repository cloning
- **Tesseract OCR 5.5.0** for text extraction
- **4GB+ RAM** for optimal performance

### Quick Start (Windows)

```bash
# Clone repository
git clone https://github.com/priyajitbiswal/RxTract.git
cd RxTract

# Run automated setup
setup.bat

# Verify installation
python check_environment.py
```

### Manual Installation

#### Step 1: Repository Setup

```bash
git clone https://github.com/priyajitbiswal/RxTract.git
cd RxTract
```

#### Step 2: Virtual Environment

```bash
# Create and activate virtual environment
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate
```

#### Step 3: Python Dependencies

```bash
# Install all required packages
pip install -r requirements.txt
```

#### Step 4: Tesseract OCR Installation

##### Windows

```bash
# Option 1: Use provided installer
install_tesseract.bat

# Option 2: Manual download
# Download from: https://github.com/UB-Mannheim/tesseract/wiki
# Install to: C:\Program Files\Tesseract-OCR
```

##### Linux (Ubuntu/Debian)

```bash
sudo apt-get update
sudo apt-get install tesseract-ocr
sudo apt-get install poppler-utils
```

##### macOS

```bash
brew install tesseract
brew install poppler
```

#### Step 5: Environment Configuration

```bash
# Windows
set TESSERACT_PATH=C:\Program Files\Tesseract-OCR\tesseract.exe

# Linux/macOS (usually auto-detected)
export TESSERACT_PATH=/usr/bin/tesseract
```

#### Step 6: Verification

```bash
# Check all dependencies
python check_environment.py

# Expected output:
# ✅ Python 3.8+ detected
# ✅ Virtual environment active
# ✅ Tesseract OCR 5.5.0 available
# ✅ All Python packages installed
# ✅ SmolDocling components ready
```

## 🚦 Usage Guide

### Quick Start

#### Option 1: Automated Scripts (Windows)

```bash
# Terminal 1: Start backend server
run_backend.bat

# Terminal 2: Start frontend application
run_frontend.bat
```

#### Option 2: Manual Execution

```bash
# Activate virtual environment
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/macOS

# Terminal 1: Backend server
cd backend/src
python main.py

# Terminal 2: Frontend application
cd frontend
streamlit run app.py
```

### Application Access

- **🌐 Frontend Interface**: http://localhost:8501
- **🔧 Backend API**: http://localhost:8000
- **📚 API Documentation**: http://localhost:8000/docs
- **💚 Health Check**: http://localhost:8000/health

### Using the Web Interface

1. **📁 Upload Document**: Drag and drop or browse for medical documents
2. **📋 Select Type**: Choose "prescription" or "patient_details"
3. **⚡ Process**: Click "Process Document" for extraction
4. **👁️ View Results**: See structured data with AI insights
5. **💾 Export**: Download JSON results for integration

### Supported Formats

- **📄 PDF Documents**: .pdf (recommended for medical records)
- **🖼️ Image Formats**: .jpg, .jpeg, .png, .bmp, .tiff, .tif
- **📏 File Size**: Maximum 10MB per document
- **🎯 Quality**: Higher resolution (300+ DPI) yields better results

## 📚 API Documentation

### Core Endpoints

#### POST `/extract_from_doc`

**Primary endpoint for medical document processing**

**Request Parameters:**

- `file`: Binary file upload (multipart/form-data)
  - Supported: PDF, JPG, PNG, BMP, TIFF (max 10MB)
- `file_format`: Document type (form parameter)
  - Values: `"prescription"` or `"patient_details"`

**Example Request:**

```python
import requests

# Process prescription document
with open('prescription.pdf', 'rb') as file:
    response = requests.post(
        'http://localhost:8000/extract_from_doc',
        files={'file': ('prescription.pdf', file, 'application/pdf')},
        data={'file_format': 'prescription'}
    )

result = response.json()
```

**Response Format (Prescription):**

```json
{
  "patient_name": "John Doe",
  "patient_address": "123 Main St, City, State 12345",
  "medicines": "Amoxicillin 500mg\nIbuprofen 200mg",
  "directions": "Take Amoxicillin 3 times daily with food\nTake Ibuprofen as needed for pain",
  "refill": "2 refills remaining",
  "ai_analysis": {
    "likely_diagnosis": ["Bacterial infection", "Inflammatory condition"],
    "recommended_routine": [
      "Take medications with food to reduce stomach irritation",
      "Complete full antibiotic course even if feeling better"
    ],
    "dietary_recommendations": [
      "Increase probiotic intake during antibiotic treatment",
      "Stay well hydrated",
      "Avoid alcohol while on antibiotics"
    ],
    "warnings": [
      "Monitor for allergic reactions to amoxicillin",
      "Do not exceed recommended ibuprofen dosage",
      "Contact doctor if symptoms worsen"
    ]
  }
}
```

#### GET `/health`

**System health and dependency status check**

**Response:**

```json
{
  "status": "healthy",
  "tesseract_available": true,
  "tesseract_path": "C:/Program Files/Tesseract-OCR/tesseract.exe"
}
```

#### GET `/`

**API status information**

**Response:**

```json
{
  "message": "Medical Data Extraction API is running. Use POST /extract_from_doc to process documents."
}
```

### Error Handling

**HTTP Status Codes:**

- `200`: Successful processing
- `400`: Bad request (invalid file/format)
- `500`: Server error (Tesseract missing, processing failure)

**Error Response:**

```json
{
  "detail": "Specific error description with guidance"
}
```

**Common Errors:**

- `"Invalid file format: {format}. Must be 'prescription' or 'patient_details'"`
- `"Tesseract OCR 5.5.0 is not installed or not in PATH"`
- `"Unsupported file type: {extension}"`

## 📁 Project Structure

```
RxTract/
├── 📄 README.md                    # Project documentation
├── 📄 requirements.txt             # Python dependencies
├── 📄 4.png                        # Demo - Application interface
├── 📄 5.png                        # Demo - AI analysis results
├── 📄 check_environment.py         # Dependency verification
├── 📄 SETUP.md                     # Detailed setup guide
├── 📄 SMOLDOCLING_SETUP.md         # AI integration guide
│
├── 📁 backend/                     # FastAPI backend server
│   ├── 📁 src/                     # Core source code
│   │   ├── 📄 main.py              # FastAPI application & endpoints
│   │   ├── 📄 extractor.py         # OCR processing & AI integration
│   │   ├── 📄 parser_prescription.py    # Prescription regex parser
│   │   ├── 📄 parser_patient_details.py # Patient record parser
│   │   ├── 📄 parser_generic.py    # Base parser class
│   │   ├── 📄 smoldocling_analyzer.py   # AI medical analysis
│   │   ├── 📄 utils.py             # Utility functions
│   │   └── 📄 __init__.py
│   │
│   ├── 📁 tests/                   # Unit tests
│   │   └── 📄 test_prescription_parser.py
│   │
│   ├── 📁 resources/               # Sample medical documents
│   │   ├── 📁 patient_details/
│   │   │   ├── 📄 pd_1.pdf         # Sample patient record
│   │   │   └── 📄 pd_2.pdf
│   │   └── 📁 prescription/
│   │       ├── 📄 pre_1.pdf        # Sample prescription
│   │       └── 📄 pre_2.pdf
│   │
│   ├── 📁 uploads/                 # Temporary processing files
│   └── 📁 debug/                   # Debug outputs & logs
│       ├── 📄 extracted_text.txt   # OCR extracted text
│       ├── 📄 parsed_data.json     # Structured output
│       └── 📄 processed_image_*.png # Image processing steps
│
├── 📁 frontend/                    # Streamlit web application
│   └── 📄 app.py                   # Main Streamlit interface
│
├── 📁 Notebooks/                   # Jupyter development notebooks
│   ├── 📄 01_prescription_parser.ipynb    # Prescription processing
│   ├── 📄 02_patient_details_parser.ipynb # Patient record processing
│   └── 📄 03_RegEx.ipynb           # Regex pattern development
│
├── 📁 reference/                   # Documentation & research
│   └── 📄 tesseract_paper_by_google.pdf
│
├── 📁 venv/                        # Python virtual environment
│
└── 📁 Scripts/                     # Windows batch files
    ├── 📄 setup.bat                # Complete setup automation
    ├── 📄 install_tesseract.bat    # Tesseract installer
    ├── 📄 run_backend.bat          # Backend server launcher
    └── 📄 run_frontend.bat         # Frontend launcher
```

### Key Components

#### Backend Core (`backend/src/`)

- **`main.py`**: FastAPI server with endpoint definitions, file handling, and error management
- **`extractor.py`**: Complete processing pipeline - image preprocessing, OCR execution, AI integration
- **`parser_*.py`**: Document-specific parsing with regex patterns for field extraction
- **`smoldocling_analyzer.py`**: AI-powered medical analysis providing diagnosis and recommendations

#### Processing Flow

1. **Document Upload** → `main.py` validates file and routes to extractor
2. **Image Processing** → `extractor.py` converts PDF and enhances image quality
3. **OCR Extraction** → Tesseract processes image to extract text with confidence scoring
4. **AI Analysis** → SmolDocling provides medical insights and context understanding
5. **Structured Parsing** → Document-specific parsers extract structured fields
6. **JSON Output** → Combined traditional and AI data returned to frontend

## 🧪 Development

### Development Environment Setup

```bash
# Install development dependencies
pip install pytest jupyter black flake8

# Launch Jupyter for notebook development
jupyter notebook

# Navigate to Notebooks/ for interactive development
```

### Running Tests

```bash
# Run all tests with verbose output
pytest backend/tests/ -v

# Run with coverage report
pytest backend/tests/ --cov=backend/src/ --cov-report=html

# Test specific components
python backend/src/extractor.py  # Test extraction pipeline
```

### Code Quality

```bash
# Format code
black backend/src/ frontend/

# Check style
flake8 backend/src/ frontend/

# Type checking (optional)
mypy backend/src/
```

### Adding New Document Types

1. **Create Parser**: `backend/src/parser_<new_type>.py`
2. **Define Patterns**: Implement regex patterns for field extraction
3. **Add Tests**: Create unit tests in `backend/tests/`
4. **Update API**: Add new document type to `main.py`
5. **AI Integration**: Extend SmolDocling analyzer for new type

### Development Notebooks

- **`01_prescription_parser.ipynb`**: Interactive prescription processing development
- **`02_patient_details_parser.ipynb`**: Patient record processing workflows
- **`03_RegEx.ipynb`**: Regex pattern testing and optimization

## 🔧 Troubleshooting

### Common Issues & Solutions

#### ❌ OCR Problems

```bash
# Issue: "Tesseract not found"
# Check installation
tesseract --version

# Set environment variable
export TESSERACT_PATH=/usr/bin/tesseract  # Linux/Mac
set TESSERACT_PATH=C:\Program Files\Tesseract-OCR\tesseract.exe  # Windows

# Reinstall Tesseract
install_tesseract.bat  # Windows
sudo apt-get install tesseract-ocr  # Linux
```

#### ❌ Python Environment Issues

```bash
# Issue: Module not found
# Ensure virtual environment is active
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Reinstall dependencies
pip install -r requirements.txt

# Verify environment
python check_environment.py
```

#### ❌ API Connection Problems

```bash
# Check backend status
curl http://localhost:8000/health

# Verify ports are available
netstat -an | grep 8000

# Check firewall settings for ports 8000 and 8501
```

#### ❌ Performance Issues

- **Memory**: Ensure 4GB+ RAM available
- **Image Quality**: Use 300+ DPI scans for better OCR
- **File Size**: Keep documents under 10MB
- **Debug**: Check `backend/debug/` folder for processing details

#### ❌ AI Analysis Issues

- **First Run**: Model download requires internet (~500MB)
- **Fallback Mode**: System continues without AI if model unavailable
- **Debug Logs**: Check terminal for SmolDocling initialization messages

### Getting Help

1. **Environment Check**: `python check_environment.py`
2. **Debug Logs**: Review terminal output and `backend/debug/` folder
3. **Sample Testing**: Use provided sample documents first
4. **GitHub Issues**: Report bugs with environment details and logs

## 🤝 Contributing

We welcome contributions! Here's how to get started:

### Development Setup

```bash
# Fork and clone
git clone https://github.com/YOUR_USERNAME/RxTract.git
cd RxTract

# Setup development environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows

pip install -r requirements.txt
pip install pytest black flake8 jupyter
```

### Contribution Areas

- **🔍 OCR Enhancement**: Improve preprocessing algorithms and accuracy
- **🤖 AI Integration**: Enhance SmolDocling integration and medical knowledge
- **📄 Document Support**: Add new medical document types (lab reports, discharge summaries)
- **🌐 Frontend**: Improve Streamlit interface and user experience
- **🧪 Testing**: Expand test coverage and add integration tests

### Pull Request Process

1. **Create Branch**: `git checkout -b feature/amazing-feature`
2. **Develop**: Make changes with tests and documentation
3. **Test**: `pytest backend/tests/` and `python check_environment.py`
4. **Format**: `black backend/src/ frontend/`
5. **Commit**: `git commit -m "feat: Add amazing feature"`
6. **Push**: `git push origin feature/amazing-feature`
7. **PR**: Create pull request with clear description

## 🏆 Acknowledgments

### Open Source Technologies

- **[Tesseract OCR](https://github.com/tesseract-ocr/tesseract)** - Google's powerful OCR engine
- **[FastAPI](https://fastapi.tiangolo.com/)** - Modern, fast web framework
- **[Streamlit](https://streamlit.io/)** - Rapid web app development
- **[OpenCV](https://opencv.org/)** - Computer vision library
- **[Hugging Face](https://huggingface.co/)** - Transformers and NLP models

### Research & Community

- **Google Research** - Tesseract OCR development and research
- **VIT University** - Spectrum'25 Hackathon platform
- **Healthcare Professionals** - Domain expertise and feedback
- **Open Source Community** - Continuous inspiration and support

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

**Made with ❤️ for the healthcare community**

_Transforming medical document processing through AI and OCR innovation_

---

For detailed setup instructions, see [SETUP.md](SETUP.md) | For AI integration guide, see [SMOLDOCLING_SETUP.md](SMOLDOCLING_SETUP.md)
