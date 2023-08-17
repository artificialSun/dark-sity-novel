init:
    # отзеркаливание
    transform hflip():
        xzoom -1.0
    transform vflip():
        yzoom -1.0

    # подпрыгивание персонажа
    transform leap(dyz=0.01, dxz=0.005, dt=.4):
        yzoom 1.0
        easein dt*0.25 yzoom 1.0+dyz xzoom 1.0-dxz
        easeout dt*0.25 yzoom 1.0 xzoom 1.0
        easein dt*0.25 yzoom 1.0-dyz xzoom 1.0+dxz
        easeout dt*0.25 yzoom 1.0 xzoom 1.0

    # относительное положение на экране по х(/y)-координате
    transform at_axy(ax=.5, ay=1.0):
        align (ax, ay)

    # вращение вокруг указанной точки
    transform at_rot(x=0, y=0, delay=30, xa=.5, ya=.5):
        rotate 0.0
        anchor(xa, ya)
        pos(x, y)
        linear delay rotate 360
        repeat

    # слева, но не у самого края
    #transform left2(xa=.35):
    #    xalign xa xanchor 0.5 ypos 1.0 yanchor 1.0

    # справа, но не у самого края
    #transform right2(xa=.65):
    #    xalign xa xanchor 0.5 ypos 1.0 yanchor 1.0

    # слева, за краем
    transform left0():
        xpos .0 xanchor 1.0 ypos 1.0 yanchor 1.0

    # справа, за краем
    transform right0():
        xpos 1.0 xanchor .0 ypos 1.0 yanchor 1.0

    # однократное спрайтотрясение
    transform shake(dt=.05, dxy=10, dxy_from=5):
        xoffset rnd(dxy_from, dxy) - rnd(dxy_from, dxy) yoffset rnd(dxy_from, dxy)
        pause dt
        xoffset rnd(dxy_from, dxy) - rnd(dxy_from, dxy) yoffset rnd(dxy_from, dxy)
        pause dt
        xoffset rnd(dxy_from, dxy) - rnd(dxy_from, dxy) yoffset rnd(dxy_from, dxy)
        pause dt
        xoffset rnd(dxy_from, dxy) - rnd(dxy_from, dxy) yoffset rnd(dxy_from, dxy)
        pause dt
        xoffset rnd(dxy_from, dxy) - rnd(dxy_from, dxy) yoffset rnd(dxy_from, dxy)
        pause dt
        xoffset rnd(dxy_from, dxy) - rnd(dxy_from, dxy) yoffset rnd(dxy_from, dxy)
        pause dt
        xoffset rnd(dxy_from, dxy) - rnd(dxy_from, dxy) yoffset rnd(dxy_from, dxy)
        pause dt
        xoffset rnd(dxy_from, dxy) - rnd(dxy_from, dxy) yoffset rnd(dxy_from, dxy)
        pause dt
        xoffset rnd(dxy_from, dxy) - rnd(dxy_from, dxy) yoffset rnd(dxy_from, dxy)
        pause dt
        xoffset rnd(dxy_from, dxy) - rnd(dxy_from, dxy) yoffset rnd(dxy_from, dxy)
        pause dt
        xoffset 0 yoffset 0
        pause dt

    # увеличение/уменьшение в центре экрана
    #transform wow(dt=.25, z=1.25):
        #anchor(.5, .5) align(.5, .5) zoom 1.0
        #easeout dt*.5 anchor(.5, .5) align(.5, .5) zoom z
        #easein dt*.5 anchor(.5, .5) align(.5, .5) zoom 1.0
        #repeat

    # выстрел по дуге
    transform bow(x1, y1, x2, y2, dy=300, dt=1.0, rot=0):
        pos(x1, y1) anchor(.5, .5) alpha 1.0 rotate 0
        parallel:
            alpha .0
            easein dt*.15 alpha 1.0
            pause dt*.7
            easein dt*.15 alpha .0
        parallel:
            linear dt xpos x2 rotate rot
        parallel:
            easein dt*.5 ypos(-dy+(y1+y2)/2)
            easeout dt*.5 ypos(y2)

