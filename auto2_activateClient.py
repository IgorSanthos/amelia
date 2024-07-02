import pyautogui as pa
import time
import os
#from pywinauto import application

apelido = 'dialabor'
data = '02072024'
try:
    # ativar empresa
    time.sleep(1)
    x=15
    y=64
    pa.click(x, y)
    x=393
    y=246
    pa.click(x, y)
    pa.write(data)
    pa.press('tab')
    pa.write(apelido)
    time.sleep(1)
    pa.press('tab')
    pa.press('tab')
    pa.press('tab')
    pa.press('enter')
    print ('cliente Ativo')


















except Exception as e:
    print(e)
# pa.PAUSE = 5



# pa.press('ctrl+A')
# pa.write('01072024')