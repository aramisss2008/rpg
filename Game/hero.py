from random import randint


class hero():

    name = "hero"
    class_h = "lancer"
    goldm = 0
    racem = "human"
    lvl = 1
    strong = 1
    agility = 1
    hp = 100
    mana = 100
    mapForest = [1]
    mapRuins = [1]
    mapKingdom = [1]

    def __init__(self, name, class_h, racem, goldm = 100, lvl = 1):
        """Constructor"""
        self.name = name
        self.class_h = class_h
        self.goldm = goldm
        self.racem = racem
        self.lvl = lvl

        if class_h == "lancer":
            self.strong = 5
            self.hp = 300
        if class_h=="archer":
            self.strong = 4
            self.hp = 150
            self.agility = 3
        if class_h == "summoner":
            self.strong = 3
        if class_h =="wizard":
            self.strong = 4
            self.hp = 170
            #self.mana = 150
        if racem == "orc":
            self.hp += 100 #TODO:

    def specialattack(self):
        if self.racem == "orc":
            return 100

    def attack1(self):
        return 2

    def attack2(self):
        return 1

    def printFeature(self):
        print(self.name)
        print(self.lvl)
        print(self.goldm)

    def save(self):
        f = open(self.name+".txt", 'w')
        f.write(self.name+".")
        f.write(self.class_h+".")
        f.write(self.racem + ".")
        f.write(str(self.goldm)+".")
        f.write(str(self.lvl))
#todo: добавить сохранение карт


    def fight(self, enemy):
        fightPointHero = 0
        fightPointEnemy = 0
        while enemy.hp > 0 and self.hp > 0:

            print("hp hero:" + str(self.hp))
            print("hp enemy:" + str(enemy.hp))

            fightPointHero += randint(1,12)
            fightPointEnemy += randint(1,12)
            print("Point: " + str(fightPointHero))
            print("1 - special attack cost: 12")
            print("2 - attack 1 cost: 1")
            print("3 - attack 2 cost: 2")
            num = int(input())
            while 1:
                if num >= 1 and num <=3:
                    if num ==1 and fightPointHero <12:
                        print("you can't use it!")
                        num = int(input())
                    elif num == 3 and fightPointHero <2:
                        print("you can't use it!")
                        num = int(input())
                    else:
                        break
                else:
                    print("write correct option")
                    num = int(input())
            if num == 2:
                enemy.hp -= self.attack1()
                fightPointHero -= 1
            elif num == 1:
                enemy.hp -= self.specialattack()
                fightPointHero -= 12
            else:
                enemy.hp -= self.attack2()
                fightPointHero -= 2

            if fightPointEnemy >= 12:
                self.hp -= enemy.attack2()
                fightPointEnemy -= 12
            elif fightPointEnemy >= 8:
                self.hp -= enemy.attack1()
                fightPointEnemy -= 8
            else:
                self.hp -= enemy.attack()
                fightPointEnemy -= 1

        if self.hp <= 0:
            print("you died")
        else:
            print("you win")