init -999 python:
    # сканируем папку музыки, на выходе - список мелодий без указанного расширения и папки
    def get_music_list(folder="music", ext="ogg"):
        res = []
        list = renpy.list_files()
        for i in list:
            if i.startswith(folder):
                s = i[(len(folder) + 1):]
                if s.endswith("." + ext):
                    res.append(s[:(-len(ext) - 1)])
        return res

    # сканируем папку, на выходе - список файлов нужного расширения
    # по умолчанию расширения убираются
    def get_file_list(folder="", ext="", hideext=True):
        res = []
        list = renpy.list_files()
        for i in list:
            if i.startswith(folder) or (not folder):
                if folder:
                    s = i[(len(folder) + 1):]
                else:
                    s = i
                if ext:
                    if s.endswith("." + ext):
                        if hideext:
                            s = s[:(-len(ext) - 1)]
                        res.append(s)
                else:
                    res.append(s)
        if len(res) > 1:
            # сортировка без учета регистра
            res = sorted(res, key=lambda s: s.lower())
        return res

    # получить цвета для матрицы
    def get_rgba(color):
        col = Color(color)
        rgb = col.rgb
        return rgb[0], rgb[1], rgb[2], col.alpha

    # получить спрайт с искажением цветов
    def LiveMatrix(img, matrix):
        return im.MatrixColor(renpy.easy.displayable(img), matrix)

    # получить спрайт с искажением цветов
    def LiveTint(img, r=1.0, g=1.0, b=1.0):
        return LiveMatrix(img, im.matrix.tint(r, g, b))

    # изменить насыщенность
    def LiveBlind(img, blind=.01):
        return LiveMatrix(img, im.matrix.saturation(blind))

    # изменить яркость
    def LiveBright(img, bright=.1):
        return LiveMatrix(img, im.matrix.brightness(bright))

    # силуэт спрайта
    # использовать в init 1901 и выше (после автообъявления изображений)
    def LiveShadow(img, color="#000"):
        r, g, b, a = get_rgba(color)
        return LiveMatrix(img, im.matrix((0, 0, 0, 0, r, 0, 0, 0, 0, g, 0, 0, 0, 0, b, 0, 0, 0, a, 0,)))

    # выстрел снарядом shell от перса spr_from к персу spr_to
    # по дуге высотой -dy
    def shoot(shell, spr_from, spr_to, dy=300, dt=1.0, rot=0, shell_as=None):
        if shell_as is None:
            shell_as = shell
        if spr_from == "left":
            x1, y1 = 0, config.screen_height / 2
        elif spr_from == "right":
            x1, y1 = config.screen_width / 2, config.screen_height / 2
        else:
            x, y, w, h = renpy.get_image_bounds(spr_from)
            x1, y1 = int(x + w/2), int(y + h/2)
        if spr_to == "left":
            x2, y2 = 0, config.screen_height / 2
        elif spr_to == "right":
            x2, y2 = config.screen_width / 2, config.screen_height / 2
        else:
            x, y, w, h = renpy.get_image_bounds(spr_to)
            x2, y2 = int(x + w/2), int(y + h/2)
        renpy.show(shell_as, what=shell, at_list=[bow(x1, y1, x2, y2, dy, dt, rot)])
        renpy.pause(dt)

    # сменить размер шрифта в игре
    # вызывать из init -1 python, не раньше
    def font_size(say=26, who=None, prf=None, mm=None):
        style.say_dialogue.size = say # текст в текстбоксе
        style.say_thought.size = say # текст в текстбоксе
        if not who is None:
            style.say_label.size = who # имя персонажа
        if not prf is None:
            # интерфейс (настройки и сохранения)
            style.pref_label_text.size = prf
            style.pref_button_text.size = prf
            style.small_button_text.size = prf
            style.large_button_text.size = prf
            style.file_picker_text.size = prf
            style.file_picker_button_text.size = prf
            style.file_picker_nav_button_text.size = prf
            style.button_text.size = prf # текст на кнопках
            style.label_text.size = prf # надписи
        if not mm is None:
            style.mm_button_text.size = mm # кнопки главного меню
        # применяем изменения
        style.rebuild()

    # окно игры в центре экрана (вызывается из init)
    def window_center():
        import os
        os.environ['SDL_VIDEO_CENTERED'] = '1'

    # автоматическое объявление изображений (вызывается из init)
    def images_auto(folders=["images", "gui"]):
        config.automatic_images_minimum_components = 1
        config.automatic_images = [' ', '_', '/']
        config.automatic_images_strip = folders

    # остановить перемотку
    def stop_skip():
        renpy.config.skipping = None

    # узнать текущие размеры изображения типа displayable
    # например, после масштабирования и других операций
    # не работает в разделе init
    def get_size(displayable):
        return renpy.render(renpy.easy.displayable(displayable), 0, 0, 0, 0).get_size()
    def get_width(displayable):
        return get_size(displayable)[0]
    def get_height(displayable):
        return get_size(displayable)[1]

    # если это не список, то сделать единственным элементом списка
    def make_list(param):
        if param is None:
            return None
        if not isinstance(param, list):
            param = [param]
        return param

    # эффект dissolve, но с учетом прозрачности спрайта. пример:
    # with diss
    diss = Dissolve(.1, alpha=True)
    diss25 = Dissolve(.25, alpha=True)

    # эффект вспышки нужного цвета для смены фонов. пример:
    # with flash("#822")
    def flash(color="#fff", t=1.0, w=0):
        return Fade(t*.25, w, t*.75, color=color)

