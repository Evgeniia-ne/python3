n = int(input('Введите номер месяца от 1 до 12: '))
seasons = ['зима', 'весна', 'лето', 'осень']
if 1 <= n <= 2 or n == 12:
    p = seasons[0]
elif 3 <= n <= 5:
    p = seasons[1]
elif 6 <= n <= 8:
    p = seasons[2]
else:
    p = seasons[3]
print('Результат через список:', p)


seasons2 = {'зима': [1, 2, 12], 'весна': [3, 4, 5], 'лето': [6, 7, 8], 'осень': [9, 10, 11],}
for i in seasons2:
    for j in seasons2[i]:
        if n == j:
            print('Результат через словарь:', i)