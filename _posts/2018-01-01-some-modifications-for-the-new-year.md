---
layout: post
title:  "Some modifications for the New Year"
date:   2018-01-01 15:42:39 +0000
categories: blog
excerpt_separator: <!--more-->
thumbnail_file_name: 'WP_20180101_15_40_22_Pro.jpg'
thumbnail_alt: 'Some modifications for the New Year'
author: cosma
---


Some modifications for the New Year

We have decided to make some modifications to my bot for better standardisation and code sharing.
<!--more-->

Following a long discussion we have decided that it makes sense that, moving forward, the bots should be as closely aligned as possible.  This will still allow us to develop and test different strategies, but will make code sharing easier.

As can be seen from the image below by Pi is connected to the UltraSonic sensors directly (via the ribbon cable).  

<img src="/assets/images/sz_large/WP_20180101_15_40_22_Pro.jpg" alt="DalekBot V2 Prior to clean up" >

This made sense in the initial development phase, but has led to the situation that I am running out of pins on the GPIO.

Phil has built and tested an alternative approach that uses an Arduino to “talk” to the sensors, and the Pi queries the Arduino (over SPI) every time it needs a distance measure.  This uses 4 pins, instead if the 8 I am currently using.  This may not sound like much of an improvement, but you need to understand that this approach is driving 4 sensors instead of the 3 that I am using and will require no more pin usage, even if we add more sensors, whereas my approach will require 2 more pins per additional sensor.

The following diagrams show my current pin usage and my colleagues (Phil) pin usage that I will have to replicate (and then modify my code to match).
<div class="mdl-grid">
  <div class="mdl-cell mdl-cell--6-col-desktop mdl-cell--6-col-tablet mdl-cell--12-col-phone ">
    <img src="/assets/images/sz_small/Pin_Usage01_Cos.jpg" alt="My Pin Usage" >
  </div>
  <div class="mdl-cell mdl-cell--6-col-desktop mdl-cell--6-col-tablet mdl-cell--12-col-phone ">
    <img  src="/assets/images/sz_small/Pin_Usage_Phil.jpg" alt="Phil’s Pin Usage" >
  </div>
</div>
As can be seen, I will need to make the following moves:

<img  class="mdl-cell mdl-cell--6-col-desktop mdl-cell--6-col-tablet mdl-cell--12-col-phone " src="/assets/images/sz_large/Cos_Pin_Swaps.jpg" alt="Cos Pin Swaps" width="50">

I will then have to make the code changes to make it work.

On top of that I want to swap from using a WiiMote to using a PS3 controller (Christmas present to myself) as it has more buttons.

Wish me luck!

about an hour later....

Changes made and it seems to work!!

Now I need to work out what to do with all these wires :)

<img src="/assets/images/Processed/WP_20180101_18_12_11_Pro.jpg" alt="Spare bits">

I am actually waiting for some female header connectors to get here from China so I can build a controller board for the Ultrasonic sensor array. My initial thought is to mount it above the current board (removing the ribbon cable and directly connecting to the pins).  One consideration is that I do need to be able to remove the sensor array.

Another possible alternative is to install the UltraSonic sensors permanently, much in the same way as Phil has done (by drilling holes in the sides of the body).  All my batteries and speaker are hidden under there, so I would need to decide if there is space.  Another small issue-ette is that I have run out of sensors so I would need to get some more ordered ASAP.  Oh the pain! 

There are pros and cons to relocating the sensors.  Yes, they would be safer and less prone to being damaged and yes, I could leave them connected permanently, but having the side sensors ahead of the body could be advantageous for the Minimal Maze.  I think some testing is in order.

But first I need to get the board built and working.  Also I need to get the control modified for the PS3 Controller.

Better see the family now before they think I have been abducted.
  