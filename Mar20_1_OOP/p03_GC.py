# 1 + 2 => 멤버 변수를 따로 안 하고, 생성자에서 결정짓는 형태로 많이들 작업
class Pen:
    # 1) 어차피 외부에서 추가할 수 있음 -> 여기다 쓰는 게 무슨...
    # name = None
    # color = None
    # price = None

    # 2) Python은 overloading이 불가능하니 생성자는 하나만 가능
    # -> 펜 만들려면 이름, 색깔, 가격 써야만 함
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    def __del__(self):
        print("ㅃㅇ")

    def showInfo(self):
        print(self.name, self.color, self.price)
########################################
# Garbage Collection
#   stack : 프로그램 종료 시 자동정리
#   heap : 자동정리 x, 개발자가 직접 정리해야 
#   GC : heap 영역을 자동으로 정리
#       그 자동 발동시점
#           그 번지를 더이상 사용하지 못하게 되면
#           그 번지를 가리키던 변수가 더이상 안 가리키게 되면
#   => Python은 정리는 어떻게든 다 됨
p = Pen("모나미153", "빨강", 500)
p.showInfo()

p2 = Pen("모나미153", "파랑", 1000)
p2.showInfo()

# p랑 속성이 같은 펜 하나 더 - x
# p를 p3로도 부르게 하자
p3 = p
p3.showInfo()

p.price = 300
p3.showInfo()

p = None
p3 = None
print("ㅋㅋㅋㅋㅋㅋㅋㅋ")