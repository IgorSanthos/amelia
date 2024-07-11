import pyautogui as pa
import time

procurar = 'sim'

while procurar == 'sim':
    try:
        img = pa.locateCenterOnScreen('g5/Ativar.png', confidence=0.8)
        pa.click(img.x, img.y)
        procurar = "não"
        print("Imagem não encontrada")
        time.sleep(1)
    except Exception as e:
        print(f"Erro: {e}")
        time.sleep(1)
