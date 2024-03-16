import csv

# с помощью open считываем файл
with open('books.csv', encoding='utf-8', newline='') as file, open('books_grade1.csv', 'w', encoding='utf-8', newline='') as newfile:
    data = list(csv.reader(file, delimiter=';'))
    res = csv.writer(newfile, delimiter=';')
    # проходимся по строчкам в полученном списке и присваиваем ярлыки
    # в зависимости от рейтинга
    # после записываем результат в новый файл
    for stroke in data[1:]:
        stroke[-1] = stroke[-1].replace(',', '.')
        if float(stroke[-1]) < 5:
            res.writerow(stroke + ['не рекомендовать'])
        if 5 <= float(stroke[-1]) < 8:
            res.writerow(stroke + ['рекомендовать после'])
        if float(stroke[-1]) >= 8:
            res.writerow(stroke + ['рекомендовать в первую очередь'])
