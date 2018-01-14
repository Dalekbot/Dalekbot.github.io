---
layout: page
title: Help
permalink: /help/
---
### Getting Started 

The site is using GitHub version of Jekyll. it is quite simple when you get how it works.

I find GitHub desktop is the easiest as it does all the login and ssh key stuff for you once you log into your GitHub account in the app.

The best way to work is to pull the repo and work locally,  then push it back when you have finished this way you always have a local copy. If you can use a linx box or windows with a version of ruby on it you can run the jekyll server and see your results locally too.

You can work directly on the GitHub server if you want too but it is a pain if you see any errors as you have to keep adding a new commit.

The posts and pages are in the markdown format that GitHub uses

The Master branch of the repo is the branch that is compiled to the web site.



Check out the [Jekyll docs][jekyll-docs] for more info on how to get the most out of Jekyll. 

[jekyll-docs]: https://jekyllrb.com/docs/home


### Blog Posts
You’ll find the blog posts in your `_posts` directory. Go ahead and edit it and re-build the site to see your changes. 

To add new posts, simply add a file in the `_posts` directory that follows the convention `YYYY-MM-DD-name-of-post.ext` eg: "2016-11-10-start-of-bot.md" and includes the necessary front matter. Take a look at the source for this post to get an idea about how it works.

This is the default 'front matter' for a post
```javascript
---
layout: post
title:  "Title of the post"
date:   2017-02-01 09:20:39 +0000
categories: code electronics
excerpt_separator: <!--more-->
thumbnail_file_name: 'DSC_1630.jpg'
thumbnail_alt: 'a picture of something'
author: phil
---
```

### Images

Images are uploaded to the "/assets/images/sz_original" folder.
I will resize them with a script in Photoshop or the size are

1. sz_small: max With=600px max Hight=600px 
1. sz_Large: max With=1200px max Hight=1200px 


### Video

For your Video wrap it in an outer div as follows

```html
   <div class="videoWrapper">
       <!-- Copy & Pasted from YouTube -->
       <iframe width="560" height="315" src="your-video-url" frameborder="0" allowfullscreen></iframe>
   </div>
```



### Pages 

Pages are created in the "/assets/" folder. Just add a new file and the 'front matter' at the top of the file and it will be added to the main site menu.

```javascript
---
layout: page
title: Help
permalink: /Help/
---
```


