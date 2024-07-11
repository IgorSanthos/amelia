
cliente = 'CYPRIANO'
def ativar_cliente(cliente):
    import pyautogui as pa
    import time
    from datetime import datetime, timedelta
    data_atual = datetime.now()
    primeiro_dia_mes_atual = data_atual.replace(day=1)
    ultimo_dia_mes_anterior = primeiro_dia_mes_atual - timedelta(days=1)
    primeiro_dia = primeiro_dia_mes_atual.strftime('%d')
    mes_anterior = ultimo_dia_mes_anterior.strftime('%m')
    ano_atual = ultimo_dia_mes_anterior.strftime('%Y')
    data_ativar = f"{primeiro_dia}{mes_anterior}{ano_atual}"
    try:
        # ativar empresa
        time.sleep(2)
        img = pa.locateCenterOnScreen('g5/Ativar.png', confidence=0.8)
        pa.click(img.x, img.y)# Ativar
        time.sleep(2)
        img = pa.locateCenterOnScreen('g5/data.png', confidence=0.8)
        pa.click(img.x, img.y)# Data
        pa.write(data_ativar)
        pa.press('tab')
        pa.write(cliente)
        time.sleep(1)
        pa.press('tab')
        pa.press('tab')
        pa.press('tab')
        pa.press('enter')
        print ('cliente Ativo')
    except Exception as e:
        print(e)
    print ('Empresa Ativa')
    # return print('Cliente Ativado')
ativar_cliente(cliente)