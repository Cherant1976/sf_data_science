import numpy as np

def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь
    #Количество попыток
    count = 0

    # Перовначальные границы интервала поиска равны границам задания случайного числа
    number_min = 1
    number_max = 101
    
    #Т.к. я оставил в начале кода count=0, то predict не должен быть в загадываемом диапазоне.
    # Если predict будет равен числу из диапазона, то можно сразу угадать с 0 попытки  
    predict = 0 

    # В цикле меняем границы интервала поиска в зависимости от сравнения числа 
    # из интервала поиска с "загаданным" числом
    while number != predict:
        count += 1      
        predict = number_min + int((number_max-number_min)/2)
        if predict > number:
            number_max = predict                
        elif predict < number:
            number_min = predict
    # Ваш код заканчивается здесь

    return count