import pandas as pd
import numpy as np


chat_id = 515069313
 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
def solution(x_success, x_cnt, y_success, y_cnt):
    res = proportions_ztest([x_success, y_success],
                            [x_cnt, y_cnt],
                            alternative='smaller')
    return res[1] < 0.05 # Ваш ответ, True или False
