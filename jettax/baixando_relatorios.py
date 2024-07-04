

# funcao de download de notas
def download_relatorios(cliente):
    
    import pyautogui as pa
    import time
    import os
    from datetime import datetime, timedelta
    date = ((datetime.now().replace(day=1) - timedelta(days=1)).strftime('%B'))
# Inicio
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

# tela de relatorios
    print('indo para pagina de download relatorios')
    #   pagina de download de relatorios'
    x=2032
    y=64
    pa.click(x, y)
    pa.write('https://app.jettax.com.br/jettax/nfe/list/received')
    pa.press('enter')
    time.sleep(10)
        # pagina de download de relatorios'
        # selecionar cliente
    x=1823 
    y=371
    pa.click(x, y)
    pa.write(cliente)
    pa.press('enter')        
    print('# selecionar cliente')    
    time.sleep(10)
        # selecionar cliente
        # exportar resultados
    x=1851 
    y=219
    pa.click(x, y)
    time.sleep(2)
    x=2007 
    y=378
    pa.click(x, y)        
    pa.press('up')  
    pa.press('tab')
    pa.press('tab')
    pa.press('tab')
    pa.press('tab')
    pa.press('enter')
    time.sleep(10)
    pa.write(f'{cliente}_Entradas_{date}')
    pa.press('enter')
    print ('relatorio baixadas-entradas')
#relatorio de saidas
    time.sleep(10)
    x=2252
    y=776
    pa.click(x, y)
    time.sleep(10)
    x=1851 
    y=219
    pa.click(x, y)
    time.sleep(2)
    x=2007 
    y=378
    pa.click(x, y)        
    pa.press('up')  
    pa.press('tab')
    pa.press('tab')
    pa.press('tab')
    pa.press('tab')
    pa.press('enter')
    time.sleep(10)
    pa.write(f'{cliente}_Saidas_{date}')
    pa.press('enter')
    print ('relatorio baixadas-Saidas')










