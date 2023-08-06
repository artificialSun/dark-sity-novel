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
        #renpy.say("aa","начинаю генерировать")     
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
            #renpy.say("aa","Сгенерировал картинки")
            morg_note[i]=renpy.random.choice([_("УНЕСТИ"),_("УНЕСТИ"),_("ЗАПИСАТЬ В АНКЕТУ")])



label init_morg_mini_game:
    $ morg = {""}
    $ morg_name = ["","",""] #сет имен, которые предложит лист
    $ morg_note = ["","",""] #сет отметок записать или нет, которые предложит лист
    $ morg_img = ["","",""]   #рандомные изображения для красоты     
    $ morg_img_hover = ["","",""]
    $ zp = 0                    #текущая зарплата за этот день
    $ this_morg_name = ""       #имя мертвого для анкеты введенное игроком
    $ work_hours = 0            #сколько рабочих часов прошло (1ч - 1 итерация листа)
    $ mistakes = 0              #количество ошибок, если их нет, может начисляться премия

    $ morg_take_away_dict = {0:False, 1:False, 2:False} #лист унесения (видимости людей, пока false видимы)
    $ take_away_count = 0   
    return

#####

init python:
    def reload_morg_list():
        global morg_button_index, take_away_count, morg_take_away_dict, work_hours
        generate_morg()
        #renpy.say("aa","Сгенерировал все")
        morg_button_index = -1 # текущий индекс выбранной кнопки
        take_away_count = 0
        morg_take_away_dict = {0:False, 1:False, 2:False} #лист унесения
        

    def check_morg_man_away():#(index, this_morg_name):
        #renpy.notify("запустилась")
        global mistakes, zp
        i = morg_button_index
        global take_away_count, zp        
        if morg_note[i] == "ЗАПИСАТЬ В АНКЕТУ":
            if this_morg_name == morg_name[i]:
                zp += 8
            else:
                renpy.notify("Вы неправильно записали имя. Штраф 15$")
                zp -= 15
                mistakes += 1
        else:
            zp += 5
        take_away_count += 1

#######################################################            

screen morg_mini_game():
    modal True

    imagemap:
        ground "images/job/bg morg.jpg"
    
    style_prefix "morg"

    text "{size=+20}[zp]${/size}" xalign 0.05 yalign 0.05
    text "{size=+20}[work_hours] ч.{/size}" xalign 0.95 yalign 0.05
    showif take_away_count == 3:
        frame:
            align(0.5, 0.1)
            textbutton "ОТКРЫТЬ СЛЕДУЮЩИЙ ЛИСТ" align(0.5, 0.05) action Hide("morg_mini_game")
    #textbutton "TEST" align(0.5, 0.05) action Function(check_morg_man_away) #Function(func1)

    hbox:        
        xalign 0.75
        yalign 0.45        
        xsize 1100
        ysize 250
        for i in range(3):
            vbox:      # заменить циклом      
                frame:
                    xsize 265
                    text morg_name[i] 
                null height 15
                frame:
                    xsize 265
                    ysize 265
                    showif morg_take_away_dict[i] == False:
                        imagebutton:
                            idle morg_img[i]
                            hover morg_img_hover[i]
                            action [SetVariable("morg_button_index", i), SetVariable("this_morg_name", ""), Show("morg_notice")]
                null height 10
                frame:
                    text morg_note[i]
        

style morg_text:
    color "#fdc200"
    size 16
    xalign 0.5    
    #font "DejaVuSans.ttf"

style morg_frame:
    xalign 0.5
    padding(20, 10)

####################

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
            textbutton "УНЕСТИ" action [SetDict(morg_take_away_dict, morg_button_index, True), Function(check_morg_man_away), Hide("morg_notice")] align (0.5, 0.5)

#================================================================================================            
#===================================== LABEL ====================================================
#================================================================================================










label start_game_morg:
    call init_morg_mini_game #инициализация или обнуление начальны переменных

    "текст текст текст"
    if my_can_skip_work["morg"] == False:
        show screen info_many_strings(["Эта мини-игра представляет собой один ваш рабочий день.","", "В следующий раз вы сможете ее пропустить","и получить примерно ту же зарплату, за то же время","или сыграть заново, чтобы улучшить результат."])


    if my_can_skip_work["morg"]:  #проверяем, первый раз игрок на эту работу пришел или нет
        "Пропустить мини-игру?"
        menu:
            "Да":
                $ zp_now = renpy.random.randint(max(my_av_zp-20, 0), my_av_zp+20) 
                $ change_stat("m", zp_now)
                $ global_time.add_time("h", workhours_in_day["morg"])
                jump .end_workday
            "Нет":                
                "Можешь приступать к обязанностям"
    else:
        #show screen info_many_strings(["Эта мини-игра представляет собой один ваш рабочий день.","", "В следующий раз вы сможете ее пропустить","и получить примерно ту же зарплату, за то же время","или сыграть заново, чтобы улучшить результат."])
          
        while work_hours < workhours_in_day["morg"]:            
            $ reload_morg_list() 
            show screen morg_mini_game 
            $ work_hours += 1
            "{cps=160}Моя задача унести все тела, а для некоторых нужно правильно указать имя в анкете.{/cps}" 
            pause(0.01)
        $ my_can_skip_work["morg"] = True
        $ my_av_zp = zp

    label .end_workday:
        "На сегодня мой рабочий день закончен"
        
        jump start_game_morg  #временно
    
    return
    



    # здесь должно быть 8 вызовов, проверки правильности и тп
init:
    $ workhours_in_day={
        "morg": 3,
        "shop": 2
    }
        
    

       

return


