import pyautogui as pa
import time
import os
from client.df_cliente_giss_diadema import dados

cliente = dados
try:
    time.sleep(2)
    os.system('start chrome')
    time.sleep(2)
    pa.write('https://wwwx.gissonline.com.br/contador_clientes.asp')
    pa.press('enter')    # Pressiona Enter para abrir o Chrome
    time.sleep(5)
    # busca
    img_busca = pa.locateCenterOnScreen('gissonline/img/busca.png', confidence=0.8)
    pa.click(img_busca.x, img_busca.y)
    pa.press('tab')
    pa.press('space')
    pa.press('tab')
    pa.write(cliente)
    time.sleep(2)
    # busca 2
    img_busca2 = pa.locateCenterOnScreen('gissonline/img/busca2.png', confidence=0.8)
    pa.click(img_busca2.x, img_busca2.y)
    time.sleep(2)
    # ir
    img_ir = pa.locateCenterOnScreen('gissonline/img/ir.png', confidence=0.8)
    pa.click(img_ir.x, img_ir.y)
    time.sleep(5)
    # prestador
    img_prestador = pa.locateCenterOnScreen('gissonline/img/prestador.png', confidence=0.8)
    pa.click(img_prestador.x, img_prestador.y)    
    time.sleep(5)
    # encerrar
    img_encerrar = pa.locateCenterOnScreen('gissonline/img/encerrar.png', confidence=0.8)
    pa.click(img_encerrar.x, img_encerrar.y)
    print ('...')


except Exception as e:
    print (e)