import pygame
import random


class Snake:
    blok_snake = int
    predkosc = int
    def __init__(self,blok, szybkosc):
        self.blok_snake = blok
        self.predkosc = szybkosc
    def rysuj(self, snake_list):
        for x in snake_list:
            pygame.draw.rect(ekran, czarny, [x[0], x[1], self.blok_snake, self.blok_snake])
            
class Kolor:
    odcien = str
    wartosc = tuple
    def __init__(self, od, war):
        self.odcien = od
        self.wartosc = war

def pozycje_jedzenia():
    global jedzenie_poz_x
    global jedzienie_poz_y
    jedzenie_poz_x = random.randrange(0, szerokosc_ekranu - blok_snake, blok_snake)
    jedzienie_poz_y = random.randrange(0, wysokosc_ekranu - blok_snake, blok_snake)

def glowna_petla():
    koniec_gry = False
    zamknij = False
    elementy_snake = []
    dlugosc_weza = 1
    x1 = szerokosc_ekranu / 2
    y1 = wysokosc_ekranu / 2
    x1_przesuniecie = 0
    y1_przesuniecie = 0
 
    pozycje_jedzenia()
 
    while not koniec_gry:
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                koniec_gry = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_przesuniecie = -blok_snake
                    y1_przesuniecie = 0
                elif event.key == pygame.K_RIGHT:
                    x1_przesuniecie = blok_snake
                    y1_przesuniecie = 0
                elif event.key == pygame.K_UP:
                    y1_przesuniecie = -blok_snake
                    x1_przesuniecie = 0
                elif event.key == pygame.K_DOWN:
                    y1_przesuniecie = blok_snake
                    x1_przesuniecie = 0
        
        glowa_weza = []
        glowa_weza.append(x1)
        glowa_weza.append(y1)
        elementy_snake.append(glowa_weza)
                    
        while zamknij == True:
            ekran.fill(bialy)
            informacja = font_style.render("Przegrales! Zamknij okno, aby zakonczyc.", True, czerwony)
            ekran.blit(informacja, [szerokosc_ekranu / 4, wysokosc_ekranu / 2])
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        koniec_gry = True
                        zamknij = False
                        raise "gra zostala zakonczona przez uzytkownika"
 
       
        ekran.fill(bialy)
        pygame.draw.rect(ekran, fioletowy, [jedzenie_poz_x, jedzienie_poz_y, blok_snake, blok_snake])
        
        if len(elementy_snake) > dlugosc_weza:
            del elementy_snake[0]
        for x in elementy_snake[:-1]:
            if x == glowa_weza:
                zamknij = True
        if x1 >= szerokosc_ekranu or x1 < 0 or y1 >= wysokosc_ekranu or y1 < 0:
            zamknij = True
        x1 += x1_przesuniecie
        y1 += y1_przesuniecie
        obiekt_snake.rysuj(elementy_snake)
        
        pygame.display.update()
 
        if x1 == jedzenie_poz_x and y1 == jedzienie_poz_y:
            pozycje_jedzenia()
            dlugosc_weza += 1
 
        clock.tick(obiekt_snake.predkosc)
 
    pygame.quit()
    quit()



pygame.init()

 
bialy = Kolor("bialy",(255,255,255)).wartosc
fioletowy =  Kolor("fioletowy",(238, 130, 238)).wartosc
czarny = Kolor("czarny",(0,0,0)).wartosc
zielony = Kolor("zielony",(0,255,0)).wartosc
czerwony = Kolor("czerwony",(255,0,0)).wartosc

blok_snake = 20
 
szerokosc_ekranu = 600
wysokosc_ekranu = 600

obiekt_snake = Snake(20, 10)
 
ekran = pygame.display.set_mode((szerokosc_ekranu, wysokosc_ekranu))
pygame.display.set_caption('Gra Snake')
 
clock = pygame.time.Clock()
 

predkosc = 10
 
font_style = pygame.font.SysFont("arial", 20)

glowna_petla()