# 함수
# 숫자를 하나 넣으면
# 홀수인지 판별해서 결과를 출력해주는 함수
from time import sleep


def printIsOdd(a):
    print(a % 2 == 1)

# 1) 콘솔창에 출력만 하고 사나
# 2) 출력 말고 다른 용도도...

# 숫자를 하나 넣으면
# 홀수인지 판별해주는 함수
def getIsOdd(a):
    return a % 2 == 1
    # print("aa") 여기는 실행 안 됨

# 숫자를 하나 넣으면 
# 2배한 결과를 구해주는 함수
def getMul(a):
    return a * 2

# 어떤 함수의 결과가 여러개(return이 여러개)는 불가능
# => collection 하나로 하면 될 것
# => Python은 return이 여러개가 가능?? -> 아님
# 숫자 2개 넣으면
# 합을 구해주는 함수
def getSum(x, y):
    a = x + y
    b = x - y
    c = x * y
    d = x / y
    return a, b, c, d
###############
# 함수 호출 (다른 언어의 main)
aa, bb, _, dd = getSum(20, 30)
print(aa, type(aa))
print(bb, type(bb))
print(dd, type(dd))

aa = getSum(20, 30)
print(aa, type(aa))

a = getMul(2)
sleep(a)

printIsOdd(1)
printIsOdd(10)
print(getIsOdd(1))
