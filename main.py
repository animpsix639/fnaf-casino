import pygame, random


if __name__ == '__main__':
    pygame.init()
    size = width, height = 1200, 800
    screen = pygame.display.set_mode(size)

    font = pygame.font.Font("./Fonts/font1.ttf", 48)
    text1 = font.render("Начать Игру", True, [130, 0, 10])
    text2 = font.render("Как Играть", True, [130, 0, 10])
    text3 = font.render("Выйти Из Игры", True, [130, 0, 10])

    font_big = pygame.font.Font("./Fonts/font1.ttf", 54)
    text1b = font_big.render("Начать Игру", True, [130, 0, 10])
    text2b = font_big.render("Как Играть", True, [130, 0, 10])
    text3b = font_big.render("Выйти Из Игры", True, [130, 0, 10])

    background = pygame.image.load('./Sourses/bkg.png')
    logo = pygame.image.load('./Sourses/logo.png')
    freddy1 = pygame.image.load('./Sourses/freddy1.png')
    freddy2 = pygame.image.load('./Sourses/freddy2.png')
    freddy3 = pygame.image.load('./Sourses/freddy3.png')
    buttons = pygame.image.load('./Sourses/buttons.png')

    fps = 60
    fred_lag_pause = 300
    fred_lag = 90
    x_move_time = 5
    x_move = 0
    x = 1

    clock = pygame.time.Clock()
    running = True
    while running:
        t1 = t2 = t3 = True
        screen.blit(background, (0, 0))
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
                fred_lag = random.randint(60, 90)
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