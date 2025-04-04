@echo off
echo Starting Medical Data Extraction Backend Server...
echo.

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Run the backend server
python backend\src\main.py

REM If the server exits, deactivate the virtual environment
call venv\Scripts\deactivate.bat
