import pygame as pg
import sys, time
from random import randrange
#импорт библиотек

pg.init() #инициализация

res = 800 #разрешение экрана
size = 25 #размер кубиков(еда, змейка, стенка)
screen = pg.display.set_mode((res,res)) #устанавливаем окно
x = y = res // 2 #задаем координаты змейки по середине экрана
snake = [(x,y)] #создаем список с координатами змейки по кубикам
apple = (randrange(size, res - size, size), randrange(size, res - size, size)) #генерируем рандомные корды для яблока
dx, dy = 0, 0 #являются направлениями движения
dirs = {"W": True, "S": True, "A": True,"D": True} #чтобы не могли пойти в противоположную сторону.
lenght = 1 #длина змейки
score = 0 
level = 1
fps = 10 #fps, он же скорость
framePerSeconds = pg.time.Clock()
font_score = pg.font.SysFont("Arial", 26, bold = True)
font_end = pg.font.SysFont("Arial", 66, bold = True)

walls_cord = [] #список с кордами стенок

def gameover(): #функция при проигрыше 
    screen.fill((255,0,0)) #заливаем экран красным
    end_text = font_end.render("GAME OVER!!",True, pg.Color("black"))
    score_text = font_score.render("SCORE: {}".format(str(score)), True, pg.Color("black"))
    level_text = font_score.render("LEVEL: {}".format(str(level)), True, pg.Color("black"))
    screen.blit(end_text, (175, 350))
    screen.blit(score_text, (225, 500))
    screen.blit(level_text, (425, 500))
    pg.mixer.Sound("LAB8/files/gameover.mp3").play()
    pg.display.flip()
    time.sleep(3)
    pg.quit()
    sys.exit()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    screen.fill((0,0,0))
    pressed = pg.key.get_pressed()
    if pressed[pg.K_w] and dirs["W"]: #проверяем нажата ли клавиша, и можно ли ее нажать(dirs)
        dirs = {"W": True, "S": False, "A": True,"D": True} #задаем false противоположному значению
        dx, dy = 0, -1 #указываем направление скорости, по х, у
    if pressed[pg.K_s] and dirs["S"]:
        dirs = {"W": False, "S": True, "A": True,"D": True}
        dx, dy = 0, 1
    if pressed[pg.K_a] and dirs["A"]:
        dirs = {"W": True, "S": True, "A": True,"D": False}
        dx, dy = -1, 0
    if pressed[pg.K_d] and dirs["D"]:
        dirs = {"W": True, "S": True, "A": False,"D": True}
        dx, dy = 1, 0
    if snake[-1] == apple: #[-1] - это ласт элемент. если их координаты равны, значит голова змеи у яблока и мы его едим
        appx = randrange(size, res - size, size)
        appy = randrange(size, res - size, size)
        check = True #проверка для спавна яблока, чтобы не упало на стены и змею
        for cords in walls_cord:
            if (appx, appy) == cords:
                check = False
        for cords in snake:
            if (appx, appy) == snake:
                check = False
        if check == True:
            apple = (appx, appy) #присваиваем корды
        lenght += 1
        score += 1
        pg.mixer.Sound("LAB8/files/coin.mp3").play()
    if (x < 0 or x > res - size or y < 0 or y > res - size) or (len(snake) != len(set(snake))): #проверка границ и то, чтобы snake не имел одинаковых координат, т.е не накладывался друг на друга
        gameover()
    for cords in walls_cord:
        if cords == snake[-1]: #проверка, соприкасается ли голова с любой стеной
            gameover()
    [pg.draw.rect(screen, pg.Color("green"), (x, y, size - 1, size -1)) for x, y in snake] #понимание списка. используем, для отрисовки кубиков нашей змеи
    pg.draw.rect(screen, pg.Color("red"), (apple[0], apple[1], size, size)) #рисуем яблоко
    score_text = font_score.render("SCORE: {}".format(str(score)), True, pg.Color("orange"))
    level_text = font_score.render("LEVEL: {}".format(str(level)), True, pg.Color("orange"))
    screen.blit(score_text, (5, 5))
    screen.blit(level_text, (600, 5))
    x += dx * size #задаем координаты головы (направление на размер кубика)
    y += dy * size 
    snake.append((x,y)) #добавляем корды в список
    snake = snake[-lenght:] #срезаем прошлые координаты, которые меньше чем длина с конца, чтобы змейка не шла беск.линией, а имело только кол-во кубиков равных своей длине
    for cords in walls_cord:
        pg.draw.rect(screen, pg.Color("gray"), (cords[0], cords[1], size, size)) #отрисовываем стены
    pg.display.flip() #обновляем экран, чтобы отобразить изменения
    framePerSeconds.tick(fps) #задаем фпс


    if score % 5 == 0 and score != 0: #проверка для повышения уровня
        check = True
        x1, y1 = randrange(0, res, size), randrange(0, res, size) #задаем рандом кординаты и дальше проверяем их, чтобы стена не накладывалась на что либо
        for cords in snake:
            if (x1,y1) == cords:
                check = False
        if (x1,y1) == apple: check = False
        if check == True: 
            walls_cord.append((x1,y1)) #добавляем корды в список стен
            level += 1
            pg.mixer.Sound("LAB8/files/level.mp3").play()
            score += 1
            fps += 1

                        