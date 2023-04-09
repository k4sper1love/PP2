import pygame as pg
import sys, math

# Инициализация Pygame
pg.init()

# Создание окна
screen = pg.display.set_mode((1200, 800))

# Задание цвета
radius = 5 #задаем radius 
current_choice = None #выбор цвета в данный момент, изначально None
figure = 0 # номер фигуры в данный момент
font = pg.font.SysFont("Arial", 15, bold=True) #прописываем шрифты
font_small = pg.font.SysFont("Arial", 9, bold=True)
time = pg.time.Clock() #задаем clock для fps
fps = 120 #120 фпс

def choice(): #прописываем меню выбора
    pg.draw.rect(screen, pg.Color("red"), (10, 10, 50, 50)) #рисуем выбор цвета
    pg.draw.rect(screen, pg.Color("green"), (10, 70, 50, 50))
    pg.draw.rect(screen, pg.Color("blue"), (10, 130, 50, 50))
    pg.draw.rect(screen, pg.Color("white"), (10, 190, 50, 50))
    pg.draw.rect(screen, pg.Color("white"), (70, 10, 50, 50)) 
    font_text = font.render("Line", 1, pg.Color("black")) #рисуем выбор фигуры. рендерим текст
    screen.blit(font_text, (75, 20)) #отображаем текст
    pg.draw.rect(screen, pg.Color("white"), (70, 70, 50, 50))
    font_text = font.render("Rect", 1, pg.Color("black"))
    screen.blit(font_text, (75, 80))
    pg.draw.rect(screen, pg.Color("white"), (70, 130, 50, 50))
    font_text = font.render("Circle", 1, pg.Color("black"))
    screen.blit(font_text, (72, 140))
    pg.draw.rect(screen, pg.Color("white"), (70, 190, 50, 50))
    font_text = font.render("Eraser", 1, pg.Color("black"))
    screen.blit(font_text, (72, 200))
    pg.draw.rect(screen, pg.Color("white"), (10, 250, 50, 50))
    font_text = font.render("Square", 1, pg.Color("black"))
    screen.blit(font_text, (10, 260))
    pg.draw.rect(screen, pg.Color("white"), (70, 250, 50, 50))
    font_text = font_small.render("RTriangle", 1, pg.Color("black"))
    screen.blit(font_text, (73, 265))
    pg.draw.rect(screen, pg.Color("white"), (10, 310, 50, 50))
    font_text = font_small.render("EqTriangle", 1, pg.Color("black"))
    screen.blit(font_text, (10.5, 325))
    pg.draw.rect(screen, pg.Color("white"), (70, 310, 50, 50))
    font_text = font_small.render("Rhombus", 1, pg.Color("black"))
    screen.blit(font_text, (72, 325))
    pg.draw.rect(screen, pg.Color("white"), (10, 370, 50, 50))
    font_text = font.render("Delete", 1, pg.Color("black"))
    screen.blit(font_text, (12, 380))


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.quit()
    pressed = pg.key.get_pressed() #получаем словарь нажатых кнопок
    if pressed[pg.K_SPACE]: #увеличиваем радиус при нажатии на пробел
        radius += 0.1
    if pressed[pg.K_LSHIFT]: #при нажатии на шифт, уменьшаем радиус
        if radius > 2: #не даем радиусу стать отрицательным
            radius -= 0.1
    mouse_pos = pg.mouse.get_pos() #получаем (x,y) мыши
    if mouse_pos[0] >= 10 and mouse_pos[0] <= 60 and mouse_pos[1] >= 10 and mouse_pos[1] <= 60: #проверяем, наведена ли мышь на кнопку
        if pg.mouse.get_pressed()[0]: #если наведена и нажата левая клавиша
            current_choice = "red"
    elif mouse_pos[0] >= 10 and mouse_pos[0] <= 60 and mouse_pos[1] >= 70 and mouse_pos[1] <= 120:
        if pg.mouse.get_pressed()[0]:
            current_choice = "green"
    elif mouse_pos[0] >= 10 and mouse_pos[0] <= 60 and mouse_pos[1] >= 130 and mouse_pos[1] <= 180:
        if pg.mouse.get_pressed()[0]:
            current_choice = "blue"
    elif mouse_pos[0] >= 10 and mouse_pos[0] <= 60 and mouse_pos[1] >= 190 and mouse_pos[1] <= 240:
        if pg.mouse.get_pressed()[0]:
            current_choice = "white"
    elif mouse_pos[0] >= 70 and mouse_pos[0] <= 120 and mouse_pos[1] >= 10 and mouse_pos[1] <= 60:
        if pg.mouse.get_pressed()[0]:
            figure = 1
    elif mouse_pos[0] >= 70 and mouse_pos[0] <= 120 and mouse_pos[1] >= 70 and mouse_pos[1] <= 120:
        if pg.mouse.get_pressed()[0]:
            figure = 2
    elif mouse_pos[0] >= 70 and mouse_pos[0] <= 120 and mouse_pos[1] >= 130 and mouse_pos[1] <= 180:
        if pg.mouse.get_pressed()[0]:
            figure = 3
    elif mouse_pos[0] >= 70 and mouse_pos[0] <= 120 and mouse_pos[1] >= 190 and mouse_pos[1] <= 240:
        if pg.mouse.get_pressed()[0]:
            figure = 4
    elif mouse_pos[0] >= 10 and mouse_pos[0] <= 60 and mouse_pos[1] >= 250 and mouse_pos[1] <= 300:
        if pg.mouse.get_pressed()[0]:
            figure = 5
    elif mouse_pos[0] >= 70 and mouse_pos[0] <= 120 and mouse_pos[1] >= 250 and mouse_pos[1] <= 300:
        if pg.mouse.get_pressed()[0]:
            figure = 6
    elif mouse_pos[0] >= 10 and mouse_pos[0] <= 60 and mouse_pos[1] >= 310 and mouse_pos[1] <= 360:
        if pg.mouse.get_pressed()[0]:
            figure = 7
    elif mouse_pos[0] >= 70 and mouse_pos[0] <= 120 and mouse_pos[1] >= 310 and mouse_pos[1] <= 360:
        if pg.mouse.get_pressed()[0]:
            figure = 8
    elif mouse_pos[0] >= 10 and mouse_pos[0] <= 60 and mouse_pos[1] >= 370 and mouse_pos[1] <= 420:
        if pg.mouse.get_pressed()[0]:
            screen.fill((0,0,0))
    elif pg.mouse.get_pressed()[0]: #если мы нажимаем левую кнопку мыши
        if current_choice and figure == 1: #проверяем, выбран ли цвет и какой тип фигуры рисуем
            pg.draw.circle(screen, pg.Color(current_choice), mouse_pos, radius) #рисуем линию
        elif current_choice and figure == 2: 
            pg.draw.rect(screen, pg.Color(current_choice), (mouse_pos[0] - radius, mouse_pos[1] - radius, radius * 15, radius * 10)) #рисуем прямоугольник
        elif current_choice and figure == 3:
            pg.draw.circle(screen, pg.Color(current_choice), mouse_pos, radius * 5)  #рисуем круг
        elif current_choice and figure == 4:
            pg.draw.circle(screen, pg.Color("black"), mouse_pos, radius * 10) #ластик
        elif current_choice and figure == 5:
            pg.draw.rect(screen, pg.Color(current_choice), (mouse_pos[0] - radius, mouse_pos[1] - radius, radius * 10, radius * 10)) #квадрат
        elif current_choice and figure == 6:
            x, y = mouse_pos
            vertices = [(x, y), (x, y + radius * 10), (x + radius * 10, y + radius * 10)] #прописываем вершины для треугольника
            pg.draw.polygon(screen, pg.Color(current_choice), vertices) #рисуего прямоуг. треугольник
        elif current_choice and figure == 7:
            x, y = mouse_pos
            height = math.sqrt(3)/2 * radius * 10 #находим высоту для равносторонего треугольника
            vertices = [(x, y - radius * 10), (x + height, y + radius * 5), (x - height, y + radius * 5)] #вершины для равносторонего треугольника
            pg.draw.polygon(screen, pg.Color(current_choice), vertices) #рисуем полигон с 3 вершинами
        elif current_choice and figure == 8:
            x, y = mouse_pos
            vertices = [(x, y - radius * 10), (x + radius * 10, y), (x, y + radius * 10), (x - radius * 10, y)] #вершины ромба
            pg.draw.polygon(screen, pg.Color(current_choice), vertices) #рисуем полигон с 4 вершинами
    choice() #запускаем функцию отображения меню
    pg.display.update() #обновляем дисплей
    time.tick(fps) #указываем фпс