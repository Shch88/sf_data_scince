"""Игра угадай число.
Компьютер сам загадывает и угадывает число
"""
import numpy as np

def random_predict(number:int=1) -> int:
    """Угадываем число халвингом списка

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    count = 0
    numbers_list = list(range(1,101)) # Создадим список возможных чисел
    count_list = [] # Для "отлова" верного результата реверсивной ф-ции     
    
    def halved_predict_func(numbers_list, count): # Функция поиска числа халвингом
        count +=1
        if number != numbers_list[0] and number != numbers_list[-1]: # Исключаем первое и последнее числа
            ind = len(numbers_list)//2 #  Индекс списка (середина)
            predict_number = numbers_list[ind]  # Определяем точку халвинга (угадываем число)
            if number == predict_number:
                count_list.append(count)
            elif number < predict_number:
                numbers_list = numbers_list[1:ind] # Халвим список
                halved_predict_func(numbers_list, count) # Продолжаем поиск с новым списком
            else:
                ind += 1
                numbers_list = numbers_list[ind:-1] # Халвим список
                halved_predict_func(numbers_list, count) # Продолжаем поиск с новым списком
        elif number == numbers_list[0]: # Подразумеваем, что отгадали )
            count_list.append(count)
        else: # Подразумеваем, что отгадали )
            count_list.append(count) 
        return count_list[0]
    result = halved_predict_func(numbers_list, count)
    return result
#print(f'Количество попыток: {random_predict()}')

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict (_type_): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    
    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируес сид случайной геренации с 1 (последовательность с этим сидом всегда будет одинаковая)
    random_array = np.random.randint(1, 101, size = (1000)) # загадали 1000 случайных чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls)) # находим среднее количество попыток
    
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return score

# RUN
if __name__ == '__main__':
    score_game(random_predict)