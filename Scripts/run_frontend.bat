@echo off
echo Starting RxTract Frontend...
echo.

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Run the Streamlit app
streamlit run frontend\app.py

REM If the app exits, deactivate the virtual environment
call venv\Scripts\deactivate.bat
