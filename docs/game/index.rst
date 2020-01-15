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

In Egg Collector, both eggs and bombs rain down from the sky as the chicken (your player character) attempts to catch them by moving along the ground and positioning itself underneath them. In my version of the game, catching an egg awards the player with one point, and missing one deducts two. Missing a bomb awards no points but catching one ends the game. First and foremost, in order to make the eggs rain down from the sky, an extra function is required for each to reposition them above the screen once they finish moving across the screen. These functions are found here:

.. code-block:: python
  :linenos:

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

should be placed inside of the game scene but before the game loops.

Next we need to generate the eggs and bombs and place them in their respective lists by using for loops like this 

.. code-block:: python
  :linenos:
  #!/usr/bin/env python3

  # Created by: Douglass Jeffrey
  # Created on: Dec 2019
  # This file is an example of how to generate eggs and bombs


  def game_scene():

      eggs = []
      # generates eggs to fall from the top of the screen
      for egg_number in range(constants.TOTAL_NUMBER_OF_EGGS):
          a_single_egg = stage.Sprite(image_bank_2, 3, constants.OFF_SCREEN_X,
                                      constants.OFF_SCREEN_Y)
          eggs.append(a_single_egg)

      egg_count = 1
      show_egg()

      # generates bombs to fall from the top of the screen
      bombs = []
      for bomb_number in range(constants.TOTAL_NUMBER_OF_BOMBS):
          a_single_bomb = stage.Sprite(image_bank_2, 4, constants.OFF_SCREEN_X,
                                      constants.OFF_SCREEN_Y)
          bombs.append(a_single_bomb)

      bomb_count = 1
      show_bomb()

  if __name__ == "__main__":
      game_scene()


these loops simply append the amount of eggs you choose to be in your game into a list and places them off screen. 

In order to determine if the eggs are touching the bottom of the screen, one must make a loop in the game loop to check whether or not they are in contact with the screen Y value (bottom of screen). This loop can be found here:

.. code-block:: python
  :linenos:
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


I added many other things like increase in bomb and egg speed and some sounds to signify when they touch the bottom of the screen but that design choice is entirely up to the creator. From here making the eggs and bombs rain down is simple enough, I added an else to the if statement which determines if the bombs are touching the ground to allow them to continue moving at a specific speed if they are not touching the ground.

The final piece of logic determines if the eggs and bombs touch the chicken. What happens when they touch is a decision the creator must make but the main part of the logic remains the same nonetheless. To determine when the eggs and bombs touch the chicken, we will be defining the area of each sprite onscreen then using an if statement and stage.collide to determine if any of the 16X16 sprites overlap eachother at any given moment. Here is an example from my version of the game : 


#!/usr/bin/env python3

# Created by: Douglass Jeffrey
# Created on: Dec 2019
# This file is an example of how to to make eggs and bombs collide with 
#   a chicken sprite

.. code-block:: python
  :linenos:

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


Score

The score system in egg collector relies upon catching the eggs in my version of the game. This part of the code is honestly your choice whether or not you wish to include it or how you wish to include it. Firstly I set the score variable to 0 at the top of my function. Then set up where the score text would appear in my game, chose the pallette its text would use and formatted it. I didnt forget to set its layer above the background to allow it to actually show up, and I remembered to render it along with the chicken eggs and bombs in the game loop. I set the score up so that whenever an egg is caught it would increase by one and whenever an egg was lost it would decrease by 2. This is done in the collision detection loops. Here is how I set up score in my version of the game: 

.. code-block:: python
  :linenos:
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


.. toctree::
   :maxdepth: 1
   :glob:

   Background <background>
   Space Ship <space_ship>
