import csv


with open('books.csv', encoding='utf-8', newline='') as file, open('books_rowling1.csv', 'w', encoding='utf-8', newline='') as newfile:
    data = list(csv.reader(file, delimiter=';'))
    res = csv.writer(newfile, delimiter=';')
    res.writerow([data[0][0], data[0][2], data[0][4], data[0][-1]])

    for stroke in data[1:]:
        if 'Роулинг' in stroke[2]:
            res.writerow([stroke[0], stroke[2], stroke[4], stroke[-1]])

    for book in data[1:]:
        if 'Роулинг' in stroke[2]:
            if int(stroke[4]) > 8:
                print(f'{book[1]} - {book[2]}\t {book[-1]}')


