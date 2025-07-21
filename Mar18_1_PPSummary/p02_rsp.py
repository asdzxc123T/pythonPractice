from random import randint

def comAns():
    return randint(0, 2)

def userAns():
    a = int(input("뭐 : "))
    if 0 < a < 4:
        return a
    return userAns()

def game(rsp):
    winCnt = 0
    while True:
        com = comAns()
        a = userAns() - 1
        print("나 : %s" % rsp[a])
        print("컴 : %s" % rsp[com])
        t = a - com
        if t == 0:
            print("무")
        elif t == 1 or t == -2:
            print("승")
            winCnt += 1
        else:
            print("패")
            return winCnt
        print("-----")
    
rsp = ["가위", "바위", "보"]
for i in range(len(rsp)):
    print("%d) %s" % (i + 1, rsp[i]))
print("-----")

print("%d연승" % game(rsp))