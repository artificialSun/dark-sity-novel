#адвокат, который напивается, можно его обворовать, но вообще нпс
define adv = Character('[adv.name]', color="#077010", image='adv')
$ adv.name = "Пьяница"
$ adv.rel = 0
$ adv.is_alife = True

label nps_adv_meet:
    "Тот парень явно перебрал. Идет мне навстречу."
    "Ему явно нехорошо."
    
    "В такой темный вечер он легко может стать жертвой грабителей."

    show adv alco
    with fade 
    
    adv "ВАА-аа-рх"

    