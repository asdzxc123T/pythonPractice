# range : 범위 표현, 규칙적인 list가 필요할 때
a = range(15) # 0 ~ 14
a = range(1, 15) # 1 ~ 14
a = range(1, 15, 2) # 1 ~ 14, 2칸씩
print(a, type(a))

# list 1 ~ 20
b = list(range(1, 21))
print(b)

# tuple : 특징은 list랑 같음
# 데이터 여러개 저장용 x
# 변수 여러개 한꺼번에 값 넣을 때
c = (10, 10, 20, 30, 40)
print(c, type(c))
print(c[2])

q = 100
w = 200
# q랑 w 값 바꾸기
# 다른 언어의 경우 : 추가 변수가 필요함
# e = q
# q = w
# w = e

# Python의 경우 : tuple 활용
(q, w) = (w, q) # tuple의 소괄호는 생략 가능] q, w = w, q
print(q)
print(w) 

t, y, u = 120, 123, 150
print(t, y, u)