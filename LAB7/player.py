import pygame as p

p.init()
screen = p.display.set_mode((500,500))
status = ["start.png","stop.png"]
sounds = ['peremen.mp3', "18.mp3", "krovi.mp3","komarovo.mp3", "sigaret.mp3","sun.mp3", "dver.mp3", "iphone.mp3" ]
sounds_name = {"peremen.mp3": ["Хочу перемен", "Виктор Цой"], "18.mp3" : ["18 мне уже", "Руки Вверх!"],"iphone.mp3":["Айфон рингтон", "Apple"],"krovi.mp3":["Группа крови", "Виктор Цой"], "komarovo.mp3":["Komarovo", "Игорь Скляр, DVRST, Atomic Heart"], "sigaret.mp3":["Пачка сигарет", "Виктор Цой"], "sun.mp3": ["Звезда по имени Солнце", "Виктор Цой"], "dver.mp3": ["Закрой за мной дверь", "Виктор Цой"]}
music_play = False
photo = False
number = 0
font = p.font.SysFont("Arial", 40)
font2 = p.font.SysFont("Arial", 24)
clock = p.time.Clock()
background = None
status_img = None
back = p.image.load("LAB7/photo/back.png")
back = p.transform.scale(back, (50,50))
next = p.image.load("LAB7/photo/next.png")
next = p.transform.scale(next, (50,50))
print('''

Инструкция по использованию плеера:
S - пуск/стоп музыки,
D - следующий трек,
A - предыдущий трек.''')

def get_photo():
    bg = p.image.load("LAB7/photo/{}.jpg".format(sounds[number].split('.')[0]))
    bg = p.transform.scale(bg, (300, 300))
    return bg

def icon_music():
    status_img = p.image.load("LAB7/photo/{}".format(status[music_play]))
    status_img = p.transform.scale(status_img, (40, 50))
    return status_img

def check_music():
    if not p.mixer.music.get_busy():
        global status_img, number
        if music_play:
            number = (number + 1) % len(sounds)
            p.mixer.music.load('LAB7/music/{}'.format(sounds[number]))
            p.mixer.music.play()
            status_img = icon_music()
while True:
    if not photo: 
        background = get_photo()
        status_img = icon_music()
    for event in p.event.get():
        if event.type == p.QUIT:
            exit()
        if event.type == p.KEYDOWN and event.key == p.K_s:
            if not music_play:
                p.mixer.music.load('LAB7/music/{}'.format(sounds[number]))
                p.mixer.music.play()
                music_play = True
                status_img = icon_music()
            else:
                p.mixer.music.stop()
                music_play = False
                status_img = icon_music()
        if event.type == p.KEYDOWN and event.key == p.K_d:
            number = (number + 1) % len(sounds)
            if music_play: 
                p.mixer.music.stop()
                music_play = True
                p.mixer.music.load('LAB7/music/{}'.format(sounds[number]))
                p.mixer.music.play()
        if event.type == p.KEYDOWN and event.key == p.K_a:
            if number - 1 < 0:
                number = len(sounds) - 1
            else:
                number -= 1
            if music_play:
                p.mixer.music.stop()
                music_play = True
                p.mixer.music.load('LAB7/music/{}'.format(sounds[number]))
                p.mixer.music.play()
    check_music()
    screen.fill((204, 204, 204))
    screen.blit(background, (107,20))
    screen.blit(status_img, (240, 340))
    screen.blit(back, (137, 340))
    screen.blit(next, (325, 340))
    text_name = font.render(sounds_name[sounds[number]][0], True, (0,0,0))
    author_name = font2.render(sounds_name[sounds[number]][1], True, (0,0,0))
    screen.blit(text_name, (250 - text_name.get_width() // 2, 430 - text_name.get_height() // 2))
    screen.blit(author_name, (250 - author_name.get_width() // 2, 470 - author_name.get_height() // 2))
    p.display.flip()
    clock.tick(60)