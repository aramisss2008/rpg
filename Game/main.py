from Game.func import load
from hero import hero

def createHero():
    print(" enter name")
    name = input()

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
    dict1 = {"1": "orc", "2": "human", "3": "dwarf"}
    num1 = input()
    while 1:
        if dict1.get(num1) == None:
            print("chose rigth number!")
            num1 = input()
        else:
            break
    racem = dict1.get(num1)

    myHero = hero(name, class_h, racem)
    myHero.save()
    return myHero

print("hello friend")
print("choose hero-1")
print("create hero-2")

code = int(input())
#toDo proverka
if code ==1:
    print("write name")
    chooseName = input() #TODO: предлогать персонажей
    player = load(chooseName + ".txt")
if code ==2:
    player = createHero()

print("chose map")
print("choose forest-1")
print("create ruins-2")
print("create kingdom-3")
code = int(input())

#todo: на какой уровень зайти




