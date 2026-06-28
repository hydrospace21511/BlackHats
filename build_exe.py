import os
import sys
import subprocess
import shutil

def install_deps():
    print("=== [1/3] Instalando dependencias do requirements.txt e o PyInstaller ===")
    req_path = os.path.join("Game", "requirements.txt")
    
    try:
        print("Atualizando o pip...")
        subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pip"], check=True)
        
        if os.path.exists(req_path):
            print(f"Instalando pacotes do arquivo: {req_path}...")
            subprocess.run([sys.executable, "-m", "pip", "install", "-r", req_path], check=True)
        else:
            print("AVISO: requirements.txt nao encontrado em Game/. Instalando dependencias basicas...")

        print("Instalando/Atualizando PyInstaller...")
        subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller"], check=True)
        print("[OK] Dependencias instaladas com sucesso!\n")
    except subprocess.CalledProcessError as e:
        print(f"[ERRO] Falha ao instalar dependencias: {e}")
        sys.exit(1)

def generate_spec():
    print("=== [2/3] Gerando arquivo de configuracao do PyInstaller (DarkHats.spec) ===")
    
    spec_content = """# -*- mode: python ; coding: utf-8 -*-

import os
import sys

project_root = os.path.abspath(os.getcwd())

datas = [
    (os.path.join('Game', 'Sounds'), os.path.join('Game', 'Sounds')),
    (os.path.join('Game', 'Main', 'DataStore.json'), os.path.join('Game', 'Main')),
]

optional_files = [
    (os.path.join('Game', 'Backup', 'Admin', 'HoneyPot.txt'), os.path.join('Game', 'Backup', 'Admin')),
    (os.path.join('Game', 'ItemsLib', 'Items', 'items.txt'), os.path.join('Game', 'ItemsLib', 'Items')),
]

for src, dest in optional_files:
    if os.path.exists(os.path.join(project_root, src)):
        datas.append((src, dest))

a = Analysis(
    [os.path.join('Game', 'Main', 'Main.py')],
    pathex=[project_root],
    binaries=[],
    datas=datas,
    hiddenimports=[
        'pygame',
        'pygame-ce',
        'colorama',
        'keyboard',
        'pillow',
        'numpy',
        'pandas',
        'docx',
        'lxml',
        'rich',
        'curses',
    ] + (['windows-curses'] if sys.platform == 'win32' else []),
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=None)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='DarkHats',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=os.path.join(project_root, 'logo.ico') if os.path.exists(os.path.join(project_root, 'logo.ico')) else None,
)
"""
    
    with open("DarkHats.spec", "w", encoding="utf-8") as f:
        f.write(spec_content)
    print("[OK] Arquivo DarkHats.spec gerado com sucesso!\n")

def get_desktop_path():
    home = os.path.expanduser("~")
    candidates = [
        os.path.join(home, "Desktop"),
        os.path.join(home, "Área de Trabalho"),
        os.path.join(home, "OneDrive", "Desktop"),
        os.path.join(home, "OneDrive", "Área de Trabalho"),
        os.path.join(home, "Area de Trabalho"),
    ]
    for path in candidates:
        if os.path.exists(path):
            return path
    return home

def build_exe():
    print("=== [3/3] Iniciando a compilacao com PyInstaller ===")
    
    try:
        print("Executando compilacao...")
        subprocess.run([sys.executable, "-m", "PyInstaller", "DarkHats.spec", "--clean"], check=True)

        ext = ".exe" if os.name == 'nt' else ""
        src_path = os.path.abspath(os.path.join("dist", f"DarkHats{ext}"))

        desktop_dir = get_desktop_path()
        dest_path = os.path.join(desktop_dir, f"DarkHats{ext}")
        
        copiado = False
        if os.path.exists(src_path):
            print(f"Copiando executavel para a Area de Trabalho...")
            try:
                shutil.copy(src_path, dest_path)
                copiado = True
            except Exception as e:
                print(f"[AVISO] Nao foi possivel copiar para a Area de Trabalho: {e}")
                copiado = False
        else:
            copiado = False
            
        print("\n" + "="*70)
        print(" [SUCESSO] Compilacao concluida!")
        print(" O jogo foi instalado e esta pronto para jogar!")
        print(f" -> Local do Executavel: {src_path}")
        if copiado:
            print(f" -> Copiado para a Area de Trabalho: {dest_path}")
            print("    (Agora qualquer pessoa pode abrir o jogo direto pela Area de Trabalho!)")
        print("="*70 + "\n")
    except subprocess.CalledProcessError as e:
        print(f"[ERRO] Ocorreu um erro durante a compilacao: {e}")
        sys.exit(1)

if __name__ == "__main__":
    install_deps()
    generate_spec()
    build_exe()
