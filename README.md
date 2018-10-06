DalekBot_web

## To create a new new blog post

To create a new blog post you will need to  be in the root of the repo and have python 3. installed

note: I use  _'py'_ to run _'python'_ as it handles the different versions on the computer better.

Requirements:
```
> py -m pip install pillow
```


```
>py .\create_new_blog_post.py -t 'this is a test blog'
```
you can use the -h flag to see all options
```
>py .\create_new_blog_post.py -h
```

Once the blog post has been created, just add your pictures to the "assets/images/imagesToProcess" folder, they should
be processed and added to your blog automatically.

The blog post lives in the /_posts folder, if you are using visual studio code click the 'open preview button' at the top of the tabs and your will see a rough preview or the post

when done ctrl + c to stop the process

## To Only resize images only
Here we use the -p or --pics flag.

```
>py .\create_new_blog_post.py -p 
```

