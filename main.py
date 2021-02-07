import json
import math
import pydot
from os import remove
import pandas as pd
from anytree import Node, RenderTree, PreOrderIter
from anytree.exporter import UniqueDotExporter
import dictionary
import random

class weapon:
    name = ""
    coating = False
    weight = 0.0
    strength = 0
    physical_damage = 0
    critical_damage = 0
    power = ""
    agility = ""
    intellect = ""
    belief = ""

    def __init__(self, name, coating, weight, strength, physical_damage, critical_damage, power, agility, intellect, belief):
        self.name = name
        self.coating = coating
        self.weight = weight
        self.strength = strength
        self.physical_damage = physical_damage
        self.critical_damage = critical_damage
        self.power = power
        self.agility = agility
        self.intellect = intellect
        self.belief = belief

    def print_info(self):
        line = ""
        line += "Имя: " + str(self.name)+'\n'
        line += "Возможность кратковременного усиления: "
        if self.coating == False:
            line += "нет\n"
        else:
            line += "да\n"
        line += "Вес: " + str(self.weight)+'\n'
        line +="Прочность: "+str(self.strength)+'\n'
        line +="Физический урон: "+str(self.physical_damage)+'\n'
        line +="Критический урон: "+str(self.critical_damage)+'\n'
        line +="Влияние силы: "+str(self.power)+'\n'
        line +="Влияние ловкости: "+str(self.agility)+'\n'
        line +="Влияние интеллекта: "+str(self.intellect)+'\n'
        line +="Влияние веры: "+str(self.belief)+'\n'
        return line