# автоматическое объявление анимации
    # описание функции Ani:
    # автоматическое объявление картинки с анимацией,
    # например есть кадры "images/neko%s.png",
    # где %s - числа от 1 до 5, тогда объявляем анимацию так:
    # image neko = Ani("neko", 5, 0.5, reverse = False)
    # где:
    # img_name - имя файла без номера (например, "neko")
    # frames - количество кадров
    # delay - пауза между кадрами в секундах
    # если delay это кортеж, например (1, 2), то скорость будет меняться от 1 до 2 секунд
    # loop - зациклить анимацию (по умолчанию включено)
    # reverse - нужно ли проигрывание анимации в обратную сторону
    # effect - эффект для смены кадров
    # start - с какой цифры начинать отсчет кадров
    # ext - расширение, если оно отлично от Null, то работаем с файлами,
    # при ext=Null - с displayable (уже объявленными или даже измененными изображениями)
    # так же можно добавлять любые стандартные для изображений параметры, типа масштабирования или прозрачности:
    # image neko = Ani("neko", 5, 0.5, zoom=2.0, alpha=0.75)
    def Ani(img_name, frames, delay=.1, loop=True, reverse=False, effect=diss, start=1, ext=None, **properties):
        args = []
        # если пауза переменная, то вычисляем ее шаг
        if isinstance(delay, tuple):
            d0 = delay[0]
            d1 = delay[1]
            f = (frames - 1)
            if f <= 0:
                dp = 0
            else:
                dp = (d1 - d0) * 1.0 / f
            delay = d0
        else:
            dp = 0
        # перебираем все кадры анимации
        for i in range(start, start + frames):
            if ext:
                img = renpy.display.im.image(img_name + str(i) + "." + ext)
            else:
                img = renpy.easy.displayable(img_name + str(i))
            img = Transform(img, **properties)
            args.append(img)
            if reverse or loop or (i < start + frames - 1):
                args.append(delay)
                delay += dp
                # добавляем эффект для смены кадров
                args.append(effect)
        if reverse: # обратная анимация, если нужна
            dp = -dp
            delay += dp
            for i in range(start + frames - 2, start, -1):
                if ext:
                    img = renpy.display.im.image(img_name + str(i) + "." + ext)
                else:
                    img = renpy.easy.displayable(img_name + str(i))
                img = Transform(img, **properties)
                args.append(img)
                if loop or (i > start + 1):
                    args.append(delay)
                    delay += dp
                    args.append(effect)
        return anim.TransitionAnimation(*args)

    # анимированная текстура с вырезанием по маске
    def AniMask(mask_name, img_name, frames, delay=.1, loop=True, reverse=False, effect=diss, start=1, ext=None, **properties):
        args = []
        # если пауза переменная, то вычисляем ее шаг
        if isinstance(delay, tuple):
            d0 = delay[0]
            d1 = delay[1]
            f = (frames - 1)
            if f <= 0:
                dp = 0
            else:
                dp = (d1 - d0) * 1.0 / f
            delay = d0
        else:
            dp = 0
        # перебираем все кадры анимации
        for i in range(start, start + frames):
            if ext:
                img = renpy.display.im.image(img_name + str(i) + "." + ext)
            else:
                img = renpy.easy.displayable(img_name + str(i))
            img = AlphaMask(img, renpy.easy.displayable(mask_name))
            img = Transform(img, **properties)
            args.append(img)
            if reverse or loop or (i < start + frames - 1):
                args.append(delay)
                delay += dp
                # добавляем эффект для смены кадров
                args.append(effect)
        if reverse: # обратная анимация, если нужна
            dp = -dp
            delay += dp
            for i in range(start + frames - 2, start, -1):
                if ext:
                    img = renpy.display.im.image(img_name + str(i) + "." + ext)
                else:
                    img = renpy.easy.displayable(img_name + str(i))
                img = AlphaMask(img, renpy.easy.displayable(mask_name))
                img = Transform(img, **properties)
                args.append(img)
                if loop or (i > start + 1):
                    args.append(delay)
                    delay += dp
                    args.append(effect)
        return anim.TransitionAnimation(*args)

    # показать фон с именем bg указанного цвета color
    def bg(color="#000", bg="bg"):
        renpy.scene()
        renpy.show(bg, what=renpy.easy.displayable(color))

    # меняем стандартное время всех или некоторых эффектов для появления/исчезновения спрайтов
    def move_time(delay=.5, effects=["move", "ease"]):
        effects = make_list(effects)
        for i in effects:
            define.move_transitions(i, delay)

    # для цифровых часиков (не менять, не вызывать)
    clock_properties = None
    def show_digital_clock(st, at):
        import datetime
        cur_time = datetime.datetime.now().strftime("%H:%M:%S")
        img = Text(cur_time, **clock_properties)
        return img, .25

    # создать цифровые часики с любым именем картинки (только в init!):
    # $ create_clock("digital_clock", size=48, color="#fff8", outlines=[(2, "#0008", 0, 0)], align=(.05, .05))
    # применение - на любом экране screen:
    # add "digital_clock"
    # или в виде спрайта:
    # show digital_clock
    def create_clock(name, **properties):
        global clock_properties
        clock_properties = properties
        renpy.image(name, DynamicDisplayable(show_digital_clock))

    # показать экран на слое "мастер",
    # чтобы он не исчезал, когда прячем интерфейс
    def show_s(screen):
        renpy.show_screen(screen, _layer="master")

    # убрать экран со слоя "мастер"
    def hide_s(screen):
        renpy.show_screen(screen, layer="master")

    # показать рамку, неубирающуюся вместе с другими экранами
    # вызов: $ show_forever("имя_картинки_для_рамки")
    def show_forever(forever_frame):
        renpy.show_screen("forever_screen", forever_frame, _layer="foreverlayer")

    # спрятать рамку, неубирающуюся вместе с другими экранами
    def hide_forever():
        renpy.hide_screen("forever_screen", layer="foreverlayer")

    # получить английское название времени суток
    # если не указывать время в часах,
    # то будет взято системное время
    # можно задать начало утра, дня, вечера и ночи в часах от 0 до 23
    def time_of_day(hours=None, morning=7, day=11, evening=18, night=23):
        if hours is None:
            hours = int(datetime.datetime.now().strftime("%H"))
        res = "night" # по умолчанию ночь
        # границы любого времени суток можно поменять
        if (hours >= morning) and (hours <= day):
            res = "morning"
        if (hours > day) and (hours <= evening):
            res = "day"
        if (hours > evening) and (hours < night):
            res = "evening"
        return res

    # словарь цветов для времен суток
    color_filters = {"morning": "#8404", "day": "#0000", "evening": "#0484", "night": "#000b"}

    # получить цвет фильтра, соответствующий времени суток
    def color_of_day(hours=None):
        return color_filters[time_of_day(hours)]

    # действие - продолжить игру оттуда, где закончили
    # если загружать пока нечего, то кнопка неактивна
    # textbutton _("Продолжить игру") action Continue()
    class Continue(Action, DictEquality):
        def __call__(self):
            FileLoad(1, confirm=False, page="auto", newest=True)()
        # кликабельность кнопки
        def get_sensitive(self):
            return FileLoadable(1, page="auto")

    # объявлена ли картинка с именем name
    def has_image(name):
        for i in renpy.display.image.images:
            # такая конструкция позволяет исключить пустые теги
            if name == " ".join(" ".join(i).split()):
                return True
        return False

    # задан ли курсор с таким именем
    def has_mouse(mouse):
        if config.mouse:
            if mouse in config.mouse.keys():
                return True
        return False

    # рандомное целое число в заданных пределах
    # (i_to можно не указывать, тогда максимум берется из i_from)
    def rnd(i_from=0, i_to=None):
        if i_to is None:
            i_to = i_from
            i_from = 0
        return renpy.random.randint(int(i_from), int(i_to))

    # рандомное дробное число в заданных пределах
    # (f_to можно не указывать, тогда максимум берется из f_from)
    def rndf(f_from=0, f_to=None):
        if f_to is None:
            f_to = f_from
            f_from = .0
        return f_from + renpy.random.random() * (f_to - f_from)

    # канал для эффекта
    renpy.music.register_channel("effect", "sfx", loop=True)

    # зацикленный звуковой эффект, не музыка
    def sfxplay(name, channel="effect", loop=True, fadein=0, fadeout=0, ext="ogg"):
        if name:
            renpy.music.play("sounds/" + name + "." + ext, channel=channel, loop=loop, fadein=fadein, fadeout=fadeout)

    # костыли для звуков и музыки - сокращают писанину
    # можно запускать музыку или звуки, не указывая папки и расширения
    # по умолчанию для музыки music/*.ogg
    # по умолчанию для звуков sounds/*.ogg

    # запустить музыку, если она еще не играет
    def mplay(mname, fadein=1.5, fadeout=1.5, loop=True, channel="music", ext="ogg"):
        old_fn = renpy.music.get_playing()
        new_fn = "music/"+ mname + "." + ext
        if mname:
            if old_fn != new_fn:
                renpy.music.play(new_fn, channel=channel, loop=loop, fadein=fadein, fadeout=fadeout)

    # перезапустить музыку, даже если уже играет она же
    def mreplay(mname, fadein=1.5, fadeout=1.5, loop=True, channel="music", ext="ogg"):
        new_fn = "music/"+ mname + "." + ext
        renpy.play(new_fn, channel=channel, loop=loop, fadein=fadein, fadeout=fadeout)

    # запустить музыку для имени файла и пути
    def fnplay(new_fn, fadein=1.5, fadeout=1.5, channel="music"):
        old_fn = renpy.music.get_playing()
        if old_fn != new_fn and new_fn:
            renpy.play(new_fn, channel=channel, loop=True, fadein=fadein, fadeout=fadeout)

    # последняя сохраненная мелодия
    last_music_fn = ""

    # сохранить в памяти играющую мелодию
    def msave():
        global last_music_fn
        last_music_fn = renpy.music.get_playing()

    # восстановить игравшую при сохранении мелодию
    def mrestore(fadein=1.5, fadeout=1.5, channel="music"):
        fnplay(last_music_fn, fadein=fadein, fadeout=fadeout, channel=channel)

    # воспроизвести звук для канала audio, который поддерживает многопоточность
    def splay(mname, fadein=0, fadeout=0, channel="audio", ext="ogg"):
        if mname:
            renpy.play("sounds/" + mname + "." + ext, channel=channel, fadein=fadein, fadeout=fadeout)

    # воспроизвести звук
    def sndplay(mname, fadein=0, fadeout=0, channel="sound", ext="ogg"):
        if mname:
            renpy.play("sounds/" + mname + "." + ext, channel=channel, fadein=fadein, fadeout=fadeout)

    # голос
    def vplay(mname, fadein=0, fadeout=0, channel="voice", ext="ogg"):
        if mname:
            renpy.play("voices/" + mname + "." + ext, channel=channel, fadein=fadein, fadeout=fadeout)

    # остановить звук
    def sstop(fadeout=None, channel='audio'):
        renpy.music.stop(channel=channel, fadeout=fadeout)

    # остановить звук
    def sndstop(fadeout=0, channel='sound'):
        renpy.music.stop(channel=channel, fadeout=fadeout)

    # остановить музыку
    def mstop(fadeout=1.5, channel='music'):
        renpy.music.stop(channel=channel, fadeout=fadeout)

    # остановить зацикленный эффект
    def sfxstop(fadeout=1.5, channel='effect'):
        renpy.music.stop(channel=channel, fadeout=fadeout)

    # превращаем функции в action для экранов screen
    SPlay = renpy.curry(splay)
    SFXPlay = renpy.curry(sfxplay)
    MPlay = renpy.curry(mplay)
    FNPlay = renpy.curry(fnplay)
    VPlay = renpy.curry(vplay)
    SStop = renpy.curry(sstop)
    MStop = renpy.curry(mstop)

    # установить громкость канала в коэффициенте от громкости звуков
    def sfxvolume(volume=1.0, channel='effect', delay=1.0):
        volume = _preferences.get_volume('sfx') * volume
        if volume < 0:
            volume = 0
        if volume > 1.0:
            volume = 1.0
        renpy.music.set_volume(volume, delay, channel=channel)

    import re

    def get_tags(text, prefix='#'):
        res = {}
        # выуживаем все теги ремарок
        tags = re.findall('{' + prefix + '([^}]+)}', text)
        # перебираем полученные теги
        for i in tags:
            parts = i.split('=')
            if len(parts) > 0:
                key = parts[0].strip()
                val = None
                if len(parts) > 1:
                    val = parts[1]
                # добавляем тэг и его значение в словарь
                res[key] = val
        # возвращаем значения тэгов в виде словаря
        return res

    # убрать все тэги из строки
    def del_tags(txt, prefix='#'):
        return re.sub(r'{' + prefix + '([^}]+)}', '', txt)

    # разделить строку на две части - до и после знака равно
    # (или другого разделителя) и убрать пробелы вокруг этих частей
    def get_key_val(text, sep='='):
        txt = text.split(sep, 1)
        val, key = None, None
        if len(txt) > 0:
            key = txt[0].strip()
        if len(txt) > 1:
            val = txt[1].strip()
        return key, val

    # поиск в строке значения невидимого читателю тега
    # пример использования:
    # $ text = "Текст текст {#image=logo.png} текст."
    # $ img = get_tag(text, 'image')
    # на выходе в img будет logo.png
    def get_tag(text, tag, default=None, prefix='#'):
        tag = tag.strip()
        tags = get_tags(text, prefix)
        if tag in tags.keys():
            return tags[tag]
        return None

    # есть ли тэг в строке
    def have_tag(text, tag, prefix='#'):
        return tag in get_tags(text, prefix).keys()

    # получить цвета для матрицы
    def get_rgba(color):
        col = Color(color)
        rgb = col.rgb
        return rgb[0], rgb[1], rgb[2], col.alpha

    # показать спрайт с искажением цветов
    def LiveMatrix(img, matrix):
        return im.MatrixColor(renpy.easy.displayable(img), matrix)

    # изменить насыщенность
    def LiveBlind(img, blind=.01):
        return LiveMatrix(img, im.matrix.saturation(blind))

    # силуэт спрайта
    def LiveShadow(img, color="#000"):
        r, g, b, a = get_rgba(color)
        return LiveMatrix(img, im.matrix((0, 0, 0, 0, r, 0, 0, 0, 0, g, 0, 0, 0, 0, b, 0, 0, 0, a, 0,)))

    # список слоев. наш экран не будет исчезать при нажатии 'h'
    config.layers.insert(config.layers.index("transient") + 1, "foreverlayer")

    # нужно включить автоматические сохранения, чтобы работала Continue (подставить = True)
    config.has_autosave = False

    # для input
    current_input_text = ""
    input_changes = False

    # функция вызова поля ввода с кнопками ок и отмена. пример:
    # $ s = input("Введите имя:", default="Аноним")
    def input(prompt=None, default=None, allow=None, caption_bg=None):
        global current_input_text, input_changes
        input_changes = False
        current_input_text = ""
        ShowMenu("my_input", prompt, default, allow, caption_bg=caption_bg)()
        if current_input_text is None:
            return None
        if not input_changes:
            current_input_text = default
        return current_input_text
    Input = renpy.curry(input)

    # функция вызова сообщения с кнопкой ок. пример:
    # $ message("Всё в норме.", size=26, color="#8a8")
    def message(message_text=" ", **args):
        ShowMenu("my_message", message_text, **args)()
    Message = renpy.curry(message)

    # узнать, что за символ введён или стёрт
    def input_changed(input_str):
        global current_input_text, input_changes
        current_input_text = input_str
        input_changes = True

