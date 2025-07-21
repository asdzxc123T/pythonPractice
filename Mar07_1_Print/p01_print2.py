# -*- coding:utf-8 -*-
# 해당 소스가 utf-8로 인코딩되었다고 표시

# 콘솔창에 ㅋ 출력
print("ㅋ")

# 콘솔창에 \ 출력
# print("\")?

# \n : new line : 줄만 바꾸기
#       ㅋㅋ\nㅎㅎ
#       => ㅋㅋ
#               ㅎㅎ
# \r : carriage return : 커서를 맨 앞으로
#       ㅋㅋ\rㅎㅎ
#       => ㅎㅎ
# 엔터 : \r\n

# \n만 해도 줄이 바뀜 : Python이 고급 언어
print("ㅠㅠ\r\nㅜㅜ")

# \t : tab(대충 4~5칸 띄우기)
print("ㅇㅇ\tㅈㅅ")
print("ㅇㅇㅇ\tㅈㅅ")

# \b : backspace(1byte 지우기)
# C언어 : 1글자당 1byte
# Python, Java : 1글자당 2bytes
print("ㅡㅡ\b")

# \\ : \ 출력
print("\\")

# \" : " 출력
# \' : ' 출력
print("\"이재원\"")

# abcd : PL 문법 취급
# "abcd" : 여러 글자 데이터
# 'a' : 한 글자 데이터 (Python은 여러 글자도 알아서 처리함)
print(print)
print("print")
print('zzzzzz')