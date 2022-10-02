from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг

    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    def test_add_new_book_same_books_added_only_one_book(self):
        collector = BooksCollector()

        collector.add_new_book('Преступление')
        collector.add_new_book('Преступление')

        assert len(collector.get_books_rating()) == 1

    def test_set_book_rating_change_rating_must_be_change(self):
        collector = BooksCollector()

        collector.add_new_book('Преступление')
        collector.set_book_rating('Преступление', 5)

        dict_value = collector.get_books_rating()

        assert dict_value.get('Преступление') == 5

    def test_get_book_rating_getting_dict_with_book(self):
        collector = BooksCollector()

        collector.add_new_book('Преступление')

        assert collector.get_book_rating('Преступление') == 1

    def test_get_books_with_specific_rating_output_books_with_specific_rating(self):
        collector = BooksCollector()

        collector.add_new_book('Преступление')
        collector.add_new_book('Наказание')
        collector.add_new_book('Мир')
        collector.set_book_rating('Наказание', 5)

        result = collector.get_books_with_specific_rating(1)

        assert all([book in ('Преступление', 'Мир') for book in result])

    def test_get_books_rating_getting_book_rating(self):
        collector = BooksCollector()

        collector.add_new_book('Преступление')

        assert collector.get_books_rating() == {'Преступление': 1}


    def test_add_book_in_favorites_book_added_in_favourite_list(self):
        collector = BooksCollector()

        collector.add_new_book('Преступление')
        collector.add_book_in_favorites('Преступление')

        assert collector.favorites == ['Преступление']

    def test_delete_book_from_favorites_book_deleted_from_favourites(self):
        collector = BooksCollector()

        collector.add_new_book('Преступление')
        collector.add_book_in_favorites('Преступление')

        collector.delete_book_from_favorites('Преступление')

        assert collector.favorites == []

    def test_get_list_of_favorites_books_names_in_favourite_list(self):
        collector = BooksCollector()

        collector.add_new_book('Преступление')
        collector.add_new_book('Наказание')
        collector.add_book_in_favorites('Преступление')
        collector.add_book_in_favorites('Наказание')

        assert all([book in ('Преступление', 'Наказание') for book in collector.get_list_of_favorites_books()])