def init_tree(self):
    #корень(1уровень)
    root = Node('Оружие')
    #2 уровень
    Melee = Node('Ближний Бой', parent = root, fil = 0)
    Ranged = Node('Дальний бой', parent = root, fil = 0)
    #3уровень
    One_handed = Node('Одноручное оружие', parent= Melee)
    Two_handed  = Node('Двуручное оружие', parent= Melee)
    Spears_Halberds = Node('Копья и Алебарды', parent= Melee)
    Heavy = Node('Тяжелое', parent= Ranged)
    Light = Node('Легкое', parent= Ranged)
    #4 уровень
    Dagger = Node('Кинжалы', parent=One_handed)
    Straight_Swords = Node('Прямые мечи', parent=One_handed)
    Crooked_Swords = Node('Кривые мечи', parent=One_handed)
    Katanas = Node('Катаны', parent=One_handed)
    Swords_for_thrusts = Node('Мечи для выпадов', parent=One_handed)
    Axes = Node('Топоры', parent=One_handed)
    Whips = Node('Кнуты', parent=One_handed)
    Fists = Node('Кулаки', parent=One_handed)
    Big_Swords = Node('Большие мечи', parent=Two_handed)
    Huge_swords = Node('Огромные мечи', parent=Two_handed)
    Big_curved_swords = Node('Большие кривые мечи', parent=Two_handed)
    Big_axes = Node('Большие секиры', parent=Two_handed)
    Hammers = Node('Молоты', parent=Two_handed)
    Big_Hammers = Node('Большие молоты', parent=Two_handed)
    Spears = Node('Копья', parent=Spears_Halberds)
    Halberds = Node('Алебарды', parent=Spears_Halberds)
    Crossbows = Node('Арбалеты', parent=Heavy)
    Large_bows = Node('Большие луки', parent=Heavy)
    Bows = Node('Луки', parent=Light)
    #листья(5 уровень)
    tmp = Node('Большой лук драконоборца', parent = Large_bows, fil = 0,
                inf = weapon('Большой лук драконоборца', False, 10.0, 100, 90, 100, 'C', 'C', '-','-'))
    self.append(tmp)
    tmp = Node('Большой лук Гоха', parent=Large_bows, fil = 0,
                inf=weapon('Большой лук Гоха', False, 13.0, 100, 85, 100, 'B', 'C', '-', '-'))
    self.append(tmp)
    tmp = Node('Утигатана', parent=Katanas,fil = 0,
                inf=weapon('Утигатана', False, 5.0, 80, 90, 100, '-', 'B', '-', '-'))
    self.append(tmp)
    tmp = Node('Иайто', parent=Katanas,fil = 0,
                inf=weapon('Иайто', False, 5.0, 80, 88, 100, '-', 'B', '-', '-'))
    self.append(tmp)
    tmp = Node('Катана', parent=Katanas,fil = 0,
                inf=weapon('Катана', False, 8.0, 60, 90, 100, 'D', 'C', '-', '-'))
    self.append(tmp)
    tmp = Node('Клинок Хаоса', parent=Katanas,fil = 0,
                inf=weapon('Клинок Хаоса', False, 6.0, 120, 144, 100, '-', 'C', '-', '-'))
    self.append(tmp)
    tmp = Node('Нож бандита', parent=Dagger,fil = 0,
                inf=weapon('Нож бандита', False, 1.0, 200, 56, 147, 'E', 'B', '-', '-'))
    self.append(tmp)
    tmp = Node('Кинжал', parent=Dagger,fil = 0,
                inf=weapon('Кинжал', True, 0.5, 200, 56, 131, 'E', 'B', '-', '-'))
    self.append(tmp)
    tmp = Node('Парирующий кинжал', parent=Dagger,fil = 0,
                inf=weapon('Парирующий кинжал', True, 0.5, 200, 54, 131, 'E', 'B', '-', '-'))
    self.append(tmp)
    tmp = Node('Призрачный клинок', parent=Dagger,fil = 0,
                inf=weapon('Призрачный клинок', False, 0.5, 100, 110, 127, 'E', '-', '-', '-'))
    self.append(tmp)
    tmp = Node('Кинжал Присциллы', parent=Dagger,fil = 0,
                inf=weapon('Кинжал Присциллы', False, 1.0, 100, 80, 100, '-', 'A', '-', '-'))
    self.append(tmp)
    tmp = Node('Тёмный Серебряный След', parent=Dagger,fil = 0,
                inf=weapon('Тёмный Серебряный След', False, 1.0, 120, 75, 160, 'E', 'S', '-', '-'))
    self.append(tmp)
    tmp = Node('Большой меч', parent=Huge_swords,fil = 0,
                inf=weapon('Большой меч', True, 12.0, 200, 130, 100, 'C', 'D', '-', '-'))
    self.append(tmp)
    tmp = Node('Двуручный меч', parent=Huge_swords,fil = 0,
                inf=weapon('Двуручный меч', True, 10.0, 200, 130, 100, 'C', 'D', '-', '-'))
    self.append(tmp)
    tmp = Node('Демоническое мачете', parent=Huge_swords,fil = 0,
                inf=weapon('Демоническое мачете', True, 18.0, 600, 133, 100, 'B', '-', '-', '-'))
    self.append(tmp)
    tmp = Node('Большой меч Черного Рыцаря', parent=Huge_swords,fil = 0,
                inf=weapon('Большой меч Черного Рыцаря', False, 14.0, 300, 220, 100, 'B', 'E', '-', '-'))
    self.append(tmp)
    tmp = Node('Большой меч дракона', parent=Huge_swords,fil = 0,
                inf=weapon('Большой меч дракона', False, 24.0, 400, 390, 100, '-', '-', '-', '-'))
    self.append(tmp)
    tmp = Node('Легкий арбалет', parent=Crossbows,fil = 0,
                inf=weapon('Легкий арбалет', False, 3.0, 150, 50, 100, '-', '-', '-', '-'))
    self.append(tmp)
    tmp = Node('Тяжелый арбалет', parent=Crossbows,fil = 0,
                inf=weapon('Тяжелый арбалет', False, 5.0, 150, 55, 100, '-', '-', '-', '-'))
    self.append(tmp)
    tmp = Node('Меткий арбалет', parent=Crossbows,fil = 0,
                inf=weapon('Меткий арбалет', False, 8.0, 150, 52, 100, '-', '-', '-', '-'))
    self.append(tmp)
    tmp = Node('Авелин', parent=Crossbows,fil = 0,
                inf=weapon('Авелин', False, 6.0, 150, 37, 100, '-', '-', '-', '-'))
    self.append(tmp)
    return (root)

def find_Weapon(self, name):
    for item in self:
        if item.name == name:
            return item
    return None
