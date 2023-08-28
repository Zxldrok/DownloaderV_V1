@echo off
setlocal
set "SCRIPT_DIR=%~dp0"
set "PYTHON_EXE=%SCRIPT_DIR%runtime\python.exe"
set "SCRIPT_FILE=%SCRIPT_DIR%gui.py"
"%PYTHON_EXE%" "%SCRIPT_FILE%"
endlocal
