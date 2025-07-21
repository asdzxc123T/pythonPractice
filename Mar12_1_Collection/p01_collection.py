# list : 주력
a = [1, 1, 1, 1, 2, 3, 4, 6]
# set : 중복 x, 순서? => 잘 안 쓰게 됨
# a = set(a) # list -> set
# a = list(a) # set -> list
a = list(set(a))
print(a)

# JSON과 생김새가 유사
# dict : 키-값, 순서x
student = {"홍길동" : [100, 90, 80],
           "김길동" : [50, 30, 20],
           "이길동" : [30, 10, 0]}
print(student["김길동"])

# 홍길동 국어 점수 출력
print(student["홍길동"][0])
# 유지보수의 시대, Python은 객체지향언어
# 이렇게는 하지 말자

print(list(student.keys())) # 키만 추출해서 출력

# 학생 중에 최길동이 있나
print("최길동" in student)