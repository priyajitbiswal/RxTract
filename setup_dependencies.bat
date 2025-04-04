@echo off
echo Medical Data Extraction - Dependencies Setup
echo ===========================================
echo.
echo This script will help you set up the external dependencies required for the project.
echo.

REM Create directories for dependencies
if not exist "dependencies" mkdir dependencies
cd dependencies

echo Downloading Tesseract installer...
powershell -Command "& {[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; Invoke-WebRequest -Uri 'https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-5.3.3.20231005.exe' -OutFile 'tesseract-installer.exe'}"

echo.
echo Please run the Tesseract installer manually and follow the installation instructions.
echo After installation, set the TESSERACT_PATH environment variable to point to the tesseract.exe file.
echo For example: setx TESSERACT_PATH "C:\Program Files\Tesseract-OCR\tesseract.exe"
echo.

cd ..

echo Dependencies setup completed!
echo.
echo Next steps:
echo 1. Install Tesseract OCR by running: dependencies\tesseract-installer.exe
echo 2. After installation, restart your command prompt
echo 3. Run the application using run_backend.bat and run_frontend.bat
echo.
pause
