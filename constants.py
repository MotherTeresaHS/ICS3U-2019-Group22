#!/usr/bin/env python3

# Created by: Douglass Jeffrey
# Created on: January 2020
# This is the constants file for the egg collector game

# CircuitPython screen size is 160x128 and sprites are 16x16
SCREEN_X = 160
SCREEN_Y = 128
SCREEN_GRID_X = 16
SCREEN_GRID_Y = 8
SPRITE_SIZE = 16
OFF_TOP_SCREEN = -1 * SPRITE_SIZE
OFF_BOTTOM_SCREEN = SCREEN_Y + SPRITE_SIZE
GRASS_POINT = 0
TOTAL_NUMBER_OF_EGGS = 3
TOTAL_NUMBER_OF_BOMBS = 3
EGG_SPEED = 1
BOMB_SPEED = 1
OFF_SCREEN_X = -100
OFF_SCREEN_Y = -100
CHICKEN_SPEED = 2

MT_GAME_STUDIO_PALETTE = (b'\xf8\x1f\x00\x00\xcey\x00\xff\xf8\x1f\xff\x19\xfc\xe0\xfd\xe0'
       b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')

SCORE_PALETTE = (b'\xf8\x1f\x00\x00\xcey\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff'
       b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')

# Using for button state
button_state = {
    "button_up": "up",
    "button_just_pressed": "just pressed",
    "button_still_pressed": "still pressed",
    "button_released": "released",
}