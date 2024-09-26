class IncorrectVinNumber(Exception):
    def __init__(self, *args):
        if len(args) > 0:
            self.message = args[0]
        else:
            self.message = ''

class IncorrectCarNumbers(Exception):
    def __init__(self, *args):
        if len(args) > 0:
            self.message = args[0]
        else:
            self.message = ''

class Car:
    def __init__(self, model, vin, numbers):
        if self.__is_valid_vin(vin) and self.__is_valid_numbers(numbers):
            self.__vin = vin
            self.__numbers = numbers
            self.model = model
        pass

    def __is_valid_vin(self, vin_number):
        if isinstance(vin_number,int):
            if vin_number > 9999999 or vin_number < 1000000:
                raise IncorrectVinNumber('Неверный диапазон для vin номера')
        else:
            raise IncorrectVinNumber('Некорректный тип vin номер')
        return True

    def __is_valid_numbers(self, numbers):
        if isinstance(numbers,str):
            if len(numbers) != 6:
                raise IncorrectCarNumbers('Неверная длина номера')
        else:
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        return True

# try:
#   first = Car('Model1', 1000000, 'f123dj')
# except IncorrectVinNumber as exc:
#   print(exc.message)
# except IncorrectCarNumbers as exc:
#   print(exc.message)
# else:
#   print(f'{first.model} успешно создан')
#
# try:
#   second = Car('Model2', 300, 'т001тр')
# except IncorrectVinNumber as exc:
#   print(exc.message)
# except IncorrectCarNumbers as exc:
#   print(exc.message)
# else:
#   print(f'{second.model} успешно создан')
#
# try:
#   third = Car('Model3', 2020202, 'нет номера')
# except IncorrectVinNumber as exc:
#   print(exc.message)
# except IncorrectCarNumbers as exc:
#   print(exc.message)
# else:
#   print(f'{third.model} успешно создан')