# OOP : 실생활 묘사
# OOD(Object Oriented Design)
#   1) 실제로 비만도 검사센터에 가서 검사받는 상황을 생각
#   2) 등장인물(프로그램에 필요한 것만 남기기)
#   3) 속성(프로그램에 필요한 것만)
#   4) 상황 진행 -> 액션
#   5) 실제 구현(최대한 실생활스럽게)

# 멤버변수 : 의사가 자기소개할 때 할만한 거
# 지역변수 : 메소드 진행 중에만 쓰고 버림
# 패러미터
# 리턴
class Doctor:
    def start(self):
        guest = self.callGuest()
        self.ask(guest)
        self.calculate(guest)
        self.tellResult(guest)

    def callGuest(self):
        return Guest()
    
    def ask(self, guest):
        guest.tell()

    def calculate(self, guest):
        guest.bmi = guest.weight / (guest.height / 100) ** 2
    
    def tellResult(self, guest):
        print("BMI : %.1f" % guest.bmi)
        print("%s씨는 " % guest.name, end="")
        if guest.bmi >= 39: print("고도 비만")
        elif guest.bmi >= 32: print("중도 비만")
        elif guest.bmi >= 30: print("경도 비만")
        elif guest.bmi >= 24: print("과체중")
        elif guest.bmi >= 10: print("정상 체중")
        else: print("저체중")

class Guest:
    def tell(self):
        self.name = input("이름 : ")
        self.height = float(input("키 : "))
        self.weight = float(input("몸무게 : "))

####################################
d = Doctor()
d.start()