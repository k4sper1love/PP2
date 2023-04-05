import pygame as pg
import sys

# Инициализация Pygame
pg.init()

# Создание окна
screen = pg.display.set_mode((1200, 800))

# Задание цвета
radius = 5
current_choice = None
figure = 0
font = pg.font.SysFont("Arial", 15, bold=True)
time = pg.time.Clock()
fps = 120

def choice():
    pg.draw.rect(screen, pg.Color("red"), (10, 10, 50, 50))
    pg.draw.rect(screen, pg.Color("green"), (10, 70, 50, 50))
    pg.draw.rect(screen, pg.Color("blue"), (10, 130, 50, 50))
    pg.draw.rect(screen, pg.Color("white"), (10, 190, 50, 50))
    pg.draw.rect(screen, pg.Color("white"), (70, 10, 50, 50))
    font_text = font.render("Line", 1, pg.Color("black"))
    screen.blit(font_text, (75, 20))
    pg.draw.rect(screen, pg.Color("white"), (70, 70, 50, 50))
    font_text = font.render("Rect", 1, pg.Color("black"))
    screen.blit(font_text, (75, 80))
    pg.draw.rect(screen, pg.Color("white"), (70, 130, 50, 50))
    font_text = font.render("Circle", 1, pg.Color("black"))
    screen.blit(font_text, (72, 140))
    pg.draw.rect(screen, pg.Color("white"), (70, 190, 50, 50))
    font_text = font.render("Eraser", 1, pg.Color("black"))
    screen.blit(font_text, (72, 200))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.quit()
    pressed = pg.key.get_pressed()
    if pressed[pg.K_SPACE]:
        radius += 1
    if pressed[pg.K_LSHIFT]:
        if radius > 2:
            radius -= 1
    mouse_pos = pg.mouse.get_pos()
    if mouse_pos[0] >= 10 and mouse_pos[0] <= 60 and mouse_pos[1] >= 10 and mouse_pos[1] <= 60:
        if pg.mouse.get_pressed()[0]:
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
    elif pg.mouse.get_pressed()[0]:
        if current_choice and figure == 1:
            pg.draw.circle(screen, pg.Color(current_choice), mouse_pos, radius) 
        elif current_choice and figure == 2:
            pg.draw.rect(screen, pg.Color(current_choice), (mouse_pos[0] - radius, mouse_pos[1] - radius, radius * 10, radius * 10))
        elif current_choice and figure == 3:
            pg.draw.circle(screen, pg.Color(current_choice), mouse_pos, radius * 5) 
        elif current_choice and figure == 4:
            pg.draw.circle(screen, pg.Color("black"), mouse_pos, radius * 5)
    choice()
    pg.display.update()
    time.tick(fps)