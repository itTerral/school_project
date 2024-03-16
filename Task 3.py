import csv

def search(book, data):
    ''' Функция search организует поиск по полученным данным из файла books.csv
    если в строке есть название нужной книги, функция возвращает строчку с необходимыми данными,
    если книги не найдено, функция возвращает строчку 'Данной книги в этой библиотеке нет'
    Описание аргументов:
    book - строка с названием книги
    data - список проверяемых данных
    '''
    for stroke in data[1:]:
        if book in stroke[4]:
            return (f'{stroke[-2]} - {stroke[1]} - {stroke[0]} - {stroke[-1]}')
    return 'Данной книги в этой библиотеке нет'

# с помощью open считываем файл
with open('books.csv', encoding='utf-8', newline='') as file:
    data = list(csv.reader(file, delimiter=';'))
    # получаем  из консоли от пользователя название книги в переменную book
    book = input('ВВедите название книги: ')
    while book != 'хватит':
        ans = search(book, data[1:])
        print(ans)
        book = input('ВВедите название книги: ')