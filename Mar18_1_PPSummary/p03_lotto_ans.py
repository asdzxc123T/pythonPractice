# 로또 번호 자동 생성기
# 1 ~ 45 랜덤한 숫자 6개(중복 없어야)
# 컬렉션 중에 set 쓰지 말고, list만 쓰는 쪽으로

# 첫번째 숫자 : 그냥 뽑
# 두번째 숫자 :
#       일단 뽑고 -> 첫번째 숫자와 비교해서 같으면 다시 뽑자
# 세번째 숫자 :
#       일단 뽑고 -> 첫번째/두번째 숫자와 비교해서 같으면 다시 뽑자
# ...

from random import randint

def pick(lotto):
    ball = randint(1, 45)
    for i in lotto:
        if i == ball:
            return pick(lotto)
    return ball

lotto = []
for i in range(6):
    lotto.append(pick(lotto))
print(lotto)
