import pyautogui as pa
import time
import os
#from pywinauto import application

apelido = 'dialabor'
data = '02072024'
try:
    # escrituracao
    x=104
    y=32
    pa.click(x, y)
    # notas ISS
    x=115
    y=80
    pa.click(x, y)
    # importar nfse municipal
    x=525
    y=362
    pa.click(x, y)


















except Exception as e:
    print(e)
# pa.PAUSE = 5



# pa.press('ctrl+A')
# pa.write('01072024')