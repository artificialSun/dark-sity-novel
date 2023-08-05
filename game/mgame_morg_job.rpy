# это миниигра про работу в морге
init:
    $ this_morg_name = ""
    $ morg_button_index = -1

init python:

    names_f = [
        "Dorothy",
        "Marge",
        "Brenda",
        "Jane"
        "Daisy",
        "Agata",
        "Dolores",
        "Alice",
        "Marjory",
        "Ruth",
        "Ginger",
        "Debbie",
        "Belinda",
        "Emily",
        "Jamie"
    ]

    names_m = [
        "Michael",
        "Robbie",
        "James",
        "Lucas",
        "Juan",
        "Logan",
        "Jacques",
        "Alexander",
        "Jacques",
        "Nicola",
        "Frank",
        "Adrian",
        "Iron",
        "Patrick",
        "Benjamin"
    ]

    surnames = [
        "Elmers",
        "Baldwin",
        "Albertson",
        "Lee",
        "Evans",
        "Babcock",
        "Berrington",
        "Francis",
        "Gilmore",
        "Green",
        "Goldman",
        "Gerald",
        "Creighton",
        "Archibald",
        "Farmer",
        "Forman",
        "Charlson",
        "Jackson",
        "Carter",
        "Abramson",
        "Alsopp",
        "Barnes",
        "Gonzalez",
        "Garrison",
        "Eddington",
        "Aldridge",
        "Rodriguez",
        "Miller"
    ]

    def generate_morg():      
        morg_img_sklad = "images/job/morg_"        
        for i in range(3):
            male = renpy.random.choice(['m', 'f'])
            num = renpy.random.choice(['1', '2'])            
            if male == 'f':
                morgname = renpy.random.choice(names_f)
            else:
                morgname = renpy.random.choice(names_m)
            morg_name[i]=morgname+" "+renpy.random.choice(surnames)
            morg_img[i]=morg_img_sklad + male +"_"+ num+'.jpg'
            morg_img_hover[i]=morg_img_sklad + male +"_"+ num + "_hover.jpg"
            morg_note[i]=renpy.random.choice([_("УНЕСТИ"),_("УНЕСТИ"),_("ЗАПИСАТЬ В АНКЕТУ")])

screen morg_mini_game():

    imagemap:
        ground "images/job/bg morg.jpg"
    
    style_prefix "morg"

    text "{size=+20}[zp]${/size}" xalign 0.05 yalign 0.05
    text "{size=+20}[work_hours] ч.{/size}" xalign 0.95 yalign 0.05

    hbox:        
        xalign 0.75
        yalign 0.45        
        xsize 1100
        ysize 250
        vbox:            
            frame:
                xsize 265
                text morg_name[0] 
            null height 15
            frame:
                xsize 265
                ysize 265
                imagebutton:
                    idle morg_img[0]
                    hover morg_img_hover[0]
                    action [SetVariable("morg_button_index", 0), SetVariable("this_morg_name", ""), Show("morg_notice")]
            null height 10
            frame:
                text morg_note[0]
        vbox:            
            frame:
                xsize 265
                text morg_name[1]
            null height 15
            frame:
                xsize 265
                ysize 265
                imagebutton:
                    idle morg_img[1]
                    hover morg_img_hover[1]
                    action [SetVariable("morg_button_index", 1), SetVariable("this_morg_name", ""), Show("morg_notice")]
            null height 10
            frame:
                text morg_note[1]
        vbox:            
            frame:
                xsize 265
                text morg_name[2]
            null height 15
            frame:
                xsize 265
                ysize 265
                imagebutton:
                    idle morg_img[2]
                    hover morg_img_hover[2]
                    action [SetVariable("morg_button_index", 2), SetVariable("this_morg_name", ""), Show("morg_notice")]
            null height 10
            frame:
                text morg_note[2]

style morg_text:
    color "#fdc200"
    size 16
    xalign 0.5    
    #font "DejaVuSans.ttf"

style morg_frame:
    xalign 0.5
    padding(20, 10)


screen morg_notice():
    modal True
    zorder 10

    frame:
        padding(40,40)
        xalign 0.5
        yalign 0.5
        xsize 500
        ysize 200
        vbox:
            xalign 0.5
            yalign 0.5
            text "Введите имя погибшего"
            input default "": 
                pixel_width(500)#this to not allow too long name
                value VariableInputValue("this_morg_name")#with this you save the input to a variable.            
            textbutton "УНЕСТИ" action Hide("morg_notice") xalign 0.5 yalign 0.5

#================================================================================================            
#===================================== LABEL ====================================================
#================================================================================================

label init_morg_mini_game:
    $ morg_name = ["","",""] #сет имен, которые предложит лист
    $ morg_note = ["","",""] #сет отметок записать или нет, которые предложит лист
    $ morg_img = ["","",""]   #рандомные изображения для красоты     
    $ morg_img_hover = ["","",""]
    $ zp = 0                    #текущая зарплата за этот день
    $ this_morg_name = ""       #имя мертвого для анкеты введенное игроком
    $ work_hours = 1            #сколько рабочих часов прошло (1ч - 1 итерация листа)

    $ morg_right_list = [False, False, False]
    $ morg_anket_list = ["","",""] 
    return

label start_game_morg:
    call init_morg_mini_game #инициализация или обнуление начальны переменных

    # здесь должно быть 8 вызовов, проверки правильности и тп

return


