from Game.func import load
from hero import hero
import os.path

print("hello friend")
print("choose hero-1")
print("create hero-2")
code = int(input())

if code ==1:
    print("write name")
    chooseName = input() #TODO: предлогать персонажей
    myHero = load(chooseName + ".txt")

if code ==2:
    print(" enter name")
    name = input()

    while 1:
        if os.path.exists(name + '.txt '):
            print("Такое имя уже существует введите другое имя")
            name = input()
        else:
            break

    print("chose class: 1. lancer 2. wizard 3. archer, 4. summoner")
    dict = {"1": "lancer", "2": "wizard", "3": "archer", "4": "summoner"}
    num = input()
    while 1:
        if dict.get(num) == None:
            print("chose rigth number!")
            num = input()
        else:
            break
    class_h = dict.get(num)

    print("chose race: 1.orc , 2.human, 3.dwarf")
    dict1 = {"1" : "orc", "2" : "human", "3" : "dwarf"}
    num1 = input()
    while 1:
        if dict1.get(num1) == None:
            print("chose rigth number!")
            num1 = input()
        else:
            break
    racem = dict1.get(num1)

    goldm = 0
    lvl = 1
    myHero = hero(name,class_h,goldm,racem,lvl)
    myHero.save()

myHero