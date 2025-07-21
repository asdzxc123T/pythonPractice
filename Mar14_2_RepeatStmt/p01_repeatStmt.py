# 반복
#   횟수 : 푸쉬업 100개
#   조건 : 푸쉬업 점심먹고 5교시 시작전까지

# Python
#   컬렉션 탐색용 - for
#   조건 따져서 반복 - while

a = [234, 56, 12, 98, 3, 7896]
# for 변수명 in 컬렉션명:
#     내용
for v in a:
    print(v)
print("-----")

# 1 ~ 5 출력
for v in range(1, 6):
    print(v)
print("-----")
# 변수 만들기만 하고 값은 안 넣으면
#       PL마다 다른데(0, 쓰레기값, 안됨, ...)
#       Python은 존재자체가 불가능한데 => 안됨
# 10!
g = 1
for v in range(2, 11):
    g *= v
print(g)
print("-----")

b = [1, 231, 2, 3]
# len(b) == 내용물 수(4)
# range(4) == 0 ~ 3
for i in range(len(b)):
    print(i, b[i])
print("-----")

# list => enumerate() -> (인덱스, 값) 형태의 tuple
for i, v in enumerate(b):
    print(i, v, type(v))
print("-----")

# dict => .items() -> (key, value) 형태의 tuple
c = {"기온":20, "미세먼지":"심함"}
for k, v in c.items():
    print(k, v, type(v))