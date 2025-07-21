# operator(연산자)
# = : 대입연산자
#       우항에 있는 걸 좌항에 넣어라
#       우선순위 마지막
x = int(input("x : "))
y = int(input("y : "))
print("--------------")
print("x는 %d, y는 %d" % (x, y))

# + - * / // % : 산술연산자
# 다른 언어에서 /는 소수점 삭제(정수 나누기)
# Python
#   /는 소수점 살림(실수 나누기)
#   //가 정수 나누기
a = x + y
b = x - y
c = x * y
d = x / y
e = x // y
f = x % y
print(a, b, c, d, e, f)

print("------------")
z = "ㅋ"
zz = "ㅎ"
# int + str
#   일반적인 언어에서는 붙여서 str(10ㅋ)
#   Python에서는 안 됨
# g = x + z 
# print(g)

# str + str
h = z + zz
print(h)

# int * str
#   일반적인 다른 언어에서 안 됨
#   Python은 글자 반복
i = x * z
print(i)

# int ** int
#   일반적인 다른 언어에는 없음
#   Python에서는 x의 y승
j = x ** y
print(j)

print("------------")

# 산술+대입연산자
# += -= *= /= %=
x += 3 # x = x + 3
y *= 2 # y = y * 2
print(x, y)

# 일반적인 다른 언어에 ++, --
# Python에는 없음
#       Python : 인간친화적 -> 공부할 거리를 줄이자
#                대체할 수 있으면 삭제
#                효율성이 떨어짐
# x = x + 1
# x += 1
# x++
# y = y - 1
# y -= 1
# y--