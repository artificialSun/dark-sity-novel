# Главный герой
default my_type = "man" #параметр используется для подбора картинки в зависимости от выбора персонажа. me man - молодой мужчина, me oldman - пожилой мужчина
default mу_name = _("Фрэнк")

default me = Character("[my_name]", color="#dfbe03", image="me "+"[my_type]")

image my_room = "images/my_room1.jpg"    


# Определение персонажей игры. ======= перенести в соответствующие блоки
define al = Character('Эллис', color="#e7461e", image='alice')
define jul = Character('Джулия', color="#c1ff15", image='juli') #Джулия девушка из казино



init:
    $ left2 = Position(xalign=0.99, yalign = 1)

    #статы
    $ stat_money = 0
    $ stat_good = 0
    $ stat_bad = 0
    $ stat_strong = 0
    $ stat_ratio = 0

    $ stat_health = 200
    $ max_health = 200

    $ stat_mind = 50
    $ max_mind = 200
    $ max_mad = 200

    #мини-игры
    $ stavka_num = ""
    $ roulette_order_num = 1000
    

init python:
    import random



#===========================ВСПОМОГАТЕЛЬНЫЕ МЕТКИ И ФУНЦИИ 
init python:
    #изменение статистик
    def change_stat(statname, sum):
        global stat_bad, stat_good, stat_health, stat_mind, stat_money, stat_ratio, stat_strong
        if statname == "m" :                
            if sum > 0:
                renpy.notify("Вы получили" + str(sum) + "$")
            elif sum < 0:
                renpy.notify("Потрачено " + str(sum*(-1)) + "$")
            stat_money += sum
            renpy.notify("Ваш капитал: " + str(stat_money) + "$")
        elif statname == "g" :
            stat_good += sum
            renpy.notify("Хорошая репутация" + str(sum) + "$")
        elif statname == "b" :
            stat_bad += sum
        elif statname == "s" :
            stat_strong += sum
        elif statname == "r" :
            stat_ratio += sum
        elif statname == "h":
            stat_health += sum
            if stat_health < 60:
                renpy.notify('Вы плохо себя чувствуете, пора обратиться к врачу')
            elif stat_health < 0:
                renpy.notify('Вы потеряли сознание')            
        elif statname == "md":
            stat_mind += sum
            if stat_mind < 0:
                renpy.notify('Вы начинаете сходить с ума')
        return True


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
    elif statname == "h":
        $ stat_health += sum
        if stat_health < 60:
            $ renpy.notify('Вы плохо себя чувствуете, пора обратиться к врачу')
        elif stat_health < 0:
            $ renpy.notify('Вы потеряли сознание')            
    elif statname == "md":
        $ stat_mind += sum
        if stat_mind < 0:
            $ renpy.notify('Вы начинаете сходить с ума')
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


#===================ВРЕМЯ
init:  
    $ hour_start = 6  #стартовое время 7 утра
    $ minut_start = 50 

    $ hours_actual = hour_start  #текущее время
    $ minutes_actual = minut_start 

    $ g_hours = 0  #игровое время в часах
    $ g_minutes = 0   #минуты, не вошедшие в час


init python:   
    def day_postfix(num):
        if num == 1:
            return "день"
        elif num in [2, 3, 4]:
            return "дня"
        else:
            return "дней"
    
    def get_days(hours):
        return hours // 24    

    def show_game_time():
        d = get_days()
        h = g_hours % 24
        part1 = ""
        if d > 0:
            part1 = str(d) + " " + day_postfix(d % 10)
        renpy.notify("Прошло "+ part1 +" " + str(h)+ " ч.")     

    def add_time(prefix, sum): #добавление времени минут, часов или дней
        global g_minutes, g_hours
        if prefix == "m":
            g_minutes += sum
            if g_minutes > 59:
                add_time("h", g_minutes // 60)
                g_minutes %= 60
        elif prefix == "h":
            g_hours += sum
        elif prefix == "d":
            g_hours += sum*24
        

    def show_time():
        actual_time()
        renpy.notify("Текущее время: " + str(hours_actual)+" ч. "+ str(minutes_actual)+ " .мин")

    def actual_time():
        global minutes_actual, hours_actual
        minutes_actual = g_minutes + minut_start
        ost = minutes_actual // 60 #0 если нет переполнения минут при складывании со стартовым временем
        minutes_actual %= 60 # чтобы было не больше 60
        hours_actual = (g_hours + hour_start + ost) % 24



    




