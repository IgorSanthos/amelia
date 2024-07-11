import pyautogui as pa
import time
import os

try:
    time.sleep(1)
    os.system('start chrome')
    time.sleep(2)
    pa.write('https://web.contmatic.com.br/login')
    pa.press('enter')    # Pressiona Enter para abrir o Chrome
    time.sleep(5)
    pa.press('tab')
    pa.press('tab')
    pa.press('tab')
    time.sleep(5)
    pa.press('enter')
    print ('Abrindo o remoto da phoenix...')

# abrindo G5
    time.sleep(50)
    windows = pa.getWindowsWithTitle('(Remoto)')
    for window in windows:
        window.activate()
        break
    x=480
    y=240
    pa.doubleClick(x, y)
    print ('carregando tela de login...')
    time.sleep(10)
    x=777
    y=205
    pa.click(x, y)
    pa.press('tab')
    pa.write('Igor123.')
    pa.hotkey('shift', 'tab')
    pa.write('igorsantos@fenixconsultores')
    x=769
    y=373
    pa.doubleClick(x, y) 
    print ('ABRINDO G5')


















except Exception as e:
    print(e)
# pa.PAUSE = 5



# pa.press('ctrl+A')
# pa.write('01072024')