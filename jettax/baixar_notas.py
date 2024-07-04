import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from outro_modulo.date import date

data_inicial, data_final = date()

# funcao de download de notas
def download_notas(data_inicial,data_final):
    import os
    import pyautogui as pa
    import time

    # abrindo google
    time.sleep(1)
    os.system('start chrome')
    print('abrindo google')
    time.sleep(4)

    print('login Jettax')
    # login Jettax
    pa.write('https://app.jettax.com.br/login')
    pa.press('enter')
    time.sleep(4)


    #   pagina de home
    pa.press('tab')
    pa.press('tab') 
    pa.press('tab')
    pa.write('suellen@fenixconsultores.com.br')
    pa.press('tab')
    pa.write('123456')
    pa.press('tab')
    pa.press('tab')
    pa.press('tab')
    pa.press('enter')
    print('pagina de home')
    time.sleep(5)

    print('indo para pagina de download de notas')
    #   indo para pagina de download de notas
    x=2032
    y=64
    pa.click(x, y)
    pa.write('https://app.jettax.com.br/jettax/nfe/downloads/new')
    pa.press('enter')
    time.sleep(10)

    #   confimacao de download
    print('confimacao de download')
    for _ in range(24):
        pa.press('tab')
    pa.press('space')
    x=2304
    y=474
    pa.click(x, y)
    pa.hotkey('ctrl','a')
    pa.write(data_inicial)
    pa.press('tab')
    pa.write(data_final)
    for _ in range(7):
        pa.press('tab')
    pa.press('enter')
    time.sleep(3)
    
    x=2197
    y=663
    pa.click(x, y)
    print ('notas baixadas')

download_notas(data_inicial,data_final)


