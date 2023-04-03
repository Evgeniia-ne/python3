rating = [7, 5, 3, 3, 2]
print('Текущий рейтинг:',  rating)
new_score = int(input("Введите новый элемент рейтинга: "))
rating.append(new_score)
rating.sort(reverse = True)
print('Новый рейтинг:', rating)