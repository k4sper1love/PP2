import pygame as pg 
from pygame.locals import *
import sys, random, time
#импорт библиотек

pg.init() #инициализация pygame

#устанавливаем желаемое кол-во кадров в секунду
fps = 60
framePerSeconds = pg.time.Clock() #объект для ограничения кол-во кадров

#colors
black = (0, 0, 0)
red = (255, 0, 0)
white = (255,255,255)

#параметры экрана и прочие переменные
width = 400
height = 600
speed = 1
score = 0
money = 0

#прописываем шрифты
font = pg.font.SysFont("Verdana", 60)
font_small = pg.font.SysFont("Verdana", 20)
game_over = font.render("Game Over!", True, black) #рендерим заранее текст, чтобы не отрисовывать его в цикле каждый раз

#bg
background = pg.image.load("LAB8/files/AnimatedStreet.png") #загружаем фон

#screen
screen = pg.display.set_mode((width, height)) #устанавливаем размеры окна
screen.fill(white) #заливаем фон белым цветом
pg.display.set_caption("Game") #задаем название окна

#classes: Enemy, Player, Coin
#делаем классы дочерними pg.sprite.Sprite(класс для работы со спрайтами)
class Enemy(pg.sprite.Sprite):
    def __init__(self):
        super().__init__() #(инициализируем его как дочерний)
        self.image = pg.image.load("LAB8/files/Enemy.png")
        self.rect = self.image.get_rect() #получаем его rect
        self.rect.center = (random.randint(40, width - 40), 0) #устанавливаем его положение на экране по x,y

    def move(self):
        global score
        self.rect.move_ip(0, speed) #move_ip(x,y) - перемещает наш rect на +-x, +-y
        if (self.rect.top > 600): #проверяем границы
            score += 1
            self.rect.top = 0 #возвращаем обьект наверх, в начальное положение
            self.rect.center = (random.randint(40, width - 40), 0) #задаем случайное положение по x

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("LAB8/files/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
    
    def move(self):
        pressed_keys = pg.key.get_pressed() #присваиваем объект, содержащий инфу о нажатых клавишах
        if self.rect.top > 0: #проверяем границы
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -5) #перемещаем
        if self.rect.bottom < 600:
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0, 5)
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < width:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

class Coin(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("LAB8/files/coin.png")
        self.image = pg.transform.scale(self.image, (30, 30)) #меняем размеры x - длина, y - ширина
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(50, width - 50), random.randint(50, height - 50))
    
    def move(self):
        self.rect.center = (random.randint(50, width - 50), random.randint(50, height - 50)) #делаем respawn/перемещаем в случайное место
        
#создаем объекты из классов
P1 = Player()
E1 = Enemy()
C1 = Coin()
C2 = Coin()
#создаем группы спрайтов и добавляем
coins = pg.sprite.Group() #по сути, как классификация
coins.add(C1)
coins.add(C2)
enemies = pg.sprite.Group()
enemies.add(E1)
all_sprites = pg.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

#создаем свой user event
inc_speed = pg.USEREVENT + 1 # + 1 чтобы быть уверенными, что наш event имеет уникальный id
pg.time.set_timer(inc_speed, 1000) #таймер, который каждую секунду вызывает event

while True:
    for event in pg.event.get(): #получаем список events
        if event.type == inc_speed: #проверяем наличие event
            speed += 0.5
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    screen.blit(background, (0,0)) #отображаем задний фон
    scores = font_small.render("Score: {}".format(str(score)), True, black) #рендерим и выводим score
    money_text = font_small.render("Money: {}".format(str(money)), True, black) #рендерим и выводим money
    screen.blit(scores, (10,10))
    screen.blit(money_text, (250, 10))
    for x in coins: #отображаем каждую монетку
        screen.blit(x.image, x.rect) 
    if pg.sprite.spritecollideany(P1, coins): #если p1 столкнулся с любым спрайтом из coins
        pg.mixer.Sound("LAB8/files/coin.mp3").play() #проигрываем звук
        money += 1
        for x in coins:
            if pg.sprite.collide_rect(P1, x): #проверяем, с каким конкретным coin в coins столкнулся p1
                x.move() #перемещаем его
    for x in all_sprites:
        screen.blit(x.image, x.rect) #отрисовываем все спрайты
        x.move() # задаем им движение

    if pg.sprite.spritecollideany(P1, enemies): #если p1 столкнется с любым спрайтом из enemies
        pg.mixer.Sound("LAB8/files/crash.wav").play() 
        time.sleep(0.5) #таймаут, 0.5 секунд
        screen.fill(red) #заливаем экран красным
        screen.blit(game_over, (30, 250)) #отображаем текст
        screen.blit(scores, (60,350))
        screen.blit(money_text, (250, 350))
        pg.display.update() #обновляем display, чтобы отобразить изменения
        for x in all_sprites:
            x.kill() #убиваем/убираем все спрайты
        time.sleep(2) 
        pg.quit()
        sys.exit()
    pg.display.update()
    framePerSeconds.tick(fps) #задаем .tick(fps). для контроля фпс. задаем фпс