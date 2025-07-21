# function 함수 : 소스 정리 차원
#   연관된 작업 묶어서 정의해놓고
#   필요할 때마다 사용

# 다른 언어 : main 함수 영역이 존재
# Python : 그런 게 없음 => interpreter 방식 언어

# 다른 언어 : 띄어쓰기, 엔터는 무의미
#            영역 표시할 때 {} 사용
# Python : 의미 있음
#          영역 표시할 때 :와 들여쓰기 사용
#          : 뒤에는 무조건 들여쓰기가 있어야 함

# 함수명 짓는 규칙은 변수명 짓는 규칙과 동일한데
# 변수 : 데이터 담는 그릇 => 명사형
# 함수 : 액션들 모아놓은 => 동사형
# 유지보수의 시대 -> 알파벳순 정렬
# 동사를 앞으로 -> 기능별로 정렬
# 동사를 뒤로 -> 주제별로 정렬


# 1) 정의
# def 함수명(변수명, 변수명, ...):
#     함수 내용
#     함수 내용
#     ...
#     return 값
# 함수 밖
def printNum():
    print("12345")
    print("1234")
    print("123")
    print("12")
    print("1")


def test():
    pass  # 자리만 차지하는


# 두 수의 합을 출력하는 함수
# 합을 구하려면 두 수가 있어야
# 함수를 수행하는데 필요한 재료 : parameter, 인자, argument, ...
def printSum(a, b = 99): # b의 기본값을 99
    print(a)
    print(b)
    print(a + b)
    print("--")

# 세 수의 합을 출력하는 함수
def printSum3(a, b = 50, c = 99):
    print(a + b + c)
    print("---")

# overriding vs overloading
# parameter(갯수, 자료형)가 다르면 함수명 같아도 됨
# => 함수 호출 때 구별 가능
# => overloading : 일부러 함수명 같게 짓는 기술명
# Python] parameter 지정 기능 + 기본값 + 자료형 자동
# => 함수 호출 때 구별 불가 => overloading 불가

# 2) 함수 호출
printNum()
printNum()
printNum()
printNum()
printSum(10, 20)
printSum(1, 200)
printSum(b = 500, a = 90)
printSum(100) # b값 안 넣으면 기본값으로