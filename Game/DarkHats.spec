# -*- mode: python ; coding: utf-8 -*-

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
