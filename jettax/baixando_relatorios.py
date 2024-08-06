import pyautogui as pa
import time
import os
from datetime import datetime, timedelta
import easygui

def download_relatorios(clientes):
    date = ((datetime.now().replace(day=1) - timedelta(days=1)).strftime('%B'))
    
    while clientes:
        cliente = clientes.pop(0)
        # Início
        # abrindo googlehttps://app.jettax.com.br/jettax/nfe/list/received

        time.sleep(1)
        os.system('start chrome')
        print('abrindo google')
        time.sleep(4)
        print('login Jettax')
        # login Jettax
        pa.write('https://app.jettax.com.br/login')
        pa.press('enter')
        time.sleep(4)
        
        # # pagina de home
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
        
        # # tela de relatorios
        
        # pagina de download de relatorios
        img_ender = pa.locateCenterOnScreen('jettax/endereco.png', confidence=0.8)
        pa.click(img_ender.x, img_ender.y)
        pa.write('https://app.jettax.com.br/jettax/nfe/list/received')
        pa.press('enter')
        print('indo para pagina de download relatorios')
        time.sleep(10)
        img_cliente = pa.locateCenterOnScreen('jettax/cliente.png', confidence=0.8)
        pa.click(img_cliente.x, img_cliente.y)
        # selecionar cliente
        pa.write(cliente)
        pa.press('down')
        time.sleep(2)
        pa.press('enter')
        print('selecionar cliente')
        time.sleep(5)
        
        # exportar resultados
        img_download = pa.locateCenterOnScreen('jettax/download.png', confidence=0.8)
        pa.click(img_download.x, img_download.y)
        time.sleep(2)
        img_exp = pa.locateCenterOnScreen('jettax/export_option.png', confidence=0.8)
        pa.click(img_exp.x, img_exp.y)
        pa.press('tab')
        pa.press('up')
        pa.press('tab')
        pa.press('tab')
        pa.press('tab') 
        pa.press('enter')
        time.sleep(15)
        pa.write(f'{cliente}_Relatorio_Entradas_Jettax_{date}')
        pa.press('enter')
        print('relatorio baixadas-entradas')
        

    # relatorio de saidas
        time.sleep(10)
        img_saidas = pa.locateCenterOnScreen('jettax/saidas_button.png', confidence=0.8)
        pa.click(img_saidas.x, img_saidas.y)
        time.sleep(5)
        img_download = pa.locateCenterOnScreen('jettax/download.png', confidence=0.8)
        pa.click(img_download.x, img_download.y)
        time.sleep(2)
        img_exp = pa.locateCenterOnScreen('jettax/export_option.png', confidence=0.8)
        pa.click(img_exp.x, img_exp.y)
        pa.press('tab')
        pa.press('up')
        pa.press('tab')
        pa.press('tab')
        pa.press('tab')
        pa.press('enter')
        time.sleep(15)
        pa.write(f'{cliente}_Relatorio_Saidas_Jettax_{date}')
        pa.press('enter')
        print('relatorio baixadas-Saidas')
    easygui.msgbox('Todos os relatórios foram baixados com sucesso!')

# Lista de clientes
clientes = ["OURO BRANCO TRANSP. DE AGUA",	"R&Y SISTEMA M. E. E. E PERSOLIZADO",	"TEMPERSOL ENGENHARIA LTDA.",	"TUBOLAR MATERIAIS",	"TUTTI BELLI COMERCIO DE FLORES LTDA ME",	"TWR MATRIZ",	"TWR FILIAL AM",	"YABIKU FILIAL L7",	"SISNAC FILIAL SC",	"DIXMEDICAL PRODUTOS PARA A SAUDE LTDA",	"CLISOL MATRIZ",	"CLISOL FILIAL",	"OPTICAM TECNOLOGIA",	"TEKNOVATION EQUIPAMENTOS E SERVIcOS LTDA",	"R2 EMPREENDIMENTOS",	"KHROMO TECHNOLOGY DO BRASIL SOCIEDADE LTDA"
            ]

# Chama a funcão para baixar os relatórios "LS COMERCIO E SOLUCAO ESPECIALIZADA EM",	OURO BRANCO TRANSP. DE AGUA
download_relatorios(clientes)
