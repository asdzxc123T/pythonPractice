# V
from p02_Guest import Guest


class ConsoleScreen:
    def getGuestInfo():
        name = input("이름 : ")
        height = input("키 : ")
        weight = input("몸무게 : ")
        return Guest(name, height, weight)
    def printBMI(guest):
        print("-------------")
        print("BMI : %.1f" % guest.bmi)
        print("%s씨는 %s" % (guest.name, guest.bmiRes))