init 1 python:
    # параметры текста для ввода
    style.input_text.xalign = .5
    style.input_text.font = style.say_dialogue.font
    style.input_text.size = style.say_dialogue.size

# экран ввода с кнопками ок и отмена
screen my_input(prompt=None, default=None, allow=None, caption_bg=None):
    modal True
    tag menu
    window style "gm_root":
        background "#0008" # необязательное затемнение экрана
        key "dismiss" action []
        key "input_enter" action Return()
        key "K_ESCAPE" action [SetVariable("current_input_text", None), Return()]
        frame:
            style_group "yesno"
            align (.5, .5)
            vbox align (.5, .5):
                spacing config.screen_width / 60
                if prompt:
                    frame:
                        if caption_bg:
                            background caption_bg
                        align (.5, .0) xminimum config.screen_width / 4
                        label prompt style "pref_label" xalign .5
                input id "input" style "input_text" changed input_changed default default allow allow
                hbox xalign .5:
                    textbutton _("OK") xalign .5 action Return()
                    textbutton _("Отмена") xalign .5 action [SetVariable("current_input_text", None), Return()]

# экран сообщения с кнопкой ок
screen my_message(message_text=" ", **args):
    modal True
    tag menu
    window style "gm_root":
        key "dismiss" action []
        key "input_enter" action Return()
        key "K_ESCAPE" action Return()
        frame:
            style_group "yesno"
            align (.5, .5)
            vbox align (.5, .5):
                spacing config.screen_width / 60
                xminimum config.screen_width / 4
                text " "
                label message_text style "pref_label" xalign .5
                textbutton _("OK") xalign .5 action Return()
                text " "

