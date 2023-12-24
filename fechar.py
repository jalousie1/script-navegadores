import subprocess

#Lista dos processos dos navegadores para fechar
browsers = [
    'firefox.exe', 
    'msedge.exe',
    'chrome.exe',
    'brave.exe',
    'vivaldi.exe',
    'opera.exe',
    'AvastBrowser.exe',
    'waterfox.exe',
]

# Fecha todos os navegadores
for browser in browsers:
    subprocess.run(f'taskkill /IM {browser} /F', shell=True)