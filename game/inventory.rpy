
# еще один массив для запоминания разных важных в дальнейшем выборов персонажа
$ my_choises = []


#=======================================================================================
#================================================= ОБЪЯВЛЕНИЕ ЛИЧНОГО ИНВЕНТАРЯ И ТАЙНИКОВ
label init_inventoryes:
    $ my_inventory = Inventory({"cureSleep" : 6})  

    # в тайниках можно хранить деньги и предметы и не таскать их с собой
    $ room1_secret = Inventory({"myDagger": 1, "money": room1_secret_money}) 
    #$ room1_secret_money = 0






#=======================================================================================
#================================================= КЛАСС ИНВЕНТАРЬ
init python:
    class Inventory(object):
        #inv_items = {}  # здесь хранятся пары ключ из all_items_dict - количество  !!!сами объекты не хранятся

        def __init__(self, set_of_items={}):  #на вход должен поступать набор из: ключ all_items_dict - количество
            self.inv_items = set_of_items.copy()
        #@property
        #добавить свойство, через которое прямо объект получать можно будет и его свойства


        def add_item(self, item_key, count = 1, notify=True):  #должна принимать объекты типа ключ all_items_dict и количество (по умолчанию 1)
            if count < 1:   #может оказаться вызов с 0
                return False
            item_name = all_items_dict[item_key].name # получаем имя объекта на русском

            count += self.how_mutch(item_key) #посчитали сколько предметов всего будет c теми которые есть 
            self.inv_items[item_key] = count  #обновим значение
            if notify:
                renpy.notify("добавлено "+str(count)+" "+item_name)
            return True

        def remove_item(self, item_key, count=1):     #должна принимать объекты типа ключ all_items_dict и количество (по умолчанию 1)
            item_name = all_items_dict[item_key].name # получаем имя объекта на русском
            if item_key in self.inv_items:
                if self.inv_items[item_key] > count:
                    self.inv_items[item_key] -= count
                elif self.inv_items[item_key] == count:
                    del self.inv_items[item_key]
                else:
                    
                    renpy.notify("Недостаточно предметов "+ item_name)
            else:
                renpy.notify("У вас нет предмета "+item_name)

        # #позволяет забрать деньги из хранилища или у персонажа из инвентаря и добавить себе в стат
        # по умолчанию забираем все, но если all=false, то забираем количество
        def take_money(self, all = True, count = 0): 
            if "money" in self.inv_items:
                if all or (all==False and count==self.inv_items["money"]):
                    change_stat("m", self.inv_items["money"])
                    del self.inv_items["money"]
                    return True                  
                elif (all==False and count < self.inv_items["money"]):
                    change_stat("m", count)
                    self.inv_items["money"] -= count
                    return True
            else:
                renpy.notify("Действие невозможно")
                return False

    
        def put_money(self, count): #положить деньги из стата в инвентарь
            if money_enough(count):
                change_stat("m", (-1)*count)
                if "money" in self.inv_items:
                    self.inv_items["money"] += count
                else:
                    self.inv_items["money"] = count
                return True
            else:
                return False

        def remove_all (self, item_key): #убрать все предметы одного вида и получить их количество
            count = self.how_mutch(item_key)
            if count > 0:  # выяснили 
                #count = self.inv_items[item_key]            
                del self.inv_items[item_key]
            return count

        # переложить объект из одного инвентаря в другой селф - откуда         
        def give_away(self, another_inv, item_key, all = True, count = 0):    
            if all:
                count = self.remove_all(item_key)
                #renpy.say("dd","[count]")
                another_inv.add_item(item_key, count) 
                return count               
            else:
                if self.how_mutch(item_key) >= count:
                    self.remove_item(item_key, count)
                    another_inv.add_item(item_key, count)
                    return count
            return 0
        

        def how_mutch(self, item_key):
            if item_key in self.inv_items:
                return self.inv_items[item_key]
            else:
                return 0

        def show_all(self):
            str1 = ""
            for key in self.inv_items:
                str1 += key +": "+ all_items_dict[key].name + " - "+str(self.inv_items[key])+" шт. \n"
            renpy.say("inv", str1)

        #def show_something(self):            
        #    renpy.say("invv","rrrrrrrrrrrrr")            



#=======================================================================================
#=================================================КЛАСС ПРЕДМЕТОВ
    class Item_types(enum.Enum):
        either : "общего назначения"
        weapon : "оружие"
        food : "можно употребить" 
        money : "деньги"

    class Item(object):

        def __init__(self, name, cost = 0, unique = False): #, item_type = Item_types.either):
            self.name = name
            self.unique = unique
            self.cost = cost
            #self.item_type = item_type
        @property

        def toString(self):
            return self.name
            

#==================ВСЕ ИГРОВЫЕ ПРЕДМЕТЫ
    all_items_dict = {
        "money":        Item(_("деньги"), 0, False),# Item_types.money),
        "myDagger":     Item(_("старинный кинжал"), 7000, True),# Item_types.weapon),
        "cureSleep":    Item(_("таблетка от бессонницы"), 1, False,)# item_type = Item_types.food)

    }