# экран для неубирающейся рамки
screen forever_screen (forever_frame, _layer="foreverlayer"):
    # выводится, если это игра, но не экран настроек
    if not ("preferences" in renpy.current_screen().screen_name):
        add forever_frame

# стандартное автообъявление картинок, но с webp
# выполняется после всего остального
init 1900 python hide:
    def create_automatic_images():
        seps = config.automatic_images
        if seps is True:
            seps = [ ' ', '/', '_' ]
        for dir, fn in renpy.loader.listdirfiles():
            if fn.startswith("_"):
                continue
            # Only .png and .jpg and .webp
            if not fn.lower().endswith(".png") and not fn.lower().endswith(".jpg") and not fn.lower().endswith(".webp"):
                continue
            # Strip the extension, replace slashes.
            shortfn = fn[:-4]
            if fn.lower().endswith(".webp"):
                shortfn = fn[:-5]
            shortfn = shortfn.replace("\\", "/")
            # Determine the name.
            name = ( shortfn, )
            for sep in seps:
                name = tuple(j for i in name for j in i.split(sep))
            # Strip name components.
            while name:
                for i in config.automatic_images_strip:
                    if name[0] == i:
                        name = name[1:]
                        break
                else:
                    break
            # Only names of 2 components or more by default.
            if len(name) < config.automatic_images_minimum_components:
                continue
            # Reject if it already exists.
            if name in renpy.display.image.images:
                continue
            renpy.image(name, fn)
    if config.automatic_images:
        create_automatic_images()


