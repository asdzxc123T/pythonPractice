#   DB는 서버 -> 10TB 저장 가능
#   실수로 삭제 불가
#   분석 기능도 있음(서버라서 PC에서 분석하는 것보다 빠름)

# 1) .csv/.txt는 무쓸모
#       데이터(10TB) -> PC에서 분석 -> 결과 : 불가능
#       데이터(10TB) -> Hadoop(서버급 컴 여러대로 병렬 전처리)(10MB) -> PC에서 분석 -> 결과 : 가능
#       Hadoop이 DB 연동 불가, 파일 처리만 가능 -> .csv/.txt 필요

# 2) Python BD분석 라이브러리(NumPy, Pandas)가 무쓸모
#       DB가 AI 쪽은 부실 -> Python의 AI 라이브러리
#       그 AI 라이브러리가 NumPy, Pandas를 씀