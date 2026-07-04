python3 -m pip install --upgrade pip
python3 -m pip install pyinstaller windows-curses

PROJECT_ROOT="$(cd "$(dirname "$0")" && pwd)"
ICON_PATH="$PROJECT_ROOT/darkhats_icon.ico"

pyinstaller \
  --onefile \
  --name DarkHatsGame \
  --icon "$ICON_PATH" \
  --add-data "Game/Sounds:Sounds" \
  --add-data "Game/Main/DataStore.json:Game/Main" \
  --add-data "Game/ItemsLib/Items/items.txt:Game/ItemsLib/Items" \
  --add-data "Game/Backup/Admin/HoneyPot.txt:Game/Backup/Admin" \
  "$PROJECT_ROOT/Game/Main/Main.py"

mkdir -p "$PROJECT_ROOT/dist"
cp "dist/DarkHatsGame.exe" "$PROJECT_ROOT/dist/"

echo "Build complete. Executable located at $PROJECT_ROOT/dist/DarkHatsGame.exe"
