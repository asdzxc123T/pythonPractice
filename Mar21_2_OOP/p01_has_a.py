# 다른 언어] 기본형 따로, 객체 따로
# Python] 객체만 존재

# 객체간의 관계
#   Dog has a Human : 주인
#   Human has a Dog : 반려동물

# 사람
#   str 이름
#   str 집주소
#   Dog 개
####################
class Bug:
    def __init__(self, name, size):
        self.name = name
        self.size = size
    def showInfo(self):
        print(self.name, self.size)

class Dog:
    def __init__(self, name, age, bug):
        self.name = name
        self.age = age
        self.bug = bug
    def showInfo(self):
        print(self.name, self.age)
        self.bug.showInfo()

class Human:
    def __init__(self, name, addr, pet):
        self.name = name
        self.addr = addr
        self.pet = pet
    def showInfo(self):
        # print(self.name, self.addr, self.pet.name, self.pet.age)
        print(self.name, self.addr)
        self.pet.showInfo()

# 인천에 사는 홍길동
#   이 키우는 2살짜리 만득이라는 개
#       몸에 붙어있는 5mm짜리, 빈대라는 벌레
d = Dog("만득이", 2, Bug("빈대", 5))
h = Human("홍길동", "인천", d)

h.showInfo()

print("-----")
# h의 이름
print(h.name)
# h가 키우는 개 이름
print(h.pet.name)
# h가 키우는 개의 모든 정보
h.pet.showInfo()
# h가 키우는 개에 붙어있는 벌레 이름
print(h.pet.bug.name)
# h가 키우는 개에 붙어있는 벌레의 모든 정보
h.pet.bug.showInfo()