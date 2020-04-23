import pygame
from random import randint

pygame.init()

xx = 0
yy = 0

x = 180     # 180 340 540   #posição x do carro play
y = 370         #posição y do carro play

pos_x02 = 200     # posição x do carro 02
pos_y02 = -200     # posição y do carro 02

pos_x03 = 355    # posição x do carro 03
pos_y03 = -900    # posição y do carro 03

pos_x04 = 510
pos_y04 = -600

ajuste_carro2 = 0
ajuste_carro3 = 0
ajuste_carro4 = 0


timer = 0
tempo_segundo = 0

velocidade = 20     #velocidade do carro Play
velocidade02 = 20   #velocidade dos demais carros

 

#carregamento das imagens
fundo = pygame.image.load(r'C:\Users\Paulo Trindade\Documents\Meu_GitHub\Jogos\Jogo carro\arquivos\pista.png')
carroPlay = pygame.image.load(r'C:\Users\Paulo Trindade\Documents\Meu_GitHub\Jogos\Jogo carro\arquivos\carroPlay.png')
carro02 = pygame.image.load(r'C:\Users\Paulo Trindade\Documents\Meu_GitHub\Jogos\Jogo carro\arquivos\carro02.png')
carro03 = pygame.image.load(r'C:\Users\Paulo Trindade\Documents\Meu_GitHub\Jogos\Jogo carro\arquivos\carro03.png')
carro04 = pygame.image.load(r'C:\Users\Paulo Trindade\Documents\Meu_GitHub\Jogos\Jogo carro\arquivos\carro04.png')

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
    if comandos[pygame.K_RIGHT] and x <= 478:
        x+= velocidade
    if comandos[pygame.K_LEFT]  and x >= 200:
        x-= velocidade
    
    if (pos_y02 >= 900):
        pos_y02 =randint(-4000,-1250)
        #print('Carro Azul',pos_y02)
    if (pos_y03 >= 900):
        pos_y03 = randint(-4000,-1250 )
        #print('carro vermelho',pos_y03)
    if (pos_y04 >= 900):
        pos_y04 = randint(-4000,-1250)
        #print('carro laranja', pos_y04)        

    if pos_y02 >= -700 and pos_y02 <= -200:
        ajuste_carro2 = 10
        #print(ajuste_carro2,pos_y02)
    else:
        ajuste_carro2 = 5
    if pos_y03 >= -700 and pos_y03 <= -200:
        ajuste_carro3 = 10
        #print(ajuste_carro3,pos_y03)
    else:
        ajuste_carro3 = 3
    if pos_y04 >= -700 and pos_y04 <=-200:
        ajuste_carro4 = 10
        #print(ajuste_carro4,pos_y04)
    else:
        ajuste_carro4 = 7
    if ajuste_carro2 == ajuste_carro3 == ajuste_carro4:
        print(ajuste_carro2,pos_y02,ajuste_carro3,pos_y03,ajuste_carro4,pos_y04,'ajuste')
        pos_y02 = 900
        pos_y03 = 900
        pos_y04 = 900


    
    print(x,y)

   
    




    if (timer <20):
        timer += 1
    else:
        tempo_segundo += 1
        texto = font.render("Tempo: "+str(tempo_segundo),True,(255,255,255),(0,0,0))
        timer = 0
    
    pos_y02 += velocidade02
    pos_y03 += velocidade02  #+ 5
    pos_y04 += velocidade02  #+ 10


    janela.blit(fundo,(0,0,))

    janela.blit(carroPlay,(x,y))
    janela.blit(carro02,(pos_x02,pos_y02))
    janela.blit(carro03,(pos_x03,pos_y03))
    janela.blit(carro04,(pos_x04, pos_y04))

    janela.blit(texto,pos_texto)



    pygame.display.update()

pygame.quit()
