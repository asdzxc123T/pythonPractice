# Java가 1991년 : 2000년대 고려를 안 하던
#               두자리만 쓰면 90
# Python : 2000년대를 고려함

# 프로그래밍 언어의 어떤 기능이 만들어짐 : 2025/3/25
# 세월이 가면, 기술이 발전하면 -> 그 기능이 안 맞게 됨
# 그 기능을 업그레이드 or 삭제하고 다시 만들게 됨

# deprecated : 유예기간
#       현재 버전에서 사용은 가능
#       업그레이드 or 새로 만들 or 대체품 출시할 거니까
#       다음 버전에서 없어져도 토달지 마라

# 패키지명 : x
# 모듈명 : datetime.py
# 클래스명 : datetime
# today의 정체? : static 메소드
from datetime import datetime
from time import strftime

now = datetime.today() # 현재 시간 날짜
print(now)

print(now.year) # 연도만
print(now.month)
print(now.day)

# 특정 시간 날짜
d = datetime(2000,1,1)
print(d)

d2 = "1999,12,31"
# datetime객체로
d2 = d2.split(",")
d2 = datetime(int(d2[0]), int(d2[1]), int(d2[2]))
print(d2)

# 패턴 확인
# help(strftime)

# 날짜 패턴 쓰는 스타일
d3 = "2002/02/02"
d3 = datetime.strptime(d3, "%Y/%m/%d")
print(d3, type(d3))

d4 = datetime.today()
# 2025.03.25 형태로 나오게
d4 = d4.strftime("%Y.%m.%d")
print(d4, type(d4))

# 1) 올해는 2025년 x -> 올해 연도값을 구해야
# 2) 날짜라서 날짜 x -> 날짜로서 의미가 있으면 날짜

# 생일(yyyy-MM-dd) :
# --------------------
# 한국 나이 출력
birth = "2001-09-02"
# birth = datetime.strptime(birth, "%Y-%m-%d")
# print(now.year - birth.year + 1)
birth = int(birth[:4])
print(now.year - birth + 1)

# 무슨 요일에 태어났나
birth = "2001/09/02"
birth = datetime.strptime(birth, "%Y/%m/%d")
# w = birth.weekday()
# weekDay = ["월", "화", "수", "목", "금", "토", "일"]
# print(weekDay[w] + "요일")

birth = datetime.strftime(birth, "%A")
print(birth)