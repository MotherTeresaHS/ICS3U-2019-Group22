#!/usr/bin/env python3

# Created by: Douglass Jeffrey
# Created on: Dec 2019
# This file is the contains the egg and bomb moving functions for Egg collector


def game_scene():
    # Function to make eggs reappear at the top of the screen
    def show_egg():
        for egg_number in range(len(eggs)):
            if eggs[egg_number].x < 0:  # meaning it is off the screen,
                eggs[egg_number].move(random.randint(0 + constants.SPRITE_SIZE,
                                                     constants.SCREEN_X -
                                                     constants.SPRITE_SIZE),
                                      constants.OFF_TOP_SCREEN)
                break

    # Function to make bombs reappear at the top of the screen
    def show_bomb():
        for bomb_number in range(len(bombs)):
            if bombs[bomb_number].x < 0:  # meaning it is off the screen
                bombs[bomb_number].move(random.randint
                                        (0 + constants.SPRITE_SIZE,
                                         constants.SCREEN_X -
                                         constants.SPRITE_SIZE),
                                        constants.OFF_TOP_SCREEN
                                        - random.randint(0, 50))
                break


if __name__ == "__main__":
    game_scene()
