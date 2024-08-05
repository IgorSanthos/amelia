import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from outro_modulo.date import date

data_inicial, data_final = date()

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
    img_ender = pa.locateCenterOnScreen('jettax/endereco.png', confidence=0.8)
    pa.click(img_ender.x, img_ender.y)
    pa.write('https://app.jettax.com.br/jettax/nfe/downloads')
    pa.press('enter')
    print('confimacao de download')
    time.sleep(15)

    #   confimacao de download
    print('confimacao de download')

    try:
        img_plus = pa.locateCenterOnScreen('jettax/plus.png', confidence=0.8)
        pa.click(img_plus.x, img_plus.y)
    except Exception as e:
        pass

    img_selecionar = pa.locateCenterOnScreen('jettax/selecionar.png', confidence=0.8)
    pa.click(img_selecionar.x, img_selecionar.y)
    time.sleep(15)

    img_data_init = pa.locateCenterOnScreen('jettax/data_init.png', confidence=0.8)
    pa.click(img_data_init.x, img_data_init.y)
    pa.hotkey('ctrl','a')
    pa.write(data_inicial)
    pa.press('tab')
    pa.write(data_final)
    time.sleep(15)
    pa.press('tab')
    pa.press('tab')
    pa.press('tab')
    pa.press('tab')
    pa.press('tab')
    pa.press('tab')
    pa.press('tab')
    pa.press('enter')
    print ('notas baixadas')

download_notas(data_inicial,data_final)


