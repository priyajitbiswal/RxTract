@echo off
echo Medical Data Extraction - Complete Setup
echo =======================================
echo.

REM Check if Python is installed
python --version > nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Python is not installed or not in PATH.
    echo Please install Python 3.8 or higher and try again.
    pause
    exit /b 1
)

echo Step 1: Creating virtual environment...
python -m venv venv
if %ERRORLEVEL% NEQ 0 (
    echo Failed to create virtual environment.
    echo Please make sure you have the venv module available.
    pause
    exit /b 1
)

echo.
echo Step 2: Activating virtual environment...
call venv\Scripts\activate.bat
if %ERRORLEVEL% NEQ 0 (
    echo Failed to activate virtual environment.
    pause
    exit /b 1
)

echo.
echo Step 3: Installing Python dependencies...
pip install -r requirements.txt
if %ERRORLEVEL% NEQ 0 (
    echo Failed to install dependencies.
    pause
    exit /b 1
)

echo.
echo Step 4: Setting up external dependencies...
echo.
echo You need to install Poppler and Tesseract OCR for this project.
echo.
echo Options:
echo 1. Run the dependency setup script (downloads and sets up dependencies)
echo 2. Skip (if you already have Poppler and Tesseract installed)
echo.
set /p choice="Enter your choice (1/2): "

if "%choice%"=="1" (
    call setup_dependencies.bat
) else (
    echo Skipping external dependency setup.
    echo Please make sure Poppler and Tesseract are installed and environment variables are set.
)

echo.
echo Step 5: Checking environment...
python check_environment.py

echo.
echo Setup completed!
echo.
echo To run the application:
echo 1. Start the backend server: run_backend.bat
echo 2. In a new terminal, start the frontend: run_frontend.bat
echo.
echo For more detailed instructions, see SETUP.md
echo.
pause
