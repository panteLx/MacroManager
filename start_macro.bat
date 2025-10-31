@echo off
echo Checking Python installation...

where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Python is not installed. Installing Python...
    winget install Python.Python.3.11
    if %errorlevel% neq 0 (
        echo Failed to install Python. Please install Python 3.11 manually from https://www.python.org/downloads/
        pause
        exit /b 1
    )
)

if not exist ".venv" (
    echo Creating virtual environment...
    python -m venv .venv
)

echo Activating virtual environment...
call .venv\Scripts\activate.bat

echo Installing requirements...
python -m pip install -r requirements.txt

echo Starting macro...
python app.py

deactivate
