if __name__ == "__main__":
    class SocialNetwork:
        """Базовый класс для социальных сетей"""

        def __init__(self, name: str, users_count: int):
            """
            Конструктор класса SocialNetwork

            Args:
                name (str): Название социальной сети
                users_count (int): Количество пользователей

            Attributes:
                name (str): Название социальной сети
                users_count (int): Количество пользователей
            """
            self.name = name
            self.users_count = users_count

        def __str__(self) -> str:
            """
            Метод для строкового представления объекта

            Returns:
                str: Строковое представление объекта
            """
            return f"{self.name} - пользователей: {self.users_count}"

        def __repr__(self) -> str:
            """
            Метод для представления объекта в виде строки кода

            Returns:
                str: Представление объекта в виде строки кода
            """
            return f"{self.__class__.__name__}(name='{self.name}', users_count={self.users_count})"

        def get_user_count(self) -> int:
            """
            Метод для получения количества пользователей

            Returns:
                int: Количество пользователей
            """
            return self.users_count


    class VK(SocialNetwork):
        """Дочерний класс для социальной сети ВКонтакте"""

        def __init__(self, name: str, users_count: int, registered_users: int):
            """
            Конструктор класса VK

            Args:
                name (str): Название социальной сети
                users_count (int): Количество пользователей
                registered_users (int): Количество зарегистрированных пользователей

            Attributes:
                name (str): Название социальной сети
                users_count (int): Количество пользователей
                registered_users (int): Количество зарегистрированных пользователей
            """
            super().__init__(name, users_count)
            self.registered_users = registered_users

        def __str__(self) -> str:
            """
            Метод для строкового представления объекта

            Returns:
                str: Строковое представление объекта
            """
            return f"ВКонтакте - пользователей: {self.users_count}, зарегистрированных пользователей: {self.registered_users}"

        def get_registered_user_count(self) -> int:
            """
            Метод для получения количества зарегистрированных пользователей

            Returns:
                int: Количество зарегистрированных пользователей
            """
            return self.registered_users

        def post_photo(self, photo_url: str) -> str:
            """
            Метод для публикации фотографии в социальной сети ВКонтакте

            Args:
                photo_url (str): URL фотографии

            Returns:
                str: Результат публикации фотографии
            """
            # Код для публикации фотографии
            return f"Фотография успешно опубликована в VK: {photo_url}"


    class Facebook(SocialNetwork):
        """Дочерний класс для социальной сети Facebook"""

        def __init__(self, name: str, users_count: int, friends_count: int):
            """
            Конструктор класса Facebook

            Args:
                name (str): Название социальной сети
                users_count (int): Количество пользователей
                friends_count (int): Количество друзей

            Attributes:
                name (str): Название социальной сети
                users_count (int): Количество пользователей
                friends_count (int): Количество друзей
            """
            super().__init__(name, users_count)
            self.friends_count = friends_count

        def __str__(self) -> str:
            """
            Метод для строкового представления объекта

            Returns:
                str: Строковое представление объекта
            """
            return f"Facebook - пользователей: {self.users_count}, друзей: {self.friends_count}"

        def get_friends_count(self) -> int:
            """
            Метод для получения количества друзей

            Returns:
                int: Количество друзей
            """

    pass
