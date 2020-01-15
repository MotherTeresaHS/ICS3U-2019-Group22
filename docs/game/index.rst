.. _game:

****
Game
****

This section contains the logic you will need to create your version of the Egg Collector Game. Other functions that the game requires will be explained in their respective sections.

Chicken(s)

In Egg Collector the main playable character is a chicken who moves to collect the egg and avoid the bombs descending the screen. The sprite list I made contains a left facing chicken and a right one, and if you wish to make your chicken sprite turn one must swap the chickens every movement and run checks on both of them while they are on screen to determine if a bomb or egg touches either. So in order to make the chickens we must first generate sprites sprite in the game scene outside of the game loop. Always remember to render the layers and set which appear above the others in your game scene with your background always at the back. I set my chicken sprites as the foremost layer at the end of the scene outside of the game loop and created it like this :

.. code-block:: python
  :linenos:
  
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
  
   


I made sure to append it to a list and refresh it as well as the bomb and egg sprites 60 times per second inside of the game loop.

Because the chicken has to save the falling eggs, I allow it to move left and right based on user input. I also chose to allow the chicken to move past one side of the screen and appear at the other but having something like that in your game is up to you. To move the chicken I had the user press the d-pad pertaining to the direction they wish to travel in. To do this I set up an if statement using the button states that were declared in our constants file. The if statement first checks if the chicken is touching an edge of the screen and moves it if it is not. If you dont want to include this piece of code, moving the chicken can be as simple as: if X button pressed: chickenR.move(chickenR.x + chicken_speed, chickenR.y). An example of my code for moving the chicken can be found here (I also added a speed button ) : 

.. code-block:: python
  :linenos:
    
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
  
  
Eggs and Bombs

In Egg Collector, both eggs and bombs rain down from the sky as the chicken (your player character) attempts to catch them by moving along the ground and positioning itself underneath them. In my version of the game, catching an egg awards the player with one point, and missing one deducts two. Missing a bomb awards no points but catching one ends the game. First and foremost, in order to make the eggs rain down from the sky, an extra function is required for each to reposition them above the screen once they finish moving across the screen: These functions found here https://github.com/Douglass-Jeffrey/ICS3U-2019-Group22/blob/master/readthedocs_examples/egg%2Bbomb_function_example.py should be placed inside of the game scene but before the game loops.

Next we need to generate the eggs and bombs and place them in their respective lists by using for loops like this https://github.com/Douglass-Jeffrey/ICS3U-2019-Group22/blob/master/readthedocs_examples/eggs%2Bbombs_generation_example.py these loops simply append the amount of eggs you choose to be in your game into a list and places them off screen. 

In order to determine if the eggs are touching the bottom of the screen, one must make a loop in the game loop to check whether or not they are in contact with the screen Y value (bottom of screen). This loop can be found here: https://github.com/Douglass-Jeffrey/ICS3U-2019-Group22/blob/master/readthedocs_examples/egg%2Bbomb_offscreen_falling_demo.py . I added many other things like increase in bomb and egg speed and some sounds to signify when they touch the bottom of the screen but that design choice is entirely up to the creator. From here making the eggs and bombs rain down is simple enough, I added an else to the if statement which determines if the bombs are touching the ground to allow them to continue moving at a specific speed if they are not touching the ground.

The final piece of logic determines if the eggs and bombs touch the chicken. What happens when they touch is a decision the creator must make but the main part of the logic remains the same nonetheless. To determine when the eggs and bombs touch the chicken, we will be defining the area of each sprite onscreen then using an if statement and stage.collide to determine if any of the 16X16 sprites overlap eachother at any given moment. Here is an example from my version of the game : https://github.com/Douglass-Jeffrey/ICS3U-2019-Group22/blob/master/readthedocs_examples/egg%2Bbomb_collision_demo.py

Score

The score system in egg collector relies upon catching the eggs in my version of the game. This part of the code is honestly your choice whether or not you wish to include it or how you wish to include it. Firstly I set the score variable to 0 at the top of my function. Then set up where the score text would appear in my game, chose the pallette its text would use and formatted it. I didnt forget to set its layer above the background to allow it to actually show up, and I remembered to render it along with the chicken eggs and bombs in the game loop. I set the score up so that whenever an egg is caught it would increase by one and whenever an egg was lost it would decrease by 2. This is done in the collision detection loops. Here is how I set up score in my version of the game: https://github.com/Douglass-Jeffrey/ICS3U-2019-Group22/blob/master/readthedocs_examples/score_example.py

.. toctree::
   :maxdepth: 1
   :glob:

   Background <background>
   Space Ship <space_ship>
