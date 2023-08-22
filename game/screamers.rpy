screen screamer_day_dream1:
    modal True

    imagemap:
        idle "images/screamer1/bg old_room_mirror.jpg"



label day1_day_dream:
    scene bg old_room_mirror with fade 
    #(2)    
    "Эта комната... как будто бы не было всех этих лет..."
    "Все такое знакомое..." 
    "Мертвенная тишина вокруг"
    "...не к добру..."
    "...тревожно..."
    ""
    "...какая-то неправильность..."
    #show ghost_day_dream1 #align(0.5, 0.5)
    show ghost_day_dream_in_mirror1 at ghost_appear
    $ renpy.pause(6.0, hard = True)
    "...это еще что за хрень?.."
    show ghost_day_dream_in_mirror2 at ghost_appear
    pause 0.5
    show ghost_day_dream_in_mirror2 at ghost_appear
    #show "images/screamer1/ghost_s1_2.png" at ghost_appear
    ""
    ""
    hide ghost_day_dream_in_mirror1 with dissolve
    hide ghost_day_dream_in_mirror2 with dissolve
    ""
    "...нужно уйти отсюда..."
    ""
    show ghost_day_dream_in_room 
    $ renpy.pause(3.0, hard = True)
    ""
    hide ghost_day_dream_in_room
    ""
    "...ноги не слушаются..."
    ""
    ""
    #"сейчас"
    show ghost_day_dream_screamer1 at fast_horror_blink2 
    #test_blink 
    # fast_horror_blink
    $ renpy.pause(1.5, hard = True)
    show ghost_day_dream_skull1 at skull_appear
    show ghost_day_dream_skull2 at skull_appear, skull2_cick
    $ renpy.pause(2, hard = True)
    #show ghost_day_dream_screamer1 at fast_horror_blink
    ""
    ""
    ""
    return

image ghost_day_dream_in_mirror1 = "images/screamer1/ghost_s1_1.png" 
image ghost_day_dream_in_mirror2 = "images/screamer1/ghost_s1_2.png" 
image ghost_day_dream_skull1 = "images/screamer1/ghost_s1_skull1.png"
image ghost_day_dream_skull2 = "images/screamer1/ghost_s1_skull2.png"

image ghost_day_dream_in_room:
    "images/screamer1/ghost_s1_3.png"
    #alpha 0.0
    alpha 0.4
    zoom 0.7    
    anchor(0.5, 0.5)
    xpos 620 ypos 400
    #linear 0.05 alpha 0.2
    1.3
    zoom 1.3
    alpha 0.5
    ypos 500
    1
    alpha 0.6    
    zoom 1.7
    ypos 600
    1
    alpha 0.7
    zoom 2.4
    ypos 700
    1
    linear 2 alpha 0.0 


transform ghost_day_dream_in_room_appear:
    

image ghost_day_dream_screamer1: 
    "images/screamer1/ghost_s1_3.png" 
    xpos 150
    ypos -100
    zoom 3.5   
    #xpos 650
    #ypos 2000
    

transform skull_appear:
    xpos 530
    ypos 35
    zoom 0.54
    alpha 0
    linear 2 alpha 1.0
    linear 0.5 alpha 0.0
    pause 2.5
    #anchor(0.5, 0.5)
    anchor(0.5, 0.5)
    zoom 3 xpos 550 ypos 300
    pause 0.2
    alpha 0
    pause 0.05    
    alpha 1
    pause 0.1    
    linear 0.1 rotate -4
    alpha 0
    pause 0.07
    alpha 1
    pause 0.3
    alpha 0



transform skull2_cick:    
    ypos 35
    linear 0.5 ypos 60 
    pause 0.2   
    linear 0.05 ypos 35
    pause 0.3
    linear 0.05 ypos 40 
    pause 0.2   
    linear 0.05 ypos 35


transform ghost_appear:
    align (0.535, 0.4)
    alpha 0  
    linear 4 alpha 1.0
    5


transform test_blink:
    xpos 650
    ypos 2000
    linear 5 alpha 0.0
    linear 5 alpha 1.0
    repeat

transform fast_horror_blink2:
    block:
        alpha 0.98
        pause 0.06
        alpha 0.2
        pause 0.02
        alpha 0.9
        pause 0.01
        alpha 0.1
        pause 0.09
        alpha 0.8
        pause 0.02
        alpha 0.9
        pause 0.07
        alpha 0.7
        pause 0.01
        alpha 0.9
        pause 0.01
        alpha 0.6
        pause 0.06
        alpha 0.3
        pause 0.07
        alpha 0.9
        pause 0.01
        alpha 0.1
        pause 0.03
        alpha 0.99
        pause 0.09
        alpha 0.87
        pause 0.01
        alpha 0.94
        pause 0.09
        alpha 0.65
        pause 0.04
        alpha 0.3
        pause 0.07
        alpha 0.98
        pause 0.5
        repeat 3
    linear 1 alpha 0

transform fast_horror_blink():
    alpha 0.3
    pause 0.06
    alpha 0.2
    pause 0.02
    alpha 0.9
    pause 0.01
    alpha 0.1
    pause 0.09
    alpha 0.8
    pause 0.02
    alpha 0.09
    pause 0.07
    alpha 0.7
    pause 0.01
    alpha 0.9
    pause 0.01
    alpha 0.6
    pause 0.06
    alpha 0.3
    pause 0.07
    alpha 0.9
    pause 0.01
    alpha 0.
    pause 0.03
    alpha 0.2
    pause 0.09
    alpha 0.3
    pause 0.01
    alpha 0.4
    pause 0.09
    alpha 0.7
    pause 0.04
    alpha 0.3
    pause 0.07
    alpha 0.9
    pause 0.03
    repeat







transform scream_fliks():
    block:
        function get_rand
        alpha get_rand_value
        pause get_rand_value
        repeat

init -1:
    default get_rand_value = 0
init -1 python:
    def get_rand1(trans,st,at):
        #store.get_rand_value = renpy.random.random()
        return None



transform ghost_zoom:
    zoom 0
    linear 1.0 zoom 1.0
    linear 1.0 zoom 0
    repeat

transform zoomin:
    zoom 0 xpos 640 ypos 360 anchor(0.5, 0.5)
    linear 3 zoom 1
