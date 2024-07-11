cliente = 'sisnac'
def importar_notas ():
    import pyautogui as pa
    import time

    data = '6'

    time.sleep(2)
    img_escrituracao = pa.locateCenterOnScreen('g5/Escrituracao.png', confidence=0.8)
    pa.click(img_escrituracao.x, img_escrituracao.y) # Ativar
    # Abrindo escrituracao
    try:
        pa.press('down')
        pa.press('right')
        pa.press('down')
        pa.press('down')
        pa.press('down')
        pa.press('down')
        pa.press('down')
        pa.press('right')
        pa.press('down')
        pa.press('enter')
    except Exception as e:
        print(e)
    print ('abrindo escrituracao')

    procurar = 'sim'
    while procurar == 'sim':
        try:
            time.sleep(2)
            img_atl_cadastro = pa.locateCenterOnScreen('g5/atualizar_cadastro_de_participante.png', confidence=0.8)
            pa.click(img_atl_cadastro.x, img_atl_cadastro.y)
            time.sleep(2)
            img_arquivo = pa.locateCenterOnScreen('g5/arquivo.png', confidence=0.8)
            pa.click(img_arquivo.x, img_arquivo.y)

            time.sleep(2)
            img_select = pa.locateCenterOnScreen('g5/selecionar_pasta.png', confidence=0.8)
            pa.click(img_select.x, img_select.y)

            time.sleep(2)
            img_computador= pa.locateCenterOnScreen('g5/computador.png', confidence=0.8)
            pa.click(img_computador.x, img_computador.y)

            time.sleep(2)
            img_discoM = pa.locateCenterOnScreen('g5/discoM.png', confidence=0.8)
            pa.doubleClick(img_discoM.x, img_discoM.y)
            time.sleep(2)
            pa.press('down')
            pa.press('down')
            pa.press('enter')
            pa.press('down')
            pa.press('enter')
            pa.press('down')
            time.sleep(5)
            pa.write(cliente)
            pa.press('enter')
            time.sleep(10)
            pa.press('down')
            pa.write('2024')
            pa.press('enter')
            time.sleep(2)
            pa.press('down')
            pa.press('down')
            pa.press('enter')
            time.sleep(2)
            pa.press('down')
            pa.write(data)
            pa.press('enter')
            time.sleep(2)
            pa.write('arq')
            pa.press('enter')
            time.sleep(2)
            pa.write('sai')
            pa.press('enter')
            time.sleep(5)
            img_slct_pasta= pa.locateCenterOnScreen('g5/slct_pasta.png', confidence=0.8)
            pa.click(img_slct_pasta.x, img_slct_pasta.y)

            time.sleep(10)
            img_next= pa.locateCenterOnScreen('g5/next.png', confidence=0.8)
            pa.click(img_next.x, img_next.y)

            time.sleep(5)
            img_confirmar= pa.locateCenterOnScreen('g5/confirmar.png', confidence=0.8)
            pa.click(img_confirmar.x, img_confirmar.y)

            procurar = "não"
            print("Achei as pastas")
            time.sleep(1)

        except Exception as e:
            print(f"Erro: {e}")
            time.sleep(1)
importar_notas ()

# down
# down
# enter
# donw 
# enter 
# (procurar nome do cliente)