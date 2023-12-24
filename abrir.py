import subprocess

# lista dos navegadores para abrir
browsers = [
    ['C:\\Program Files\\Mozilla Firefox\\firefox.exe', 'https://www.google.com/'], 
    ['C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe', 'https://www.google.com/'],
    ['C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe', 'https://www.google.com/'],
    ['C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe', 'https://www.google.com/'],
    ['C:\\Users\\user123\\AppData\\Local\\Vivaldi\\Application\\vivaldi.exe', 'https://www.google.com/'],
    ['C:\\Users\\user123\\AppData\\Local\\Programs\\Opera\\opera.exe', 'https://www.google.com/'],
    ['C:\\Users\\user123\\AppData\\Local\\Programs\\Opera GX\\launcher.exe', 'https://www.google.com/'],
    ['C:\\Program Files\\AVAST Software\\Browser\\Application\\AvastBrowser.exe', 'https://www.google.com/'],
    ['C:\\Program Files\\Waterfox\\waterfox.exe', 'https://www.google.com/'],
    ['C:\\Users\\user123\\AppData\\Local\\Google\\Chrome SxS\\Application\\chrome.exe', 'https://www.google.com/'],

]

# abre todos os navegadores
for browser in browsers:
    subprocess.Popen(browser)

# abre todos os perfis criados no chrome
subprocess.Popen(['C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe', '--profile-directory=Default', 'https://www.google.com/'])
subprocess.Popen(['C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe', '--profile-directory=Profile 1', 'https://www.google.com/'])
subprocess.Popen(['C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe', '--profile-directory=Profile 2', 'https://www.google.com/'])
subprocess.Popen(['C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe', '--profile-directory=Profile 3', 'https://www.google.com/'])
subprocess.Popen(['C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe', '--profile-directory=Profile 4', 'https://www.google.com/'])
subprocess.Popen(['C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe', '--profile-directory=Profile 5', 'https://www.google.com/'])
subprocess.Popen(['C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe', '--profile-directory=Profile 6', 'https://www.google.com/'])
subprocess.Popen(['C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe', '--profile-directory=Profile 7', 'https://www.google.com/'])
subprocess.Popen(['C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe', '--profile-directory=Profile 8', 'https://www.google.com/'])
subprocess.Popen(['C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe', '--profile-directory=Profile 9', 'https://www.google.com/'])
subprocess.Popen(['C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe', '--profile-directory=Profile 10', 'https://www.google.com/'])
subprocess.Popen(['C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe', '--profile-directory=Profile 11', 'https://www.google.com/'])
subprocess.Popen(['C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe', '--profile-directory=Profile 12', 'https://www.google.com/'])
