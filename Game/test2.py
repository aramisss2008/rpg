#Запись двух массивов в файл
a1 = [51, 42, 33]
a2 = [23,11,1223,5,54] #TODO
f = open("ttt" + ".txt", 'w')

for i in range(len(a1)):
    f.write(str(a1[i])+"\n")

#Чтение двух массивов из файла
f = open("ttt" + ".txt", 'r')
b1 = []
b2 = []
stroka = f.readline()
while stroka:
    b1.append(int(stroka))
    stroka = f.readline()




