import os
import time
import webbrowser
import subprocess
import disclaimer
import commands

def dushigub():
    os.system('clear')
    disclaimer.DISCLAIMER()
    os.system('chmod +x *')
    os.system('clear')
    print('Для помощи пиши help!')
    time.sleep(3)
    os.system('clear')
    time.sleep(0.3)
    commands.welcome()

dushigub()
