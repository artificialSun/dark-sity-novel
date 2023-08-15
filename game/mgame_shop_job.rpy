init:
    define shop_job_items = [_("Ножницы"), _("Тарелка картошки"), _("Виски"), _("Овощи"), _("Бутерброд"), _("Коробка конфеты"), _("Хлеб"), _("Продолговатые штуки"), _("Молоко"), _("Сыр")]
     

#####################################################################################################################################################################
#########################################################    ЭКРАНЫ ИГРЫ    #########################################################################################
screen shop_mini_game():
    modal True

    imagemap:
        ground "images/job/bg shop_inside.jpg"

    default tt = Tooltip("Ни одна область не выбрана")
    
    style_prefix "shop" 

    hbox:
        align(0.8, 0.2)
        grid 5 2:
            spacing 10

            for i in range(10):
                vbox:
                    frame:
                        vbox:
                            showif mouse_array[i]==1:
                                imagebutton:
                                    idle "job/shop_mouse.jpg"
                                    hover "job/shop_mouse_hover.jpg"
                                    action Function(mouse_run)
                            else:
                                imagebutton:                          
                                    idle "job/shop_item_"+str(i)+".jpg" 
                                    hovered tt.Action(shop_job_items[i])                                             
                    hbox:
                        imagebutton:
                            idle "gui/my_button/but_back.png"
                            hover "gui/my_button/but_back_hover.png"
                            action [SetDict(shop_job_items_count_user, i, shop_job_items_count_user[i]-1), Function(randomouse)] 
                        #null width 70
                        frame:
                            xsize 73
                            padding (8, 8)
                            yalign 0.5
                            text str(shop_job_items_count_user[i]) align (0.5, 0.5)
                        imagebutton:
                            idle "gui/my_button/but_forward.png"
                            hover "gui/my_button/but_forward_hover.png"   
                            action [SetDict(shop_job_items_count_user, i, shop_job_items_count_user[i]+1), Function(randomouse)]
        vbox:
            xsize 250
            ysize 480
            align(0.5, 0.5)            
            hbox:
                xsize 190
                xalign 0.5
                text "{size=+20}[zp]${/size}" xalign 0.1 
                text "{size=+20}[work_hours] ч.{/size}" xalign 0.9 
            frame:
                xalign 0.5
                ysize 350
                xsize 200
                vbox:
                    xsize 200
                    text "{b}ЗАКАЗ:{/b}"
                    null height 15
                    for i in range(10):
                        if shop_job_items_count[i] > 0:
                            text shop_job_items[i] + " - " + str(shop_job_items_count[i]) + " шт."

            frame:
                padding (5, 5)
                frame:
                    xalign 0.5
                    textbutton "ЗАКАЗ СОБРАН" align(0.5, 0.05) action [Hide("shop_mini_game"), Function(check_shop_list)]



#################### 2 экран

style shop_text:
    color "#fdc200"
    size 18
    xalign 0.5    
    #font "DejaVuSans.ttf"

style shop_frame:
    xalign 0.5
    padding(3, 3)

#================================================================================================            
#===================================== ФУНКЦИИ ==================================================
#================================================================================================

label init_shop_mini_game:
    $ zp = 0                    #текущая зарплата за этот день
    $ work_hours = 0            #сколько рабочих часов прошло (1ч - 1 итерация листа)
    $ mistakes = 0              #количество ошибок, если их нет, может начисляться премия
    $ mistakes_total = 0              #количество ошибок, если их нет, может начисляться премия
    $ mouse_array = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    $ shop_job_items_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    $ shop_job_items_count_user = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
    $ reload_shop_job()
    $ mouse_in_bag = False
    return



init python:
    def reload_shop_job():
        new_zakaz()
        mouse_run()


    def mouse_run():
        global mouse_array
        how_many_mouse = renpy.random.choice([1, 1, 1, 1, 2, 2, 2, 3])
        for i in range(10):
            mouse_array[i] = 0
        for i in range(how_many_mouse):
            mouse_array[renpy.random.randint(0,9)] = 1  

    def randomouse(): # функция используется, чтобы мыши иногда бегали сами
        if renpy.random.randint(1,10) == 1:
            mouse_run()      

    def new_zakaz():        
        for i in range(10):
            shop_job_items_count[i] = 0
            shop_job_items_count_user[i] = 0
        for i in range(6):
            shop_job_items_count[renpy.random.randint(0,9)] = renpy.random.randint(1,5)

    def check_shop_list():
        global mouse_in_bag
        global mistakes, zp, mistakes_total
        shtraf = 0
        for i in range(10):
            if shop_job_items_count[i] == shop_job_items_count_user[i]: 
                if shop_job_items_count[i] > 0:
                    zp += 10
            else:
                shtraf += 12
                mistakes += 1
            if shop_job_items_count_user[i] > 0 and mouse_array[i] > 0:                
                shtraf += 30
                mistakes += 1
                mouse_in_bag = True
        renpy.notify("Текущая зарплата: " + str(zp) + "$")
        if mistakes > 0 :
            renpy.notify("Вы ошиблись при выдаче товара. Штраф " + str(shtraf) + "$")
            mistakes_total += mistakes
            mistakes = 0 #обнулили ошибки за текущий заказ после подсчета
        else:
            renpy.notify("Вы молодец, начальник вами доволен!")
        