#перед исчисляемого строкового параметка в число
def str_to_number(self):
    if self == 'E':
        return 1
    elif self == 'D':
        return 2
    elif self == 'C':
        return 3
    elif self == 'B':
        return 4
    elif self == 'A':
        return 5
    elif self == 'S':
        return 6
    else:
        return 0
#приведение информации по оружию в удобный для обработки вид
def preparation_data(self):
    if self.coating == False:
        self.coating = 0
    else:
        self.coating = 1
    self.power = str_to_number(self.power)
    self.agility = str_to_number(self.agility)
    self.intellect = str_to_number(self.intellect)
    self.belief = str_to_number(self.belief)
#обнуление
def zero_fil(List):
    for item in List:
        item.fil = 0
#для сортировки по фильтру
def key_func(item):
    return item.fil
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Лабораторная работа 2
#манхэттенское расстояние
def manhetten(weapon1, weapon2):
    tmp1 = weapon1.coating + weapon1.strength + weapon1.physical_damage + weapon1.critical_damage + weapon1.power + weapon1.agility + weapon1.intellect + weapon1.belief
    tmp2 = weapon2.coating + weapon2.strength + weapon2.physical_damage + weapon2.critical_damage + weapon2.power + weapon2.agility + weapon2.intellect + weapon2.belief
    return abs(tmp1 - tmp2)
#евклидово расстояние
def euclidian(weapon1, weapon2):
    tmp = [pow(weapon1.coating-weapon2.coating,2),pow(weapon1.physical_damage-weapon2.physical_damage,2),pow(weapon1.critical_damage-weapon2.critical_damage,2),
    pow(weapon1.power-weapon2.power,2),pow(weapon1.agility-weapon2.agility,2),pow(weapon1.intellect-weapon2.intellect,2),pow(weapon1.belief-weapon2.belief,2)]
    return math.sqrt(sum(tmp))
#близость по дереву
def tree_vicinity(weapon1, weapon2):
    way1 = []
    way2 = []
    item1 = weapon1
    item2 = weapon2
    while not(item1 == None):
        way1.append(item1)
        item1 = item1.parent
    while not(item2 == None):
        way2.append(item2)
        item2 = item2.parent
    for i in range(1, len(way1)):
        if way1[i] == way2[i]:
            return (i*2)
#коффициент корреляции
def corelation(weapon1, weapon2):
    tmp1 = [weapon1.coating, weapon1.physical_damage, weapon1.critical_damage, weapon1.power, weapon1.agility, weapon1.intellect, weapon1.belief]
    tmp2 = [weapon2.coating, weapon2.physical_damage, weapon2.critical_damage, weapon2.power, weapon2.agility, weapon2.intellect, weapon2.belief]
    tmp1_sr = sum(tmp1)/7
    tmp2_sr = sum(tmp2)/7
    for i in range(7):
         tmp1[i] = tmp1[i] - tmp1_sr
         tmp2[i] = tmp2[i] - tmp2_sr
    ch = 0
    for i in range(7):
        ch+= tmp1[i] * tmp2[i]
    sig_x = 0
    sig_y = 0
    for i in range(7):
        sig_x += pow(tmp1[i], 2)
        sig_y += pow(tmp2[i], 2)
    return(ch/(math.sqrt(sig_x*sig_y)))
