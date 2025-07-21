# int, float, str, bool, ...
#   변수1 : 데이터1
# Collection
#   변수1 : 데이터n

# 어떤 언어든지 Collection이라 하면
#   List 계열 - P] list
#   Set 계열 - P] set
#   Map 계열 - P] dictionary
# C, Java의 배열이 아님 : 만들면 수정 x

# Python은 str을 list처럼 사용
s = "Hello"
print(s[2])
print(len(s))
print(s[::-1])

# list : 평범
# 영어점수가 80, 30, 54, 12, ...
eng = [80, 30, 54, 12, 10, 60, 70, 95, 100, 40]
print(eng)
print(type(eng))
print(len(eng))     # 내용물 갯수
print(eng[1])       # 1번 데이터(0번부터 셈)
print(eng.index(30)) # 30은 몇번 데이터? (1 출력, 앞에서부터 세서 맨 처음 찾아낸 것을 출력함)
print(eng[2:5])     # 2 ~ (5-1)번 데이터
print(eng[3:9:2])   # 3 ~ (9-1)번 2칸씩
print(eng[:9:2])    # 0 ~ (9-1)번 2칸씩, 안 쓰면 적당히 알아서
print(eng[::2])     # 0 ~ (10-1)번 2칸씩
print(eng[::-1])    # (10-1) ~ 0번 역순

print(eng)
eng.append(99)      # 뒤에 99 추가
eng.insert(2, 88)   # 2번 자리에 88 추가
eng[1] = 0          # 1번 데이터를 0으로 수정
del eng[0]          # 0번 데이터 삭제
print(eng)

# set : 중복 x, 순서?
#       => 순서? 때문에 사용하기가
#       => 중복x가 뭔가 있는
# 수학점수
mat = {100, 80, 50, 80, 70, 100, 50, 90}
print(mat)
print(type(mat))

# dict : 순서 개념 x, 키-값 쌍
student = {"반장":"홍길동", "부반장":"김길동"}
print(student)
print(type(student))
print(student["반장"])