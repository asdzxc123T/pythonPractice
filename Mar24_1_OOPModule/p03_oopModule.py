
class BoardMarker:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def show(self):
        print(self.name)
        print(self.color)

if __name__=="__main__":
    # import : p04_oopModule.py의 소스가 오는 셈
    from p04_oopModule import Book
    b = Book("점프 투 파이썬", 30000)
    b.show()