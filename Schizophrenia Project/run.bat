@echo off
REM Schizophrenia Detection System - Run Script for Windows

echo Starting Schizophrenia Detection System...

REM Check if virtual environment exists
if not exist "venv" (
    echo Virtual environment not found. Creating...
    python -m venv venv
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install/update dependencies
echo Installing dependencies...
pip install -r requirements.txt

REM Create necessary directories
if not exist "logs" mkdir logs
if not exist "models" mkdir models

REM Check if models exist
if not exist "models\scaler.pkl" (
    echo Models not found. Please train models first:
    echo   python train_all_models.py
    exit /b 1
)

REM Run the application
echo Starting Flask application...
python app.py

pause
