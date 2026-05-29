@echo off
title DarkHats
color 0A

echo ========================================
echo        Checking Python 3.13...
echo ========================================
echo.

py --version > temp_py_version.txt 2>&1

findstr /C:"Python 3.13" temp_py_version.txt >nul

if %errorlevel%==0 (
echo Python 3.13 detected!
goto install_requirements
)

echo Python 3.13 not found.
echo.
echo Downloading Python 3.13 installer...
echo.

powershell -Command "Invoke-WebRequest -Uri https://www.python.org/ftp/python/3.13.0/python-3.13.0-amd64.exe -OutFile python_installer.exe"

echo.
echo Installing Python 3.13...
echo.

start /wait python_installer.exe /quiet InstallAllUsers=1 PrependPath=1

echo.
echo Python installation completed.
echo.

:install_requirements

echo ========================================
echo      Installing Requirements...
echo ========================================
echo.

py -m pip install --upgrade pip
py -m pip install -r requirements.txt

echo.
echo ========================================
echo          Starting Game...
echo ========================================
echo.

cd /d "%~dp0.."
py Game\Main\Menu.py

pause
