import pygame

from blackjack import *
from drawing import Drawing
from player import Player
from ray_casting import ray_casting_walls
from sprite_objects import *
import moviepy.editor
import time

pygame.init()
icon = pygame.image.load('resources/icon.png')
pygame.display.set_icon(icon)
sc = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.mouse.set_visible(True)
pygame.display.set_caption('FNAF Casino')
sprites = Sprites()
clock = pygame.time.Clock()
player = Player(sprites)
drawing = Drawing(sc)
location = 'menu'
interact_font = pygame.font.Font('resources/fonts/monotypecorsiva.ttf', 36)
interact_txt = interact_font.render('Нажмите ENTER чтобы начать играть', True, WHITE)
balance_img = pygame.image.load('resources/balance.png')
balance_back1 = balance_img.get_rect(topright=(WIDTH, 0))
balance_font = pygame.font.Font('resources/fonts/Casino3DMarquee.ttf', 42)

pygame.mixer.music.load('resources/ost.mp3')
pygame.mixer.music.play(-1)

# BLACKJACK SETTINGS #

# variables
ccards = copy.copy(cards)
stand = False
userCard = []
dealCard = []
bet = min_bet
loseNum = winNum = 0
winB = loseB = 0
lastBet = bet

# space for arrows
arrow = pygame.image.load('resources/blackjack/arrow.png')
arrow_rev = pygame.image.load('resources/blackjack/arrow_rev.png')

# Initialize Game
screen = pygame.display.set_mode((WIDTH, HEIGHT))
blackjack_font = pygame.font.SysFont('arial', 26)
hitTxt = blackjack_font.render('Взять', 1, black)
standTxt = blackjack_font.render('Оставить', 1, black)
restartTxt = blackjack_font.render('Ещё раз', 1, black)
betTxt = blackjack_font.render('Ставка:', 1, black)
txt = blackjack_font.render('', 1, black)
userSum, userA, dealSum, dealA = initGame(ccards, userCard, dealCard)

# Fill Background
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((80, 150, 15))
hitB = pygame.draw.rect(background, gray, (10, 700, 125, 50))
standB = pygame.draw.rect(background, gray, (200, 700, 125, 50))
ratioB = pygame.draw.rect(background, gray, (1045, 650, 140, 100))
arrowRB = pygame.draw.rect(background, (80, 150, 15), (HEIGHT / 2 + 307, 650, 50, 128))
arrowLB = pygame.draw.rect(background, (80, 150, 15), (HEIGHT / 2 + 107, 650, 50, 128))
betB = pygame.draw.rect(background, gray, (HEIGHT / 2 + 155, 672, 154, 64))
restartB = pygame.draw.rect(background, (80, 150, 15), (169, 330, 89, 35))

# SLOT MACHINES SETTINGS

# variables
animatronics = ['freddy', 'bony', 'foxy', 'freddy', 'bony', 'foxy', 'golden_freddy']
slot1, slot2, slot3 = None, None, None
pressed = False
pause = 30
won = 0
ttt = ''
wonTxt = interact_font.render('', True, (100, 255, 100))

# images load
bk = pygame.image.load('img/wall3.png').convert()
backgroundS = pygame.image.load('resources/slot machine/background.png')
background2S = pygame.image.load('resources/slot machine/background2.png')
bony = pygame.image.load('resources/slot machine/bony.png').convert_alpha()
freddy = pygame.image.load('resources/slot machine/freddy.png').convert_alpha()
foxy = pygame.image.load('resources/slot machine/foxy.png').convert_alpha()
golden_freddy = pygame.image.load('resources/slot machine/golden_freddy.png').convert_alpha()

# menu
menu_font = pygame.font.Font("resources/fonts/font1.ttf", 48)
text1 = menu_font.render("Начать Игру", True, [130, 0, 10])
text2 = menu_font.render("Настройки", True, [130, 0, 10])
text3 = menu_font.render("Выйти Из Игры", True, [130, 0, 10])

font_big = pygame.font.Font("resources/fonts/font1.ttf", 54)
text1b = font_big.render("Начать Игру", True, [130, 0, 10])
text2b = font_big.render("Настройки", True, [130, 0, 10])
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

