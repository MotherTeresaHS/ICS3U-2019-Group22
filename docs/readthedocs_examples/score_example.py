#!/usr/bin/env python3

# Created by: Douglass Jeffrey
# Created on: Dec 2019
# This file is an example of score in egg collector


def game_scene():

    # game score
    score = 0

    # add text at top of screen for score
    score_text = stage.Text(width=29, height=14, font=None,
                            palette=constants.SCORE_PALETTE, buffer=None)
    score_text.clear()
    score_text.cursor(0, 0)
    score_text.move(1, 1)
    score_text.text("Score: {0}".format(score))


if __name__ == "__main__":
    game_scene()