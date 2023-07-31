

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