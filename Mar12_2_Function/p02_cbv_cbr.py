# Call By Value, Call By Reference
# 값을 넣어서 호출, 주소값 넣어서 호출
d = 10
e = 10
#############
def test(a, b, c):
    global e # 이 공간에서 e라고 쓰는 거는 4번줄의 그 e라고 선언
    print("green", a, b[0], c[0], id(a), id(b), id(c))
    a = 100 # 초록 a 100으로 바꿔
    b[0] = 100
    c = [100, 200]
    d = 100 # 3번줄 d를 100으로 바꿔 x / 3번줄 d랑 무관, green d 새로 만들고 100 넣기
    e = 100 
    print("green", a, b[0], c[0], d, e, id(a), id(b), id(c), id(d), id(e))
#############
a = 10
b = [10, 20]
c = [10, 20]
# a도 10, d도 10, e도 10
# 사실은 다 별개지만
# Python] 다 같은 데이터 넣은 건가 싶어서
# -> 같은 공간 써서 메모리 절약하게
# 고급 언어의 오지랖
print(id(a), id(d), id(e))
print("red", a, b[0], c[0], id(a), id(b), id(c))
test(a, b, c)
print("red", a, b[0], c[0], d, e, id(a), id(b), id(c), id(d), id(e))