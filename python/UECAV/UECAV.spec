# -*- mode: python -*-

block_cipher = None


a = Analysis(['UECAV.py'],
             pathex=['C:\\Users\\Gabriele\\Documents\\Workspace\\UECAV\\UECAV'],
             binaries=[],
             datas=[('C:\\Users\\Gabriele\\Documents\\Workspace\\UECAV\\UECAV\\Icon.ico', '.'), ('C:\\Users\\Gabriele\\Documents\\Workspace\\UECAV\\UECAV\\Tick.png', '.'), ('C:\\Users\\Gabriele\\Documents\\Workspace\\UECAV\\UECAV\\Cross.png', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='UECAV',
          debug=False,
          strip=False,
          upx=False,
          runtime_tmpdir=None,
          console=False , icon='Icon.ico')
