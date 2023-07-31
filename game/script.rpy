# Инициализация персонажа
label init_my_character:      
    $ choice = "молодого"   
    label choice_my_character:   #выбор внешности игрока
        $ me_old_img = "me man"        
        menu:        
            "парень" :
                show me man at left  
                $ choice = "молодого"       
                $ me_old_img = "me man"    
            "старик":
                show me oldman at right
                $ choice = "пожилого" 
                $ me_old_img = "me oldman"  
            "подтвердить выбор":
                hide me with fade  
                $ renpy.notify ("Вы выбрали " + str(choice))
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

    scene bg london

    show rain
    with fade
    pause(0.5)    

    #====тестовые блоки
    #==================

    $ renpy.notify("Твое приключение начинается здесь, но сначала выбери персонажа")
    pause(1.0)
    call init_my_character

    "Кажется этот чертов дождь никогда не закончится."
    "Мне нужно закончить одно дело."

    menu:
        "Зайти в казино":
            call go_casino
        "Продолжить путь":            
            me "Сегодня я уже достаточно потратил денег"

    # запускаем эпизоды по порядку
    call ep_alice


    
    
    

return    






