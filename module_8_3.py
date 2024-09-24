class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message

class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message

class Car:

    def __init__(self, model_name: str, vin: int, numbers: str):
        self.model = model_name
        if self.__is_valid_vin(vin):
            self.__vin = vin
        if self.__is_valid_numbers(numbers):
            self.__numbers = numbers

    def __is_valid_vin(vin_number):
        """проверяет vin_number на корректность."""
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber("Некорректный тип vin-номер.")
        elif 1000000 > vin_number or vin_number > 9999999:
            raise IncorrectVinNumber("Неверный диапазон для vin номера.")
        else:
            return True

    def __is_valid_numbers(numbers):
        """проверяет госномер number на корректность."""
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров.')
        elif len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера (не 6 символов)')
        else:
            return True

try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')