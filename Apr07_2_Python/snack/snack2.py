# DTO/VO는 join시킬 것까지 생각해서
class Snack2:
    def __init__(self, no, name, exp, price, weight, c_name, c_addr, c_ceo, c_emp):
        self.no = int(no)
        self.name = name
        self.exp = exp
        self.price = int(price)
        self.weight = int(weight)
        self.c_name = c_name
        self.c_addr = c_addr
        self.c_ceo = c_ceo
        self.c_emp = int(c_emp)
