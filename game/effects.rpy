# дождь на фоне из 3 слайдов
image rain:
    "images/texRain.png"
    0.5
    "images/texRain2.png"
    0.5
    "images/texRain3.png"
    0.5   
    repeat

# дождь на фоне анимацией в 2 слоя
image rain_img1 = VBox("images/texRain2.png", "images/texRain2.png") 
image rain_img2 = VBox("images/texRain.png", "images/texRain.png") 

transform bg_scroll_tr(t=5.0):  #прокрутка фона универсальная
    align(0.5, 1.0)
    linear t align(0.5, 0.0)
    repeat

label add_rain:
    #scene bg scrolling 
    show rain_img1 at bg_scroll_tr(2.0)
    show rain_img2 at bg_scroll_tr(4.0)
    #"?!"
    return


# белый шум виньетка
image noise1:    # виньетка, ровный по времени
    "images/effects/ef_noise1.png"
    0.2
    "images/effects/ef_noise2.png"
    0.2
    repeat


# переход с открытием глаз
init:
    # Imagedissolve Transitions.
    $ eyeopen = ImageDissolve("images/effects/eye_effect2.png", 1.5, 100)
    $ eyeclose = ImageDissolve("images/effects/eye_effect3.png", 1.5, 100, reverse=True)

#пустое изображение
# если пустое изображение должно совпадать с размерами экрана, то можно вот так его объявить в разделе init:
# image empty = "#0000"
# но если нам нужны какие-то другие размеры, то делаем вот так:
# image empty = Null(64, 64)




