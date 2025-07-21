# 어벤져스
#   본명
#   나이
#   공격하기
#   출력하기
class Avengers:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def attack(self):
        print("공격")

    def printInfo(self):
        print(self.name)
        print(self.age)
# 사람
#   이름
#   주소
#   밥먹기
#   출력하기
class Human:
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr
    
    def eat(self):
        print("밥먹기")

    def printInfo(self):
        print(self.name)
        print(self.addr)

# 로부터 상속받는 아이언맨
# Ironman is a Avengers
# Ironman is a Human
# 다중상속 : 여러클래스로부터 상속
#   대부분의 PL] 안 됨 : 멤버 이름이 같으면?
#   Python] 가능
#           멤버 이름 같으면 -> 먼저 쓴 거
#               : 이게 해결책인가(다중상속을 굳이 왜 받나)
class Ironman(Avengers, Human):
    def __init__(self, name, age, addr):
        # Avengers.__init__(self, name, age)
        # Human.__init__(self, name, addr)

        # super() : 먼저 쓴 거(Avengers)
        super().__init__(name, age)
        self.addr = addr

    def printInfo(self):
        # Avengers.printInfo(self)
        # Human.printInfo(self)
        super().printInfo()
        print(self.addr)

i = Ironman("Tony", 40, "AAA")
i.printInfo()
i.attack()
i.eat()