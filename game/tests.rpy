########тестирование инвентаря
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
    "получаю деньги"
    $ some_invent.add_item("money", 101)
    $ some_invent.show_all()
    "получаю еще деньги"
    $ some_invent.add_item("money", 10)
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

