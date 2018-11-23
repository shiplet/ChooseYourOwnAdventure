#! /usr/bin/env python3

import os
from stories import *

story = story1


def init():
    printStoryCard(0)


def isNumber(num):
    try:
        return int(num)
    except ValueError:
        return False


def waitForChoice(card, choices, notInRange=False):
    if notInRange is True:
        choice = input("Please choose an actual answer > ")
    else:
        choice = input('Which do you choose? > ')

    choice = isNumber(choice)

    if choice is False:
        return waitForChoice(card, choices, True)
    else:
        for key in choices:
            if key == choice:
                return choices[key]['cons']

    waitForChoice(card, choices, True)


def printStoryCard(card=None):
    os.system('clear')
    print(story[card]['text'])
    print("\n")
    if story[card]['choices'] is not False:
        for choice in story[card]['choices']:
            print("\n\t" + str(choice) + ": " +
                  story[card]['choices'][choice]['text'])
    print("\n\n")
    if 'final' in story[card]:
        print("\n\n\n\n\n")
        play = input('\tPlay again? [y/n] > ')
        if play == 'n':
            return
        else:
            init()
    else:
        choice = waitForChoice(card, story[card]['choices'])
        printStoryCard(choice)


init()
