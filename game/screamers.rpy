screen screamer_day_dream1:
    modal True

    imagemap:
        idle "images/screamer1/bg old_room_mirror.jpg"



label day1_day_dream:
    scene bg old_room_mirror with fade #(2)

    "Комната кажется смутно знакомой" 
    ""
    "...неправильность..."

    #show ghost_day_dream1 #align(0.5, 0.5)
    show ghost_day_dream_in_mirrow1 at ghost_appear
    pause(6.0)
    ""
    show ghost_day_dream_in_mirrow2 at ghost_appear
    #show "images/screamer1/ghost_s1_2.png" at ghost_appear
    ""
    ""
    hide ghost_day_dream_in_mirrow1 with dissolve
    hide ghost_day_dream_in_mirrow2 with dissolve
    ""
    ""
    show ghost_day_dream_in_room
    ""
    hide ghost_day_dream_in_room

    ""
    show ghost_day_dream_screamer1 at fast_horror_blink
    ""
    ""

    "fdhgkhs"
    return

image ghost_day_dream_in_mirrow1 = "images/screamer1/ghost_s1_1.png" 
image ghost_day_dream_in_mirrow2 = "images/screamer1/ghost_s1_2.png" 

image ghost_day_dream_in_room:
    "images/screamer1/ghost_s1_3.png" 
    align (0.535, 0.7)
    alpha 0  
    linear 0.05 alpha 1.0
    1
    zoom 1.3
    align (0.535, 1)
    1
    zoom 1.7
    align (0.535, 1)
    1
    zoom 2.4
    align (0.535, 1)
    1
    linear 2 alpha 0.0
    #3
    #zoom 3.5
    #align (0.535, -2)    
    #alpha 1.0
    #0.1
    #alpha 0.5
    #0.01
    #alpha 0.9  
    #0.02
    #alpha 0.3 
    #0.01
    #alpha 0.1   
    #5

image ghost_day_dream_screamer1: 
    "images/screamer1/ghost_s1_3.png" 
    zoom 3.5
    align (0.535, -2)
    

image ghost_day_dream_mask:
    "images/screamer1/ghost_s1_3.png" 

#align(0.5, 0.5)

    #rotate 0
    #leaner 5 rotate 360


transform ghost_appear:
    align (0.535, 0.4)
    alpha 0  
    linear 4 alpha 1.0
    5



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
        store.get_rand_value = renpy.random.random()
        return None



transform ghost_zoom:
    zoom 0
    linear 1.0 zoom 1.0
    linear 1.0 zoom 0
    repeat

transform zoomin:
    zoom 0 xpos 640 ypos 360 anchor(0.5, 0.5)
    linear 3 zoom 1
