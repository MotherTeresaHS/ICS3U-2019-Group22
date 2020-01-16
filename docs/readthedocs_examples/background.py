#!/usr/bin/env python3

# Created by: Douglass Jeffrey
# Created on: Dec 2019
# This file is an example of how to create the chicken sprites


def game_scene():

    image_bank_2 = stage.Bank.from_bmp16("egg_collector_image_bank_test.bmp")

    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_2, constants.SCREEN_GRID_X,
                            constants.SCREEN_GRID_Y)

    
    # list to create plants at the bottom of the screen
    plants = []
    # procedurally generating grass
    for grass_number in range(0, 10):
        a_single_grass = stage.Sprite(image_bank_2, 5, constants.GRASS_POINT
                                      + increaser, 128 - 16)
        plants.append(a_single_grass)
        increaser += 16

    # list to hold all trunk sprites
    trunk = []

    trunkL = stage.Sprite(image_bank_2, 6, constants.SPRITE_SIZE * 4, 112)
    trunk.append(trunkL)

    trunkR = stage.Sprite(image_bank_2, 7, constants.SPRITE_SIZE * 5, 112)
    trunk.append(trunkR)

    trunkM = stage.Sprite(image_bank_2, 8, 72, 96)
    trunk.append(trunkM)

    trunkM2 = stage.Sprite(image_bank_2, 8, 72, 80)
    trunk.append(trunkM2)

    trunk_branchL = stage.Sprite(image_bank_2, 9,
                                 constants.SPRITE_SIZE * 4, 64)
    trunk.append(trunk_branchL)

    trunk_branchR = stage.Sprite(image_bank_2, 10,
                                 constants.SPRITE_SIZE * 5, 64)
    trunk.append(trunk_branchR)

    # list to hold all leaf/foliage sprites
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

if __name__ == "__main__":
    game_scene()