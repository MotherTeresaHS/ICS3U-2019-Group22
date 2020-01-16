#!/usr/bin/env python3

# Created by: Douglass Jeffrey
# Created on: Dec 2019
# This file is an example of how to to make eggs and bombs collide with 
#   a chicken sprite


def game_scene():

    while True:

        # each frame check if any of the eggs are touching ChickenR
        for egg_number in range(len(eggs)):
            if eggs[egg_number].x > 0 and chickenR.x > 0:
                # https://circuitpython-stage.readthedocs.io/en/latest/#
                #    stage.collide
                # and https://stackoverflow.com/questions/306316/determine
                #   -if-two-rectangles-overlap-each-other
                if stage.collide(eggs[egg_number].x + 1, eggs[egg_number].y,
                                 eggs[egg_number].x + 15,
                                 eggs[egg_number].y + 15,
                                 chickenR.x, chickenR.y,
                                 chickenR.x + 15, chickenR.y + 15):
                    eggs[egg_number].move(constants.OFF_SCREEN_X,
                                          constants.OFF_SCREEN_Y)
                    score += 1
                    score_text.clear()
                    score_text.cursor(0, 0)
                    score_text.move(1, 1)
                    score_text.text("Score: {0}".format(score))
                    # this will freeze the screen for a split second,
                    #    but we have no option
                    game.render_block()
                    # play sound effect
                    sound.stop()
                    sound.play(coin_sound)
                    show_egg()
                    show_egg()
                    egg_count = egg_count + 1

            # each frame check if any of the eggs are touching ChickenL
            if eggs[egg_number].x > 0 and chickenL.x > 0:
                # check if any of the eggs are touching ChickenR
                if stage.collide(eggs[egg_number].x + 1, eggs[egg_number].y,
                                 eggs[egg_number].x + 15,
                                 eggs[egg_number].y + 15,
                                 chickenL.x, chickenL.y,
                                 chickenL.x + 15, chickenL.y + 15):
                    eggs[egg_number].move(constants.OFF_SCREEN_X,
                                          constants.OFF_SCREEN_Y)
                    score += 1
                    score_text.clear()
                    score_text.cursor(0, 0)
                    score_text.move(1, 1)
                    score_text.text("Score: {0}".format(score))
                    # this will freeze the screen for a split second, but we
                    #    have no option
                    game.render_block()
                    # play sound effect
                    sound.stop()
                    sound.play(coin_sound)
                    show_egg()
                    show_egg()
                    egg_count = egg_count + 1

        # each frame check if any of the bombs are touching the chickenR
        for bomb_number in range(len(bombs)):
            if bombs[bomb_number].x > 0 and chickenR.x > 0:
                # https://circuitpython-stage.readthedocs.io/en/latest/#
                #    stage.collide
                # and https://stackoverflow.com/questions/306316/determine
                #    -if-two-rectangles-overlap-each-other
                if stage.collide(bombs[bomb_number].x + 1,
                                 bombs[bomb_number].y,
                                 bombs[bomb_number].x + 15,
                                 bombs[bomb_number].y + 15,
                                 chickenR.x, chickenR.y,
                                 chickenR.x + 15, chickenR.y + 15):
                    bombs[bomb_number].move(constants.OFF_SCREEN_X,
                                            constants.OFF_SCREEN_Y)
                    game.render_block()
                    # play sound effect
                    sound.stop()
                    sound.play(big_boom_sound)
                    time.sleep(5.0)
                    game_over_scene(score)

            # each frame check if any of the bombs are touching the chickenL
            if bombs[bomb_number].x > 0 and chickenL.x > 0:
                # https://circuitpython-stage.readthedocs.io/en/latest/#
                #    stage.collide
                # and https://stackoverflow.com/questions/306316/determine
                #    -if-two-rectangles-overlap-each-other
                if stage.collide(bombs[bomb_number].x + 1,
                                 bombs[bomb_number].y,
                                 bombs[bomb_number].x + 15,
                                 bombs[bomb_number].y + 15,
                                 chickenL.x, chickenL.y,
                                 chickenL.x + 15, chickenL.y + 15):
                    bombs[bomb_number].move(constants.OFF_SCREEN_X,
                                            constants.OFF_SCREEN_Y)
                    game.render_block()
                    # play sound effect
                    sound.stop()
                    sound.play(big_boom_sound)
                    time.sleep(5.0)
                    game_over_scene(score)



if __name__ == "__main__":
    game_scene()