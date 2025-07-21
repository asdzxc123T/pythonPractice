# -*- coding: utf-8 -*-

# 연산자 : stack 영역이 대상
#   어차피 Python은 모든 데이터가 heap 영역에
#   연산자 쓰면 heap 영역으로 알아먹게 해놨을 뿐

# 논리 연산자 계열
# 초과 이상 같다 다르다 이하 미만
#  >   >=   ==   !=    <=   <

height = float(input("키 : "))
age = int(input("나이 : "))
print("---------------")
print("키는 %.1fcm, 나이는 %d살" % (height, age))

# a는 키가 140 초과해야 탈 수 있다
a = (height > 140) # 변수가 앞쪽에 배치되는 걸 선호하는 문화
print(a)

# b는 나이가 10살 이하여야 탈 수 있다
b = (age <= 10) 
print(b)

# c는 5살 전용
c = (age == 5)
print(c)

#           ~고(and)    ~거나(or)
# Python]   and         or          => 중간에 끊어주는
#           &           |           => 무식하게 끝까지 가는
# 다른 PL]  &&          ||
#           &           |

# and : 확률 낮은 거를 앞으로 배치
# d는 나이가 5살 이상이고 키도 200 이상이어야 탈 수 있다
# d = (age >= 5 and height >= 200)
d = (height >= 200 and age >= 5)
print(d)

# or : 확률 높은 거를 앞으로 배치
# e는 나이가 50살 이상이거나 키가 140 이상이어야 탈 수 있다
# e = (age >= 50 or height >= 140)
e = (height >= 140 or age >= 50)
print(e)

# f는 나이가 10살 이상이고 20살 이상이면
f = (age >= 20)
print(f)

# g는 100 <= 키 <= 130만 탈 수 있다
# Python은 100 <= height <= 130도 가능
g = (height <= 130 and height >= 100)
print(g)

# xor (eXclusive OR) : ^
# o o => x
# o x => o
# x o => o
# x x => x
# h는 나이가 5살 이상이든지
# 키가 130cm 이하든지
# 둘 중에 하나만
h = (age >= 5 ^ height <= 130)
print(h)

# not
# 다른 언어] !
# Python]    not
# i는 h를 탈 수 있는 사람은 못 타고, h 못타는 사람은 탐
# i는 h의 반대
i = not h
print(i)

# not : 1항 연산
# 대부분 연산자는 2항연산
# 3항 연산 - Python에 없음
# P : 대체할 수 있으면 삭제
# say = (age >= 10) ? "타세요" : "나가"
if age >= 10:
    say = "타세요"
else:
    say = "나가"