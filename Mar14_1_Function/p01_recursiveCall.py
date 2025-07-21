# 1 + 2 + 3 + ... + 50 = ?

# 1 + 2 + 3 + ... + 1000 = ?

# 1 + 2 + 3 + ... + 99 = ?

# 함수를 recursive(재귀적)하게 호출 : 기술명
#   함수 내부에서 자기자신을 호출해서 반복이 생기게 하는
#   언제 : 규칙적인 숫자 계산 - x
# 숫자를 넣으면 1 + ... + x까지 합 구해주는 함수
import sys


def getSum(x):
    if x == 1:
        return 1
    return x + getSum(x - 1)

# x = 5 : return getSum(4) + 5
#                return getSum(3) + 4
#                       return getSum(2) + 3
#                              return getSum(1) + 2
#                                     return 1

# factorial
def getFact(x):
    # if x == 1:
    #     return 1
    # return x * getFact(x - 1)
    if x != 1:
        return x * getFact(x - 1)
    return 1

# 피보나치 수열 값 구하기
# 1 1 2 3 5 8 13 21 34 55 89 144 ...
def getFibo(x):
    # if x < 3:
    if x == 1 or x == 2:
        return 1
    return getFibo(x - 1) + getFibo(x - 2)

################
# recursive 제한횟수 설정
# sys.setrecursionlimit(100000000)

a = getSum(5)
print(a)

b = getFact(10)
print(b)

c = getFibo(7)
print(c)