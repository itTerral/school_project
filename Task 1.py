import csv

# с помощью open считываем файл
with open('books.csv', encoding='utf-8', newline='') as file, open('books_rowling1.csv', 'w', encoding='utf-8', newline='') as newfile:
    data = list(csv.reader(file, delimiter=';'))
    res = csv.writer(newfile, delimiter=';')
    res.writerow([data[0][0], data[0][2], data[0][4], data[0][-1]])
    #проходимся по данным и добавляем в новый файл книжки нужного автора
    for stroke in data[1:]:
        if 'Роулинг' in stroke[2]:
            res.writerow([stroke[0], stroke[2], stroke[4], stroke[-1]])
    # выводим произведения по аявленным критериям
    for book in data[1:]:
        if 'Роулинг' in book[2]:
            book[-1] = book[-1].replace(',', '.')
            if float(book[-1]) > 8:
                print(f'{book[1]} - {book[2]}\t {book[-1]}')


