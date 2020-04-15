import pygame

pygame.init()


x = 340         #posição x do carro play
y = 370         #posição y do carro play

pos_x01 = 200     # posição x do carro 01
pos_y01 = 385     # posição y do carro 01

pos_x02 = 510    # posição x do carro 02
pos_y02 = 390    # posição y do carro 02

posx_f2 = 0
posy_f2 = -600

pos_xf1 = 0
pos_yf1 = 0

velocidade = 20     #velocidade do carro Play
velocidade02 = 20   #velocidade do carro 02
velocidade_Fundo2 = 5

fundo2 = pygame.image.load('C:\Users\Paulo Trindade\Documents\Meu_GitHub\Jogos\Jogo carro\arquivos\pista.png')
fundo = pygame.image.load('C:\Paulo T\VSC\PY\.vscode\Jogo\pista.png')
carro = pygame.image.load('C:\Paulo T\VSC\PY\.vscode\Jogo\carroPlay.png')
carro02 = pygame.image.load('C:\Paulo T\VSC\PY\.vscode\Jogo\carro02.png')
carro03 = pygame.image.load('C:\Paulo T\VSC\PY\.vscode\Jogo\carro03.png')
carro04 = pygame.image.load('C:\Paulo T\VSC\PY\.vscode\Jogo\carro04.png')




janela = pygame.display.set_mode((800,600))
pygame.display.set_caption('JOGO DO KAZI 1.0')

janela_aberta = True
while janela_aberta:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP]:
        y-= velocidade
    if comandos[pygame.K_DOWN]:
        y+= velocidade
    if comandos[pygame.K_RIGHT]:
        x+= velocidade
    if comandos[pygame.K_LEFT]:
        x-= velocidade
    if (pos_y01 >= 900):
        pos_y01 = -200
    if (pos_yf1 >= 600):
        pos_yf1 = -600
    if (posy_f2 >= 600):
        posy_f2 = -600
    
    
    #pos_y01 += velocidade02
    posy_f2 += velocidade_Fundo2
    pos_yf1 += velocidade_Fundo2

    janela.blit(fundo,(pos_xf1,pos_yf1,))
    janela.blit(fundo2,(posx_f2,posy_f2))
    janela.blit(carro,(x,y))
    #janela.blit(carro02,(pos_x01,pos_y01))
    janela.blit(carro03,(pos_x02,pos_y02))



    pygame.display.update()

pygame.quit()