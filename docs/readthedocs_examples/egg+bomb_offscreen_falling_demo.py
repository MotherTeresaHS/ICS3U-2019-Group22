#!/usr/bin/env python3

# Created by: Douglass Jeffrey
# Created on: Dec 2019
# This file is an example of how to to make eggs move once they reach the bottom
#   of the screen and how to make them fall

def game_scene():

    while True:

        # Egg and bomb speed increaser
        if score > 20 and egg_speed == 1:
            egg_speed += 1
            bomb_speed += 1
        elif score > 40 and egg_speed == 2:
            egg_speed += 1
            bomb_speed += 1
        elif score > 60 and egg_speed == 3:
            egg_speed += 1
            bomb_speed += 1
        elif score > 80 and egg_speed == 4:
            egg_speed += 1
            bomb_speed += 1

        # check if egg falls off the screen
        for egg_number in range(len(eggs)):
            if eggs[egg_number].x > 0:  # meaning it is on the screen
                eggs[egg_number].move(eggs[egg_number].x,
                                      eggs[egg_number].y + egg_speed)
                if eggs[egg_number].y > constants.SCREEN_Y:
                    eggs[egg_number].move(constants.OFF_SCREEN_X,
                                          constants.OFF_SCREEN_Y)
                    score = score - 2
                    score_text.clear()
                    score_text.cursor(0, 0)
                    score_text.move(1, 1)
                    score_text.text("Score: {0}".format(score))
                    # this will freeze the screen for a split second,
                    #    but we have no option
                    game.render_block()
                    # play sound effect
                    sound.stop()
                    sound.play(boom_sound)
                    show_egg()
                    if score < 0:
                        game_over_scene(score)


        # check if bomb falls off the screen
        for bomb_number in range(len(bombs)):
            if bombs[bomb_number].x > 0:  # meaning it is on the screen
                bombs[bomb_number].move(bombs[bomb_number].x,
                                        bombs[bomb_number].y + bomb_speed)
                if bombs[bomb_number].y > constants.SCREEN_Y:
                    bombs[bomb_number].move(constants.OFF_SCREEN_X,
                                            constants.OFF_SCREEN_Y)
                    # this will freeze the screen for a split second,
                    #    but we have no option
                    game.render_block()
                    # play sound effect
                    sound.stop()
                    sound.play(boom_sound)
                    show_bomb()
                    show_bomb()
                    bomb_count = bomb_count + 1


if __name__ == "__main__":
    game_scene()
