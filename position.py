import pyautogui
import time
print("Mova o mouse para a posição desejada e aguarde...")
time.sleep(4)
currentMouseX, currentMouseY = pyautogui.position()
print(f"x={currentMouseX} y={currentMouseY}pa.click(x, y)")



