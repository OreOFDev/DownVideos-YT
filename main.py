# aqui importei o pytubefix a biblioteca que faz baixar videos 
from pytubefix import YouTube
from pytubefix.cli import on_progress

# aqui importei time para dar uns time.sleep
import time

# declarei a variavel menu que o 1 e baixar video mp4 (maior resolucao) e o 2 e baixar audio m4a
menu = """
1 - Baixar Video MP4 (Maior Resolucao)
2 - Baixar Audio M4A
"""

# aqui eu printo o menu
print(menu)

# pergunto para a pessoa qual opcao ela quer do menu
opcao = input("Escolha uma opcao: \n")

# aqui eu verifico se o opcao e um numero inteiro
if opcao.isdigit():

    # se for eu transformo em int
    opcao = int(opcao)

    # se a opcao for 1
    if opcao == 1:

        # printo a opcao escolhida
        print("Opção 1 escolhida")

        # pergunto o URL do video 
        url = input("Digite o link do video: \n")

        # printo a mensagem de baixando
        print("Baixando... Aguarde")

        # espero 1 segundo
        time.sleep(1)

        # printo o titulo do video
        yt = YouTube(url, on_progress_callback=on_progress)
        print(yt.title)

        # baixo o video
        ys = yt.streams.get_highest_resolution()
        ys.download()

    # se a opcao for 2
    elif opcao == 2:

        # printo a opcao escolhida
        print("Opção 2 escolhida")

        # pergunto o URL do video
        url = input("Digite o link do video: \n")

        # printo a mensagem de baixando
        print("Baixando... Aguarde")

        # espero 1 segundo
        time.sleep(1)

        # printo o titulo do video
        yt = YouTube(url, on_progress_callback=on_progress)
        print(yt.title)

        # baixo o audio
        ys = yt.streams.get_audio_only()
        ys.download()
    
    # se o opcao nao for 1 ou 2 
    else:

        # print de erro
        print("Opção invalida")
    
# se a opcao nao for um numero inteiro e sim uma string ou float ou booleano
else:

    # aqui da print de erro
    print("Por favor escolha um numero Inteiro")
