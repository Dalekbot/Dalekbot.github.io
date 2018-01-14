---
layout: post
title:  "Dalek V2a Begins..."
date:   2017-10-14 09:20:39 +0000
categories: blog
excerpt_separator: <!--more-->
thumbnail_file_name: 'DSC_1630.jpg'
thumbnail_alt: 'DalekBot V2a'
author: cosma
---


Dalek V2a Begins...
<!--more-->

Our team is widely dispersed with between Greenwich and Horsham, which makes working together harder.  We have taken the decision to start a second bot, using the same code base, to allow testing of different approaches to the tasks.  Meet DalekBot V2a.

<img src="/assets/images/sz_large/DSC_1630.jpg" alt="DalekBot V2a" >

This bot is based upon the same hardware motor controllers and motors and can, therefore, use the same code (with some minor changes).

In this picture you can see the Magnetometer (the little board on top) and the servo controller (log board on the right with yellow and red connectors).  We have yet to decide if we will be using either one of those to control anything, but it does open up some interesting possibilities. 
<img src="/assets/images/sz_large/DSC_1624.jpg" alt="Magnetometer and Servo Controller" >
In this picture you can see the Ultrasonic distance detectors (the 2 round black items in the side)

<img src="/assets/images/sz_large/DSC_1631.jpg" alt="Ultrasonics" >

There are detectors on all 4 sides which are constantly read by an Arduino.  This frees up some pins on the Pi and reduces its workload somewhat.  This contrasts with the DalekBot V2 which has the detectors on a removable module that sits at the front.
<img src="/assets/images/sz_large/216.jpg" alt="More Ultrasonics" >

Further testing will allow us to decide which is the best approach.

This Video shows the V2a running the new, improved, motor control code.

<div class="videoWrapper">
    <!-- Copy & Pasted from YouTube -->
<iframe width="560" height="315" src="https://www.youtube.com/embed/lDWncYVLexs" frameborder="0" gesture="media" allow="encrypted-media" allowfullscreen></iframe></div>

Now we have the basic bots working we can start to address the code for performing the tasks.
