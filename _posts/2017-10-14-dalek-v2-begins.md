---
layout: post
title:  "Dalek V2 Begins..."
date:   2017-10-14 09:20:39 +0000
categories: blog
excerpt_separator: <!--more-->
thumbnail_file_name: '111.jpg'
thumbnail_alt: 'Dalek V1'
author: cosma
---


Dalek V2 Begins...
<!--more-->

This year we were armed with some observations from last year’s Pi Wars.  It was very apparent that going with caterpillar tracks (at least of the type we had previously used) was not going to work.  We also realised that we had nowhere near enough ground clearance for some of the tasks.

It was decided that we were going to 3D print the body this time.  An initial design was made and printed.

<img src="/assets/images/sz_large/202.jpg" alt="Initial construction" >

But some very basic testing proved that it was far too small and was going to be too weak, with nowhere near enough space for our requirements.

<img src="/assets/images/sz_large/203.jpg" alt="Initial construction" >

A second, simpler, sturdier version was designed and printed.

<img src="/assets/images/sz_large/201.jpg" alt="Initial construction" >

<img src="/assets/images/sz_large/204.jpg" alt="Initial construction" >

<img src="/assets/images/sz_large/205.jpg" alt="Initial construction" >

This one was sturdier and had plenty of space.  We had already decided on 4-WD for better power, this would require 2 motor controllers and more batteries (we went with 8 rechargeable AA’s).

<img src="/assets/images/sz_large/206.jpg" alt="Initial construction" >

At this point it struck us that we should make sure that we were within the rules in terms of size!

<img src="/assets/images/sz_large/207.jpg" alt="Initial construction" >

<img src="/assets/images/sz_large/208.jpg" alt="Initial construction" >

<img src="/assets/images/sz_large/209.jpg" alt="Initial construction" >

<img src="/assets/images/sz_large/210.jpg" alt="Initial construction" >

We breathed a collective sigh of relief when we discovered we were (by the skin of our teeth).

We decided that we needed a new motor controller module, as the one we had only worked for 2 wheel drive and steering.  We wrote one and started to test it.

<div class="videoWrapper">
    <!-- Copy & Pasted from YouTube -->
<iframe width="560" height="315" src="https://www.youtube.com/embed/gXLWULd3ya8" frameborder="0" gesture="media" allow="encrypted-media" allowfullscreen></iframe></div>

As you can see, the bot moves (which is a good thing), but very poorly.

After much head scratching and crying we made a break through.  Extra batteries were added (now up to 16!), they were moved to underneath the bot (for stability) and also a speaker and amp were added for sound effects.

<img src="/assets/images/sz_large/214.jpg" alt="More POWER!!!" >

We also added some voltage monitors and a pHat as a status indicator.  With all the extra batteries we installed a MoPi.  This allows us to use the 2 banks of batteries as fall-back for each other and power the Pi up and down cleanly, without having a screen attached.  The MoPi regulates the 2 12v battery banks so the Pi only gets the 5V it needs.  It transpires that the MoPi is not fully compatible with a Pi 3, but it works well enough for our needs.

<img src="/assets/images/sz_large/215.jpg" alt="Rearranged" >

We also modified the motor controller module so that it now works!!

Time to work on the tasks!.