#================================================================================================            
#===================================== LABELS ===================================================
#================================================================================================        

#### на что-то в этом роде нужно будет заменить повторябщийся элемент
label do_you_can_skip_work(workname):
    if my_can_skip_work[workname]:  #проверяем, первый раз игрок на эту работу пришел или нет
        "Пропустить мини-игру?"
        menu:
            "Да":
                $ zp_now = renpy.random.randint(max(my_av_zp-20, 0), my_av_zp+20) 
                "Сегодня моя зарплата составила [zp_now]$"
                $ change_stat("m", zp_now)
                $ global_time.add_time("h", workhours_in_day[workname])
                #jump .end_workday
                return True
            "Нет":                
                "Пора приступать к обязанностям"                
    else:
        show screen info_many_strings(["Эта мини-игра представляет собой один ваш рабочий день.","", "В следующий раз вы сможете ее пропустить","и получить примерно ту же зарплату за то же время","или сыграть заново, чтобы улучшить результат."])
    return False
      
#############################



label start_game_shop_job:
    call init_shop_mini_game
    if my_can_skip_work["shop"]:  #проверяем, первый раз игрок на эту работу пришел или нет
        "Пропустить мини-игру?"
        menu:
            "Да":
                $ zp_now = renpy.random.randint(max(my_av_zp-20, 0), my_av_zp+20) 
                "Сегодня моя зарплата составила [zp_now]$"
                $ change_stat("m", zp_now)
                $ global_time.add_time("h", workhours_in_day["shop"])
                jump .end_workday
                return True
            "Нет":                
                "Пора приступать к обязанностям"                
    else:
        show screen info_many_strings(["Эта мини-игра представляет собой один ваш рабочий день.","", "В следующий раз вы сможете ее пропустить","и получить примерно ту же зарплату за то же время","или сыграть заново, чтобы улучшить результат."])
        
        "Я переодеваюсь в фартук. Пора работать."
        show me_big at right
        "Мерзкие мыши! Опять эти твари повсюду!"
        "Я должен правильно собрать заказ. Если мышь сидит на товаре, который входит в список покупателя, ее нужно прогнать!" 
            
        while work_hours < workhours_in_day["shop"]:                        
            $ reload_shop_job() 
            show screen shop_mini_game with dissolve
            $ work_hours += 2
            "{cps=120}{color=#2ad9f8}Нужно дать по носу этой долбанной мыши, если она сидит на нужном продукте. \nЯ не должен запаковывать мышь вместе с товаром!{/color}{/cps}" 
            pause(0.01)
            #"aaa"
            if mouse_in_bag:
                $ renpy.say("Покупатель", "О боже! Это же мышь! МЫШЬ В МОЕЙ ПОКУПКЕ!!!")
                $ renpy.say("Покупатель", "Прямо в корзине, куда вы мне все сложили!!!")
                $ renpy.say("Покупатель", "ААААААААААААААА!!! УБЕРИТЕ ЕЕ ОТ МЕНЯ!")
                boss "Эй, [my_name]! Там на тебя жалуются!"
                $ renpy.notify("Списан мышиный штраф 30$")
                $ change_stat("g", -1)
                $ mouse_in_bag = False
        $ my_can_skip_work["shop"] = True
        if mistakes_total == 0:
            $ renpy.notify("Вы идеально справились! Премия 50$")
            $ zp += 50
            $ change_stat("g", 2)
        elif mistakes_total > 4:
            if my_boss_kind == boss_kind["bad"]:
                boss "Совсем охренел?! Ошибка на ошибке! Ты и мышей клиентам складываешь, а?!"
                boss "Работать кто будет??? Еще один такой фокус, выкину тебя к чертям!"
                $ job_zalet += 1
            elif my_boss_kind == boss_kind["good"]:
                boss "Что с тобой? Ты нездоров? Иди проспись. Если будешь работать так же плохо, мне придется тебя уволить."
            $ change_stat("g", -1)
            $ renpy.notify("Вы очень плохо работаете! Дополнительный штраф 30$")
            $ zp -= 30    
            $ global_time.add_time("h", workhours_in_day["shop"])    

        $ my_av_zp = max (zp, 0) # если штрафов слишком много, зп может оказаться меньше 0
        $ renpy.notify("Получена зарплата за день")
        $ change_stat("m", my_av_zp)
            

    label .end_workday:
        "На сегодня мой рабочий день закончен" 
        return
  



