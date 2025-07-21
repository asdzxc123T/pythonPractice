# 쇼핑몰
# 상속
#   Pen is a Product
#   -> OOP가 말하는 상속 사용 가능
#   부모 클래스의 멤버들(멤버변수, 메소드)이 자식클래스에도 전달됨
#   + 기능 추가
########
# 보통 상속을 쓰면, 추가되기 마련
# 다른언어] 생성자는 상속을 안 시킴
# Python] 보통 생성자에서 멤버변수를 정하는데, 상속을 안 시키면
#           -> 멤버변수를 상속 안 시키는?
#           -> 생성자도 상속됨

# Product : 상위클래스, 부모클래스
# Pen : 하위클래스, 자식클래스

# self : 자신
# super : 자신의 부모 클래스

class Product: # object로부터 상속을 받음, class Product(object)
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def showInfo(self):
        print(self.name, self.price)

class Pen(Product): # Product로부터 상속받은 Pen
    # overriding이 아님
    def __init__(self, name, price, color):
        super().__init__(name, price) # Product의 __init__ 호출 -> 이름, 가격 세팅
        self.color = color
    # showInfo를 상속 받았는데, 이름/가격 출력 기능만
    # 색깔도 출력되게
    # overriding : 상속받은 메소드 기능 바꾸기 or 추가
    #              바꾸기보다는 추가형태로 많이
    def showInfo(self):
        super().showInfo() # Product의 showInfo 호출 -> 이름, 가격 출력
        print(self.color)

p = Pen("모나미153", 500, "빨강")
p.showInfo()

# 품명이 조던123, 가격이 10만원, 사이즈가 250인 신발
class Shoes(Product):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size
    def showInfo(self):
        super().showInfo()
        print(self.size)
s = Shoes("조던123", 100000, 250)
s.showInfo()

# 품명이 매직스테이션123, 가격이 200만원,
# cpu i5-1234, ram 16gb, hdd 500gb 컴
class Computer(Product):
    def __init__(self, name, price, cpu, ram, hdd):
        super().__init__(name, price)
        self.cpu = cpu
        self.ram = ram
        self.hdd = hdd
    def showInfo(self):
        super().showInfo()
        print(self.cpu, self.ram, self.hdd)
c = Computer("매직스테이션123", 2000000, "i5-1234", 16, 500)
c.showInfo()

# 품명이 그램123, 가격이 250만원,
# cpu i7-4567, ram 32gb, hdd 250gb,
# 무게가 3kg 노트북

# Product is a object
# Computer is a Product
# Notebook is a Computer

# Product로부터 상속받는 Computer로부터 상속받는 Notebook
# 다단상속
class Laptop(Computer):
    def __init__(self, name, price, cpu, ram, hdd, weight):
        super().__init__(name, price, cpu, ram, hdd)
        self.weight = weight
    def showInfo(self):
        super().showInfo()
        print(self.weight)
n = Laptop("그램123", 2500000, "i7-4567", 32, 250, 3)
n.showInfo()