import shutil
from pathlib import Path
from datetime import datetime, timedelta
import tkinter as tk
from tkinter import Tk, Label, Frame, TOP, messagebox, Scrollbar, Text
from tkinter.ttk import Progressbar
import pandas as pd
from client.df_clientes import dados

def move_xml():
    messages_list = []
    # Data da origem
    hoje = datetime.now()
    date_month = '7'

    # Data do destino
    data_atual = datetime.now()
    primeiro_dia_mes_atual = data_atual.replace(day=1)
    ultimo_dia_mes_anterior = primeiro_dia_mes_atual - timedelta(days=1)
    mes_anterior = ultimo_dia_mes_anterior.month
    meses_em_portugues = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    nome_mes = meses_em_portugues[mes_anterior - 1]
    dtCliente = f"{mes_anterior}_{nome_mes}"

    # Criando o DataFrame
    df = pd.DataFrame(dados)

    # Configuração da janela de progresso
    root = Tk()
    root.title("Progresso de Movimentação de Arquivos")
    root.geometry("400x150")
    # Garante que a janela fique sempre no topo
    root.lift()
    root.attributes('-topmost', True)
    # Frame para conter os elementos
    frame = Frame(root)
    frame.pack(pady=20)
    # Label informativa
    lbl_info = Label(frame, text="Movendo arquivos...", font=("Arial", 12))
    lbl_info.pack(side=TOP)
    # Barra de progresso
    progress = Progressbar(frame, orient="horizontal", length=300, mode="determinate")
    progress.pack(pady=10)

    # Função para atualizar a barra de progresso
    def update_progress(count, total):
        progress['value'] = (count / total) * 100
        root.update_idletasks()

    # Função para fechar a janela Tkinter
    def close_window():
        root.destroy()

    # Inicia a barra de progresso com o total de iterações
    total_files = len(df)
    for index, row in df.iterrows():
        # Caminho Origem
        clienteJettax = Path(row['Origem'])

        # Verificar se o caminho de origem existe
        if not clienteJettax.exists():
            # Separando as barras para que seja retirado do endereço o nome do cliente
            clienteJettax = str(clienteJettax)
            ultima_barra = clienteJettax.rfind('\\')
            clienteJettax_name = clienteJettax[ultima_barra + 1:]
            messages_list.append(f"Caminho de origem não encontrado: {clienteJettax_name}")
            update_progress(index + 1, total_files)
            continue  # Continua para o próximo arquivo

        # Caminho Destino
        clienteDest = Path(row['Destino']) / dtCliente
        arquivos = {
            'Recebida': list((clienteJettax / '2024' / date_month / 'Recebida' / 'Autorizada').glob('*')),
            'Emitidas': list((clienteJettax / '2024' / date_month / 'Emitida' / 'Autorizada').glob('*')),
            'Canceladas': list((clienteJettax / '2024' / date_month / 'Emitida' / 'Cancelada').glob('*')),
        }
        destinos = {
            'danfe': [clienteDest / 'Arquivos XML/Saídas', clienteDest / 'Arquivos XML/Entradas']
        }
        
        # Verificar se os diretórios de destino existem e criar se não existirem
        for destino in destinos['danfe']:
            destino.mkdir(parents=True, exist_ok=True)
        
        # Envio para Movimentação de Arquivos
        try:
            for arquivo in arquivos['Recebida']:
                shutil.copy(arquivo, destinos['danfe'][1] / arquivo.name)

            for arquivo in arquivos['Emitidas']:
                shutil.copy(arquivo, destinos['danfe'][0] / arquivo.name)
            
            for arquivo in arquivos['Canceladas']:
                shutil.copy(arquivo, destinos['danfe'][0] / arquivo.name)

            # Separando as barras para que seja retirado do endereço o nome do cliente
            clienteDest = str(clienteDest)
            terceira_barra = clienteDest.find('\\', clienteDest.find('\\', clienteDest.find('\\') + 1) + 1)
            quarta_barra = clienteDest.find('\\', terceira_barra + 1)
            client_name = clienteDest[terceira_barra + 1:quarta_barra]
            messages_list.append(f"Arquivos do ( {client_name} ) copiados com sucesso !\n")
        
        except (FileNotFoundError, PermissionError) as e:
            messages_list.append(f"Erro ao copiar arquivo: {e}\n")
        except Exception as e:
            messages_list.append(f"Erro inesperado ao copiar arquivo: {e}\n")
        
        update_progress(index + 1, total_files)

    # Salva todas as mensagens ao final do processamento
    save_messages_list_to_desktop(messages_list)
    messagebox.showinfo("Aviso", "Arquivos do dia enviados com sucesso")
    # Fecha a janela Tkinter após o término do processamento
    root.after(1000, close_window)  # Espera 1 segundo antes de fechar a janela
    root.mainloop()
    return messages_list

def save_messages_list_to_desktop(messages_list):
    # Cria uma janela tkinter
    root = tk.Tk()
    root.title("Mensagens")
    root.configure(bg="white")
    root.attributes('-topmost', True)
    root.geometry('900x200')

    # Adicionar uma barra de rolagem
    scrollbar = Scrollbar(root)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Adicionar um widget Text para exibir as mensagens
    text_box = Text(root, wrap=tk.WORD, yscrollcommand=scrollbar.set)
    text_box.pack(expand=True, fill=tk.BOTH)
    scrollbar.config(command=text_box.yview)

    # Adicionar as mensagens ao widget Text
    for message in messages_list:
        text_box.insert(tk.END, message + "\n")
    text_box.config(state=tk.DISABLED)  # Impede a edição do conteúdo
    root.mainloop()

def processar_dados_cluster():
    messages_list = []
    try:
        move_xml()
    except FileNotFoundError as e:
        messages_list.append(f"Erro: Arquivo não encontrado - {e}")
        save_messages_list_to_desktop(messages_list)
        messagebox.showinfo("Erro", f"Arquivo não encontrado: {e}")
    except PermissionError as e:
        messages_list.append(f"Erro: Permissão negada - {e}")
        save_messages_list_to_desktop(messages_list)
        messagebox.showinfo("Erro", f"Permissão negada: {e}")
    except Exception as e:
        messages_list.append(f"Erro inesperado: {e}")
        save_messages_list_to_desktop(messages_list)
        messagebox.showinfo("Erro", f"Erro inesperado: {e}")
    return messages_list

processar_dados_cluster()

if __name__ == "__main__":
    pass
