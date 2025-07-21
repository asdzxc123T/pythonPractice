# DTO, VO(Value Object)
class Snack:
    def __init__(self, name, exp, price, weight, c_name):
        self.name = name
        self.exp = exp
        self.price = int(price)
        self.weight = int(weight)
        self.c_name = c_name

    