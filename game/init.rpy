# Я
default me_old = "me man"
default mу_name = "Фрэнк"
default me = Character("[my_name]", color="#dfbe03", image="[me_old]")
image me1:
    "images/"+"[me_old]" + ".png"
image me_big:
    "images/"+"[me_old]" + " big.png"


# Определение персонажей игры.
define al = Character('Эллис', color="#e7461e", image='alice')
define jul = Character('Джулия', color="#c1ff15", image='juli') #Джулия девушка из казино



init:
    $ left2 = Position(xalign=0.99, yalign = 1)

    #статы
    $ stat_money = 250
    $ stat_good = 0
    $ stat_bad = 0
    $ stat_strong = 0
    $ stat_ratio = 0

    #мини-игры
    $ stavka_num = ""
    $ roulette_order_num = 1000
    



init python:
    import random



#===========================ВСПОМОГАТЕЛЬНЫЕ МЕТКИ И ФУНЦИИ
# изменение статистик 
label change_stat(statname, sum):
    if statname == "m" :                
        if sum > 0:
            $ renpy.notify("Вы получили" + str(sum) + "$")
        elif sum < 0:
            $ renpy.notify("Потрачено " + str(sum*(-1)) + "$")
        $ stat_money += sum
        $ renpy.notify("Ваш капитал: " + str(stat_money) + "$")

    elif statname == "g" :
        $ stat_good += sum
        $ renpy.notify("Хорошая репутация" + str(sum) + "$")
    elif statname == "b" :
        $ stat_bad += sum
    elif statname == "s" :
        $ stat_strong += sum
    elif statname == "r" :
        $ stat_ratio += sum
    return True

#проверка наличия денег
label money_enough(sum):
    if sum > stat_money:
        $ renpy.notify("У вас недостаточно денег! На вашем счету " + str(stat_money) + "$")
        pause(0.5)
        $ is_money_enough = False
    else:
        $ is_money_enough = True
    return


label show_stats:
    $ renpy.notify("деньги: " + str(stat_money) + "$ \n"
    "хорошая репутация: " + str(stat_good) +
    "\nдурная слава: " + str(stat_bad) +
    "\nсила: " + str(stat_strong) +
    "\nрасчетливость: " + str(stat_ratio) 
    )
    pause(4)


#===================ПРОСТО ПЕРЕМЕННЫЕ
