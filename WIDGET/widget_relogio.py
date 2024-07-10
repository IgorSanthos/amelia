import tkinter as tk
from PIL import Image, ImageTk
import time

# def update_clock():
#     now = time.strftime("%H:%M:%S")
#     canvas.itemconfig(clock_text, text=now)
#     root.after(1000, update_clock)

def close_app():
    root.destroy()

root = tk.Tk()
root.title("Relógio Digital com Imagem")
root.geometry("450x450+1000+450")
root.resizable(False, False)
root.attributes("-topmost", True)
root.wm_attributes("-transparentcolor", 'white')  # Define o branco como transparente
root.overrideredirect(True)  # Remove a barra de título

# Carregar imagens
pessoa_img = Image.open("pessoa.png")
balao_img = Image.open("balao.png")

# Converter imagens para PhotoImage
pessoa_photo = ImageTk.PhotoImage(pessoa_img)
balao_photo = ImageTk.PhotoImage(balao_img)

# Criar canvas para desenhar
canvas = tk.Canvas(root, width=450, height=450, bg='white', highlightthickness=0)
canvas.pack()

# POSIÇÃO NA TELA
canvas.create_image(130, 220, image=pessoa_photo)
canvas.create_image(330, 200, image=balao_photo)

# Adicionar texto do relógio ao canvas
clock_text = canvas.create_text(350, 100, text="", font=('Helvetica', 24, 'bold'), fill='black')

# Adicionar botão de fechar
close_button = tk.Button(root, text="X", command=close_app, bg='red', fg='white', bd=0)
canvas.create_window(430, 20, anchor='ne', window=close_button)

# update_clock()
root.mainloop()
