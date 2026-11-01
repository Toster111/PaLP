#Вариант 24. Вариант Д

from operator import itemgetter

class Chapter:
    def __init__(self, id, title, number_pages, id_book):
        self.id = id
        self.title = title
        self.number_pages = number_pages
        self.id_book = id_book

class Book:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class ChapterBook:
    def __init__(self, chap_id, book_id):
        self.chap_id = chap_id
        self.book_id = book_id

books = [
    Book(1, "Бандитский Петербург"),
    Book(2, "Улитка на склоне"),
    Book(3, "Норма")
]

chapter = [
    Chapter(1, "Государство в государстве", 50, 1),
    Chapter(2, "Время великой легализации", 50, 1),
    Chapter(3, "Перец", 20, 2),
    Chapter(4, "Перец", 20, 2),
    Chapter(5, "Кандид", 20, 2),
    Chapter(6, "Нормальная жизнь", 15, 3),
    Chapter(7, "Летучка", 15, 3)
]

chapt_book = [
    ChapterBook(1, 1),
    ChapterBook(2, 1),
    ChapterBook(3, 2),
    ChapterBook(4, 2),
    ChapterBook(5, 3),
    ChapterBook(6, 3),

    ChapterBook(3, 1),
    ChapterBook(5, 2),
    ChapterBook(1, 3)
]

def main():

    one_to_many = [(c.title, c.number_pages, b.name)
                   for c in chapter
                   for b in books
                   if c.id_book == b.id
                   ]

    print("Задание Д1")
    # Вывeсти название глав, в которых есть буква 'е' и книги, в которых они находятся

    spisok_1 = [n[::2] for n in list(filter(lambda i: 'е' in itemgetter(0)(i), one_to_many))]
    print(spisok_1)

    print("Задание Д2")
    # Ввести список книг, отсортированные по среднему кол-ву страниц всех глав и среднее кол-во страниц

    spisok_2 = list()

    for n in set(i[2] for i in one_to_many):
        pages = [k[1] for k in list(filter(lambda x: x[2] == n, one_to_many))]
        pages = round(sum(pages) / len(pages), 2)
        spisok_2.append([n, pages])

    spisok_2 = sorted(spisok_2, key= lambda x: x[1])

    print(spisok_2)

    print("Задание Д3")
    # Вывести список всех книг, у которых название начинается с буквы "Б", и список глав в них (связь многие-ко-многим)

    # Соединение данных многие-ко-многим (книга - глава)
    many_to_many_temp = [(b.name, cb.book_id, cb.chap_id)
                         for b in books
                         for cb in chapt_book
                         if b.id == cb.book_id]

    many_to_many = [(c.title, c.number_pages, book_name)
                    for book_name, book_id, chap_id in many_to_many_temp
                    for c in chapter if c.id == chap_id]

    res_3 = {}
    # Перебираем все книги
    for b in books:
        if b.name.startswith('Б'):
            # Список глав этой книги
            b_chaps = list(filter(lambda i: i[2] == b.name, many_to_many))
            # Только названия глав
            b_chaps_names = [x for x, _, _ in b_chaps]
            res_3[b.name] = b_chaps_names

    print(res_3)

if __name__ == '__main__':
    main()
