
class Calculator:
    """
    Класс, представляющий калькулятор.

    Attributes:
        num1 (int): Первое число.
        num2 (int): Второе число.

    Examples:
        >>> calc = Calculator(5, 3)
        >>> calc.add()
        8
        >>> calc.subtract()
        2
        >>> calc.multiply()
        15
    """

    def __init__(self, num1: int, num2: int):
        self.num1 = num1
        self.num2 = num2

    def add(self) -> int:
        """Сложение: возвращает сумму двух чисел"""
        return self.num1 + self.num2

    def subtract(self) -> int:
        """Вычитание: возвращает разность двух чисел"""
        return self.num1 - self.num2

    def multiply(self) -> int:
        """Умножение: возвращает произведение двух чисел"""
        return self.num1 * self.num2


class AddressBook:
    """
    Класс, представляющий адресную книгу.

    Attributes:
        contacts (dict): Словарь контактов, где ключ - имя контакта, значение - номер телефона.

    Examples:
        >>> address_book = AddressBook()
        >>> address_book.add_contact('John', '123456789')
        >>> address_book.add_contact('Jane', '987654321')
        >>> address_book.get_contact('John')
        '123456789'
        >>> address_book.get_contact('Jane')
        '987654321'
    """

    def __init__(self):
        self.contacts = {}

    def add_contact(self, name: str, phone: str) -> None:
        """Добавление контакта в адресную книгу"""
        self.contacts[name] = phone

    def get_contact(self, name: str) -> str:
        """Получение номера телефона по имени контакта"""
        return self.contacts.get(name, 'Contact not found')

from math import pi

class Circle:
    """
    Класс, представляющий круг.

    Attributes:
        radius (float): Радиус круга.

    Examples:
        >>> circle = Circle(5)
        >>> circle.calculate_area()
        78.53981633974483
        >>> circle.calculate_circumference()
        31.41592653589793
    """

    def __init__(self, radius: float):
        self.radius = radius

    def calculate_area(self) -> float:
        """Вычисление площади круга"""
        return pi * self.radius * self.radius

    def calculate_circumference(self) -> float:
        """Вычисление длины окружности круга"""
        return 2 * pi * self.radius


if __name__ == "__main__":
    import doctest
    doctest.testmod()
