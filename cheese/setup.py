import PyInstaller.__main__

PyInstaller.__main__.run([
    'client.py',
    '--onefile',
    '--windowed',
    '--add-data="account.csv:."',
    '-n cheese_v1_sun18',
    '--paths=.'
])
