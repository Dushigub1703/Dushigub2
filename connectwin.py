import os
import time
import subprocess

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   HEADER = '\033[95m'
   OKBLUE = '\033[94m'
   OKGREEN = '\033[92m'
   WARNING = '\033[93m'
   FAIL = '\033[91m'

os.system('clear')

try:
    conf = open('windows/config/config.txt', 'r')
    print(color.FAIL+conf.read()+color.END)
    time.sleep(0.5)
    connect=input(color.DARKCYAN+'Какой файл *.rc будем использовать? '+color.END)
    print(color.DARKCYAN+'Подключаемся к '+connect+color.END)
    os.system('./msfconsole -r windows/config/'+connect)
except:
    time.sleep(0.7)
    os.system('clear')
    print(color.FAIL+'Выход...'+color.END)
