import pygame as pg
import sys, time
from random import randrange
import random
#импорт библиотек

pg.init() #инициализация

res = 800 #разрешение экрана
size = 25 #размер кубиков(еда, змейка, стенка)
screen = pg.display.set_mode((res,res)) #устанавливаем окно
x = y = res // 2 #задаем координаты змейки по середине экрана
snake = [(x,y)] #создаем список с координатами змейки по кубикам
apple = (randrange(size, res - size, size), randrange(size, res - size, size)) #генерируем рандомные корды для яблока
apple_time = pg.time.get_ticks() #присваиваем время еды
foods = ["red", "blue", "purple"] #выбор еды, 3 варианта
dx, dy = 0, 0 #являются направлениями движения
dirs = {"W": True, "S": True, "A": True,"D": True} #чтобы не могли пойти в противоположную сторону.
lenght = 1 #длина змейки
score = 0 #кол-во очков
level = 1 #уровень
timeout = False #вышло ли время еды
eatfood = False #сьели ли еду
fps = 10 #fps, он же скорость
framePerSeconds = pg.time.Clock()
font_score = pg.font.SysFont("Arial", 26, bold = True) #прописываем шрифты
font_end = pg.font.SysFont("Arial", 66, bold = True)
var = random.choices(foods, weights = [70, 20, 10])[0] #рандом выбор еды с вероятностями


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
    screen.fill((0,0,0)) #заливаю черным
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
    if pg.time.get_ticks() - apple_time > 5000: #если еде больше 5 секунд, то таймаут тру
        timeout = 1
    if snake[-1] == apple or timeout: #[-1] - это ласт элемент. если их координаты равны, значит голова змеи у яблока и мы его едим
        appx = randrange(size, res - size, size) #генерируем рандом корды по х и у для еды
        appy = randrange(size, res - size, size)
        check = True #проверка для спавна яблока, чтобы не упало на стены и змею
        if not timeout: #если условный оператор вызван тем, что еду сьели, а не тем, что время закончилось
            if var == foods[0]:
                lenght += 1
                score += 1
            elif var == foods[1]:
                lenght += 2
                score += 5
            elif var == foods[2]:
                lenght += 3
                score += 10
            eatfood = True #еду сьели, делаем тру
            pg.mixer.Sound("LAB8/files/coin.mp3").play()
        for cords in walls_cord: #проверка координатов, чтобы избежать наложения еды на стены
            if (appx, appy) == cords:
                check = False
        for cords in snake: #проверка корд, чтобы не было наложения еды на змею
            if (appx, appy) == cords:
                check = False
        if check == True: #если все проверки прошли
            var = random.choices(foods, weights = [70, 20, 10])[0] #выбираем рандом еду
            apple = (appx, appy) #присваиваем корды
        apple_time = pg.time.get_ticks() #присваиваем новое время жизни еды
        timeout = 0
    if (x < 0 or x > res - size or y < 0 or y > res - size) or (len(snake) != len(set(snake))): #проверка границ и то, чтобы snake не имел одинаковых координат, т.е не накладывался друг на друга
        gameover()
    for cords in walls_cord:
        if cords == snake[-1]: #проверка, соприкасается ли голова с любой стеной
            gameover()
    [pg.draw.rect(screen, pg.Color("green"), (x, y, size - 1, size -1)) for x, y in snake] #понимание списка. используем, для отрисовки кубиков нашей змеи
    pg.draw.rect(screen, pg.Color(var), (apple[0], apple[1], size, size)) #рисуем яблоко
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


    if eatfood: #проверка для повышения уровня
        lastlevel = level #сохраняем прошлый уровень
        level = score // 5 + 1 #задаем новый уровень
        if lastlevel < level: #если уровень повысился
            check = True #для проверки столкновений
            x1, y1 = randrange(0, res, size), randrange(0, res, size) #задаем рандом кординаты и дальше проверяем их, чтобы стена не накладывалась на что либо
            for cords in snake:
                if (x1,y1) == cords:
                    check = False
            if (x1,y1) == apple: check = False
            if check == True: 
                walls_cord.append((x1,y1)) #добавляем корды в список стен
                pg.mixer.Sound("LAB8/files/level.mp3").play()
                fps += level - lastlevel #увеличивем фпс на разницу в уровнях
                eatfood = False #возвращаем переменную eatfood в False

                        