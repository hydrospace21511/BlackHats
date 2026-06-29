@echo off
setlocal enabledelayedexpansion
title DarkHats Launcher
color 0A

echo ========================================
echo        Verifying Python 3.13...
echo ========================================
echo.

py --version > temp_py_version.txt 2>&1
findstr /C:"Python 3.13" temp_py_version.txt >nul

if %errorlevel%==0 (
    echo [OK] Python 3.13 detected!
    del temp_py_version.txt
    goto check_update
)

echo [!] Python 3.13 not found.
echo.
echo Installing Python 3.13 Launcher...
powershell -Command "Invoke-WebRequest -Uri https://www.python.org/ftp/python/3.13.0/python-3.13.0-amd64.exe -OutFile python_installer.exe"

echo.
echo Installing Python 3.13...
start /wait python_installer.exe /quiet InstallAllUsers=1 PrependPath=1

del python_installer.exe
del temp_py_version.txt
echo [OK] Python downloaded succefully.
echo.

:check_update
echo ========================================
echo          Verifying Updates...
echo ========================================
echo.

set "REPO_API=https://api.github.com/repos/hydrospace21511/DarkHats/commits/main"
set "ZIP_URL=https://github.com/hydrospace21511/DarkHats/archive/refs/heads/main.zip"
set "LOCAL_HASH_FILE=version.txt"

powershell -Command "$Response = Invoke-RestMethod -Uri '!REPO_API!' -UseBasicParsing; $Response.sha | Out-File -FilePath remote_hash.txt -Encoding ascii" 2>nul

if not exist remote_hash.txt (
    echo [AVISO] Wasn't able to found update in GitHub. Being offline...
    goto find_files
)

set /p REMOTE_HASH=<remote_hash.txt
set LOCAL_HASH=none

if exist "!LOCAL_HASH_FILE!" (
    set /p LOCAL_HASH=<!LOCAL_HASH_FILE!
)


if "!REMOTE_HASH!"=="!LOCAL_HASH!" (
    echo [OK] The game its updated!
    del remote_hash.txt
    goto find_files
)

echo [!] New version found. Downloading from GitHub...
powershell -Command "Invoke-WebRequest -Uri '!ZIP_URL!' -OutFile update.zip"

echo Extracting new archives...
powershell -Command "Expand-Archive -Path update.zip -DestinationPath . -Force"

echo !REMOTE_HASH!> "!LOCAL_HASH_FILE!"
del remote_hash.txt
del update.zip

echo [OK] Updated downloaded!
echo.

:find_files
echo ========================================
echo       Searching game archives...
echo ========================================
echo.

set "REQ_PATH="
set "MAIN_PATH="

for /f "delims=" %%a in ('dir /b /s "%~dp0requirements.txt" 2^>nul') do set "REQ_PATH=%%a"
for /f "delims=" %%a in ('dir /b /s "%~dp0Main.py" 2^>nul') do set "MAIN_PATH=%%a"

if not defined REQ_PATH (
    echo [AVISO] requirements.txt not found in any folder. skipping dependencies...
) else (
    echo Installing dependencies from: !REQ_PATH!
    py -m pip install --upgrade pip >nul 2>&1
    py -m pip install -r "!REQ_PATH!" >nul 2>&1
    echo [OK] Dependencies downloaded.
)

if not defined MAIN_PATH (
    echo.
    echo [ERRO] Main.py not found! The game can't be launched.
    echo Verify if the archives were correctly extracted.
    pause
    exit /b
)

echo.
echo ========================================
echo             Starting game...
echo ========================================
echo.

for %%F in ("!MAIN_PATH!") do cd /d "%%~dpF"
py "!MAIN_PATH!"

pause