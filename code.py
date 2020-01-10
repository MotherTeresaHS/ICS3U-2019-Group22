#!/usr/bin/env python3

# Created by: Douglass Jeffrey
# Created on: Dec 2019
# This file is the "Egg Collector" game
#   for CircuitPython

import ugame
import stage
import board
import time
import random

import constants


def blank_white_reset_scene():
    # THIS IS COMPLETE
    # this function is the splash scene game loop

    # do house keeping to ensure everythng is setup

    # reset sound to be off
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    # an image bank for CircuitPython
    image_bank_1 = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_1, 160, 120)

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input

        # update game logic

        # Wait for 1/2 seconds
        time.sleep(0.5)
        mt_splash_scene()

        # redraw sprite list

def mt_splash_scene():
    # THIS IS COMPLETE
    # this function is the MT splash scene

    # an image bank for CircuitPython
    image_bank_1 = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_1, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    # used this program to split the iamge into tile: https://ezgif.com/sprite-cutter/ezgif-5-818cdbcc3f66.png
    background.tile(2, 2, 0)  # blank white
    background.tile(3, 2, 1)
    background.tile(4, 2, 2)
    background.tile(5, 2, 3)
    background.tile(6, 2, 4)
    background.tile(7, 2, 0)  # blank white

    background.tile(2, 3, 0)  # blank white
    background.tile(3, 3, 5)
    background.tile(4, 3, 6)
    background.tile(5, 3, 7)
    background.tile(6, 3, 8)
    background.tile(7, 3, 0)  # blank white

    background.tile(2, 4, 0)  # blank white
    background.tile(3, 4, 9)
    background.tile(4, 4, 10)
    background.tile(5, 4, 11)
    background.tile(6, 4, 12)
    background.tile(7, 4, 0)  # blank white

    background.tile(2, 5, 0)  # blank white
    background.tile(3, 5, 0)
    background.tile(4, 5, 13)
    background.tile(5, 5, 14)
    background.tile(6, 5, 0)
    background.tile(7, 5, 0)  # blank white

    text = []

    text1 = stage.Text(width=29, height=14, font=None, palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text1.move(20, 10)
    text1.text("MT Game Studios")
    text.append(text1)

    text2 = stage.Text(width=29, height=14, font=None, palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text2.move(35, 110)
    text2.text("PRESS START")
    text.append(text2)

    # get sound ready
    # follow this guide to convert your other sounds to something that will work
    #    https://learn.adafruit.com/microcontroller-compatible-audio-file-conversion
    coin_sound = open("coin.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(coin_sound)

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = text + [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input

        # update game logic

        # Wait for 1 seconds
        time.sleep(1.0)
        game_splash_scene()

        # redraw sprite list

def game_splash_scene():
    # Done dont touch
    # this function is the game splash scene

    # an image bank for CircuitPython
    image_bank_2 = stage.Bank.from_bmp16("egg_collector_image_bank_test.bmp")

    background = stage.Grid(image_bank_2, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    # displays text onscreen
    text = []

    text1 = stage.Text(width=40, height=20, font=None, palette=constants.SCORE_PALETTE, buffer=None)
    text1.move(35, 10)
    text1.text("Produced By")
    text.append(text1)

    text2 = stage.Text(width=29, height=14, font=None, palette=constants.SCORE_PALETTE, buffer=None)
    text2.move(19, 110)
    text2.text("Douglass Jeffrey")
    text.append(text2)

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = text + [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input

        # update game logic

        # Wait for 1 seconds
        time.sleep(1.0)
        main_menu_scene()

        # redraw sprite list


def main_menu_scene():
    # this function is the game scene
    
    # variables
    increaser = 0

    def show_egg():
        # I know this is a function that is using variables outside of itself!
        #   BUT this code is going to be used in 2 places :)
        # make an alien show up on screen in the x-axis
        for egg_number in range(len(eggs)):
            if eggs[egg_number].x < 0: # meaning it is off the screen, so available to move on the screen
                eggs[egg_number].move(random.randint(0 + constants.SPRITE_SIZE, constants.SCREEN_X - constants.SPRITE_SIZE), constants.OFF_TOP_SCREEN)
                break

    image_bank_2 = stage.Bank.from_bmp16("egg_collector_image_bank_test.bmp")

    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_2, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    # displays text onscreen
    text = []

    text1 = stage.Text(width=40, height=20, font=None, palette=constants.SCORE_PALETTE, buffer=None)
    text1.move(35, 10)
    text1.text("EGG COLLECTOR")
    text.append(text1)

    text2 = stage.Text(width=29, height=40, font=None, palette=constants.SCORE_PALETTE, buffer=None)
    text2.move(1, 100)
    text2.text("PRESS START TO BEGIN")
    text.append(text2)

    plants = []

    for grass_number in range(0, 10):
        a_single_grass = stage.Sprite(image_bank_2, 5 , constants.GRASS_POINT + increaser , 128 - 16)
        plants.append(a_single_grass)
        increaser += 16

    trunk = []
    
    trunkL = stage.Sprite(image_bank_2, 6, constants.SPRITE_SIZE * 4, 112)
    trunk.append(trunkL)
    
    trunkR = stage.Sprite(image_bank_2, 7, constants.SPRITE_SIZE * 5, 112)
    trunk.append(trunkR)

    trunkM = stage.Sprite(image_bank_2, 8, 72, 96)
    trunk.append(trunkM)
    
    trunkM2 = stage.Sprite(image_bank_2, 8, 72, 80)
    trunk.append(trunkM2)
    
    trunk_branchL = stage.Sprite(image_bank_2, 9, constants.SPRITE_SIZE * 4, 64)
    trunk.append(trunk_branchL)
    
    trunk_branchR = stage.Sprite(image_bank_2, 10, constants.SPRITE_SIZE * 5, 64)
    trunk.append(trunk_branchR)

    foliage = []

    foliageLBB = stage.Sprite(image_bank_2, 12, 60, 59)
    foliage.append(foliageLBB)
    
    foliageRBB = stage.Sprite(image_bank_2, 11, 84, 59)
    foliage.append(foliageRBB)

    foliageLMB = stage.Sprite(image_bank_2, 13, constants.SPRITE_SIZE * 4, 50)
    foliage.append(foliageLMB)
    
    foliageRMB = stage.Sprite(image_bank_2, 13, constants.SPRITE_SIZE * 5, 50)
    foliage.append(foliageRMB)

    foliageLLB = stage.Sprite(image_bank_2, 12, constants.SPRITE_SIZE * 3, 50)
    foliage.append(foliageLLB)
    
    foliageRRB = stage.Sprite(image_bank_2, 11, constants.SPRITE_SIZE * 6, 50)
    foliage.append(foliageRRB)
    
    foliageLMM = stage.Sprite(image_bank_2, 13, constants.SPRITE_SIZE * 4, 40)
    foliage.append(foliageLMM)
    
    foliageRMM = stage.Sprite(image_bank_2, 13, constants.SPRITE_SIZE * 5, 40)
    foliage.append(foliageRMM)
    
    foliageLLM = stage.Sprite(image_bank_2, 13, constants.SPRITE_SIZE * 3, 40)
    foliage.append(foliageLLM)
    
    foliageRRM = stage.Sprite(image_bank_2, 13, constants.SPRITE_SIZE * 6, 40)
    foliage.append(foliageRRM)
    
    foliageLLLM = stage.Sprite(image_bank_2, 12, 38, 40)
    foliage.append(foliageLLLM)
    
    foliageRRRM = stage.Sprite(image_bank_2, 11, 104, 40)
    foliage.append(foliageRRRM)
    
    foliageLLLT = stage.Sprite(image_bank_2, 15, 38, 26)
    foliage.append(foliageLLLT)
    
    foliageRRRT = stage.Sprite(image_bank_2, 14, 104, 26)
    foliage.append(foliageRRRT)
    
    foliageLLMT = stage.Sprite(image_bank_2, 13, 54, 26)
    foliage.append(foliageLLMT)
    
    foliageRRMT = stage.Sprite(image_bank_2, 13, 88, 26)
    foliage.append(foliageRRMT)
    
    foliageLMMT = stage.Sprite(image_bank_2, 13, 70, 26)
    foliage.append(foliageLMMT)
    
    foliageRMMT = stage.Sprite(image_bank_2, 13, 72, 26)
    foliage.append(foliageRMMT)
    
    foliageLLTT = stage.Sprite(image_bank_2, 15, 50, 14)
    foliage.append(foliageLLTT)
    
    foliageRRTT = stage.Sprite(image_bank_2, 14, 91, 14)
    foliage.append(foliageRRTT)
    
    foliageLMTT = stage.Sprite(image_bank_2, 13, 65, 14)
    foliage.append(foliageLMTT)
    
    foliageRMTT = stage.Sprite(image_bank_2, 13, 75, 14)
    foliage.append(foliageRMTT)
    
    foliage_deco_1 = stage.Sprite(image_bank_2, 12, 60, 20)
    foliage.insert(0, foliage_deco_1)
    
    foliage_deco_2 = stage.Sprite(image_bank_2, 11, 80, 30)
    foliage.insert(1, foliage_deco_2)




    sprites = []
    # create a sprite
    # parameters (image bank, image # in bank, x, y)
    chicken = stage.Sprite(image_bank_2, 1, 12, 8 )
    sprites.insert(0, chicken)  # insert at top of sprite list

    eggs = []
    for egg_number in range(constants.TOTAL_NUMBER_OF_EGGS):
        a_single_egg = stage.Sprite(image_bank_2, 3 , constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        eggs.append(a_single_egg)

    egg_count = 1
    show_egg()

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the background layer
    game.layers = sprites + eggs + text + plants + trunk + foliage + [background]
    # render the background
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input
        # update game logic
        keys = ugame.buttons.get_pressed()
        #print(keys)

        if keys & ugame.K_START != 0:  # Start button
            game_scene()
            #break

        for egg_number in range(len(eggs)):
            if eggs[egg_number].x > 0: # meaning it is on the screen
                eggs[egg_number].move(eggs[egg_number].x, eggs[egg_number].y + constants.EGG_SPEED)
                if eggs[egg_number].y > constants.SCREEN_Y:
                    eggs[egg_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                    show_egg() # make it randomly show up at top again

        # redraw sprite list
        game.render_sprites(eggs)
        game.tick()

def game_scene():
    # this function is the game scene

    # game score
    score = 0

    # variables
    increaser = 0
    
    chicken_speed = 1

    # buttons that you want to keep state information on
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    # get sound ready
    coin_sound = open("coin.wav", 'rb')
    boom_sound = open("boom.wav", 'rb')
    big_boom_sound = open("big_boom.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    def show_egg():
        # I know this is a function that is using variables outside of itself!
        #   BUT this code is going to be used in 2 places :)
        # make an alien show up on screen in the x-axis
        for egg_number in range(len(eggs)):
            if eggs[egg_number].x < 0: # meaning it is off the screen, so available to move on the screen
                eggs[egg_number].move(random.randint(0 + constants.SPRITE_SIZE, constants.SCREEN_X - constants.SPRITE_SIZE), constants.OFF_TOP_SCREEN)
                break

    image_bank_2 = stage.Bank.from_bmp16("egg_collector_image_bank_test.bmp")

    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_2, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    # add text at top of screen for score
    score_text = stage.Text(width=29, height=14, font=None, palette=constants.SCORE_PALETTE, buffer=None)
    score_text.clear()
    score_text.cursor(0, 0)
    score_text.move(1, 1)
    score_text.text("Score: {0}".format(score))

    plants = []

    for grass_number in range(0, 10):
        a_single_grass = stage.Sprite(image_bank_2, 5 , constants.GRASS_POINT + increaser , 128 - 16)
        plants.append(a_single_grass)
        increaser += 16

    trunk = []
    
    trunkL = stage.Sprite(image_bank_2, 6, constants.SPRITE_SIZE * 4, 112)
    trunk.append(trunkL)
    
    trunkR = stage.Sprite(image_bank_2, 7, constants.SPRITE_SIZE * 5, 112)
    trunk.append(trunkR)

    trunkM = stage.Sprite(image_bank_2, 8, 72, 96)
    trunk.append(trunkM)
    
    trunkM2 = stage.Sprite(image_bank_2, 8, 72, 80)
    trunk.append(trunkM2)
    
    trunk_branchL = stage.Sprite(image_bank_2, 9, constants.SPRITE_SIZE * 4, 64)
    trunk.append(trunk_branchL)
    
    trunk_branchR = stage.Sprite(image_bank_2, 10, constants.SPRITE_SIZE * 5, 64)
    trunk.append(trunk_branchR)

    foliage = []

    foliageLBB = stage.Sprite(image_bank_2, 12, 60, 59)
    foliage.append(foliageLBB)
    
    foliageRBB = stage.Sprite(image_bank_2, 11, 84, 59)
    foliage.append(foliageRBB)

    foliageLMB = stage.Sprite(image_bank_2, 13, constants.SPRITE_SIZE * 4, 50)
    foliage.append(foliageLMB)
    
    foliageRMB = stage.Sprite(image_bank_2, 13, constants.SPRITE_SIZE * 5, 50)
    foliage.append(foliageRMB)

    foliageLLB = stage.Sprite(image_bank_2, 12, constants.SPRITE_SIZE * 3, 50)
    foliage.append(foliageLLB)
    
    foliageRRB = stage.Sprite(image_bank_2, 11, constants.SPRITE_SIZE * 6, 50)
    foliage.append(foliageRRB)
    
    foliageLMM = stage.Sprite(image_bank_2, 13, constants.SPRITE_SIZE * 4, 40)
    foliage.append(foliageLMM)
    
    foliageRMM = stage.Sprite(image_bank_2, 13, constants.SPRITE_SIZE * 5, 40)
    foliage.append(foliageRMM)
    
    foliageLLM = stage.Sprite(image_bank_2, 13, constants.SPRITE_SIZE * 3, 40)
    foliage.append(foliageLLM)
    
    foliageRRM = stage.Sprite(image_bank_2, 13, constants.SPRITE_SIZE * 6, 40)
    foliage.append(foliageRRM)
    
    foliageLLLM = stage.Sprite(image_bank_2, 12, 38, 40)
    foliage.append(foliageLLLM)
    
    foliageRRRM = stage.Sprite(image_bank_2, 11, 104, 40)
    foliage.append(foliageRRRM)
    
    foliageLLLT = stage.Sprite(image_bank_2, 15, 38, 26)
    foliage.append(foliageLLLT)
    
    foliageRRRT = stage.Sprite(image_bank_2, 14, 104, 26)
    foliage.append(foliageRRRT)
    
    foliageLLMT = stage.Sprite(image_bank_2, 13, 54, 26)
    foliage.append(foliageLLMT)
    
    foliageRRMT = stage.Sprite(image_bank_2, 13, 88, 26)
    foliage.append(foliageRRMT)
    
    foliageLMMT = stage.Sprite(image_bank_2, 13, 70, 26)
    foliage.append(foliageLMMT)
    
    foliageRMMT = stage.Sprite(image_bank_2, 13, 72, 26)
    foliage.append(foliageRMMT)
    
    foliageLLTT = stage.Sprite(image_bank_2, 15, 50, 14)
    foliage.append(foliageLLTT)
    
    foliageRRTT = stage.Sprite(image_bank_2, 14, 91, 14)
    foliage.append(foliageRRTT)
    
    foliageLMTT = stage.Sprite(image_bank_2, 13, 65, 14)
    foliage.append(foliageLMTT)
    
    foliageRMTT = stage.Sprite(image_bank_2, 13, 75, 14)
    foliage.append(foliageRMTT)
    
    foliage_deco_1 = stage.Sprite(image_bank_2, 12, 60, 20)
    foliage.insert(0, foliage_deco_1)
    
    foliage_deco_2 = stage.Sprite(image_bank_2, 11, 80, 30)
    foliage.insert(1, foliage_deco_2)

    sprites = []
    # create a sprite
    # parameters (image bank, image # in bank, x, y)
    chicken = stage.Sprite(image_bank_2, 1, 80, 128 - constants.SPRITE_SIZE)
    sprites.insert(0, chicken)  # insert at top of sprite list

    eggs = []
    for egg_number in range(constants.TOTAL_NUMBER_OF_EGGS):
        a_single_egg = stage.Sprite(image_bank_2, 3 , constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        eggs.append(a_single_egg)

    egg_count = 1
    show_egg()

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the background layer
    game.layers = sprites + eggs + plants + trunk + foliage + [score_text] + [background]
    # render the background
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()
        #print(keys)

        if keys & ugame.K_X != 0:  # A button
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                a_button = constants.button_state["button_up"]

        # update game logic

        # if right D-Pad is pressed
        if keys & ugame.K_RIGHT != 0:
            # if chicken moves off right screen, move it back
            if chicken.x > constants.SCREEN_X - constants.SPRITE_SIZE:
                chicken.x = constants.SCREEN_X - constants.SPRITE_SIZE
            # else move chicken right
            else:
                chicken.move(chicken.x + chicken_speed, chicken.y)

        # if left D-Pad is pressed
        if keys & ugame.K_LEFT != 0:
            # if chicken moves off left screen, move it back
            if chicken.x < 0:
                chicken.x = 0
            # else move chicken left
            else:
                chicken.move(chicken.x - chicken_speed, chicken.y)

        # if A Button (speed) is pressed
        if a_button == constants.button_state["button_still_pressed"]:
            chicken_speed += 1
            if chicken_speed > 3:
                chicken_speed = 3

        # if A Button (speed) is not pressed
        if a_button == constants.button_state["button_up"]:
            chicken_speed = 2

        for egg_number in range(len(eggs)):
            if eggs[egg_number].x > 0: # meaning it is on the screen
                eggs[egg_number].move(eggs[egg_number].x, eggs[egg_number].y + constants.EGG_SPEED)
                if eggs[egg_number].y > constants.SCREEN_Y:
                    eggs[egg_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                    score = score - 2
                    score_text.clear()
                    score_text.cursor(0, 0)
                    score_text.move(1, 1)
                    score_text.text("Score: {0}".format(score))
                    # this will freeze the screen for a split second, but we have no option
                    game.render_block()
                    # play sound effect
                    sound.stop()
                    sound.play(boom_sound)
                    show_egg()
                    if score < 0:
                        game_over_scene(score)
        
        
        
        # each frame check if any of the eggs are touching the chicken
        for egg_number in range(len(eggs)):
            if eggs[egg_number].x > 0:
                # https://circuitpython-stage.readthedocs.io/en/latest/#stage.collide
                # and https://stackoverflow.com/questions/306316/determine-if-two-rectangles-overlap-each-other
                if stage.collide(eggs[egg_number].x + 1, eggs[egg_number].y,
                                 eggs[egg_number].x + 15, eggs[egg_number].y + 15,
                                 chicken.x, chicken.y,
                                 chicken.x + 15, chicken.y + 15):
                    eggs[egg_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                    score += 1
                    score_text.clear()
                    score_text.cursor(0, 0)
                    score_text.move(1, 1)
                    score_text.text("Score: {0}".format(score))
                    # this will freeze the screen for a split second, but we have no option
                    game.render_block()
                    # play sound effect
                    sound.stop()
                    sound.play(coin_sound)
                    show_egg()




                    # alien hit the ship
                    #sound.stop()
                    #sound.play(coin_sound)
                    #time.sleep(4.0)
                    #sound.stop()
                    #game_over_scene(final_score)


        # redraw sprite list
        game.render_sprites(eggs + sprites)
        game.tick()


def game_over_scene(score):
    # this function is the game over scene

    # repeat forever, game loop
    while True:
        # get user input

        # update game logic

        # redraw sprite list
        pass # just a placeholder until you write the code


if __name__ == "__main__":
    blank_white_reset_scene()