#основная функция
def lab2(root, leaves):
    print("какие оружия ты бы хотел сравнить?")
    weapon1 = input()
    weapon1 = find_Weapon(leaves, weapon1)
    if weapon1 == None:
        er = dictionary.error_find[random.choice(range(3))]
        print(er)
        return
    weapon2 = input()
    weapon2 = find_Weapon(leaves,weapon2)
    if weapon2 == None:
        er = dictionary.error_find[random.choice(range(3))]
        print(er)
        return
    preparation_data(weapon1.inf)
    preparation_data(weapon2.inf)
    print('Манхетенское расстояние: {}'.format(manhetten(weapon1.inf, weapon2.inf)))
    print('Евклидово расстояние: {}'.format(euclidian(weapon1.inf, weapon2.inf)) )
    print('Близость по дереву:{}'.format(tree_vicinity(weapon1, weapon2)))
    print('Корреляция: {}'.format(corelation(weapon1.inf, weapon2.inf)))
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#лабораторная работа 3
#коллаборативная фильтрация на основе опыта других игроков(таблица)
def lab3(root, leaves):
    df = pd.read_excel('Book1.xlsx', engine= 'openpyxl')
    df = df.astype(str)
    df = df.set_index('Оружие').T
    df.to_excel('DataSet.xlsx', engine='openpyxl')
    df = pd.read_excel('DataSet.xlsx', index_col=0, engine='openpyxl')
    print("Скажи же, какое оружие ты используешь")
    name_weap = input()
    find = ''
    for row in df:
        if row == name_weap:
            find = row
    if find == '':
        er = dictionary.error_find[random.choice(range(3))]
        print(er)
        return
    zero_fil(leaves)
    for item in df:
        if not(item == find):
            i = 0
            weapon1 = find_Weapon(leaves, item)
            for item1 in df[item]:
                if (item1 == 1) and (df[find][i] == 1):
                    weapon1.fil +=1
                i+=1
    remove('DataSet.xlsx')
    weapon1 = find_Weapon(leaves, find)
    weapon.fil = -1
    leaves.sort(reverse = True, key = key_func)
    print("Я думаю, что тебе подойдет это оружие, взгляни:")
    i = 0
    while i < 5:
        print(leaves[i].name)
        i+=1
    zero_fil(leaves)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#лабораторная работа 4
#Контентно-ориентированная фильтрация на основе разделения объектов по группам
def lab4(root, leaves):
    df = pd.read_excel('Book2.xlsx', engine= 'openpyxl')
    df = df.astype(str)
    df = df.set_index('Оружие').T
    df.to_excel('DataSet.xlsx', engine='openpyxl')
    df = pd.read_excel('DataSet.xlsx', index_col=0, engine='openpyxl')
    print("Скажи же, какое оружие ты используешь")
    name_weap = input()
    find = ''
    for row in df:
        if row == name_weap:
            find = row
    if find == '':
        er = dictionary.error_find[random.choice(range(3))]
        print(er)
        return
    zero_fil(leaves)
    weapon2 = find_Weapon(leaves, find)
    for item in df:
        if not(item == find):
            i = 0
            weapon1 = find_Weapon(leaves, item)
            for item1 in df[item]:
                if (item1 == 1) and (df[find][i] == 1):
                    weapon1.fil +=1
                i+=1
            if weapon1.parent == weapon2.parent:
                weapon1.fil +=1
    remove('DataSet.xlsx')
    weapon2.fil = -1
    leaves.sort(reverse = True, key = key_func)
    print("Я думаю, что тебе подойдет это оружие, взгляни:")
    i = 0
    while i < 5:
        print(leaves[i].name)
        i+=1
    zero_fil(leaves)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#лабораторная работа 5
#тестирование оружий на соответствие параметрам
def par_filtr(List, coating, min_we, max_we, min_stre, max_stre, min_pd, max_pd, min_cd, max_cd, min_power, max_power, min_ag, max_ag, min_in, max_in, min_bel, max_bel):
    for item in List:
        if item.inf.coating == coating:
            item.fil += 1
        if item.inf.weight >= min_we and item.inf.weight <= max_we:
            item.fil += 1
        if item.inf.strength >= min_stre and item.inf.strength <= max_stre:
            item.fil += 1
        if item.inf.physical_damage >= min_pd and item.inf.physical_damage <= max_pd:
            item.fil += 1
        if item.inf.critical_damage >= min_cd and item.inf.critical_damage <= max_cd:
            item.fil += 1
        pw = str_to_number(item.inf.power)
        ag = str_to_number(item.inf.agility)
        inte = str_to_number(item.inf.intellect)
        bel = str_to_number(item.inf.belief)
        if pw >= min_power and pw <= max_power:
            item.fil += 1
        if ag >= min_ag and ag <= max_ag:
            item.fil += 1
        if inte >= min_in and inte <= max_in:
            item.fil +=1
        if bel >= min_bel and bel <= max_bel:
            item.fil +=1
#отсечение оружий невыбраных типов
def unsearch(List):
    for item in List:
        if item.parent.parent.parent.fil == 0:
            item.fil = -1
