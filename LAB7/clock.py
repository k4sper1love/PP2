import pygame as p
import datetime
p.init()
screen = p.display.set_mode((1210, 850))
bg = p.image.load("LAB7/photo/newbg.jpg")
sec = p.image.load("LAB7/photo/seconds2.png")
# sec = p.transform.scale(sec, (100,100))
sec_rect = sec.get_rect()
minutes = p.image.load("LAB7/photo/minutes2.png")
minutes = p.transform.scale(minutes, (40,425))
minutes_rect = minutes.get_rect()
angle_sec = 0
angle_minutes = 0
clock = p.time.Clock()

def get_angle():
    sec = int(datetime.datetime.now().second)
    minutes = int(datetime.datetime.now().minute)
    angle_sec = -(sec * 6)
    angle_minutes = -(minutes * 6)
    if sec != 60:
        angle_minutes -= sec // 10
    return angle_sec, angle_minutes

def sec_rotate(sec, angle_sec):
    rotated_sec = p.transform.rotate(sec, angle_sec)
    rotated_sec_rect = rotated_sec.get_rect()
    rotated_sec_rect.center = (482, 463)
    screen.blit(rotated_sec, rotated_sec_rect)

def min_rotate(minutes, angle_minutes):
    rotated_minutes = p.transform.rotate(minutes, angle_minutes)
    rotated_minutes_rect = rotated_minutes.get_rect()
    rotated_minutes_rect.center = (482, 463)
    screen.blit(rotated_minutes, rotated_minutes_rect)
while True:
    for event in p.event.get():
        if event.type == p.QUIT:
            exit()
    angle_sec, angle_minutes = get_angle()
    screen.fill((255, 255, 255))
    screen.blit(bg, (0,0))
    p.draw.circle(screen, (0, 0, 0), (482, 463), 18 )
    min_rotate(minutes, angle_minutes)
    sec_rotate(sec, angle_sec)
    p.display.flip()
    clock.tick(60)