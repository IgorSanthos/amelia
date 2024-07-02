import pyautogui as pa
import time
import os
#from pywinauto import application
try:
    # Pressiona a tecla Win para abrir o menu Iniciar
    time.sleep(5)
    os.system('start chrome')
    time.sleep(5)
    # Digita "chrome" para buscar o Google Chrome
    pa.write('https://web.contmatic.com.br/login')
    pa.press('enter')
    time.sleep(5)
    # Pressiona Enter para abrir o Chrome
    pa.press('enter')
    pa.write('https://web.contmatic.com.br/login')
    pa.press('enter')
    time.sleep(5)
    pa.press('tab')
    pa.press('tab')
    pa.press('tab')
    time.sleep(5)
    pa.press('enter')
    print ('Abri o remoto da phoenix')
    time.sleep(5)
    pa.press('tab')
    pa.press('G5')
    pa.press('enter')
    time.sleep(5)
    print ('ABRINDO G5...')


















except Exception as e:
    print(e)
# pa.PAUSE = 5



# pa.press('ctrl+A')
# pa.write('01072024')