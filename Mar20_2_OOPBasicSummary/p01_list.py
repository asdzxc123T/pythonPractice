class Student:
    def __init__(self, name, kor, eng, mat):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.mat = mat
    def showInfo(self):
        print(self.name, self.kor, self.eng, self.mat)
# 2차원, 3차원 list -> 유지보수가...
# 객체 list
#   소스 가독성
#   메소드 사용 가능
#   정렬 편해짐
s = Student("홍길동", 100, 50, 50)
score = [s,
         Student("김길동", 30, 50, 60),
         Student("이길동", 70, 50, 40),
         Student("최길동", 80, 80, 20)
         ]
# 2번 학생 국어 점수
print(score[1].kor)
# 3번 학생 전체 정보
score[2].showInfo()
print("-----")

# 정식
# def totalScore(s):
#     return s.kor + s.eng + s.mat
# print(totalScore(score[1]))

# lambda 함수
# print((lambda s: s.kor + s.eng + s.mat)(score[1]))

# 성적순 정렬(list에 있는 학생 하나씩 빼서 자동으로 해줌)
# score.sort(key=lambda s: s.kor + s.eng + s.mat) # 오름차순
score.sort(key=lambda s: s.kor + s.eng + s.mat, reverse=True) # 내림차순

# 이름 가나다 역순
score.sort(key=lambda s:s.name, reverse=True)

for s in score:
    s.showInfo()