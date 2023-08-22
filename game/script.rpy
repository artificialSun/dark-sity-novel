# Инициализация персонажа
label init_my_character:      
    $ choice = "молодого"   
    $ my_type = "man" 
    $ room1_secret_money = 250 #деньги в тайнике, которые гг сможет забрать
    label choice_my_character:   #выбор внешности игрокаR               
        menu:        
            "парень" :
                show me man normal at left  
                $ choice = "молодого"       
                $ my_type = "man"  
                $ room1_secret_money = 250 #деньги в тайнике, которые гг сможет забрать
            "старик":
                show me oldman normal at right
                $ choice = "пожилого" 
                $ my_type = "oldman"  
                $ room1_secret_money = 500
            "подтвердить выбор":
                hide me with fade  
                $ renpy.notify ("Вы выбрали " + str(choice))
                #image me_img = "images/me "+"[my_type]" + ".png"
                #image me_big = "images/me "+"[my_type]" + " big.png"
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

    call init_global_timer from _call_init_global_timer

#tests
    #call test_morg_first_day     
    #call start_game_morg
    #call init_morg_mini_game

  

    show screen disklamer

    show rain
    with fade
    pause(0.5)  

    #====тестовые блоки
    call test_big_info_panel

    #call animation_test  

    #call test_me_show  

    #call day1_day_dream

    #call test_shop_job
    #"hhhhh1"
    #image boss_img = "images/boss bad.png"    
    #"вот сейчас выведу сцуко картинку"
    #show boss_img at right
    #show me_img at left
    #"смотри сюда блин"
    #hide boss_img
    #image boss_img2 = "images/boss good.png"
    #"вот сейчас выведу сцуко картинку"
    #show boss_img2 at right
    #"fhjkdshfjg"
    #"hfdskjgf"
    # call test_inventory
    # show screen letter("Это больльшой тестовый текст записки \n можно мне этих вкусных пончиков?", "me")
    
    #==================

    $ renpy.notify("Твое приключение начинается здесь, но сначала выбери персонажа")
    pause(1.0)

    call init_my_character from _call_init_my_character

    call init_inventoryes from _call_init_inventoryes

    

    # запускаем эпизоды по порядку
    jump ep001_wakeup


    "Кажется этот чертов дождь никогда не закончится."    
    "Мне нужно закончить одно дело."

    menu:
        "Зайти в казино":
            call go_casino from _call_go_casino_2
        "Продолжить путь":            
            me "Сегодня я уже достаточно потратил денег"

    
    call ep_alice from _call_ep_alice


    
    
    

return    






