class enemy():
    strength = 1
    hp = 1
    name = ""

    def attack(self):
        return 0

    def dodge(self):
        return 0

class shadow1(enemy):

    def __init__(self):
        self.strength = 2
        print("krik")

    def attack(self, power):
        return 100+power