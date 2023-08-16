init python:
    boss_kind = {
        "good": "отличный парень",
        "bad": "настоящий козлина" 
    }
init:
    #image boss_img = "images/boss good.png"
    default boss = Character(name = "Начальник", color="#9b1200", image="[boss_img]")
    $ boss_img_path = "images/boss good.png"

    

label init_boss:
    if my_boss_kind == boss_kind["bad"]:
        if my_job == "morg":
            $ boss_img_path = "images/boss bad.png"
        else:
            $ boss_img_path = "images/boss bad shop.png"
        #"тестовая запись плохой"
    else:
        if my_job == "morg":
            $ boss_img_path = "images/boss good.png"
        else:
            $ boss_img_path = "images/boss good shop.png"
        #"тестовая запись хороший"
    image boss_img = "[boss_img_path]"
    return