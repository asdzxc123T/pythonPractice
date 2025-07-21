# 콘솔출력 : 중간 테스트

# 형식 지정해서 이쁘게 출력?
#   1) 콘솔출력만 해당 x
#   2) 모든 PL들 다 

# %d : 정수데이터 들어갈 자리
# %05d : 0 채워서 5자리로
age = 30
print(age)
print("나이 : %d살" % age)
print("나이 : %05d살" % age)

# %f : 실수데이터 들어갈 자리
# %.3f : 소수점 이하 3자리(반올림)
eye = 1.2347
print(eye)
print("시력 : %f" % eye)
print("시력 : %.3f" % eye)

# %s : 글자데이터 들어갈 자리
addr = "분당"
print(addr)
print("집 : %s" % addr)

# %b : 논리형데이터 들어갈 자리
# 맞기는 한데, Python은 삭제
# hungry = False
# print(hungry)
# print("배고픈가 : %b" % hungry)

# %% : % 출력
humi = 30.123123
print("습도 : %.1f%%" % humi)

temp = 10
print("기온은 %d도고, 습도는 %.1f%%다." % (temp, humi))

today = "기온은 %d도고, 습도는 %.1f%%다." % (temp, humi)
print(today)