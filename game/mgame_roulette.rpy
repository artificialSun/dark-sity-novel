init:
    $ stavka_num = ""
    $ roulette_order_num = 1000
    $ roulette_luck_36 = False #особая удачная ставка сюжетная в течение суток с момента получения записки
# экран рулетки
screen roulette(): 
    imagemap:
        ground "images/casino/casino_stav.png"
        hover "images/casino/casino_stav_hover.png"

        hotspot(262, 186, 44, 132) action [SetVariable("roulette_order_num", 0), SetVariable("stavka_num", 'zero'), Hide("roulette"), Jump("set_stavka")] #0         
        hotspot(307, 231, 54, 89) action [SetVariable("roulette_order_num", 1), SetVariable("stavka_num", 'номер 1'), Hide("roulette"), Jump("set_stavka")] #1
        hotspot(307, 140, 56, 86) action [SetVariable("roulette_order_num", 2), SetVariable("stavka_num", 'номер 2'), Hide("roulette"), Jump("set_stavka")] #2
        hotspot(307, 45, 55, 91) action [SetVariable("roulette_order_num", 3), SetVariable("stavka_num", 'номер 3'), Hide("roulette"), Jump("set_stavka")] #3
        hotspot(362, 231, 56, 87) action [SetVariable("roulette_order_num", 4), SetVariable("stavka_num", 'номер 4'), Hide("roulette"), Jump("set_stavka")]#4
        hotspot(364, 138, 53, 89) action [SetVariable("roulette_order_num", 5), SetVariable("stavka_num", 'номер 5'), Hide("roulette"), Jump("set_stavka")]#5
        hotspot(362, 45, 55, 90) action [SetVariable("roulette_order_num", 6), SetVariable("stavka_num", 'номер 6'), Hide("roulette"), Jump("set_stavka")]#6
        hotspot(417, 229, 55, 90) action [SetVariable("roulette_order_num", 7), SetVariable("stavka_num", 'номер 7'), Hide("roulette"), Jump("set_stavka")]#7
        hotspot(417, 138, 55, 90) action [SetVariable("roulette_order_num", 8), SetVariable("stavka_num", 'номер 8'), Hide("roulette"), Jump("set_stavka")]#8
        hotspot(416, 46, 57, 89) action [SetVariable("roulette_order_num", 9), SetVariable("stavka_num", 'номер 9'), Hide("roulette"), Jump("set_stavka")]#9
        hotspot(472, 229, 55, 91) action [SetVariable("roulette_order_num", 10), SetVariable("stavka_num", 'номер 10'), Hide("roulette"), Jump("set_stavka")]#10
        hotspot(471, 138, 57, 89) action [SetVariable("roulette_order_num", 11), SetVariable("stavka_num", 'номер 11'), Hide("roulette"), Jump("set_stavka")]#11
        hotspot(472, 46, 55, 89) action [SetVariable("roulette_order_num", 12), SetVariable("stavka_num", 'номер 12'), Hide("roulette"), Jump("set_stavka")]#12
        hotspot(528, 230, 54, 89) action [SetVariable("roulette_order_num", 13), SetVariable("stavka_num", 'номер 13'), Hide("roulette"), Jump("set_stavka")]#13
        hotspot(527, 138, 56, 90) action [SetVariable("roulette_order_num", 14), SetVariable("stavka_num", 'номер 14'), Hide("roulette"), Jump("set_stavka")]#14
        hotspot(528, 45, 55, 90) action [SetVariable("roulette_order_num", 15), SetVariable("stavka_num", 'номер 15'), Hide("roulette"), Jump("set_stavka")]#15
        hotspot(582, 230, 55, 89) action [SetVariable("roulette_order_num", 16), SetVariable("stavka_num", 'номер 16'), Hide("roulette"), Jump("set_stavka")]#16
        hotspot(582, 138, 55, 89) action [SetVariable("roulette_order_num", 17), SetVariable("stavka_num", 'номер 17'), Hide("roulette"), Jump("set_stavka")]#17
        hotspot(582, 45, 56, 90) action [SetVariable("roulette_order_num", 18), SetVariable("stavka_num", 'номер 18'), Hide("roulette"), Jump("set_stavka")]#18
        hotspot(638, 229, 54, 90) action [SetVariable("roulette_order_num", 19), SetVariable("stavka_num", 'номер 19'), Hide("roulette"), Jump("set_stavka")]#19
        hotspot(639, 138, 53, 89) action [SetVariable("roulette_order_num", 20), SetVariable("stavka_num", 'номер 20'), Hide("roulette"), Jump("set_stavka")]#20
        hotspot(639, 45, 53, 89) action [SetVariable("roulette_order_num", 21), SetVariable("stavka_num", 'номер 21'), Hide("roulette"), Jump("set_stavka")]#21
        hotspot(695, 230, 54, 89) action [SetVariable("roulette_order_num", 22), SetVariable("stavka_num", 'номер 22'), Hide("roulette"), Jump("set_stavka")]#22
        hotspot(695, 138, 52, 89) action [SetVariable("roulette_order_num", 23), SetVariable("stavka_num", 'номер 23'), Hide("roulette"), Jump("set_stavka")]#23
        hotspot(693, 44, 54, 90) action [SetVariable("roulette_order_num", 24), SetVariable("stavka_num", 'номер 24'), Hide("roulette"), Jump("set_stavka")]#24
        hotspot(748, 230, 55, 90) action [SetVariable("roulette_order_num", 25), SetVariable("stavka_num", 'номер 25'), Hide("roulette"), Jump("set_stavka")]#25
        hotspot(748, 140, 55, 87) action [SetVariable("roulette_order_num", 26), SetVariable("stavka_num", 'номер 26'), Hide("roulette"), Jump("set_stavka")]#26
        hotspot(748, 43, 55, 92) action [SetVariable("roulette_order_num", 27), SetVariable("stavka_num", 'номер 27'), Hide("roulette"), Jump("set_stavka")]#27
        hotspot(804, 229, 56, 91) action [SetVariable("roulette_order_num", 28), SetVariable("stavka_num", 'номер 28'), Hide("roulette"), Jump("set_stavka")]#28
        hotspot(805, 135, 54, 93) action [SetVariable("roulette_order_num", 29), SetVariable("stavka_num", 'номер 29'), Hide("roulette"), Jump("set_stavka")]#29
        hotspot(805, 45, 55, 91) action [SetVariable("roulette_order_num", 30), SetVariable("stavka_num", 'номер 30'), Hide("roulette"), Jump("set_stavka")]#30
        hotspot(859, 230, 54, 89) action [SetVariable("roulette_order_num", 31), SetVariable("stavka_num", 'номер 31'), Hide("roulette"), Jump("set_stavka")]#31
        hotspot(860, 138, 54, 90) action [SetVariable("roulette_order_num", 32), SetVariable("stavka_num", 'номер 32'), Hide("roulette"), Jump("set_stavka")]#32
        hotspot(860, 46, 53, 86) action [SetVariable("roulette_order_num", 33), SetVariable("stavka_num", 'номер 33'), Hide("roulette"), Jump("set_stavka")]#33
        hotspot(919, 236, 45, 77) action [SetVariable("roulette_order_num", 34), SetVariable("stavka_num", 'номер 34'), Hide("roulette"), Jump("set_stavka")]#34
        hotspot(918, 141, 49, 82) action [SetVariable("roulette_order_num", 35), SetVariable("stavka_num", 'номер 35'), Hide("roulette"), Jump("set_stavka")]#35
        hotspot(918, 47, 50, 83) action [SetVariable("roulette_order_num", 36), SetVariable("stavka_num", 'номер 36'), Hide("roulette"), Jump("set_stavka")]#36
        hotspot(971, 231, 53, 86) action [SetVariable("roulette_order_num", 37), SetVariable("stavka_num", '1й ряд'), Hide("roulette"), Jump("set_stavka")]#1 ряд
        hotspot(973, 143, 48, 80) action [SetVariable("roulette_order_num", 38), SetVariable("stavka_num", '2й ряд'), Hide("roulette"), Jump("set_stavka")]#2 ряд
        hotspot(972, 46, 51, 85) action [SetVariable("roulette_order_num", 39), SetVariable("stavka_num", '3й ряд'), Hide("roulette"), Jump("set_stavka")]#3 ряд
        hotspot(321, 329, 198, 76) action [SetVariable("roulette_order_num", 40), SetVariable("stavka_num", '1й квадрат числа 1-12'), Hide("roulette"), Jump("set_stavka")]#1-12 
        hotspot(537, 330, 203, 74) action [SetVariable("roulette_order_num", 41), SetVariable("stavka_num", '2й квадрат числа 13-24'), Hide("roulette"), Jump("set_stavka")]#13-24
        hotspot(756, 329, 205, 75) action [SetVariable("roulette_order_num", 42), SetVariable("stavka_num", '3й квадрат числа 25-36'), Hide("roulette"), Jump("set_stavka")]#25-36
        hotspot(309, 416, 106, 86) action [SetVariable("roulette_order_num", 43), SetVariable("stavka_num", 'числа с 1 по 18'), Hide("roulette"), Jump("set_stavka")]#1-18
        hotspot(861, 414, 106, 87) action [SetVariable("roulette_order_num", 44), SetVariable("stavka_num", 'числа с 19 по 36'), Hide("roulette"), Jump("set_stavka")]#19-36
        hotspot(420, 417, 105, 85) action [SetVariable("roulette_order_num", 45), SetVariable("stavka_num", 'нечетные'), Hide("roulette"), Jump("set_stavka")]#эвен нечет
        hotspot(751, 416, 105, 87) action [SetVariable("roulette_order_num", 46), SetVariable("stavka_num", 'четные'), Hide("roulette"), Jump("set_stavka")]#одд чет
        hotspot(530, 415, 107, 88) action [SetVariable("roulette_order_num", 47), SetVariable("stavka_num", 'красные'), Hide("roulette"), Jump("set_stavka")]#ред
        hotspot(642, 416, 104, 87) action [SetVariable("roulette_order_num", 48), SetVariable("stavka_num", 'черные'), Hide("roulette"), Jump("set_stavka")]#черн
        hotspot(258, 44, 48, 137) action [SetVariable("roulette_order_num", -1), SetVariable("stavka_num", 'double zero'), Hide("roulette"), Jump("set_stavka")]#00

