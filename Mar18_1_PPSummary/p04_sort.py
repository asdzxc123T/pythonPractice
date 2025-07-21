# list를 정렬하는 함수

from random import randint
import time


def bubbleSort(l):
    # 두 개 비교해서 앞에가 크면 자리 바꾸기
    for i in range(len(l) - 1): # 0 ~ 3
        for j in range(len(l) - i - 1): # 0턴 : 0 ~ 3, 1턴 : 0 ~ 2, ...
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
            print(l, i, j)
    # return 필요 없음 (call by value, call by reference)

def selectionSort(l):
    for i in range(len(l) - 1): # 0 ~ 3
        least = i # 일단은 i번째가 가장 작다고 치고
        for j in range(i + 1, len(l)): # 0턴 : 1 ~ 4, 1턴 : 2 ~ 4, ...
            if l[j] < l[least]:
                least = j
            print(l, i, j)
        l[i], l[least] = l[least], l[i]

def insertionSort(l):
    for i in range(1, len(l)):
        for j in range(i):
            print(l, i, j)
            if l[i] < l[j]:
                t = l[i]
                for k in range(i, j, -1):
                    l[k] = l[k - 1]
                l[j] = t
                break

l1 = []
l2 = []
l3 = []
number = 5
for i in range(number):
    l1.append(randint(1, 10000))
    l2.append(l1[i])
    l3.append(l2[i])

print(l1, l2, l3)

# l.sort()
# 그 함수 써서 정렬

start = time.time()
bubbleSort(l1)
end = time.time()
print(end - start)

start = time.time()
selectionSort(l2)
end = time.time()
print(end - start)

start = time.time()
insertionSort(l3)
end = time.time()
print(end - start)

print(l1, l2, l3)