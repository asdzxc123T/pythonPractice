def getBMI(h, w):
    return w / (h / 100) ** 2

name = input("이름 : ")
height = float(input("키 : "))
weight = float(input("몸무게 : "))
print("-------------")
bmi = getBMI(height, weight)
print("BMI : %.1f" % bmi)

# 소스가 길다 : 프로그램 용량이 큼 => HDD를 많이
# if bmi >= 39:
#     print("%s씨는 고도 비만" % name)
# elif bmi >= 32:
#     print("%s씨는 중도 비만" % name)
# ...

# 소스가 짧다
# result라는 변수 사용 : 램 써 => RAM을 많이
print("%s씨는 " % name, end="")
if bmi >= 39:
#   result = "고도 비만" 
    print("고도 비만")
elif bmi >= 32:
    print("중도 비만")
elif bmi >= 30:
    print("경도 비만")
elif bmi >= 24:
    print("과체중")
elif bmi >= 10:
    print("정상 체중")
else:
    print("저체중")
