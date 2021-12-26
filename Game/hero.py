class hero():
    name = "hero"
    class_h = "lancer"
    goldm = 0
    racem = "human"
    lvl = 1
    def __init__(self, name, class_h, goldm, racem, lvl):
        """Constructor"""
        self.name = name
        self.class_h = class_h
        self.goldm = goldm
        self.racem = racem
        self.lvl = lvl
    def printFeature(self):
        print(self.name)
        print(self.lvl)
        print(self.goldm)
    def save(self):
        f = open(self.name+".txt", 'w')
        f.write(self.name+".")
        f.write(self.class_h+".")
        f.write(str(self.goldm)+".")
        f.write(self.racem+".")
        f.write(str(self.lvl))


