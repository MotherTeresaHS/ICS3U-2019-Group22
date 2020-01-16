#!/usr/bin/env python3

# Created by: Douglass Jeffrey
# Created on: Dec 2019
# This file is an example of how to create the chicken sprites


def game_scene():

    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()
        # print(keys)

        # sets button states
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

        # if right D-Pad is pressed
        if keys & ugame.K_RIGHT != 0:
            # if chicken moves off right screen, move it back
            if chickenR.x > constants.SCREEN_X - constants.SPRITE_SIZE:
                chickenR.x = 0
            # else move chicken right
            else:
                # if chickenL is onscreen and right d-pad is pressed
                    # replace chickenL with chickenR
                if chickenL.x > 0:
                    chickenR.move(chickenL.x, chickenL.y)
                    chickenL.move(constants.OFF_SCREEN_X,
                                  constants.OFF_SCREEN_Y)
                    # once chicken is faced in direction of pressed d-pad
                    #    move chicken that way
                    chickenR.move(chickenR.x + chicken_speed, chickenR.y)
                else:
                    # if chickenL isnt onscreen and right d-pad is
                    #    pressed move chickenR
                    chickenR.move(chickenR.x + chicken_speed, chickenR.y)

        # if left D-Pad is pressed
        if keys & ugame.K_LEFT != 0:
            # if chicken moves off left screen, move it back
            if chickenL.x < 0 and chickenL.y != constants.OFF_SCREEN_Y:
                chickenL.x = constants.SCREEN_X
            # else move chicken left
            else:
                # if chickenR is onscreen and left d-pad is pressed replace
                #    chickenL with chickenL
                if chickenR.x > 0:
                    chickenL.move(chickenR.x, chickenR.y)
                    chickenR.move(constants.OFF_SCREEN_X,
                                  constants.OFF_SCREEN_Y)
                    # once chicken is faced in direction of pressed d-pad
                    #    move chicken that way
                    chickenL.move(chickenL.x - chicken_speed, chickenL.y)
                else:
                    # if chickenR isnt onscreen and left d-pad is
                    #    pressed move chickenL
                    chickenL.move(chickenL.x - chicken_speed, chickenL.y)


        # if A Button (speed) is pressed
        if a_button == constants.button_state["button_still_pressed"]:
            chicken_speed += 1
            # increase speed at which chicken moves
            if chicken_speed > 3:
                chicken_speed = 3

        # if A Button (speed) is not pressed
        if a_button == constants.button_state["button_up"]:
            chicken_speed = 2


if __name__ == "__main__":
    game_scene()