import numpy as np

def bisection(number):
    count_attempt = 0 
    search_range = []
    for i in range(1, 101):
        search_range.append(i)          # Создаем упорядоченный список возможных значений
    index = int(len(search_range) / 2)  # Запоминаем порядковый номер серединного значения
    predict = search_range[index]       # Задаем начальное предположение об искомом значении 
    while number != predict:
        count_attempt += 1
        if number > predict:            # Если загаданное число больше серединного значения, смещаем нижнюю границу поиска
            search_range = search_range[index + 1:]  # берем следующее число после проверенного
            index = int(len(search_range) / 2)
            predict = search_range[index]
        elif number < predict:          # Если загаданное число меньше серединного значения, смещаем верхнюю границу поиска
            search_range = search_range[:index]
            index = int(len(search_range) / 2)
            predict = search_range[index]
    else:
        count_attempt += 1     # Учитываем успешную попытку
    return(count_attempt)
            
    
def main_func(bisection):
    count_s = []       # список количества попыток в каждом из подходов
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))      # создаем список из случайных чисел для каждого из подходов
    for number in random_array:
        count_s.append(bisection(number))                 # ищем каждое из случайных чисел и записываем количество попыток
    mean_attempt = int(np.mean(count_s))                  # выводим среднее количество попыток на поиск случайного числа
    print(f"Алгоритм угадывает число в среднем за {mean_attempt} попыток")
    return(mean_attempt)

# Запуск
main_func(bisection)