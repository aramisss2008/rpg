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
            self.strong = 0.5
            self.hp = 30
        if class_h == "archer":
            self.strong = 0.4
            self.hp = 15
            self.agility = 3
        if class_h == "summoner":
            self.strong = 0.3
            self.agility = 2.3
        if class_h =="wizard":
            self.strong = 0.4
            self.hp = 17
            self.mana = 150
        if racem == "orc":
            self.hp += 100 #TODO:
            self.strong += 0.2
            self.agility -= 1
        if racem == "gnome":
            self.strong -= 1.5
            self.hp -= 5
            self.agility += 2

    def specialattack(self):
        if self.racem or self.class_h == "lancer""gnome":
            return
        
    def specialattack(self):
        if self.racem or self.class_h == "lancer":
            return

    def specialattack(self):
        if self.racem or self.class_h == "lancer":
            return

    def specialattack(self):
        if self.racem or self.class_h == "lancer":
            return

    def specialattack(self):
        if self.racem or self.class_h == "lancer":
            return

    def specialattack(self):
        if self.racem or self.class_h == "lancer":
            return

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


