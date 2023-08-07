# это миниигра про работу в морге
init:
    $ this_morg_name = ""
    $ morg_button_index = -1
    $ job_zalet = 0 #после двух вас выкинут с работы

# словарь с целевым временем в часах для каждой работы. вероятно, будет перенесен в другой блок    
    $ workhours_in_day={
        "morg": 8,
        "shop": 2
    }
    
###########################################################################################
################################################### ГЕНЕРАЦИЯ ОДНОГО ЛИСТА В МОРГЕ
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


######################### Проверочные функции

init python:
    def reload_morg_list():
        global morg_button_index, take_away_count, morg_take_away_dict, work_hours
        generate_morg()
        #renpy.say("aa","Сгенерировал все")
        morg_button_index = -1 # текущий индекс выбранной кнопки
        take_away_count = 0
        morg_take_away_dict = {0:False, 1:False, 2:False} #лист унесения
        mistakes = 0 #обнуление количества ошибок на лист
        

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
                mistakes_total += 1
        else:
            zp += 5
        take_away_count += 1

    def morg_list_premia():
        global zp
        if mistakes == 0:
            zp += 10
            renpy.notify("10$ премия правильно заполненный лист")
        elif mistakes > 1:
            renpy.say("босс", "По-моему, у тебя проблемы "+me.name +". Будь внимательнее!")

######################### Инициализация переменных для игры и очистка (нужно запускать перед каждым включением мини-игры, чтобы обнулять время, зп и пр)
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
    $ mistakes_total = 0              #количество ошибок, если их нет, может начисляться премия

    $ morg_take_away_dict = {0:False, 1:False, 2:False} #лист унесения (видимости людей, пока false видимы)
    $ take_away_count = 0   
    return

#####################################################################################################################################################################
#########################################################    ЭКРАНЫ ИГРЫ    #########################################################################################

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
            textbutton "ОТКРЫТЬ СЛЕДУЮЩИЙ ЛИСТ" align(0.5, 0.05) action [Function(morg_list_premia), Hide("morg_mini_game")]
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

#################### 2 экран

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
            align (0.5, 0.5)
            text "Введите имя погибшего"
            input default "": 
                pixel_width(500)#this to not allow too long name
                value VariableInputValue("this_morg_name")#with this you save the input to a variable.            
            textbutton "УНЕСТИ" action [SetDict(morg_take_away_dict, morg_button_index, True), Function(check_morg_man_away), Hide("morg_notice")] align (0.5, 0.5)

#================================================================================================            
#===================================== LABEL ====================================================
#================================================================================================



### метка запускается непосредственно перед началом или пропуском мини-игры
label start_game_morg:
    call init_morg_mini_game #инициализация или обнуление начальны переменных
    ## XX поправить текст вводный
    #"текст текст текст"
   
    if my_can_skip_work["morg"]:  #проверяем, первый раз игрок на эту работу пришел или нет
        "Пропустить мини-игру?"
        menu:
            "Да":
                $ zp_now = renpy.random.randint(max(my_av_zp-20, 0), my_av_zp+20) 
                "Сегодня моя зарплата составила [zp_now]$"
                $ change_stat("m", zp_now)
                $ global_time.add_time("h", workhours_in_day["morg"])
                jump .end_workday
            "Нет":                
                "Пора приступать к обязанностям"
    else:
        show screen info_many_strings(["Эта мини-игра представляет собой один ваш рабочий день.","", "В следующий раз вы сможете ее пропустить","и получить примерно ту же зарплату за то же время","или сыграть заново, чтобы улучшить результат."])

        "Я спускаюсь на -1 этаж, чтобы вновь встретиться с моими молчаливыми клиентами.В"
          
        while work_hours < workhours_in_day["morg"]:                        
            $ reload_morg_list() 
            show screen morg_mini_game with dissolve
            $ work_hours += 1
            "{cps=160}Моя задача унести все тела, а для некоторых нужно правильно указать имя в анкете.{/cps}" 
            pause(0.01)
        $ my_can_skip_work["morg"] = True
        if mistakes_total == 0:
            $ renpy.notify("Вы идеально справились! Премия 50$")
            $ zp += 50
            $ change_stat("g", 2)
        elif mistakes_total > 4:
            if my_boss_kind == boss_kind["bad"]:
                boss "Совсем охренел?! Работать кто будет??? Еще один такой фокус, выкину тебя к чертям!"
                $ job_zalet += 1
            elif my_boss_kind == boss_kind["good"]:
                boss "Что с тобой, [me]? Ты нездоров? Иди проспись. Если будешь работать так же плохо, мне придется тебя уволить."
            $ change_stat("g", -1)
            $ renpy.notify("Вы очень плохо работаете! Дополнительный штраф 30$")
            $ zp -= 30        

        $ my_av_zp = max (zp, 0) # если штрафов слишком много, зп может оказаться меньше 0
        $ renpy.notify("Получена зарплата за день")
        $ change_stat("m", my_av_zp)
        

    label .end_workday:
        "На сегодня мой рабочий день закончен"        
  
    return
    


#======================================================================================================================           
#===================================== первый раз пришел на работу ====================================================

label morg_first_day:
    "Неприметное здание почти в самом центре города рядом с полицейским управлением."
    "Еще один день в темном подвальном помещении."
    menu:
        "Я люблю свою работу":
            "Никаких людей. Минимум взаимоотношений. Идеально для интроверта."
        "Я ненавижу своб работу":
            "Как же я это все ненавижу! Холод и смрад, уродливые тела, которых надо перепаковывать и записывать их гребанные имена"
    
    call job_first_day_boss_dialog1

    "Переодеваюсь в рабочую одежду"
    call start_game_morg
            
    return
        

label job_first_day_boss_dialog1:        
    #проверка опозданий:
    $ global_time.show_time()
    $ t = my_job_timemark.how_long("m", global_time)
    #"показываю разницу с меткой времени: [t] мин"

    if my_boss_kind == boss_kind["good"]:
        if t < -20:
            boss "Ты у нас как всегда ранняя пташка! Не даром сотрудник года. Там нам кое-кого подвезли. Нужно зарегистрировать"
        elif t > 120:
            boss "Ты непозволительно задерживаешься. Дарелл работает за тебя половину дня. К сожалению, я должен занести это в твое личное дело."
            boss "Если ты не уважаешь корпоративную этику, мы вынуждены будем расстаться"
            $ job_zalet += 1
        elif t > 30:
            boss "Почему ты задержался? У тебя какие-то проблемы? Тебе придется все равно отработать все время"
    elif my_boss_kind == boss_kind["bad"]:
        if t > 15:
            boss "Ты не попутал часом? Время видел? Глаза разуй, недомерок!"
            boss "Я тебе тут плачу чтобы ты прохлаждался что ли?"
            boss "Еще одна такая херня, и я тебя уволю нахрен! И черта с два такую бестолочь куда-то еще возьмут. Уж я позабочусь."
            $ job_zalet += 1
        elif t > 1:
            boss "Опаздываешь, гаденыш! Марш работать"
        elif t < -25: 
            boss 'Что, выпендриваешься, да? Типа "я могу припереться ни свет ни заря, не то, что вы все", а?'
            boss "Вали уже в свой подвал и не мозоль мне тут глаза!"


        

       




