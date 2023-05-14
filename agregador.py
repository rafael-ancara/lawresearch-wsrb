#Juntador de arquivos

import os
import shutil

# Pasta contendo os arquivos de texto
pasta = r"G:\Outros computadores\My MacBook Pro\Coisas MacBook\Workshop Maxplanck\Documentos\Atas da subcomissao\txts extraidos"

# Nome do arquivo de saída
nome_arquivo_saida = "atascompletas.txt"

# Abre o arquivo de saída em modo de escrita
with open(nome_arquivo_saida, "w", encoding="utf-8") as arquivo_saida:
    # Percorre todos os arquivos na pasta
    for nome_arquivo in os.listdir(pasta):
        # Verifica se é um arquivo de texto
        if nome_arquivo.endswith(".txt"):
            caminho_arquivo = os.path.join(pasta, nome_arquivo)
            # Abre o arquivo de texto em modo de leitura
            with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
                # Copia o conteúdo do arquivo para o arquivo de saída
                shutil.copyfileobj(arquivo, arquivo_saida)
