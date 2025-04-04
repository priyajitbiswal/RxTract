@echo off
echo ===================================================
echo Medical Data Extraction - Tesseract OCR Installer
echo ===================================================
echo.
echo This script will download and install Tesseract OCR 5.3.1
echo.

set TESSERACT_INSTALLER=tesseract-ocr-w64-setup-5.3.1.20230401.exe
set DOWNLOAD_URL=https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-5.3.1.20230401.exe
set INSTALL_DIR=C:\Program Files\Tesseract-OCR

echo Checking if Tesseract is already installed...
if exist "%INSTALL_DIR%\tesseract.exe" (
    echo Tesseract is already installed at %INSTALL_DIR%
    goto SetEnvVar
)

echo Downloading Tesseract OCR installer...
curl -L -o %TESSERACT_INSTALLER% %DOWNLOAD_URL%

if not exist %TESSERACT_INSTALLER% (
    echo Failed to download Tesseract installer.
    echo Please download it manually from:
    echo https://github.com/UB-Mannheim/tesseract/wiki
    exit /b 1
)

echo Installing Tesseract OCR...
echo Please follow the installation wizard and use the default installation path.
echo.
echo IMPORTANT: Make sure to install to the default location: %INSTALL_DIR%
echo.
pause
start /wait %TESSERACT_INSTALLER% /SILENT /NORESTART

echo Cleaning up...
del %TESSERACT_INSTALLER%

:SetEnvVar
echo Setting TESSERACT_PATH environment variable...
setx TESSERACT_PATH "%INSTALL_DIR%\tesseract.exe"

echo.
echo Installation complete!
echo Tesseract OCR has been installed to: %INSTALL_DIR%
echo TESSERACT_PATH environment variable has been set.
echo.
echo Please restart any command prompts or applications to apply the changes.
echo.
pause
