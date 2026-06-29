@echo off
REM 

REM 
python -m pip install --upgrade pip
python -m pip install pyinstaller windows-curses

REM 
SET "PROJECT_ROOT=%~dp0"
SET "ICON_PATH=%PROJECT_ROOT%darkhats_icon.ico"

REM 
IF NOT EXIST "%ICON_PATH%" (
    echo Icon not found at %ICON_PATH%.
)

REM 
pyinstaller ^
  --onefile ^
  --name DarkHatsGame ^
  --icon "%ICON_PATH%" ^
  --add-data "Game\SOUNDS;SOUNDS" ^
  --add-data "Game\Main\DataStore.json;Game\Main" ^
  "%PROJECT_ROOT%Game\Main\Main.py"

REM 
mkdir "%PROJECT_ROOT%dist" 2>nul
copy "dist\DarkHatsGame.exe" "%PROJECT_ROOT%dist\" >nul

echo Build complete. Executable located at %PROJECT_ROOT%dist\DarkHatsGame.exe
pause
