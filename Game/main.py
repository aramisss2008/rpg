from Game.func import load
from hero import hero

print("hello friend")
print("choose hero-1")
print("create hero-2")
code = int(input())
if code ==1:
    print("write name")
    chooseName = input()
    load(chooseName + ".txt")
if code ==2:
    name = "hero"
    class_h = "lancer"
    goldm = 0
    racem = "human"
    lvl = 1
    myHero = hero(name,class_h,goldm,racem,lvl)
    myHero.save()