#============================ФУНКЦИИ ДЛЯ ОБРАБОТКИ РУЛЕТКИ        
label set_stavka:
    $ roulette_profit = 0
    $ renpy.notify("Ваша ставка "+str(stavka)+" на "+str(stavka_num))
    pause(0.3)

    "ставка принята [stavka]$ на [stavka_num]"    

    $ change_stat('m', (-1*stavka))
    
    #бросок шарика. -1 это 00    
    $ res_roulette_num = renpy.random.randint(-1, 36)

    # проверка особых условий выигрыша 1го дня
    if roulette_luck_36:
        $ count_days = timer_luch_36.how_long("d")  #таймер с момента получения записки (не более 24 часов должен быть 1440 мин)
        if count_days > 1:
            $ renpy.notify("Вы опоздали. Прошло более 24 часов с получения записки")
            $ roulette_luck_36 = False
        else:
            if stavka == 15 and stavka_num == 36:
                $ res_roulette_num = 36
                $ roulette_luck_36 = False


    "результат броска: [res_roulette_num]"    
    
    # test
    #$ res_roulette_num = 34
    #"тестовый результат броска: [res_roulette_num]" 

    #обработка результатов
    if roulette_order_num == res_roulette_num:
        "Вы выиграли!"
        if roulette_order_num == -1 or roulette_order_num == 0:
            $ roulette_profit = stavka * 36 * 2            
        else:
            $ roulette_profit = stavka * 36
    elif roulette_order_num == 37 and res_roulette_num in [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]: # 1 ряд
        $ roulette_profit = stavka * 3
    elif roulette_order_num == 38 and res_roulette_num in [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]: # 2 ряд
        $ roulette_profit = stavka * 3
    elif roulette_order_num == 39 and res_roulette_num in [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]: # 3 ряд
        $ roulette_profit = stavka * 3
    elif roulette_order_num == 40 and res_roulette_num in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]: # 1 квадрат
        $ roulette_profit = stavka * 3
    elif roulette_order_num == 41 and res_roulette_num in [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]: # 2 квадрат
        $ roulette_profit = stavka * 3   
    elif roulette_order_num == 42 and res_roulette_num in [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]: # 3 квадрат        
        $ roulette_profit = stavka * 3  
    elif roulette_order_num == 43 and res_roulette_num in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]: # 1 половина
        $ roulette_profit = stavka * 2
    elif roulette_order_num == 44 and res_roulette_num in [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]: # 2 половина 
        $ roulette_profit = stavka * 2  
    elif roulette_order_num == 45 and res_roulette_num in [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]: # нечетные
        $ roulette_profit = stavka * 2
    elif roulette_order_num == 46 and res_roulette_num in [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]: # четные 
        $ roulette_profit = stavka * 2  
    elif roulette_order_num == 47 and res_roulette_num in [3, 9, 12, 18, 21, 27, 30, 36, 5, 14, 23, 32, 1, 7, 16, 19, 25, 34]: # красные
        $ roulette_profit = stavka * 2
    elif roulette_order_num == 48 and res_roulette_num in [6, 15, 24, 33, 2, 8, 11, 17, 20, 26, 29, 35, 4, 10, 13, 22, 28, 31]: # черные 
        $ roulette_profit = stavka * 2  

    if roulette_profit > 0:
        "Вы выиграли!"
        "Ваш выигрыш [roulette_profit]$"
        $ change_stat('m', roulette_profit)
    else:
        "К сожалению, вы проиграли"              

    pause(1.0)
    jump roulette_menu          


