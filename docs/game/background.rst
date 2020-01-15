.. _background:

Background
==========

The background for Egg Collector is quite complex and includes many sprites. When I refer to the background I refer to everything that happens behind the actual game (including the large tree). Although the complexity varies, one thing remains true in all scenes except the MT games splash screen; they all utilise the first image in the egg collector bank as a canvas for the sprites to be drawn on. To use the Egg Collector image bank, I made sure to set it to a variable in each scene so I could pick out whichever 16X16 sprite I wanted from it. Once I got this out of the way, I made sure to set my background to image 0 in the bank to allow the blue sky to appear. After this I created lists for the different parts of the tree and started appending sprites to them to draw my large tree on screen. I created 3 arrays each for different parts of the background and had them show up in a specific order by setting the layers in my preferred way. 

Grass

To make the grass on the ground I created a for loop to create grass sprites at intervals of 16 from 0 (the leftmost point on the screen) to 160 (the rightmost point)

Tree Trunk

To create the tree trunk, I created the right and left bases facing eachother in the center of the screen. I then created the middle of the trunk on top and in the middle of the two base sprites before adding two branch sprites facing each other above the middle of the trunk sprite and at the saem x values as he two base sprites.

Foliage

To create the leaves on the trees I experimented with many different sprites until i found something i thought looked decent. The trick I used was to not make the leaf sprites completely symmetrical.

If you want to use my background instead of experimenting yourself, it can be found here: 

