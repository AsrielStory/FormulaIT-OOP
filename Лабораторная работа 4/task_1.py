class Vehicle:
    """Класс автомобиля"""
    def __init__(self, name: str, load_capacity: float | int, status: str, position: str) -> None:
        """
        Конструктор класса

        :param name: Модель автомобиля с его ID
        :param load_capacity: Грузоподъёмность автомобиля (указывать в кг)
        :param status: Статус автомобиля
        :param position: Местоположение автомобиля

        Примеры:

        >>> vehicle_1 = Vehicle('Hoxi 556754', 400.0, 'Заряжается', '53.905062 30.343812')
        """

        if not(isinstance(name, str)):
            raise TypeError
        self.name = name
        if not(isinstance(load_capacity, (float, int))):
            raise TypeError
        self.load_capacity = load_capacity
        if not(isinstance(status, str)):
            raise TypeError
        self.status = status
        if not(isinstance(position, str)):
            raise TypeError
        self.position = position

    def __str__(self) -> str:
        """Магический метод для получения 'читаемого' представления объекта"""
        return f'Автомобиль - {self.name}, Статус - {self.status}, Местоположение - {self.position}'

    def __repr__(self) -> str:
        """Магический метод для получения 'официального' представления объекта"""
        return (f'{self.__class__.__name__}('
                f'name={self.name!r}, '
                f'load_capacity={self.load_capacity!r}, '
                f'status={self.status!r}, '
                f'position={self.position!r})')

    def send_command(self, command: str) -> None:
        """
        Метод для отладки. Отправка команды автомобилю

        :param command: Команда для автомобилей Hoxi
        :return: None

        Примеры:

        >>> vehicle_1 = Vehicle('Hoxi 556754', 400.0, 'Заряжается', '53.905062, 30.343812')
        >>> vehicle_1.send_command('move -a -20.625833 166.305833')
        """
        ...

    def update_info(self, status: str, position: str) -> None:
        """
        Метод для отладки. Коррекция информации о машине

        :param status: Нынешний статус
        :param position: Нынешнее местоположение
        :return: None

        Примеры:

        >>> vehicle_1 = Vehicle('Hoxi 556754', 400.0, 'Заряжается', '53.905062, 30.343812')
        >>> vehicle_1.update_info('Свободен', '-20.625833 166.305833')
        """
        ...

    def move_to_cord(self, latitude: float, longitude: float) -> None:
        """
        Метод для отправки машины по координатам

        :param latitude: Широта конечной точки
        :param longitude: Долгота конечной точки
        :return: None

        Примеры:

        >>> vehicle_1 = Vehicle('Hoxi 556754', 400.0, 'Заряжается', '53.905062, 30.343812')
        >>> vehicle_1.move_to_cord(-20.625833, 166.305833)
        """
        ...


class Car(Vehicle):
    """Класс легкового автомобиля"""
    def __init__(self, name: str, load_capacity: float | int, status: str, position: str, passengers: list[str]) -> None:
        """
        Конструктор класса

        :param name: Модель автомобиля с его ID
        :param load_capacity: Грузоподъёмность автомобиля (указывать в кг)
        :param status: Статус автомобиля
        :param position: Местоположение автомобиля
        :param passengers: Список пассажиров

        Примеры:

        >>> car_1 = Car('HoxiL 556754', 400.0, 'В пути', '53.908513, 30.344322', ['Рико', 'Рэг', 'Наначи'])
        """
        super().__init__(name, load_capacity, status, position)
        if not(isinstance(passengers, list)):
            raise TypeError
        self.passengers = passengers

    def __repr__(self) -> str:
        """Перегрузка репрезентации из базового класса. Добавлен список пассажиров"""
        return (f'{self.__class__.__name__}('
                f'name={self.name!r}, '
                f'load_capacity={self.load_capacity!r}, '
                f'status={self.status!r}, '
                f'position={self.position!r}, '
                f'passengers={self.passengers!r})')

    def update_info(self, status: str, position: str, passengers: list[str]) -> None:
        """
        Метод для отладки. Коррекция информации о машине (перегружен для добавления списка груза)

        :param status: Нынешний статус
        :param position: Нынешнее местоположение
        :param passengers: Нынешние пассажиры
        :return: None

        Примеры

        >>> car_1 = Car('HoxiL 556754', 400.0, 'В пути', '53.908513, 30.344322', ['Рико', 'Рэг', 'Наначи'])
        >>> car_1.update_info('Свободен', '-20.625833 166.305833', ['Рокси', 'Рудеус', 'Сильфиета'])
        """
        ...


class Truck(Vehicle):
    """Класс грузового автомобиля"""
    def __init__(self, name: str, load_capacity: float | int, status: str, position: str, cargo: list[str]) -> None:
        """
        Конструктор класса

        :param name: Модель автомобиля с его ID
        :param load_capacity: Грузоподъёмность автомобиля (указывать в кг)
        :param status: Статус автомобиля
        :param position: Местоположение автомобиля
        :param cargo: Список груза

        Примеры:

        >>> truck_1 = Truck('HoxiM 556754', 1000.0, 'В пути', '53.908513, 30.344322', ['Акула IKEA', 'Ананас', 'Котлетки с пюрешкой'])
        """
        super().__init__(name, load_capacity, status, position)
        if not(isinstance(cargo, list)):
            raise TypeError
        self.cargo = cargo

    def __repr__(self) -> str:
        """Перегрузка репрезентации из базового класса. Добавлен список груза"""
        return (f'{self.__class__.__name__}('
                f'name={self.name!r}, '
                f'load_capacity={self.load_capacity!r}, '
                f'status={self.status!r}, '
                f'position={self.position!r}, '
                f'cargo={self.cargo!r})')

    def update_info(self, status: str, position: str, cargo: list[str]) -> None:
        """
        Метод для отладки. Коррекция информации о машине (перегружен для добавления списка груза)

        :param status: Нынешний статус
        :param position: Нынешнее местоположение
        :param cargo: Нынешний груз
        :return: None

        Примеры

        >>> truck_1 = Truck('HoxiM 556754', 1000.0, 'В пути', '53.908513, 30.344322', ['Акула IKEA', 'Ананас', 'Котлетки с пюрешкой'])
        >>> truck_1.update_info('Свободен', '-20.625833 166.305833', ['Акула IKEA', 'Косплей. Пушистые уши'])
        """
        ...


if __name__ == "__main__":
    pass
