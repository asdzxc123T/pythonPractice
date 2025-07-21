# b = 1 : 3 - 4 - 5 - 10 - 11 - 6(끝)
# b = 0 : 3 - 4 - 5(에외발생) - 7 - 8 - 10 - 11 - 9(끝)
def getMoks(a, b):
    try:
        c = a / b
        return c
    except:
        print("?")
        return -999
    finally:
        print("ㅋㅋㅋ")

######################
a = 10
b = int(input("b : "))
c = getMoks(a, b)
print(c)

# 문제가 생겼든 말든 ㅋㅋㅋ를 출력하자
#   밖에 놓지, 굳이 finally?