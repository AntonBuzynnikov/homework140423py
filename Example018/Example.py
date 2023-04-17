# Требуется найти в списке A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в списке.
# В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X
N = int(input('Введите количество элементов: '))
A = []
for i in range(N):
    A.append(int(input('Введите значение элемента: ')))
X = int(input('Введите искомый элемент: '))
A.append(X)
A.sort()
xIndex = A.index(X)
if xIndex != 0:
    previousEl = abs(A[xIndex]-A[xIndex-1])
else:
    previousEl = -1
if xIndex != (len(A)-1):
    nextEl = abs(A[xIndex]-A[xIndex+1])
else:
    nextEl = -1
if (previousEl > nextEl) and nextEl !=-1:
    print(A[xIndex+1])
elif previousEl == nextEl:
    print(A[xIndex-1],A[xIndex+1])
elif (previousEl < nextEl) and nextEl != -1:
    print(A[xIndex+1])
else:
    print(A[xIndex-1])
