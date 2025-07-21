# 프로젝트
# 고객 : 국방부
# PM
# back-end 개발자1 : MS Azure AI
# back-end 개발자2
# back-end 개발자3
# front-end 개발자1 : React
# front-end 개발자2
# DBA1 : SQL
# DBA2
# 디자이너1 : Photo
# 디자이너2
# 실제 프로젝트에서 분업

# MVC패턴
#   파일을 나누고, 한 파일은 한 명이 책임지고 끝내자
#   한 파일은 M/V/C 셋 중에 하나만
#       Model : 비즈니스 로직(실제 계산)
#       View : 실제로 사용자 눈에 보이는
#               입력받고, 결과 출력하고
#       Controller : 흐름 제어 / 상황 판단해서 M이 필요하면 M 소환, V 필요하면 V 소환
x = int(input("x : "))
y = int(input("y : "))
print("--------")
print(x + y)