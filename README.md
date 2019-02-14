# Face detection Flask back-end
please clone the project and run index.py to start the flask server  
the front-end: [face-detection](https://github.com/Combo819/face-detection)

## routers
`/`,`/homepage`,`/registerpage`,`/mainpage` are routes only to return the html index file. These are the same as the routes set in front-end. So, If the browser refresh, it can still load the page.  
What's more, the API returning json should rename and prevent duplication of name with the route.

## login
Check if an username already in session. If true, sent a json containing true to front-end, and the front-end will redirect to `'/mainpage' ` 
Otherwise, you should type in username and password to log in. If you don have one, please click sign up

## signup
not completed yet

## main
Check if an username already in session. If true, stay and the front end will call `loadimage` later

## logout
clear session and ask the front end to redirect to `'/'`

## loadImage
sent images src list to the front-end