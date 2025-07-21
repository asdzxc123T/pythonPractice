# 반복문
#   반복횟수 - for + range 써서 그런 느낌 내기
#   컬렉션 탐색용 - for 
#   반복조건 - while
#       while 조건식:
#           조건식 맞으면 실행
#       while 문법 구조상 조건식 먼저 써야하는데
#       그게 애매한 상황이 있음

# 1 + 2 + ... + 100 = ?
from random import randint


sum = 0
for i in range(1, 101):
    sum += i
print(sum)
print("-----")
# 1 + 2 + ... + ? >= 100
# 을 만족하는 최소 ?를 찾으시오
sum = 0
i = 0
while sum < 100:
    i += 1
    sum += i
print(i)
print("-----")

# 1 ~ 10 사이의 랜덤한 정수
c = randint(1, 10)
print(c)
print("-----")

# 1 ~ 5 사이 랜덤한 정수
# 10번
for i in range(10):
    print(randint(1, 5))
print("-----")

# 1 ~ 5 사이의 랜덤한 정수 4 나올 때까지 출력
e = randint(1, 5)
print(e)
while e != 4:
    e = randint(1, 5)
    print(e)
print("-----")

# 아무 숫자나 입력받아서 출력
# 10이라고 쓰면 그만
f = int(input("숫자 입력 : "))
print(f)
while f != 10:
    f = int(input("숫자 입력 : "))
    print(f)