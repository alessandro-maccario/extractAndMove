# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

datas = [('C:/Users/M/AppData/Local/pypoetry/Cache/virtualenvs/extractandmove-tG4lA2PM-py3.12/Lib/site-packages/pypdfium2_raw/pdfium.dll', 'pypdfium2_raw')]

a = Analysis(
    ['app.py'],
    pathex=['C:/solutions/learning_python/extractAndMove/extractandmove'],
    binaries=[('C:/Users/M/AppData/Local/Programs/Python/Python312/python312.dll', 'Python312')], 
	datas=[],
    hiddenimports=['.'],
    hookspath=['.'],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='app.py',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False  # Set to False if you want a windowed app
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='app.py'
)