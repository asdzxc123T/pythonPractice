# 반복문 제어
#   break : 반복문 종료
#   continue : 턴 종료
from random import randint


for i in range(10):
    if i == 3:
        # break
        continue # 남은 8번줄 안 하고 바로 4번줄로
    print(i)
print("-----")

# while True: 형태로 해서 무한루프 돌리고
# 프로그램 특성상 자연스럽게 if문은 존재할텐데
# break할 조건 추가

# 아무 숫자나 입력받아서 출력
# 10이라고 쓰면 그만
while True: # 조건은 무조건 맞다 -> 무한루프
    menu = int(input("숫자 입력 : "))
    if menu == 1:
        print("메뉴를 등록...")
    elif menu == 2:
        print("메뉴 조회...")
    elif menu == 10:
        break
print("-----")

# 1 ~ 5 사이의 랜덤한 정수 4 나올 때까지 출력
while True:
    a = randint(1, 5)
    print(a)
    if (a == 4):
        break