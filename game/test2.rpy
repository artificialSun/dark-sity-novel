init:
    transform test_alpha():
        alpha 1.0
        pause 1
        alpha get_rand()
        pause 1.0
        repeat

    transform test_alpha2():
        function random_alpha
        pause 1
        repeat


  


        


init python:
    def get_rand():
        return renpy.random.random()

    some_var = renpy.random
    def random_alpha(trans, st, at):        
        for i in range(3):
            r1 = renpy.random.random()
            renpy.notify(str(r1))
            #r2 = renpy.random.random()
            #trans.alpha = r1
            #trans.pause = 1 # r2
        return None

label animation_test:
    "тест анимации"
    "есть куда возвращаться"
    show me_big at test_alpha3()
    pause 100
    #show Object1 at TestAnim()
    #show Object2 at TestAnimB()