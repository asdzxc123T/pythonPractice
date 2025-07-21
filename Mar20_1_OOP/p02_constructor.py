# constructor(생성자)
#   객체가 만들어질 때 뭔가 작업을
#   메소드

# destructor(소멸자)
#   객체가 없어질 때 뭔가 작업을 

class Phone:
    name = None
    maker = None
    price = None

    # default constructor(기본 생성자)
    #   클래스에 생성자 작업을 안 해놓으면 
    #   Python이 자동으로 만들어서 씀
    def __init__(self): # 객체가 만들어질 때 호출됨
        print("핸드폰 입고됨")

    def __del__(self): # 없어짐
        print("없어짐")

    def showInfo(self):
        print(self.name, self.maker, self.price)

class Computer:
    cpu = None
    ram = None
    hdd = None

    # Python은 overloading이 불가능
    # 생성자 여러개 만들어놓고 필요한 거 갖다쓰기가 불가능
    # => 생성자는 하나만 가능
    def __init__(self, cpu, ram, hdd):
        self.cpu = cpu
        self.ram = ram
        self.hdd = hdd

    def showInfo(self):
        print(self.cpu, self.ram, self.hdd)


######################################
c = Computer("i5-1234", 16, 500)
c.showInfo()

# 객체 생성
# 변수명 = 클래스명()
#           생성자 호출하는 셈
p1 = Phone()
p1.name = "S24"
p1.maker = "Samsung"
p1.price = 1000000
p1.showInfo()