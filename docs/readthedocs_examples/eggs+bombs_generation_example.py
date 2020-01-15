#!/usr/bin/env python3

# Created by: Douglass Jeffrey
# Created on: Dec 2019
# This file is an example of how to generate eggs and bombs


def game_scene():

    eggs = []
    # generates eggs to fall from the top of the screen
    for egg_number in range(constants.TOTAL_NUMBER_OF_EGGS):
        a_single_egg = stage.Sprite(image_bank_2, 3, constants.OFF_SCREEN_X,
                                    constants.OFF_SCREEN_Y)
        eggs.append(a_single_egg)

    egg_count = 1
    show_egg()

    # generates bombs to fall from the top of the screen
    bombs = []
    for bomb_number in range(constants.TOTAL_NUMBER_OF_BOMBS):
        a_single_bomb = stage.Sprite(image_bank_2, 4, constants.OFF_SCREEN_X,
                                     constants.OFF_SCREEN_Y)
        bombs.append(a_single_bomb)

    bomb_count = 1
    show_bomb()

if __name__ == "__main__":
    game_scene()