# 함수
# 언제
#   소스 정리
#   만들어 놓고 계속 쓰게

# lambda함수 : 무명의 1회용 함수
# 언제
#   값 간단하게 구할 때
# (lambda param1, param2, ...: 내용)(param1 값, param2 값, ...)
# 내용 자리에 값만 있으면 return
(lambda x: print("이재원" * x))(3)
c = (lambda x, y: x + y)(5, 7)
print(c)
print("-----")

def printName(x):
    print("이재원" * x)

def getSum(a, b):
    return a + b

printName(3)
print(getSum(5, 7))