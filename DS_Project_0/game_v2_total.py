import numpy as np

def random_predict(number) -> int:
    """Наша программа пытается отгадать число

    Args:
        number (_type_): Числа для угадывания

    Returns:
        int: количество попыток
    """
    predict_list = list(range(101)) #создаем список с диапазоном от 1 до 100
    count = 0
    while True:
        count += 1 #подсчет кол-ва итераций 
        predict_number = int(np.mean(predict_list)) #присваиваем начальное число нашей программе, от которой она будет отталкиваться (среднее арифмитическое от списка predict_list)
        pre_slice = (len(predict_list))//2 #считает целочисленную половину кол-во строк нашего списка для дальнейшего среза этого-же списка, для получения меньшего диапазона поиска
        if predict_number > number:
            predict_list = predict_list[:pre_slice] 
        elif predict_number < number:
            predict_list = predict_list[pre_slice:]
        else:
            break #прекращаем цикл
    return count
def game_score(random_predict) -> int:
    """За какое количество попыток в среднем угадывает число наша программа при 1000 подходов

    Args:
        random_predict (_type_): функция угадывания

    Returns:
        int: количество попыток в среднем
    """
    count_list = []
    np.random.seed(1) #фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=1000) #загадываем список чисел
    
    for number in random_array:
        count_list.append(random_predict(number)) #присваиваем полученное значение в список
        
    score = int(np.mean(count_list))
    return f'Ваш алгоритм угадывает число в среднем за {score} попыток!'


print(game_score(random_predict))