# exception
#   수학에서 나누기 0은 없음
#   내 동생이 그걸 몰랐음 -> 나누기 0 시도하다가 실패
#   -> 나한테 와서 승질
# exception handling
#   승질 못내게 대비책을 마련해놓자
#   문제 생길만한 거를 파악해서 대비책을 마련해놓자
#       Java : 처리 안 해놓으면 에러
#       자유의 언어 : 하든말든
#   try:
#       일단 여기를 실행
#   except 예외이름 as 별칭:
#       별칭에 예외사유가 담김
#       그 문제가 발생하면 여기를 실행
#   except 예외이름:
#       그 문제가 발생하면 여기를 실행
#   ...
#   else:
#       아무 문제도 없었으면 여기를 실행
#   finally:
#       문제가 있었든 없었든 무조건 실행 + return보다 먼저
x = int(input("x : "))
y = int(input("y : "))
try:
    d = x / y
    print("-----------")
    print(d)

    e = [54, 123, 3]
    print(e[y])
# except ZeroDivisionError:
#     print("나누기 0은 없다")
# except IndexError:
#     print("리스트에 그거 없다")
except Exception as e:
    print(e) # 개발하는 동안..., 개발 종료 때 지우고
else:
    print("문제 없었음")
finally:
    print("문제 발생여부 상관 없이 어쨌든 실행")

# Exception으로부터 상속받는 IndexError, ZeroDivisionError

# OOP
#   polymorphism(다형성)
#       상위타입(Animal) 변수에 하위타입(Dog) 데이터 넣는 게 가능

#   Python] 상위타입(object) 변수에 하위타입(Dog, str, int, ...)
#   Python의 모든 변수의 자료형 : object
#   1) Python은 자료형이 자동? -> Python은 다 객체
#   2) Python은 자료형을 바꾸는 것도 가능? -> Python은 자료형을 바꾼 적이 없음