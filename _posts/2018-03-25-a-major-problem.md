---
layout: post
title:  "A Major Problem"
date:   2018-03-25 12:33:39 +0000
categories: blog
excerpt_separator: <!--more-->
thumbnail_file_name: 'WP_20180128_21_15_22_Pro.jpg'
thumbnail_alt: 'A major problem'
author: cosma
---

A Major Problem

A rash decision causes an extended period of down time.

<!--more-->

Following a long discussion we decided that it makes sense that, moving forward, the bots should be as closely aligned as possible...

Using a schematic produced by Phil I made my own version of the sensor pod.  I had to modify the design as my sensors are in a pod at the front and Phils are spread around the machine.  The end result can be seen here.  On the right, we have an Arduino and on the left is a 10 Degrees of Freedom (10DoF) sensor that helps the bot to know where it is facing (useful when turning corners).

<img src="/assets/images/sz_large/WP_20180128_21_15_22_Pro.jpg" alt="SPI Interface for sensors" >

The GPIO SPI pins conflict with the motor control pins I have been using and so, in keeping with the standardisation plan, I decided to move my pins to keep in line with Phils.

At the January meeting of Hack Horsham, I decided to start making some of the modifications that would allow me to run the new code base.  Doing this at an HH meeting was not the cleverest of choices.  

I, somewhat stupidly, started moving connections about without shutting the Pi down.  To cut a long story short, the Pi hung and would not boot anymore!

I thought I had borked the SD card.  We tested it on a different Pi and it worked!  So I tried to boot my Pi from a different card.  No go! 
It seemed to me, at that point, that I probably had a short somewhere.

There now follows a period of brain fart on my part.  I spent a good month trying to clone the SD card from my bot, in the belief that it had "issues".  In the end, I managed to use a Pi to DD an image of the card to my server and then DD it back to a new card.

This was a great bit of learning for me and I can now take Linux images across my network.  This is a useful skill, but really gets me nowhere with my problem.   

I tested my new card in the original Pi (no good) and a different Pi (it boots).  I decided to disconnect everything from the Pi and test again.  No difference.

Finally, the fog started to clear from my brain and I realised that the problem was with the  Pi on my bot!  I swapped it out and, hey presto, things started to work.  After some fiddling, with the power off, my bot now connects to a PS3 controller and can read the sensors or, more specifically, ask the Arduino for the current sensor data.

So what have I learned?  Well...  Connecting to the Pi's GPIO while the Pi is turned on is a really bad idea.  I seem to have cooked a Pi 3 by trying to be clever and save some time by not shutting down while moving things about.

So what next?  Well, Phil has managed to continue working on the bot body and has it starting to look good.  He has built it to use a Pi cam instead of a webcam, and so I need to revise the master code branch to use the Pi cam.  Fortunately, the original code was written for Pi cam and so that should not be too big a problem.  

Watch this space for future Updates...