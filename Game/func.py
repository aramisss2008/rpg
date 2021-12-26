from Game.hero import hero

def load(path):
    f = open(path, 'r')
    txt = f.read()
    words = txt.split(".")
    return hero(words[0], words[1], int(words[2]), words[3], int(words[4]))