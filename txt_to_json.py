import json

ar = [] # Создаём список

with open('cenz.txt', encoding='utf-8') as r:
    for i in r:
        n = i.lower().split('\n')[0] #Считываем слова по разделителю и - [0] символу переноса
        if n != '': #Проверяем чтобы была не пустая строка
            ar.append(n) #Добаляем в наш список 

with open('cenz.json', 'w', encoding='utf-8') as e: #Создаем файл json для чтения, 
    json.dump(ar, e)   #записываем наш список как аргумент и сам обьект чтения
