# The game starts here.
label test_eye:

    scene bg london
    "Заснул..."
    scene black with circleirisin
    "..."
    scene black with vpunch
    "Проснулся от удара."
    scene bg london with circleirisout
    "?"
    return

label test_shop_job:
    "тестирование магазина"
    $ my_can_skip_work["shop"] = False
    $ my_name = "Фрэнк"
    call start_game_shop_job from _call_start_game_shop_job_1
    #show screen shop_mini_game
    #"почему мы продаем ножницы в бакалее?"
    return


label test_morg_first_day:    
    "блок тестирования первого дня"
    $ global_time.show_time()
    $ my_job_timemark = Time_mark(global_time, 0, 2, 10) #на работу к 9
    $ t = my_job_timemark.get_time
    $ global_time.add_time("h", 3)
    $ my_boss_kind = boss_kind["good"]
    call morg_first_day from _call_morg_first_day_1
    return




########тестирование инвентаря без оболочки
label test_inventory:
    "это тест инвентаря"
    "создаю инвентарь"
    default some_invent = Inventory({"myDagger": 1, "cureSleep": 10})
    $ some_invent.show_all()
    "ем 1 таблетку"
    $ some_invent.remove_item("cureSleep")
    $ some_invent.show_all()
    "пытаюсь выкинуть 11 таблеток"
    $ some_invent.remove_item("cureSleep", 11)
    $ some_invent.show_all()
    "выкидываю 9 таблеток"
    $ some_invent.remove_item("cureSleep", 9)
    $ some_invent.show_all()
    "получаю деньги 101"
    $ some_invent.add_item("money", 101)
    $ some_invent.show_all()
    "получаю еще деньги 10"
    $ some_invent.add_item("money", 10)
    $ some_invent.show_all()
    "забираю деньги 11$ в стат"
    $ some_invent.take_money(False, 11)
    $ some_invent.show_all()
    "забираю оставшиеся деньги в стат"
    $ some_invent.take_money()
    $ some_invent.show_all()
    "пытаюсь забрать еще 100 денег в стат"
    $ some_invent.take_money(100)
    $ some_invent.show_all()
    "кладу деньги в инвентарь"
    $ some_invent.put_money(10)
    $ some_invent.show_all()
    "пытаюсь положить в инвентарь больше, чем у меня есть (500)"
    $ some_invent.put_money(500)
    $ some_invent.show_all()
    "убираю все деньги из инвентаря"
    $ count1 = some_invent.remove_all("money")
    "из было [count1]"
    $ some_invent.show_all()

    "создаю второй инвентарь"
    default some_invent2 = Inventory({"cureSleep": 20})
    $ some_invent2.show_all()
    "пытаюсь переложить из второго инвентаря в 1й 10 таблеток"
    $ some_invent2.give_away(some_invent, "cureSleep", False, 10)
    "содержимое 2 инв:"
    $ some_invent2.show_all()
    "содержимое 1 инв:"
    $ some_invent.show_all()
    "сколько денег в 1м ящике?"
    $ aaa = some_invent.how_mutch("money")
    "[aaa]"
    "пытаюсь переложить все деньги из 1го во 2й"
    $ some_invent.give_away(some_invent2, "money")
    "перекладываю кинжал из 1го во 2й"
    $ some_invent.give_away(some_invent2, "myDagger")
    "содержимое 2 инв:"
    $ some_invent2.show_all()
    "содержимое 1 инв:"
    $ some_invent.show_all()
    "перекладываю все таблетки из 1го во 2й"
    $ some_invent.give_away(some_invent2, "cureSleep")
    "содержимое 2 инв:"
    $ some_invent2.show_all()
    "содержимое 1 инв:"
    $ some_invent.show_all()

    
return






#####тестирование вложенности label
label test_block:
    me "it is test1"

    label .test_inside:
        me "it is test inside test1"
    me "мы вышли из внутреннего пространства"

label test2:
    me "it is test2"
    label .test_inside:
        me "it is test inside test2"
    menu: 
        "переход":
            me "теперь мы попробуем перейти в чужое пространство неправильно "
            jump .test_inside

        "переход правильный":

            me "теперь мы попробуем перейти в чужое пространство правильно"
            jump test1.test_inside

        "продолжить":
            me "мы не пытаемся прыгнуть куда не следует"
    
    me "блаблабала"
    return
return

