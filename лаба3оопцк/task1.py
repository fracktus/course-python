class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"

class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages
@property
def pages(self):
    return self._pages

@pages.setter
def pages(self, value):
    if isinstance(value, int) and value > 0:
        self._pages = value
    else:
        raise ValueError("Pages must be a positive integer")

def __str__(self):
    return f"Книга {self._name}. Автор {self._author}. Страницы {self._pages}"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = duration
@property
def duration(self):
    return self._duration

@duration.setter
def duration(self, value):
    if isinstance(value, float) and value >= 0:
        self._duration = value
    else:
        raise ValueError("Duration must be a non-negative float")

def __str__(self):
    return f"Книга {self._name}. Автор {self._author}. Продолжительность {self._duration}"





