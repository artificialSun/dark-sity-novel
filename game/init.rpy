#================================================= Важные импорты в python
init python:
    import random
    import copy
    import enum

#=================================================
#================================================= ГГ, его картинки, статы и пр


# Главный герой
default my_type = "man" #параметр используется для подбора картинки в зависимости от выбора персонажа. me man - молодой мужчина, me oldman - пожилой мужчина
default mу_name = _("Фрэнк")
image my_room = "images/my_room1.jpg"  #стартовая комната где живет персонаж, изображение

default me = Character("[my_name]", color="#dfbe03", image="me "+"[my_type]")

default my_av_zp = 0 #средняя зарплата, станет больше 0 после того, как персонаж сходит на работу
default my_can_skip_work = {
    "morg": False,
    "shop": False
}
default my_boss_kind = boss_kind["good"]

#default my_job_timemark #метка к какому времени нужно попасть на работу




# Определение персонажей игры. ======= перенести в соответствующие блоки
define al = Character('Эллис', color="#e7461e", image='alice')
define jul = Character('Джулия', color="#c1ff15", image='juli') #Джулия девушка из казино



init:
    $ left2 = Position(xalign=0.99, yalign = 1)
    $ boss_position_right = Position(xalign=0.95, yalign = 1.5)

    #статы
    $ stat_money = 0
    $ stat_good = 0
    $ stat_bad = 0
    $ stat_strong = 0
    $ stat_ratio = 0

    $ stat_health = 200
    $ stat_health_max = 200

    $ stat_mind = 50 #от -200 до 200 меньше 0 это уже разные степени безумия
    $ stat_mind_max = 200
    $ stat_mad_max = 200

#сводка выборов, которые на что-то влияют

init python: 
    my_choises = {
        "ep001_whiskey_drink" : False
    }
    






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


#проверка наличия денег
init python:
    def money_enough(sum):
        if sum > stat_money:
            renpy.notify("У вас недостаточно денег! На вашем счету " + str(stat_money) + "$")
            renpy.pause(0.5)
            return False
        return True

label show_stats:  
    $ renpy.notify("деньги: " + str(stat_money) + "$ \n"
    "хорошая репутация: " + str(stat_good) +
    "\nдурная слава: " + str(stat_bad) +
    "\nсила: " + str(stat_strong) +
    "\nрасчетливость: " + str(stat_ratio) 
    )
    pause(4)


#===================ВРЕМЯ 
#init:  
    #$ hour_start = 6  #стартовое время 7 утра
    #$ minut_start = 50 

    #$ hours_actual = hour_start  #текущее время
    #$ minutes_actual = minut_start 

    #$ g_hours = 0  #игровое время в часах
    #$ g_minutes = 0   #минуты, не вошедшие в час

label init_global_timer:
    $ global_time = Global_time(6, 50)

init python: 
    class Global_time(object):
        def __init__(self, hours_start = 0, minutes_start = 0):
            self.hours_start = hours_start    # запомним стартовое время внутри игры на начало игры
            self.minutes_start = minutes_start
            self.hours_actual = hours_start    # актуальное время на часах внутри игры
            self.minutes_actual = minutes_start  
            self.g_hours = 0 #игровое время внутри игры - сколько часов и минут персонаж прожил с момента начала игры
            self.g_minutes = 0

        def day_postfix(num):
            if num == 1:
                return "день"
            elif num in [2, 3, 4]:
                return "дня"
            else:
                return "дней"

        def get_days(self, hours):
            return hours // 24    

        def show_game_time():  #показать сколько времени прошло с начала игры для персонажа (дни и часы)
            d = self.get_days()
            h = self.g_hours % 24
            part1 = ""
            if d > 0:
                part1 = str(d) + " " + day_postfix(d % 10)
            renpy.notify("Прошло "+ part1 +" " + str(h)+ " ч.")     

        def add_time(self, prefix, sum): #добавление времени минут, часов или дней
            #global self.g_minutes, self.g_hours
            if prefix == "m":
                self.g_minutes += sum
                if self.g_minutes > 59:
                    self.add_time("h", self.g_minutes // 60)
                    self.g_minutes %= 60
            elif prefix == "h":
                self.g_hours += sum
            elif prefix == "d":
                self.g_hours += sum*24
            
        def show_time(self): #показать текущее время в игровом мире
            self.actual_time()
            renpy.notify("Текущее время: " + str(self.hours_actual)+" ч. "+ str(self.minutes_actual)+ " .мин")

        def actual_time(self):  #актуализировать текущее время в игровом мире (исходя их времени, которое прожил персонаж с начала игры)
            #global minutes_actual, hours_actual
            self.minutes_actual = self.g_minutes + self.minutes_start
            ost = self.minutes_actual // 60 #0 если нет переполнения минут при складывании со стартовым временем
            self.minutes_actual %= 60 # чтобы было не больше 60
            self.hours_actual = (self.g_hours + self.hours_start + ost) % 24

        #def is_equal_delta(self, hour, minutes):



init python:   
    #отметка времени - объекты нужны для учета, сколько глобально прошло времени с какого-то конкретного события, для этого события создается метка времени
    #отметка создается в абсолютном времени (сколько персонаж прожил с начала игры)
    #с вариацией "метка в будущем"
    class Time_mark(object):
        def __init__(self, global_time, future_plus_day = 0, future_plus_hours = 0, future_plus_mins = 0):             
            self.minutes = global_time.g_minutes + future_plus_mins
            self.hours = global_time.g_hours + future_plus_day*24 + future_plus_hours + self.minutes // 60 
            self.minutes %= 60           
            self.in_minutes = self.hours*60 + self.minutes
            #на всякий случай запоминаем игровое время (пока не работает для метки будущего)
            # актуальное время игровой метки:
            self.minutes_clock = self.minutes + global_time.minutes_start
            ost = self.minutes_clock // 60 #0 если нет переполнения минут при складывании со стартовым временем
            self.minutes_clock %= 60 # чтобы было не больше 60
            self.hours_clock = (self.hours + global_time.hours_start + ost) % 24


        # узнать сколько времени прошло с момента метки  #отрицательное число будет означать сколько времени осталось до метки
        def how_long(self, prefix, global_time): #в префикс передаются обозначения m h d  - минуты, часы, дни соответственно
            #переведем все в минуты
            global_mins = global_time.g_hours*60 + global_time.g_minutes
            time = global_mins - self.in_minutes #разница в минутах
            if prefix == "m":
                return time
            elif prefix == "h":
                return time // 60
            elif prefix == "d":
                return (time // 60) // 24
            else:
                renpy.notify("невозможно выполнить операцию")
                return 0

        def get_time(self, textmark = ""): #показать время на часах, которое соответствует мете
            return textmark + str(self.hours_clock)+" ч. "+ str(self.minutes_clock)+ " .мин"

        def equel_with_delta(self, delta = 0): #дельта указывается в минутах
            difference = self.how_long
            if difference >= (-1)*delta and difference <= delta:
                return True
            return False





        





    



    




