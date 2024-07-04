import pyautogui as pa
import time
import os
from datetime import datetime, timedelta

# Data atual
data_atual = datetime.now()
# Primeiro dia do mês atual
primeiro_dia_mes_atual = data_atual.replace(day=1)
# Último dia do mês anterior
ultimo_dia_mes_anterior = primeiro_dia_mes_atual - timedelta(days=1)
# Formatação das datas
primeiro_dia = primeiro_dia_mes_atual.strftime('%d')
ultimo_dia_mes = ultimo_dia_mes_anterior.strftime('%d')
mes_anterior = ultimo_dia_mes_anterior.strftime('%m')
ano_anterior = ultimo_dia_mes_anterior.strftime('%Y')

# Datas inicial e final
data_inicial = f"{primeiro_dia}{mes_anterior}{ano_anterior}"
data_final = f"{ultimo_dia_mes}{mes_anterior}{ano_anterior}"


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

# funcao de download de notas
def download_notas(data_inicial, data_final):
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
download_notas(data_inicial, data_final)



