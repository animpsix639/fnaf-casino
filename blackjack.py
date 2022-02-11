#!/usr/bin/python

#Import Library
from settings import *
import pygame
from pygame.locals import *
import random
import copy

global balance

#Load Images
r = 'resources/blackjack'
cBack = pygame.image.load('%s/cards/cardback.png' % r)
diamondA = pygame.image.load('%s/cards/ad.png' % r)
clubA = pygame.image.load('%s/cards/ac.png' % r)
heartA = pygame.image.load('%s/cards/ah.png' % r)
spadeA = pygame.image.load('%s/cards/as.png' % r)
diamond2 = pygame.image.load('%s/cards/2d.png' % r)
club2 = pygame.image.load('%s/cards/2c.png' % r)
heart2 = pygame.image.load('%s/cards/2h.png' % r)
spade2 = pygame.image.load('%s/cards/2s.png' % r)
diamond3 = pygame.image.load('%s/cards/3d.png' % r)
club3 = pygame.image.load('%s/cards/3c.png' % r)
heart3 = pygame.image.load('%s/cards/3h.png' % r)
spade3 = pygame.image.load('%s/cards/3s.png' % r)
diamond4 = pygame.image.load('%s/cards/4d.png' % r)
club4 = pygame.image.load('%s/cards/4c.png' % r)
heart4 = pygame.image.load('%s/cards/4h.png' % r)
spade4 = pygame.image.load('%s/cards/4s.png' % r)
diamond5 = pygame.image.load('%s/cards/5d.png' % r)
club5 = pygame.image.load('%s/cards/5c.png' % r)
heart5 = pygame.image.load('%s/cards/5h.png' % r)
spade5 = pygame.image.load('%s/cards/5s.png' % r)
diamond6 = pygame.image.load('%s/cards/6d.png' % r)
club6 = pygame.image.load('%s/cards/6c.png' % r)
heart6 = pygame.image.load('%s/cards/6h.png' % r)
spade6 = pygame.image.load('%s/cards/6s.png' % r)
diamond7 = pygame.image.load('%s/cards/7d.png' % r)
club7 = pygame.image.load('%s/cards/7c.png' % r)
heart7 = pygame.image.load('%s/cards/7h.png' % r)
spade7 = pygame.image.load('%s/cards/7s.png' % r)
diamond8 = pygame.image.load('%s/cards/8d.png' % r)
club8 = pygame.image.load('%s/cards/8c.png' % r)
heart8 = pygame.image.load('%s/cards/8h.png' % r)
spade8 = pygame.image.load('%s/cards/8s.png' % r)
diamond9 = pygame.image.load('%s/cards/9d.png' % r)
club9 = pygame.image.load('%s/cards/9c.png' % r)
heart9 = pygame.image.load('%s/cards/9h.png' % r)
spade9 = pygame.image.load('%s/cards/9s.png' % r)
diamond10 = pygame.image.load('%s/cards/10d.png' % r)
club10 = pygame.image.load('%s/cards/10c.png' % r)
heart10 = pygame.image.load('%s/cards/10h.png' % r)
spade10 = pygame.image.load('%s/cards/10s.png' % r)
diamondJ = pygame.image.load('%s/cards/jd.png' % r)
clubJ = pygame.image.load('%s/cards/jc.png' % r)
heartJ = pygame.image.load('%s/cards/jh.png' % r)
spadeJ = pygame.image.load('%s/cards/js.png' % r)
diamondQ = pygame.image.load('%s/cards/qd.png' % r)
clubQ = pygame.image.load('%s/cards/qc.png' % r)
heartQ = pygame.image.load('%s/cards/qh.png' % r)
spadeQ = pygame.image.load('%s/cards/qs.png' % r)
diamondK = pygame.image.load('%s/cards/kd.png' % r)
clubK = pygame.image.load('%s/cards/kc.png' % r)
heartK = pygame.image.load('%s/cards/kh.png' % r)
spadeK = pygame.image.load('%s/cards/ks.png' % r)

#Set Icon


#Global Constants
black = (0,0,0)
white = (255,255,255)
gray = (192,192,192)

cards = [ diamondA, clubA, heartA, spadeA, \
          diamond2, club2, heart2, spade2, \
          diamond3, club3, heart3, spade3, \
          diamond4, club4, heart4, spade4, \
          diamond5, club5, heart5, spade5, \
          diamond6, club6, heart6, spade6, \
          diamond7, club7, heart7, spade7, \
          diamond8, club8, heart8, spade8, \
          diamond9, club9, heart9, spade9, \
          diamond10, club10, heart10, spade10, \
          diamondJ, clubJ, heartJ, spadeJ, \
          diamondQ, clubQ, heartQ, spadeQ, \
          diamondK, clubK, heartK, spadeK ]
cardA = [ diamondA, clubA, heartA, spadeA ]
card2 = [ diamond2, club2, heart2, spade2 ]
card3 = [ diamond3, club3, heart3, spade3 ]
card4 = [ diamond4, club4, heart4, spade4 ]
card5 = [ diamond5, club5, heart5, spade5 ]
card6 = [ diamond6, club6, heart6, spade6 ]
card7 = [ diamond7, club7, heart7, spade7 ]
card8 = [ diamond8, club8, heart8, spade8 ]
card9 = [ diamond9, club9, heart9, spade9 ]
card10 = [ diamond10, club10, heart10, spade10, \
            diamondJ, clubJ, heartJ, spadeJ, \
            diamondQ, clubQ, heartQ, spadeQ, \
            diamondK, clubK, heartK, spadeK ]

def getAmt(card):
    ''' Returns the amount the card is worth.
E.g. Ace is default 11. 10/Jack/Queen/King is 10.'''
    if card in cardA:
        return 11
    elif card in card2:
        return 2
    elif card in card3:
        return 3
    elif card in card4:
        return 4
    elif card in card5:
        return 5
    elif card in card6:
        return 6
    elif card in card7:
        return 7
    elif card in card8:
        return 8
    elif card in card9:
        return 9
    elif card in card10:
        return 10
    else:
        print('getAmt broke')
        exit()

def genCard(cList, xList):
    '''Generates an card from cList, removes it from cList, and appends it to xList.
Returns if card is Ace and the card itself.'''
    cA = 0
    card = random.choice(cList)
    cList.remove(card)
    xList.append(card)
    if card in cardA:
        cA = 1
    return card, cA

def initGame(cList, uList, dList):
    '''Generates two cards for dealer and user, one at a time for each.
Returns if card is Ace and the total amount of the cards per person.'''
    userA = 0
    dealA = 0
    card1, cA = genCard(cList, uList)
    userA += cA
    card2, cA = genCard(cList, dList)
    dealA += cA
    card3, cA = genCard(cList, uList)
    userA += cA
    card4, cA = genCard(cList, dList)
    dealA += cA
    return getAmt(card1) + getAmt(card3), userA, getAmt(card2) + getAmt(card4), dealA
