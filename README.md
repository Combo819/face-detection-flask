# Face detection Flask back-end
please clone the project and run index.py to start the flask server  
the front-end: [face-detection](https://github.com/Combo819/face-detection)
## login
Check if an username already in session. If true, sent a json containing true to front-end, and the front-end will redirect to `'/mainpage' ` 
Otherwise, you should type in username and password to log in. If you don have one, please click sign up

## signup
not completed yet

## mainpage
Check if an username already in session. If true, stay and the front end will call `loadimage` later

## logou
clear session and ask the front end to redirect to `'/'`

## loadImage
sent images src list to the front-end