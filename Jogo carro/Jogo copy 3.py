import pygame
from random import randint

pygame.init()



x = 180     # 180 340 540   #posição x do carro play
y = 370         #posição y do carro play

pos_x02 = 200     # posição x do carro 02
pos_y02 = -200     # posição y do carro 02

pos_x03 = 355    # posição x do carro 03
pos_y03 = -900    # posição y do carro 03

pos_x04 = 510
pos_y04 = -600


timer = 0
tempo_segundo = 0

velocidade = 20     #velocidade do carro Play
velocidade02 = 30   #velocidade dos demais carros

    for n in range ( -400,0): 

#carregamento das imagens
fundo = pygame.image.load('C:\Paulo T\VSC\PY\Jogo\Imagens\pista.png')
carroPlay = pygame.image.load('C:\Paulo T\VSC\PY\Jogo\Imagens\carroPlay.png')
carro02 = pygame.image.load('C:\Paulo T\VSC\PY\Jogo\Imagens\carro02.png')
carro03 = pygame.image.load('C:\Paulo T\VSC\PY\Jogo\Imagens\carro03.png')
carro04 = pygame.image.load('C:\Paulo T\VSC\PY\Jogo\Imagens\carro04.png')

font = pygame.font.SysFont('arial black', 25)
texto = font.render("Tempo: ",True,(255,255,255),(0,0,0))
pos_texto = texto.get_rect()
pos_texto.center = (60,50)


janela = pygame.display.set_mode((800,600)) # tamanho da tela
pygame.display.set_caption('JOGO DO KAZI 1.0') # nome na parte superior



janela_aberta = True
while janela_aberta:
    pygame.time.delay(50)

    
    



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

  


    comandos = pygame.key.get_pressed()
    #if comandos[pygame.K_UP]:
        #y-= velocidade
    #if comandos[pygame.K_DOWN]:
        #y+= velocidade
    if comandos[pygame.K_RIGHT] and x <= 498:
        x+= velocidade
    if comandos[pygame.K_LEFT]  and x >= 190:
        x-= velocidade
    
    if (pos_y02 >= 900):
        pos_y02 = randint(-800,-200)
        #print('Carro Azul',pos_y02)
    if (pos_y03 >= 900):
        pos_y03 = randint(-1700,-1100 )
        #print('carro vermelho',pos_y03)
    if (pos_y04 >= 900):
        pos_y04 = randint(-2600,-2000)
       # print('carro laranja', pos_y04)        

    #if pos_y02 == n and pos_y03 == n:
        #print('bateu',pos_y02, pos_y03)






    if (timer <20):
        timer += 1
    else:
        tempo_segundo += 1
        texto = font.render("Tempo: "+str(tempo_segundo),True,(255,255,255),(0,0,0))
        timer = 0
    
    pos_y02 += velocidade02
    pos_y03 += velocidade02  + 2
    pos_y04 += velocidade02  + 10


    janela.blit(fundo,(0,0,))

    janela.blit(carroPlay,(x,y))
    janela.blit(carro02,(pos_x02,pos_y02))
    janela.blit(carro03,(pos_x03,pos_y03))
    janela.blit(carro04,(pos_x04, pos_y04))

    janela.blit(texto,pos_texto)



    pygame.display.update()

pygame.quit()
