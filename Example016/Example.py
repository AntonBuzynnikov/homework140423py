# Требуется вычислить, сколько раз встречается некоторое число X в списке A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
N = int(input('Введите количество элементов массива: '))
A = []
for i in range(N):
    A.append(int(input('Введите значение элемета: ')))
X = int(input('Введите искомое значение: '))
count = 0
for i in range(N):
    if A[i] == X:
        count += 1
print(count)