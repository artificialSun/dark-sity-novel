# дождь на фоне
image rain:
    "images/texRain.png"
    0.5
    "images/texRain2.png"
    0.5
    "images/texRain3.png"
    0.5   
    repeat

image rain2: #пыталась сделать зацикленное движение фона
    "images/texRain.png"
    #rotate 0
    #linear 15 rotate 360
    yalign 1.0
    linear 2 yalign -1.0
    repeat


# переход с открытием глаз
init:
    # Imagedissolve Transitions.
    $ circleirisout = ImageDissolve("images/effects/imagedissolve circleiris.png", 1.0, 8)
    $ circleirisin = ImageDissolve("images/effects/imagedissolve circleiris.png", 1.0, 8, reverse=True)


