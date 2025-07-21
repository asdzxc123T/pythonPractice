class Skill:
    def __init__(self, no, name, type, costHP, costMP, mul, price):
        self.no = int(no)
        self.name = name
        self.type = int(type)
        self.costHP = int(costHP)
        self.costMP = int(costMP)
        self.mul = float(mul)
        self.price = int(price)