#главная функция
def lab5(root, leaves):
    print("Ты хочешь оружие ближнего или дальнего боя(0 или 1)?")
    sloy2 = input()
    if sloy2 == 'ближнего' or sloy2 == 'ближнего боя':
        sloy2 = 0
    elif sloy2 == 'дальнего' or sloy2 == 'дальнего боя':
        sloy2 = 1
    else:
        pr =dictionary.error_in[random.choice(range(3))]
        print(pr)
        return
    root.children[sloy2].fil = 1
    print("Нужна ли возможность усиления? ")
    coating =input()
    if coating == 'да':
        coating = True
    elif coating == 'нет':
        coating = False
    else:
        pr =dictionary.error_in[random.choice(range(3))]
        print(pr)
        return
    print("Какой диапазон веса оружия? ")
    min_we = float(input())
    max_we = float(input())
    print("Какой диапазон прочности оружия? ")
    min_stre = int(input())
    max_stre = int(input())
    print("Какой диапазон физ. урона оружия? ")
    min_pd = int(input())
    max_pd = int(input())
    print("Какой диапазон крит. урона оружия? ")
    min_cd = int(input())
    max_cd = int(input())
    print("Какой диапазон усиления от параметра силы? ")
    min_power = input()
    min_power = str_to_number(min_power)
    max_power = input()
    max_power = str_to_number(max_power)
    print("Какой диапазон усиления от параметра ловкости? ")
    min_ag = input()
    min_ag = str_to_number(min_ag)
    max_ag = input()
    max_ag = str_to_number(max_ag)
    print("Какой диапазон усиления от параметра интеллекта? ")
    min_in = input()
    min_in = str_to_number(min_in)
    max_in = input()
    max_in = str_to_number(max_in)
    print("Какой диапазон усиления от параметра веры? ")
    min_bel = input()
    min_bel = str_to_number(min_bel)
    max_bel = input()
    max_bel = str_to_number(max_bel)
    zero_fil(leaves)
    par_filtr(leaves, coating,min_we, max_we, min_stre, max_stre, min_pd, max_pd, min_cd, max_cd, min_power, max_power, min_ag, max_ag, min_in, max_in, min_bel, max_bel)
    unsearch(leaves)
    leaves.sort(reverse = True, key = key_func)
    if not(leaves[0].fil == 9):
        print("К сожалению я не нашла оружия, которое бы удовлетворило твои желания, но возможно тебе понравится это:")
        j = 0
        while leaves[j].fil >-1 and j < 5:
            print(leaves[j].name)
            j+=1
    else:
        print("Я думаю, что тебе подойдет это оружие, взгляни:")
        i = 0
        while leaves[i].fil == 9:
            print(leaves[i].name)
            i+=1
    zero_fil(leaves)
    root.children[sloy2].fil = 0
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#компиляция лабораторных работ в виде диалога с игроком
def start():
    leaves = []
    tree = init_tree(leaves)
    print("Приветствую тебя, Избранная Нежить! Я Хранительница Костра. Я могу помочь тебе в твох нелегких странствиях, обращайся, если понадобится помощь.")
    while 1:
        pr = dictionary.menu[random.choice(range(3))]
        print(pr,"\n1.Рассказать тебе об оружии\n2.Сравнить 2 любых оружия\n3.Обратиться к мультивселенскому разуму и предложить тебе оружие на основе опыта других воинов\n4.Предложить тебе оружие похожее на твоё\n5.Подобрать оружие по твоим предпочтениям\n(6.уйти)")
        com = input()
        if com in dictionary.chek2:
            print ("Давай взглянем на них")
            lab2(tree, leaves)
        elif com in dictionary.chek3:
            lab3(tree, leaves)
        elif com in dictionary.chek4:
            lab4(tree, leaves)
        elif com in dictionary.chek5:
            print("Расскажи, чего ты желаешь")
            lab5(tree, leaves)
        elif com in dictionary.chek6:
            pr =dictionary.parting[random.choice(range(3))]
            print(pr)
            break
        else:
            pr =dictionary.error_in[random.choice(range(3))]
            print(pr)

def test():
    leaves = []
    tree = init_tree(leaves)
    lab3(tree, leaves)

if __name__ == '__main__':
    start()