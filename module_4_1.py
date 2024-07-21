# Домашняя работа по уроку "Модули и пакеты"

from fake_div import divide as fd
from true_div import divide as td

result_1 = fd(99, 3)
result_2 = fd(99, 0)
result_3 = td(33, 3)
result_4 = td(33, 0)

print(f' result 1: {result_1}')
print(f' result 2: {result_2}')
print(f' result 3: {result_3}')
print(f' result 4: {result_4}')

