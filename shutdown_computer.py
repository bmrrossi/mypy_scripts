import os

choice = input('Shutdown now? (y/n)')

if choice == 'y':
    os.system('shutdown /s /t /1')
