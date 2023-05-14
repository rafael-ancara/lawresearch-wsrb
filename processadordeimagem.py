# Processador de imagens
# Este código tem por objetivo:
#    1) Automatizar o opencv para encontrar os textos nos volumes 2, 3 e 4 dos Anais em JPEG
#    2) Usar o tesseract para transformar as imagens já tratadas para txt dos volumes 2, 3 e 4 dos anais
#    3) Construir o Corpus para analisar via VoyantTools

# Aplicações envolvidas
# OpenCV - Identificar os textos
# Tesseract - Reconhecer os textos
# Glob2 - fazer loop

#descobrir melhores formas de tratamento com opencv, o high passa parece um jeito bom mas num sei como fazer igual o photoshop, tentar estratégias com o photoshop e as actions 

import glob2
import pytesseract
import cv2

# LOOP
caminhos_imagens = glob2.glob("Documentos\Atas da subcomissao\jpgs\*.jpg")
for caminho_imagem in caminhos_imagens:
    # LOOP LEITOR DE IMAGEM
    imagem = cv2.imread(caminho_imagem)
    # página 11-v2 tem carimbo e sublinhado

    # TRANSFORMADOR DE IMAGEM
    texto = pytesseract.image_to_string(imagem, lang="por", config='--psm 6 --oem 1')

    # SALVADOR
    caminho_txt = caminho_imagem.replace(".jpg", ".txt")
    with open(caminho_txt, 'w', encoding='utf-8') as arquivo:
        arquivo.write(texto)
        