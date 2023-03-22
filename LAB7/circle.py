import pygame as p
p.init()

width = 500
height = 500
screen = p.display.set_mode((width,height))
clock = p.time.Clock()
x = 250
y = 250

while True:
    for event in p.event.get():
        if event.type == p.QUIT:
            exit()
    pressed = p.key.get_pressed()
    if pressed[p.K_w]:
        if y - 40 >= 0:
            y -= 20
    if pressed[p.K_s]:
        if y + 40 <= height:
            y += 20
    if pressed[p.K_d]:
        if x + 40 <= width:
            x += 20
    if pressed[p.K_a]:
        if x - 40 >= 0:
            x -= 20
    screen.fill((255,255,255))
    p.draw.circle(screen, (255,0,0), (x, y), 25)
    p.display.flip()
    clock.tick(60)