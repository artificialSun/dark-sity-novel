# Инициализация персонажа
label init_my_character:      
    $ choice = "молодого"   
    $ my_type = "man" 
    label choice_my_character:   #выбор внешности игрокаR               
        menu:        
            "парень" :
                show me man at left  
                $ choice = "молодого"       
                $ my_type = "man"  
                #$ stat_money = 250  
                $ room1_secret_money = 250 #деньги в тайнике, которые гг сможет забрать
            "старик":
                show me oldman at right
                $ choice = "пожилого" 
                $ my_type = "oldman"  
                #$ stat_money = 1000
                $ room1_secret_money = 1000
            "подтвердить выбор":
                hide me with fade  
                $ renpy.notify ("Вы выбрали " + str(choice))
                image me_img = "images/me "+"[my_type]" + ".png"
                image me_big = "images/me "+"[my_type]" + " big.png"
                jump choice_my_name
        jump choice_my_character
    return    
        
    label choice_my_name:       # выбор имени игрока  
        $ my_name = renpy.input("Выбери имя персонажа", length = 25, default = "Фрэнк").strip()

        if my_name == "":
            $ my_name = "Фрэнк"
        $ renpy.notify("Вас зовут "+str(my_name))
        
    return
return

#========================= НАЧАЛО ИГРЫ
label start:
    scene bg city

    show rain
    with fade
    pause(0.5)  

    #====тестовые блоки
    #==================

    $ renpy.notify("Твое приключение начинается здесь, но сначала выбери персонажа")
    pause(1.0)
    call init_my_character

    # запускаем эпизоды по порядку
    jump ep001_stavka


    "Кажется этот чертов дождь никогда не закончится."    
    "Мне нужно закончить одно дело."

    menu:
        "Зайти в казино":
            call go_casino
        "Продолжить путь":            
            me "Сегодня я уже достаточно потратил денег"

    
    call ep_alice


    
    
    

return    