t = 0
newspaper_time = 420
chip_time = 65
after_pause = 250
fred_lag_pause = 300
fred_lag = 90
x_move_time = 5
x_move = 0
x = 1


CHECK = False
# main loop
while True:
    temp = 82 if balance >= 1000 else (96 if balance > 100 else 106)

    # balance checkers
    if balance < min_bet:
        location = 'heaven'
        pygame.mixer.music.pause()
        pygame.mouse.set_visible(False)

    if balance >= aim_balance:
        if not CHECK:
            TIME = pygame.time.get_ticks()
            CHECK = True
        location = 'the end'
        pygame.mouse.set_visible(False)


    # if aim has been achieved
    if location == 'the end':
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        sc.fill(BLACK)
        sc.blit(font_big.render('Вы прошли игру!', True, WHITE), (400, 350))
        time2 = pygame.time.get_ticks()
        if time2 - TIME >= 7000:
            pygame.quit()

        # main menu
    if location == 'menu':
        if t <= newspaper_time + (chip_time * 6) + after_pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    t = newspaper_time + (chip_time * 6) + after_pause + 1
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
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 50 <= pygame.mouse.get_pos()[0]:
                        if 360 <= pygame.mouse.get_pos()[1] <= 435:
                            location = 'lobby'
                            pygame.mouse.set_visible(False)
                    if 490 <= pygame.mouse.get_pos()[1] <= 575:
                        pass
                    if 620 <= pygame.mouse.get_pos()[1] <= 690:
                        exit()

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
        clock.tick(FPS)

    # location if the player failed the game
    if location == 'heaven':
        sc.fill(BLACK)
        pygame.display.update()
        sound = pygame.mixer.Sound("resources/jumpscare.mp3")
        sound.play()
        time.sleep(4)
        video = moviepy.editor.VideoFileClip("resources/jumpscare.mp4")

        video.preview()
        pygame.quit()

    # LOBBY
    if location == 'lobby':
        bet = min_bet
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                exit()
        player.movement()
        sc.fill(BLACK)
        drawing.background(player.angle)
        walls = ray_casting_walls(player, drawing.textures)
        drawing.world(walls + [obj.object_locate(player) for obj in sprites.list_of_objects])
        if slotM_pos[0][0] <= player.pos[0] <= slotM_pos[0][1] and slotM_pos[1][0] <= player.pos[1] <= slotM_pos[1][1]:
            sc.blit(interact_txt, (340, 710))
            if keys[pygame.K_RETURN]:
                location = 'slot machines'
                pygame.mouse.set_visible(True)

        if blackjack_pos[0][0] <= player.pos[0] <= blackjack_pos[0][1] and blackjack_pos[1][0] <= player.pos[1] <= \
                blackjack_pos[1][1]:
            sc.blit(interact_txt, (340, 710))
            if keys[pygame.K_RETURN]:
                location = 'blackjack'
                pygame.mouse.set_visible(True)
        clock.tick(FPS)

        balance_back2 = balance_img.get_rect(topright=(WIDTH + temp, 64))
        sc.blit(balance_img, balance_back1)
        sc.blit(balance_font.render(str(balance), True, (202, 202, 202)), balance_back2)

    # SLOT MACHINES
    if location == 'slot machines':
        clock.tick(FPS)
        sc.blit(bk, (0, 0))
        if balance <= bet:
            bet = balance
        if pressed:
            pause -= 1
        if pause == 0:
            pause = 30
            pressed = False
        if 0 < pause < 30:
            sc.blit(background2S, (0, 0))
        else:
            sc.blit(backgroundS, (0, 0))
            y = 230
            if slot1 == 'bony':
                sc.blit(bony, (355, y))
            if slot1 == 'freddy':
                sc.blit(freddy, (355, y))
            if slot1 == 'foxy':
                sc.blit(foxy, (355, y))
            if slot1 == 'golden_freddy':
                sc.blit(golden_freddy, (355, y))

            if slot2 == 'bony':
                sc.blit(bony, (510, y))
            if slot2 == 'freddy':
                sc.blit(freddy, (510, y))
            if slot2 == 'foxy':
                sc.blit(foxy, (510, y))
            if slot2 == 'golden_freddy':
                sc.blit(golden_freddy, (510, y))

            if slot3 == 'bony':
                sc.blit(bony, (665, y))
            if slot3 == 'freddy':
                sc.blit(freddy, (665, y))
            if slot3 == 'foxy':
                sc.blit(foxy, (665, y))
            if slot3 == 'golden_freddy':
                sc.blit(golden_freddy, (665, y))
        slot_font = pygame.font.Font('resources/fonts/Casino3D.ttf', 24)
        text = slot_font.render(str(bet), True, (100, 255, 100))
        sc.blit(text, (550, 495))
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                exit()
            if keys[K_BACKSPACE]:
                location = 'lobby'
                pygame.mouse.set_visible(False)
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 910 <= event.pos[0] <= 995 and 130 <= event.pos[1] <= 340:
                    slot1, slot2, slot3 = random.choices(animatronics, k=3)
                    if slot1 == slot2 and slot2 == slot3:
                        if slot1 == 'foxy' or slot1 == 'bony':
                            won = bet * 2
                            balance += won
                        elif slot1 == 'freddy':
                            won = bet * 5
                            balance += won
                        elif slot1 == 'golden_freddy':
                            won = bet * 10
                            balance += won
                    elif slot1 == slot3 or slot1 == slot2:
                        if slot1 == 'freddy':
                            won = bet * 2
                            balance += won
                        elif slot1 == 'golden freddy':
                            won = bet * 5
                            balance += won
                    elif slot2 == slot3:
                        if slot2 == 'freddy':
                            won = bet * 2
                            balance += won
                        elif slot2 == 'golden freddy':
                            won = bet * 5
                            balance += won
                    else:
                        won = -bet
                        balance += won
                    pressed = True
                if 320 <= event.pos[0] <= 410 and 480 <= event.pos[1] <= 555:
                    if bet > 10:
                        bet -= bet_dif
                    elif bet < min_bet:
                        bet = min_bet
                if 730 <= event.pos[0] <= 820 and 480 <= event.pos[1] <= 555:
                    if bet + 10 <= balance:
                        bet += bet_dif
        if location == 'lobby':
            continue
        balance_back2 = balance_img.get_rect(topright=(WIDTH + temp, 64))
        sc.blit(balance_img, balance_back1)
        sc.blit(balance_font.render(str(balance), True, (202, 202, 202)), balance_back2)
        if won > 0:
            wonTxt = interact_font.render('Вы выиграли' + ' ' + str(won) + ' фишек', True, (100, 255, 100))
        elif won < 0:
            wonTxt = interact_font.render('Вы проиграли' + ' ' + str(abs(won)) + ' фишек', True, (100, 255, 100))
        sc.blit(wonTxt, (455, 125))
        pygame.display.flip()

    # POKER

    if location == 'poker':
        pass

    # BLACKJACK
    if location == 'blackjack':
        clock.tick(FPS)
        gameover = True if (userSum >= 21 and userA == 0) or len(userCard) == 5 else False
        if len(userCard) == 2 and userSum == 21:
            gameover = True
        elif len(dealCard) == 2 and dealSum == 21:
            gameover = True

        # background needs to be redisplayed because it gets updated
        winTxt = blackjack_font.render('Выиграно: %i' % winNum, 1, black)
        loseTxt = blackjack_font.render('Проиграно: %i' % loseNum, 1, black)
        if bet > balance:
            bet = min_bet
        betSTxt = blackjack_font.render(str(bet), 1, black)

        # checks for mouse clicks on buttons
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == QUIT:
                pygame.quit()
            elif keys[K_BACKSPACE]:
                location = 'lobby'
                pygame.mouse.set_visible(False)
                break
            elif event.type == pygame.MOUSEBUTTONDOWN and not (gameover or stand) and hitB.collidepoint(
                    pygame.mouse.get_pos()):
                # gives player a card if they don't break blackjack rules
                card, cA = genCard(ccards, userCard)
                userA += cA
                userSum += getAmt(card)
                while userSum > 21 and userA > 0:
                    userA -= 1
                    userSum -= 10
            elif event.type == pygame.MOUSEBUTTONDOWN and not gameover and standB.collidepoint(pygame.mouse.get_pos()):
                # when player stands, the dealer plays
                stand = True
                while dealSum <= userSum and dealSum < 17:
                    card, cA = genCard(ccards, dealCard)
                    dealA += cA
                    dealSum += getAmt(card)
                    while dealSum > 21 and dealA > 0:
                        dealA -= 1
                        dealSum -= 10
            elif event.type == pygame.MOUSEBUTTONDOWN and (gameover or stand) and restartB.collidepoint(
                    pygame.mouse.get_pos()):
                # restarts the game, updating scores
                if userSum == dealSum:
                    txt = 'Ничья'
                    pass
                elif userSum <= 21 and len(userCard) == 5:
                    balance += bet
                    winNum += 1
                elif 21 >= userSum > dealSum or dealSum > 21:
                    balance += bet
                    winNum += 1
                else:
                    balance -= bet
                    loseNum += 1
                gameover = False
                stand = False
                userCard = []
                dealCard = []
                ccards = copy.copy(cards)
                userSum, userA, dealSum, dealA = initGame(ccards, userCard, dealCard)
                restartB = pygame.draw.rect(background, (80, 150, 15), (169, 330, 89, 35))
            elif event.type == pygame.MOUSEBUTTONDOWN and arrowLB.collidepoint(pygame.mouse.get_pos()):
                if bet == max_bet or bet == balance:
                    continue
                bet += bet_dif
            elif event.type == pygame.MOUSEBUTTONDOWN and arrowRB.collidepoint(pygame.mouse.get_pos()):
                if bet <= min_bet:
                    continue
                bet -= bet_dif
        if location == 'lobby':
            continue
        if loseB != loseNum:
            txt = blackjack_font.render(f'Вы проиграли {lastBet} фишек', 1, white)
        elif winB != winNum:
            txt = blackjack_font.render(f'Вы выиграли {lastBet} фишек', 1, white)
        elif txt == 'Ничья':
            txt = blackjack_font.render(txt, 1, white)
        elif gameover or stand:
            txt = blackjack_font.render('', 1, (80, 150, 15))
        screen.blit(background, (0, 0))
        screen.blit(hitTxt, (44, 708))
        screen.blit(standTxt, (215, 708))
        screen.blit(winTxt, (1050, 658))
        screen.blit(loseTxt, (1050, 708))
        screen.blit(betTxt, (WIDTH / 2 - 5, 670))
        screen.blit(betSTxt, (WIDTH / 2 + 25, 710))
        screen.blit(arrow, (WIDTH / 2 - 100, 650))
        screen.blit(arrow_rev, (WIDTH / 2 + 100, 650))
        screen.blit(txt, (700, 300))
        balance_back2 = balance_img.get_rect(topright=(WIDTH + temp, 64))
        sc.blit(balance_img, balance_back1)
        sc.blit(balance_font.render(str(balance), True, (202, 202, 202)), balance_back2)

        # displays dealer's cards
        for card in dealCard:
            x = 10 + dealCard.index(card) * 110
            screen.blit(card, (x, 10))
        screen.blit(cBack, (120, 10))

        # displays player's cards
        for card in userCard:
            x = 10 + userCard.index(card) * 110
            screen.blit(card, (x, 500))

        # when game is over, draws restart button and text, and shows the dealer's second card
        if gameover or stand:
            gameoverTxt = blackjack_font.render(f'Игра окончена', 1, white)
            pygame.draw.rect(background, (80, 150, 15), (650, 300, 300, 50))
            screen.blit(gameoverTxt, (140, 300))
            restartB = pygame.draw.rect(background, gray, (169, 330, 89, 35))
            screen.blit(restartTxt, (170, 330))
            screen.blit(dealCard[1], (120, 10))
            lastBet = bet
            loseB = loseNum
            winB = winNum

        pygame.display.update()

    pygame.display.flip()