#======================================================================================================================           
#===================================== первый раз пришел на работу ====================================================

label shop_first_day:
    #"Неприметное здание почти в самом центре города рядом с полицейским управлением."
    scene bg shop_job_outside with fade
    show rain with dissolve
    "Я работаю в небольшой бакалее недалеко от парка развлечений."
    "К счастью, публика здесь довольно приличная. Хороший район."
    menu:
        "Я люблю свою работу":
            "У нас здесь отличная точка, приличный район, покупатели отзывчивые. Я отлично знаю некоторых, они приходят каждый день."
            "Но в последнее время у нас расплодилась семейка мышей, никак не можем вытравить"
            "Прямо напасть какая-то! Приходится их едва ли не из корзины с собранными для клиента покупками выгребать!"
        "Я ненавижу своб работу":
            "Целый день на ногах! И глаза замыливаются от этих рассчетов!"
            "А теперь еще и мыши! Чертовы трижды проклятые мыши, которые так и норовят залезть прямо в корзину с заказом покупателя!"
            "Как же я это все ненавижу! Как только замаячит что получше, сразу пошлю всех к дьяволу!"
    
    scene bg shop_inside with fade
    call job_first_day_boss_dialog1_shop

    "Переодеваюсь в рабочую одежду"
    call start_game_shop_job
            
    return
        

label job_first_day_boss_dialog1_shop:        
    #проверка опозданий:
    $ global_time.show_time()
    $ t = my_job_timemark.how_long("m", global_time)
    #"показываю разницу с меткой времени: [t] мин"

    show boss_img at right

    if my_boss_kind == boss_kind["good"]:
        if t < -20:
            boss "Рад тебя видеть, [my_name]! Ты как всегда вовремя. Поможешь мне немного на складе? Опять эти проклятые мыши!"
        elif t > 120:
            boss "[my_name], где тебя черти носят? Полдня за тебя отдуваюсь! У меня вообще-то другие дела есть!"
            boss "Если ты будешь продолжать в том же духе, мне придется тебя уволить!"
            $ job_zalet += 1
        elif t > 30:
            boss "Эх, задерживаешься! Задерживаешься! Я уже с ног сбился! А еще эти мыши! Давай скорее за прилавок!"
        elif t > 0:
            boss "Пошустрее, [my_name]! Раз уж так долго добираешься!"
        else:
            boss "Славное утро, [my_name]. Ты как раз вовремя! А вон и миссис Бенингтон, наверняка опять закупит ножниц."
        if my_choises["ep001_whiskey_drink"]:
            boss "Ты чего это? Навеселе что ли? Ну-ка, плесни и мне тогда уж!"            
            $ change_stat("b", 1)
    elif my_boss_kind == boss_kind["bad"]:        
        if t > 15:
            boss "По девкам шляешься? Воротник не выглажен! Приходит к середине рабочего дня, совсем охренел!"
            boss "Я тебе за что плачу вообще? Может это ты тут мышей подкармливаешь, а?"
            boss "Слабоумный что ли, в прошлый раз непонятно было, что опаздывать нельзя! Я ж тебя выгоню нахрен! И черта с два такую бестолочь куда-то еще возьмут!"
            $ job_zalet += 1
        elif t > 0:
            boss "Опаздываешь, братец! Не видать тебе выходных, как своих ушей. Марш за прилавок!"
        elif t < -25: 
            boss 'Ох посмотрите-ка, явился тут. Еще и заранее. Под дверью ждет.'
            boss "Может еще и на ставку охранника метишь, а? Не дождешься!"
        else:
            boss "Что, в этот раз притащил свою задницу вовремя? Ну давай тогда, иди, ножки разомни."
        if my_choises["ep001_whiskey_drink"]:
            boss "*принюхивается*"
            boss "Ты уже пригубил, падла?! Чрета-с-два возьмешь дополнительные выходные! Чтоб тебя."
            boss "Как только найду кого-то нового, сразу выдворю! Ух выдра, хуже мыши поганой!"
            "Он всегда так. Не обращаю внимания."
    hide boss_img with dissolve
    return






