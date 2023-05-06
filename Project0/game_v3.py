import numpy as np

def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь
    count = 0
    # Объявляются переменные/границы для задания случайного числа
    rand_max = 101
    rand_min = 1
    #np.random.seed(1)  # При необходимости фиксируем сид для воспроизводимости
    predict = np.random.randint(rand_min, rand_max)
    # Перовначальные границы интервала поиска равны границам задания случайного числа
    number_max = rand_max
    number_min = rand_min
    
    # В цикле меняем границы интервала поиска в зависимости от сравнения числа 
    # из интервала поиска с "загаданным" числом
    while number != predict:
        count += 1      
        number = number_min + int((number_max-number_min)/2)
        if number > predict:
            number_max=number                
        elif number < predict:
            number_min=number
    # Ваш код заканчивается здесь

    return count