# static member variable
#   메모리의 static 영역에 만들어지고
#   메모리를 아낄 수 있는데
#   Python에도 smv가 있기는 있는데
#   극적인 메모리 절약 효과가 안 나서
#   사실상 없는 취급
# static method

# 지역변수 : 그 함수에서 쓰고 버릴 임시
# 파라메터 : 그 함수 실행하는데 필요한 재료
# 멤버변수 : 객체의 속성

# 변수 언제 만드나? 데이터 임시 저장해야 할 때
# 객체 언제 만드나? 데이터 실생활스럽게 임시 저장해야 할 때 
# 멤버변수가 없음 -> 저장할 게 없음

# 일반 method
class Calculator:
    # static method : 객체를 만들지 않고도 사용할 수 있는 메소드
    @staticmethod # 가독성 + 없으면 빨간줄 찍어주는 툴도 존재, 없어도 됨
    def printAdd(a, b): # self 없음
        print(a + b)

# 계산기
# 1 + 2 결과 출력

# static method 호출
# 클래스명.메소드명(...)
Calculator.printAdd(1, 2)

# 일반 method 호출
# 변수명.메소드명(...)
# calc = Calculator()
# calc.printAdd(1, 2)