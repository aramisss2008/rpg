class pupil():
    a = 5

    def getA(self):
        print(self.a)

    def smth(self):
        self.getA()
        self.a -= 5
        self.getA()

Nikita = pupil()
Nikita.smth()

