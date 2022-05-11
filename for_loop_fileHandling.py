f1 = open("myData.txt", 'r')

f2 = open("personalData.txt", 'w')
for data in f1:
    f2.write(data)