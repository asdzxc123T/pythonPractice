# 1) 가위
# 2) 바위
# 3) 보
# ----------
# 뭐 : 3
# 나 : 보
# 컴 : 바위
# 승
# ----------
# 뭐 : 3
# 나 : 보
# 컴 : 보
# 무
# ----------
# 뭐 : 1
# 나 : 가위
# 컴 : 바위
# 패
# 3연승

from random import randint

def printRule(handTable):
    for i in range(len(handTable)):
        if i != 0:
            print("%d) %s" % (i, handTable[i]))
    print("-----")

def userFire():
    userHand = int(input("뭐 : "))
    if 0 < userHand < 4:
        return userHand
    return userFire()

def comFire():
    return randint(1, 3)

def printHand(userHand, comHand, handTable):
    print("나 : %s" % handTable[userHand])
    print("컴 : %s" % handTable[comHand])

# bool : True/False 2가지만 표현 가능 -> 다른 거 쓰자
# int : 42억 종류 표현가능...
# 판정하고 + 게임 계속 해야 하나
# 무 -> 0
# 패 -> -1
# 승 -> 1
def judge(userHand, comHand):
    t = userHand - comHand
    if t == 0:
        print("무")
        return 0
    elif t == 1 or t == -2:
        print("승")
        return 1
    else:
        print("패")
        return -1


#########################################
handTable = [None, "가위", "바위", "보"]
printRule(handTable)

win = 0
while True:
    userHand = userFire()
    comHand = comFire()
    printHand(userHand, comHand, handTable)

    result = judge(userHand, comHand)
    if result == -1:
        print("%d연승" % win)
        break
    win += result