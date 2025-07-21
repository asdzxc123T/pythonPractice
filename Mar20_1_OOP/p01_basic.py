# Java : 규칙의 언어 -> 통제
# Python : 자유의 언어 -> 혼란

# 멤버xx : 객체의 xx -> 변수명.xx
# class를 만든다 : 도장/붕어빵 틀

# 1) 고양이 class
class Cat:
    # 속성 : 멤버변수
    # 무슨 의미가 -> 딱히 여기를 잘 안 씀
    name = None
    age = None

    # 액션/프로그램 상 필요한 기능 : 메소드
    def meow(self, cnt): # 첫번째 패러메터로 self를 무조건, 두번째부터는 마음대로
        print("냥" * cnt)
    
    def showInfo(self):
        print(self.name, self.age, self.weight)

##############
# 2) 고양이 object
c1 = Cat()
c1.name = "후추"
c1.age = 2
c1.weight = 1 # Python은 클래스 외부에서 멤버 추가 가능
print(c1.weight) # ???

# 원래 Python의 메소드 호출 방법 : 클래스명.메소드명(변수명, ...) - 특이
Cat.meow(c1, 3)
# Python이 버전업 되다가 다른 PL처럼 쓸 수 있게 허용해준 문법
c1.meow(3) # 호출할 때는 self는 없는셈치고

Cat.showInfo(c1)
c1.showInfo()