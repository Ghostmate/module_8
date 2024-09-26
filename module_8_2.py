def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for n in numbers:
        try:
            result += n
        except(TypeError):
            print(f'Некорректный тип данных для подсчёта суммы - {n}')
            incorrect_data += 1
    return [result, incorrect_data]


def calculate_average(numbers):
    # length = 0
    try:
        length = len(numbers)
        1/length
    except(TypeError):
        print('В numbers записан некорректный тип данных.')
        return
    except ZeroDivisionError as e:
        # print(e)
        return 0
    temp = personal_sum(numbers)
    try:
        length -= temp[1]
        if length <= 0:
            # raise Exception(ZeroDivisionError('division by zero'))
            1/0
    except ZeroDivisionError as e:
        # print(e)
        return 0
    else:
        return temp[0] / length

print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать
print(f'Результат 5: {calculate_average([])}') # 0