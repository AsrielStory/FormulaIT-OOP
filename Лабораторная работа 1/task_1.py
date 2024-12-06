import doctest


class Product:
    def __init__(self, name: str, cost: int | float, weight: int | float):
        """
        Создание и подготовка к работе объекта товара

        :param name: Название товара
        :param cost: Стоимость товара
        :param weight: Вес товара (указывается в килограммах)

        Примеры:

        >>> product_1 = Product('Картошка', 4.24, 4)
        """
        if not isinstance(name, str):
            raise TypeError
        self.name = name

        if not isinstance(cost, (int, float)):
            raise TypeError
        if not cost > 0:
            raise TypeError
        self.cost = cost

        if not isinstance(weight, (int, float)):
            raise TypeError
        if not weight > 0:
            raise ValueError
        self.weight = weight

    def cost_per_g(self) -> float:
        """
        Функция, которая рассчитывает стоимость товара за килограмм

        :return: Стоимость товара за килограмм

        Примеры:

        >>> product_1 = Product('Картошка', 4.24, 4)
        >>> product_1.cost_per_g()
        """
        pass

    def get_dict(self) -> dict:
        """
        Функция упаковывающая данные о товаре в словарь

        :return: Словарь с информацией о товаре

        Примеры:

        >>> product_1 = Product('Картошка', 4.24, 4)
        >>> product_1.get_dict()
        """
        pass

    def get_line(self, style: int) -> str:
        """
        Функция, преобразующая данные о товаре в строку

        :param style: Стиль в который преобразуются данные (1-4)
        :raise ValueError: Введённого стиля не существует

        :return: Строка с данными

        Примеры:

        >>> product_1 = Product('Картошка', 4.24, 4)
        >>> product_1.get_line(1)
        """
        pass


class MemoryStorage:
    def __init__(self, name: str, total: int, used: int):
        """
        Создание и подготовка к работе объекта "Накопителя информации"

        :param name: Имя накопителя
        :param total: Всего памяти (в байтах)
        :param used: Использовано памяти (в байтах)

        Примеры:

        >>> disk_1 = MemoryStorage('Kingstone', 257698037760, 32212254720) # Накопитель на 240GB
        """
        if not isinstance(name, str):
            raise TypeError
        self.name = name

        if not isinstance(total, int):
            raise TypeError
        if not total > 0:
            raise TypeError
        self.total = total

        if not isinstance(used, int):
            raise TypeError
        if not used > 0:
            raise TypeError
        self.used = used

        self.free = self.total - self.used

    def add_mem(self, memory: int) -> None:
        """
        Функция заполняющая накопитель

        :param memory: На сколько заполняется (в байтах)

        :raise ValueError: Недостаточно места

        Примеры:

        >>> disk_1 = MemoryStorage('Kingstone', 257698037760, 32212254720) # Накопитель на 240GB
        >>> disk_1.add_mem(1073741824) # Заполнение накопителя на 1GB
        """
        pass

    def remove_mem(self, memory: int) -> None:
        """
        Функция очищающая накопитель

        :param memory: На сколько очищается (в байтах)

        :raise ValueError: Не достаточно информации для очистки

        Примеры:

        >>> disk_1 = MemoryStorage('Kingstone', 257698037760, 32212254720) # Накопитель на 240GB
        >>> disk_1.remove_mem(1073741824) # Очистка накопителя на 1GB
        """
        pass


class ProfileObject:
    def __init__(self, profile_id: int, name: str, avatar_path: str):
        """
        Создание и подготовка к работе объекта "Профиль пользователя"

        :param profile_id: ID пользователя
        :param name: Имя пользователя
        :param avatar_path: Путь к файлу аватарки

        Примеры:

        >>> profile_1 = ProfileObject(134889, 'Axi', '/users/134889/avatar.png')
        """
        if not isinstance(profile_id, int):
            raise TypeError
        if not profile_id > 0:
            raise ValueError
        self.profile_id = profile_id

        if not isinstance(name, str):
            raise TypeError
        self.name = name

        if not isinstance(avatar_path, str):
            raise TypeError
        self.avatar_path = avatar_path

    def update_id(self, profile_id: int) -> None:
        """
        Функция обновляющая ID пользователя

        :param profile_id: Новый ID пользователя

        :raise ValueError: ID занят

        Примеры:

        >>> profile_1 = ProfileObject(134889, 'Axi', '/users/134889/avatar.png')
        >>> profile_1.update_id(485321)
        """
        pass

    def update_name(self, name: str) -> None:
        """
        Функция обновляющая имя пользователя

        :param name: Новое имя пользователя

        :raise ValueError: Имя пользователя уже занято

        Примеры:

        >>> profile_1 = ProfileObject(134889, 'Axi', '/users/134889/avatar.png')
        >>> profile_1.update_name('AxiTheFox')
        """
        pass

    def update_avatar(self, path: str) -> None:
        """
        Функция обновляющая аватар пользователя

        :param path: Расположение нового файла аватара

        Примеры:

        >>> profile_1 = ProfileObject(134889, 'Axi', '/users/134889/avatar.png')
        >>> profile_1.update_avatar('C:/Users/User/Desktop/avatar_2.png')
        """
        pass


if __name__ == "__main__":
    doctest.testmod()