#===========================СЦЕНА С РУЛЕТКОЙ
label roulette:
    scene bg casino int 
    with fade

    pause 1.0
    "Сделать ставку?"

    label .roulette_menu:
        menu:            
            "Сделать ставку?"
            "Да":   
                show casino_dop 
                with fade                             
                $ stavka = int(renpy.input("Введите размер ставки", length = 10, default = "50", allow = "0123456789").strip())

                if stavka == "":
                    jump roulette_menu

                $ is_money_enough = money_enough(stavka)

                if (is_money_enough):
                    $ renpy.notify("Ваша ставка "+str(stavka)+ "$")

                    show screen roulette

                    "ставка принята"

                jump roulette.roulette_menu

            "Нет":
                menu:
                    "Выйти из казино?"
                    "Да":
                        hide casino_dop
                        with dissolve
                        pause(0.3)

                        return
                    "Нет":
                        jump roulette.roulette_menu
                
        return

    jump roulette


#==========================ВХОД В КАЗИНО
label go_casino:
    scene bg casino ext
    with fade

    show rain

    "Вот где всегда праздник"
    pause(0.5)

    scene bg casino int2
    with fade
    pause(0.5)

    show juli casino at right
    with dissolve

    jul "Привет, красавчик. Завелись лишние денежки?"

    jul "Сыграешь со мной?"
    hide juli 
    with dissolve

    show me_big at left
    with dissolve
    me "Пожалуй воздержусь"

    hide juli
    with dissolve

    menu:
        "Пойти играть в рулетку":
            jump roulette
        "Выйти на улицу":
            return
    return

