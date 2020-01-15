#!/usr/bin/env python3

# Created by: Douglass Jeffrey
# Created on: Dec 2019
# This file is an example of how to create the chicken sprites


def game_scene():

# list to hold chicken sprites
    chickens = []

    # create right chicken sprite
    chickenR = stage.Sprite(image_bank_2, 1, 80, 128 - constants.SPRITE_SIZE)
    chickens.insert(0, chickenR)  # insert at top of sprite list

    # create left chicken sprite
    chickenL = stage.Sprite(image_bank_2, 2, constants.OFF_SCREEN_X,
                            constants.OFF_SCREEN_Y)
    chickens.append(chickenL)

if __name__ == "__main__":
    game_scene()