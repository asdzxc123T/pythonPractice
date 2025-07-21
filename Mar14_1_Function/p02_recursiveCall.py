# 함수 : 소스 정리 -> 가독성 -> 사람 관점
# 컴 관점 : 느려지기만 할 뿐
# 함수 호출 : JUMP 연산 (4 -> 5 -> 6 -jump-> 2)
#             물리적으로 이동 -> 시간이 걸림

# recursive call
#   계산용 x -> 반복문
#   사용자로부터 원하는 입력 받을 때까지 반복

def getHeight():
    h = float(input("키 : "))
    if h > 3:
        return getHeight()
    return h

name = input("이름 : ")
height = getHeight()
weight = float(input("몸무게 : "))
print("-------------")
bmi = weight / height ** 2
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
