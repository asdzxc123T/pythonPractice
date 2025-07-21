# 컴이 1 ~ 10000 사이의 랜덤한 숫자 하나 생각해놓고
# 5912
# 뭐 : 4343
# UP
# 뭐 : 7000
# DOWN
# 뭐 : 2000000
# 뭐 : -200
# 뭐 : 5912
# 3번만에 정답

from random import randint

def getUserAns():
    userAns = int(input("뭐 : "))
    if 0 < userAns < 10001:
        return userAns
    return getUserAns()

def pickGameAns():
    return randint(1, 10000)

# 판정하고 + 게임 계속 해야 하나
# True/False
def judge(userAns, gameAns):
    if userAns > gameAns:
        print("DOWN")
    elif userAns < gameAns:
        print("UP")
    else:
        return True
    return False
#########################
ans = pickGameAns()
print("정답은 %d" % ans)
cnt = 0
while True:
    a = getUserAns()
    cnt += 1
    if judge(a, ans):
        break
print("%d번만에 정답" % cnt)