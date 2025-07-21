
class Book:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def show(self):
        print(self.name)
        print(self.price)


# 여기서 실행했을 때는 실행
# import당했을 때는 실행 x
if __name__=="__main__":
    # Python은 import를 무조건 먼저 해야 x
    from p03_oopModule import BoardMarker
    bm = BoardMarker("aa", "black")
    bm.show()