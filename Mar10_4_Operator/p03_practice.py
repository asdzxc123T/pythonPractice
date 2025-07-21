pay = int(input("구매한 물건가 : "))
money = int(input("낸 돈 : "))
print("---------------")
res = money - pay
print("거스름돈 : %d" % res)
print("5만원 : %d개" % (res // 50000))
res %= 50000
print("1만원 : %d개" % (res // 10000))
res %= 10000
print("5천원 : %d개" % (res // 5000))
res %= 5000
print("1천원 : %d개" % (res // 1000))
res %= 1000
print("5백원 : %d개" % (res // 500))
res %= 500
print("1백원 : %d개" % (res // 100))
res %= 100
print("50원 : %d개" % (res // 50))
res %= 50
print("10원 : %d개" % (res // 10))
res %= 10
print("10원 이하 : %d원" % res)