@echo off
setlocal
cd /d "%~dp0\.."
py -m PyInstaller --noconfirm --clean --onefile --windowed --name Updater updater\main.py
if errorlevel 1 (
  echo Failed to build Updater.exe
  exit /b 1
)
echo Build complete: dist\Updater.exe
endlocal
