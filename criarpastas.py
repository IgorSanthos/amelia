import os
import shutil

def criar_pastas_e_mover_arquivos(nomes, diretorio_origem, diretorio_destino):
    """
    Cria pastas com os nomes fornecidos e move os arquivos Excel para essas pastas.

    :param nomes: Lista de nomes para as pastas.
    :param diretorio_origem: Caminho do diretório onde os arquivos Excel estão localizados.
    :param diretorio_destino: Caminho do diretório onde as pastas serão criadas.
    """
    # Cria as pastas
    for nome in nomes:
        caminho_pasta = os.path.join(diretorio_destino, nome)
        if not os.path.exists(caminho_pasta):
            os.makedirs(caminho_pasta)

    # Move os arquivos Excel para as pastas correspondentes
    for arquivo in os.listdir(diretorio_origem):
        if arquivo.endswith('.xlsx') or arquivo.endswith('.xls'):
            for nome in nomes:
                if nome in arquivo:
                    caminho_arquivo_origem = os.path.join(diretorio_origem, arquivo)
                    caminho_pasta_destino = os.path.join(diretorio_destino, nome)
                    shutil.move(caminho_arquivo_origem, os.path.join(caminho_pasta_destino, arquivo))
                    break

# Exemplo de uso:
nomes_pastas = ["YABIKU MATRIZ", "MARCO 27 LTDA EPP",	"CINOMATIC DO BRASIL INDUSTRIA E COMERC",	"YURIKA COMERCIO DE MASSAS LTDA EPP",	"OBAH PRODUTOS E    SERVICOS ANALITICOS LT",	"A&C YABIKU MATRIZ",	"SISNAC MATRIZ",	"BARAO ESQUADRIAS DE MADEIRAS LTDA",	"NLB INDUSTRIA DE MAQUINAS E EQUIPAMENT",	"YABIKU FILIAL L3",	"A&C YABIKU FILIAL",	"SALGATERIA E PASTELARIA DA DIVISA LTDA",	"ZC RUBBER BRAZIL IMPORT E EXPORT LTDA",	"TES DESIGN LOCACAO E INSTALACAO DE EQU",	"NLB COMERCIO DE MAQUIN.E PEcAS EIRELI",	"YABIKU FILIAL L6",	"SWISS REVESTIMENTOS LTDA - EPP",	"HMF SISTEMAS DE ENERGIA COMERCIO E IMP",	"AGILE COM VAREJ DE PROD ELETROMEDICOS",	"LS COMERCIO E SOLUCAO ESPECIALIZADA EM",	"ENGPOINT SERVICOS DE ENGENHARIA LTDA",	"ITALJATO COMERCIO DE PECAS LTDA",	"BDM MICROMERCADOS LTDA",	"YABIKU FILIAL L8",	"R2C EVENTOS LTDA",	"3SIXTY PRODUTORA DE EVENTOS E LIVE MAR",	"ELABORE REPR E ASSIST TECNICA LTDA",	"ACP MATRIZ",	"AGUAPLUS POCOS ARTESIANOS - EIRELI",	"BIMETAL MATRIZ",	"BLG COMERCIAL PROD. NATURAIS E COSM.EI",	"CLINICA VETERINARIA NOSSO LAR LTDA",	"CYPRIANO VIEIRA DESIDERATO",	"DEPLASTI INDUSTRIA E COMERCIO DE PLAST",	"DESIDERATO SORVETES FINOS LTDA - ME",	"ELIAS LIBERATO ARTEFATOS",	"G4 BRASIL IND.E COM. DE EQUIP ELET.L",	"GARAGEM 120 MECANICA E PUBLICIDADE",	"GLK ELETRONICA INDUST.COM. LTDA EPP",	"I-SOLUTIONCARD COMERCIO E SERVICOS LTD",	"ITAMBRAS IMPORTACAO E EXPORTACAO LTDA",	"JOSE MARIO GALLI DESIDERATO - ME",	"MAXXIKIT AUTO PARTS INDUSTRIA & COMERC",	"MED PET SHOP LTDA ME",	"MERCADINHO E PADARIA WK",	"MT WATAYA NAKAO ME",	"NEW TECH SISTEMAS DE ENERGIA LTDA",	"OSWAR APARECIDO MOMESSO HENK ME",	"OURO BRANCO TRANSP. DE AGUA LTDA",	"R&Y SISTEMA M. E. E. E PERSOLIZADO",	"TEMPERSOL ENGENHARIA LTDA.",	"TUBOLAR MATERIAIS",	"TUTTI BELLI COMERCIO DE FLORES LTDA ME",	"TWR MATRIZ",	"TWR FILIAL AM",	"YABIKU FILIAL L7",	"SISNAC FILIAL SC",	"DIXMEDICAL PRODUTOS PARA A SAUDE LTDA",	"CLISOL MATRIZ",	"CLISOL FILIAL",	"OPTICAM TECNOLOGIA",	"TEKNOVATION EQUIPAMENTOS E SERVIcOS LTDA",	"R2 EMPREENDIMENTOS",	"KHROMO TECHNOLOGY DO BRASIL SOCIEDADE LTDA"]
diretorio_origem = r'C:\Users\Igor\Desktop\notas'
diretorio_destino = r'C:\Users\Igor\Desktop\notas'

criar_pastas_e_mover_arquivos(nomes_pastas, diretorio_origem, diretorio_destino)



