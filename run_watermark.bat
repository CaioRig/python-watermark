@echo off
setlocal

REM Run from the folder where this .bat file is located
cd /d "%~dp0"

set "PYTHON_EXE=.venv\Scripts\python.exe"

if not exist "%PYTHON_EXE%" (
    echo.
    echo Virtual environment not found at %PYTHON_EXE%.
    echo Create it first with: python -m venv .venv
    pause
    exit /b 1
)

"%PYTHON_EXE%" main.py
if errorlevel 1 (
    echo.
    echo Script failed with exit code %errorlevel%.
)

pause
