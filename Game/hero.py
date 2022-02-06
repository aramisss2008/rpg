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
            self.mana = 150
        if racem == "orc":
            self.hp += 100 #TODO:

    def specialattack(self):
        if self.racem == "orc":
            return 100

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


