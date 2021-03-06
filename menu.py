import pygame
import random

if __name__ == '__main__':
    pygame.init()
    size = width, height = 1200, 800
    screen = pygame.display.set_mode(size)

    font = pygame.font.Font("resources/fonts/font1.ttf", 48)
    text1 = font.render("Начать Игру", True, [130, 0, 10])
    text2 = font.render("Как Играть", True, [130, 0, 10])
    text3 = font.render("Выйти Из Игры", True, [130, 0, 10])

    font_big = pygame.font.Font("resources/fonts/font1.ttf", 54)
    text1b = font_big.render("Начать Игру", True, [130, 0, 10])
    text2b = font_big.render("Как Играть", True, [130, 0, 10])
    text3b = font_big.render("Выйти Из Игры", True, [130, 0, 10])

    menuBack = pygame.image.load('resources/menu/bkg.png')
    logo = pygame.image.load('resources/menu/logo.png')
    freddy1 = pygame.image.load('resources/menu/freddy1.png')
    freddy2 = pygame.image.load('resources/menu/freddy2.png')
    freddy3 = pygame.image.load('resources/menu/freddy3.png')
    buttons = pygame.image.load('resources/menu/buttons.png')
    newspaper1 = pygame.image.load('resources/menu/newspaper1.png')
    newspaper2 = pygame.image.load('resources/menu/newspaper2.png')
    chips1 = pygame.image.load('resources/menu/chip1.png')
    chips2 = pygame.image.load('resources/menu/chips2.png')
    chips3 = pygame.image.load('resources/menu/chips3.png')
    chips4 = pygame.image.load('resources/menu/chips4.png')
    chips5 = pygame.image.load('resources/menu/chips5.png')
    chips6 = pygame.image.load('resources/menu/chips6.png')

    fps = 60
    t = 0
    newspaper_time = 400
    chip_time = 50
    pause = 250
    fred_lag_pause = 300
    fred_lag = 90
    x_move_time = 5
    x_move = 0
    x = 1

    clock = pygame.time.Clock()
    running = True
    while running:
        if t <= newspaper_time + (chip_time * 6) + pause:
            if t % 20 <= 10:
                screen.blit(newspaper1, (0, 0))
            else:
                screen.blit(newspaper2, (0, 0))
            if newspaper_time < t <= newspaper_time + chip_time:
                screen.blit(chips1, (0, 0))
            elif newspaper_time + chip_time < t <= newspaper_time + (chip_time * 2):
                screen.blit(chips2, (0, 0))
            elif newspaper_time + (chip_time * 2) < t <= newspaper_time + (chip_time * 3):
                screen.blit(chips3, (0, 0))
            elif newspaper_time + (chip_time * 3) < t <= newspaper_time + (chip_time * 4):
                screen.blit(chips4, (0, 0))
            elif newspaper_time + (chip_time * 4) < t <= newspaper_time + (chip_time * 5):
                screen.blit(chips5, (0, 0))
            elif newspaper_time + (chip_time * 5) < t:
                screen.blit(chips6, (0, 0))
            t += 1
        else:
            t1 = t2 = t3 = True
            screen.blit(menuBack, (0, 0))
            screen.blit(logo, (0, 0))
            screen.blit(buttons, (0, 0))

            x_move_time -= 1
            if x_move_time == 0:
                x_move += x
                if x_move >= 20 or x_move <= 0:
                    x *= -1
                x_move_time = 5

            if fred_lag_pause == 0:
                screen.blit(random.choice([freddy1, freddy2, freddy3]), (0 + x_move, 0))
                fred_lag -= 1
                if fred_lag == 0:
                    fred_lag = random.randint(60, 120)
                    fred_lag_pause = random.randint(300, 600)
            else:
                fred_lag_pause -= 1
                screen.blit(freddy1, (0 + x_move, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            if pygame.mouse.get_focused():
                if 50 <= pygame.mouse.get_pos()[0] <= 400:
                    if 360 <= pygame.mouse.get_pos()[1] <= 435:
                        t1 = False
                        screen.blit(text1b, (90, 362))
                    if 490 <= pygame.mouse.get_pos()[1] <= 575:
                        t2 = False
                        screen.blit(text2b, (90, 490))
                    if 620 <= pygame.mouse.get_pos()[1] <= 690:
                        t3 = False
                        screen.blit(text3b, (90, 620))
            if t1:
                screen.blit(text1, (90, 362))
            if t2:
                screen.blit(text2, (90, 490))
            if t3:
                screen.blit(text3, (90, 620))
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()
