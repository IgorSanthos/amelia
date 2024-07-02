import pygetwindow as gw

# Obter todas as janelas abertas
windows = gw.getAllWindows()

# Listar o título de cada janela
for window in windows:
    print(f"Título: {window.title}")