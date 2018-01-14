---
layout: post
title:  "Copy files to Pi"
date:   2017-11-16 09:20:39 +0000
categories: code 
excerpt_separator: <!--more-->
thumbnail_file_name: '2017-12-02.jpg'
thumbnail_alt: 'a picture of something'
author: phil
---

Writing code directly  on the Raspberry Pi is fine when writing small scripts, but when your codebase gets bigger and more time has been invested into it, the better option is to work from a remote computer.
<!--more-->

The problem with working from a remote computer is yet another step in the tool chain to break the flow.

Working with web technology this problem has more or less been fixed over the past few years with tools like grunt, gulp and webpack, so while working on the Dalekbot project I thought I should use one of these tool to make life easier.

My setup is a Windows 10 PC, and I have installed [samba on the Raspberry Pi](https://www.raspberrypi.org/magpi/samba-file-server/) and have a share folder available it the Networks folder in file explorer on the PC.

Next you need to have node.js installed on your PC
from powershell run the command

```powershell
> node -v
```

You should get somthing like this as a result.


```powershell
C:\Users\userame> node -v
v9.2.0
C:\Users\username>
```

If you get and error then install [node.js from here](https://nodejs.org/en/)

Now clone or download my [copy-to-pi repo from github](https://github.com/philstenning/Copy-To-Pi) to your working folder on your PC, extract it if you downloaded the zip file. 

You need powershell to navigate to the root folder of this project or type in the full file path, so I use file explorer to navigate to it

![screen shot](/assets/images/sz_large/2017-12-02.jpg)

 Then type 'powershell' in the address bar, hit enter and it opens  to the folder for you.

![screen shot](/assets/images/sz_large/2017-12-01.jpg)

You already have npm installed as is comes with node.js, so you can install the node_modules needed by running the command  

```powershell
> npm install
```

Edit the gulpfile.js to the networked folder of you Raspberry Pi, the way I do it is by navigating to the folder on the RPI in file explorer, then copying the  path from the explorer bar and changing the \ to /.

```javascript
var gulp = require('gulp'),
watch = require('gulp-watch');

gulp.task('python', function() {
  return watch('./src/*.py')
   gulp.src('./src/*.py')
    .pipe(gulp.dest('//RASPI/PiShare/myFolderOnPi'));
});

gulp.task('default', function(){
   return watch('./src/**',function(){
     gulp.src('src/**')
     .pipe(gulp.dest('//RASPI/PiShare/myFolderOnPi'));
   })
});
```
From here on, you don't need to worry about this folder again, only to start and end the gulp script. The src is your working folder and anything you do in there is copied to the raspberry Pi automatically when a file changed in it. To start the copy process run the command
```powershell
> gulp
```
or to copy only the python files 

```powershell
> gulp python
```
or you could change it for any files you are working with 

```javascript
var gulp = require('gulp'),
watch = require('gulp-watch');

//first line is your task name
gulp.task('myCSharpfiles', function() { 
   // second is the folder to watch 
  return watch('./src/*.cs')   
   // third is the files to copy (** matches everything )
   gulp.src('./src/*.cs')
   // finally this is the folder on the Raspberry Pi 
   // but could be anywhere you like.
    .pipe(gulp.dest('//RASPI/PiShare/myFolderOnPi'));
});
```
So with the script running you are free to work in the src folder and do as you please. I usually start by creating a new git repo, and if you are only copying the python files to the RPI, your folders there do not have any of the cruft of your working folders.

One thing to remember is that files are not deleted on the RPI when they are deleted on the Development PC, if you want to do that, then use the [gulp-clean](https://www.npmjs.com/package/gulp-clean) plugin or do it manually.


For more info on [gulp.js have a look at their docs](https://github.com/gulpjs/gulp/blob/master/docs/API.md)
