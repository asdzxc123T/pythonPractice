# 위 -> 아래, 왼쪽 -> 오른쪽 순서대로 실행되는데
# 분기점 주려면
# 조건문 : 조건 따져서 소스 흐름 제어
#       다른 언어] if문 세트, switch 세트
#       Python] if문 세트

mid = float(input("중간고사 : "))
final = float(input("기말고사 : "))
print("-----------")
avg = (mid + final) / 2
print("평균 점수 : %.1f" % avg)

# if 조건식A:
#   조건 만족 시 실행할 거
# elif 조건식B:
#   A는 땡, B는 만족시 실행할 거
# else:                     <- 조건식 안 맞으면 실행
#   모든 조건 불만족 시 실행할 거
if avg >= 90:
    print("수")
elif avg >= 80:
    print("우")
elif avg >= 70:
    print("미")
elif avg >= 60:
    print("양")
else:
    print("가")
    


if avg > 80:
    print("잘했다")
else:
    print("야")
    if avg > 70:
        print("노력 좀더 해라")

# interpreter :  한줄씩 기계어로 바꿔서 실행
# if avg > 80:
#     b = 10
# 이 시점에 어쨌든 b가 있기만 하면 무사실행
# 다른 언어가 말하는 변수의 scope 얘기는 여기서 무의미
# print(b)