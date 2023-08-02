init python:
    renpy.add_layer("info_layer", above = "screens") #новый слой выше слоя экранов. на нем будут письма, инвентари и тп.

screen letter(message, author = "me"):
    modal True
    zorder 10
    
    imagemap:
        ground "images/letter me.png"

    #frame:
    #    xalign: 0.2
    #    yalign: 0.1
    #    xsize: 1000

    vbox:
        xsize 1000
        ysize 600
        xalign 0.2
        yalign 0.1
        text "[message]" xalign 0.5 yalign 0.3
        
    textbutton "ПРОЧИТАНО" action Hide("letter") xalign 0.5 yalign 0.95

    


