# Part 1 : Procedural Programming(절차지향 프로그래밍) / 시간낭비, 헛수고
#       변수, 함수, 제어문, ...
#       을 최적의 순서로 배치해서 프로그램 만들자
#           요즘 H/W 좋아져서 최적이 그닥 안 중요
#           알고리즘의 시대 -> 유지보수의 시대
#           좋은 알고리즘보다는 유지보수하기 좋게 만들자
#           유지보수하기 좋으려면 -> 소스가 보기 쉬워야

# Part 2 : Object Oriented Programming(객체지향 프로그래밍)
#       객체를 사용해서 리얼월드를 묘사
#       객체 : 실생활에 존재하는 거(실존하지 않는 추상적인 것일 수도)
#       객체를 만들려면 클래스가 필요
#           다른 언어 : 1 class = 1 file
#               Java는 파일(.java) 자체가 class
#               -> perfect한 OOL
#           Python : 마음대로
#               Python은 파일(.py)을 모듈이라 부르고
#               모듈 속에 class를 배치
#               -> hybrid한 OOL

# 변수명은 소문자로 시작
# 클래스명은 대문자로 시작

# class : 객체 찍는 도장/붕어빵틀
class Dog:
    name = None # member variable : 속성
    age = None

    def bark(self): # method : 액션
        print("멍")

    def showInfo(self): # method : 프로그램 상 필요한 기능
        print(self.name, self.age)

# 함수function vs 메소드method
#   기능 모아놓은 거 vs 객체의 액션

# object/instance : 찍어낸 거/붕어빵
d = Dog() # 개
d.name = "만득이"
d.age = 3
d.bark()
d.showInfo()
print("-----")

d2 = Dog() # 또 다른 개
d2.name = "후추"
d2.age = 2
d2.bark()
d2.showInfo()

# 변수
#       전역변수(global variable) : 그냥 밖에 있는 거
#               global만 붙이면 아무데서나 다 쓸 수 있는 거
#               자제
#       지역변수(local variable) : 함수 속에서 만들어진 거
#               그 함수 속에서만 사용 가능
#               그 함수 진행하는 동안만 쓰고 버릴 거(임시)
#       멤버변수(member variable) : 객체의 속성
#               member variable, attribute, field