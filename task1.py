vowel = ['а', 'о', 'э', 'у', 'ы' ,'ё' ,'е' ,'ю' ,'и', 'я']
poem = str(input('enter Winnie the Pooh poem: ').split())
#пара-ра-рам рам-пам-папам па-ра-па-да
res = list()
for i in range(len(poem)):
    for j in range(len(vowel)):
        list1 = list(filter(lambda x: x == vowel[j] or x == ' ', poem[i]))
        if list1 != []:
            res.append(*list1)
res2 = list()
count = 0
for i in range(len(res)):
    if res[i] == ' ' and count != 0:
        res2.append(count)
        count = 0
    elif res[i] != ' ':
        count += 1
res2.append(count)
index = 0
for i in range(len(res2)):
    temp = res2[0]
    if res2[i] == temp:
        index += 1
if index == len(res2):
    print('Парам пам-пам')
else: print('Пам парам') 