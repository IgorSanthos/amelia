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
clientes = [    "YABIKU MATRIZ",	"MARCO 27 LTDA EPP",	"CINOMATIC DO BRASIL INDUSTRIA E COMERC",	"YURIKA COMERCIO DE MASSAS LTDA EPP",
            	"OBAH PRODUTOS E SERVICOS ANALITICOS LT",	"A&C YABIKU MATRIZ",	"SISNAC MATRIZ",	"BARAO ESQUADRIAS DE MADEIRAS LTDA",	"NLB INDUSTRIA DE MAQUINAS E EQUIPAMENT",	"YABIKU FILIAL L3",	"A&C YABIKU FILIAL",	"SALGATERIA E PASTELARIA DA DIVISA LTDA",	"ZC RUBBER BRAZIL IMPORT E EXPORT LTDA",	"TES DESIGN LOCACAO E INSTALACAO DE EQU",	"NLB COMERCIO DE MAQUIN.E PEcAS EIRELI",	"YABIKU FILIAL L6",	"SWISS REVESTIMENTOS LTDA - EPP",	"HMF SISTEMAS DE ENERGIA COMERCIO E IMP",	"AGILE COM VAREJ DE PROD ELETROMEDICOS",	"LS COMERCIO E SOLUCAO ESPECIALIZADA EM",	"ENGPOINT SERVICOS DE ENGENHARIA LTDA",	"ITALJATO COMERCIO DE PECAS LTDA",	"BDM MICROMERCADOS LTDA",	"YABIKU FILIAL L8",	"R2C EVENTOS LTDA",	"3SIXTY PRODUTORA DE EVENTOS E LIVE MAR",	"ELABORE REPR E ASSIST TECNICA LTDA",	"ACP MATRIZ",	"AGUAPLUS POCOS ARTESIANOS - EIRELI",	"BIMETAL MATRIZ",	"BLG COMERCIAL PROD. NATURAIS E COSM.EI",	"CLINICA VETERINARIA NOSSO LAR LTDA",	"CYPRIANO VIEIRA DESIDERATO",	"DEPLASTI INDUSTRIA E COMERCIO DE PLAST",	"DESIDERATO SORVETES FINOS LTDA - ME",	"ELIAS LIBERATO ARTEFATOS",	"G4 BRASIL IND.E COM. DE EQUIP ELET.L",	"GARAGEM 120 MECANICA E PUBLICIDADE",	"GLK ELETRONICA INDUST.COM. LTDA EPP",	"I-SOLUTIONCARD COMERCIO E SERVICOS LTD",	"ITAMBRAS IMPORTACAO E EXPORTACAO LTDA",	"JOSE MARIO GALLI DESIDERATO - ME",	"MAXXIKIT AUTO PARTS INDUSTRIA & COMERC",	"MED PET SHOP LTDA ME",	"MERCADINHO E PADARIA WK",	"MT WATAYA NAKAO ME",	"NEW TECH SISTEMAS DE ENERGIA LTDA",	"OSWAR APARECIDO MOMESSO HENK ME",	"OURO BRANCO TRANSP. DE AGUA LTDA",	"R&Y SISTEMA M. E. E. E PERSOLIZADO",	"TEMPERSOL ENGENHARIA LTDA.",	"TUBOLAR MATERIAIS",	"TUTTI BELLI COMERCIO DE FLORES LTDA ME",	"TWR MATRIZ",	"TWR FILIAL AM",	"YABIKU FILIAL L7",	"SISNAC FILIAL SC",	"DIXMEDICAL PRODUTOS PARA A SAUDE LTDA",	"CLISOL MATRIZ",	"CLISOL FILIAL",	"OPTICAM TECNOLOGIA",	"TEKNOVATION EQUIPAMENTOS E SERVIcOS LTDA",	"R2 EMPREENDIMENTOS",	"KHROMO TECHNOLOGY DO BRASIL SOCIEDADE LTDA"
            ]

# Chama a funcão para baixar os relatórios
download_relatorios(clientes)
