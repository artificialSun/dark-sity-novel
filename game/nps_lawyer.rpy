#адвокат, который напивается, можно его обворовать, но вообще нпс
define adv = Character('[adv.name]', color="#077010", image='adv')
$ adv.name = "Пьяница"
$ adv.rel = 0
$ adv.is_alife = True

label nps_adv_meet:
    "Тот парень явно перебрал. Идет мне навстречу."
    "Ему явно нехорошо."
    
    "В такой темный вечер он легко может стать жертвой грабителей."

    show adv alco
    with fade 
    
    adv "ВАА-аа-рх"

    "*выглядит так, что вот-вот завалится*"

    hide adv
    with dissolve

    menu:
        "Подойти":
            "Подхожу и как раз успеваю придержать за руку"
            call change_stat('g', 1) from _call_change_stat            
            "Он поднимает на меня мутноватый взгляд"

            show adv alco
            with fade 
    
            if stat_bad > stat_good and stat_bad > 10:
                adv "Отвали от меня!"
                $ adv.rel = adv.rel -10
            else:
                adv "Кхе-кхе..."
                adv "ХХ-стрит... помоги дойти"

            menu:
                "Отвести до ближайшей скамейки":
                    show me1
                    with fade

                    me "Мне немного не по пути, парень."      

                    "Да уж, он чертовски пьян"

                    menu:            
                        "Пошарить у него в карманах":
                            call change_stat('b', 2) from _call_change_stat_1
                            $ sum = renpy.random.randint(200,500)
                            "Оу, [sum]$, неплохо"
                            call change_stat('m', sum) from _call_change_stat_2

                        "Оставить в покое":
                            "Пожалуй, оставлю его в покое"


                "Проводить до дома":
                    "С большим трудом мне удается выяснить адрес мужчины. Похоже, он практикующий адвокат"
                    $ adv.rel = adv.rel + 20
                    call change_stat('g', 2) from _call_change_stat_3
                    $ renpy.notify("Теперь у вас есть знакомый адвокат")

                "Завести в ближайшую подворотню":
                    "Хм, пожалуй я и стану тем, кто устроит неприятности этому парню"
                    call change_stat('r', 1) from _call_change_stat_4
                    jump adv_robbery

        "Пройти мимо":
            "Пожалуй, не буду с этим связываться"
    return

# подробнее сцена возможного ограбления адвоката
label adv_robbery:
    $ min_stat_bad_luck = 10
    "Мы прошли вдоль по улице, а дальше свернули в тупик."
    "Тут нас никто не увидит и не услышит"

    show adv alco
    with dissolve

    adv "Ет.. это какое-то не такое место..."

    menu:
        "Бросить его здесь":
            "Тьфу. Не хочется марать руки."
            $ adv.rel -= 20

        "Ограбить":
            "А теперь просто отдай мне свои деньги. Живо!"
            $ adv.rel -= 20
            call change_stat('b', 1) from _call_change_stat_5

            if stat_bad > min_stat_bad_luck:
                $ adv.rel -= 10
                adv "Забирай! Все забирай!"
                call change_stat('b', 1) from _call_change_stat_6

            else:
                adv "Ничего ты не получишь, долбаный мудак!"
        
    