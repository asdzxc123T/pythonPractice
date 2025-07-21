# 컴퓨터 통신
#   실시간 Socket : 내 의지랑 상관없이
#   안 실시간 HTTP : 내가 요청 -> 응답

# DB서버 - Python 프로그램 :
#   안 실시간, 근데 HTTP 통신은 아님
#   DB메이커 다양
#       그 다양한 메이커들 간의 표준화된 통신 x
#       통신 방식이 다 다름
#   Python 입장에서 그 다양한 통신방식들 다 만들어 놓을 수가...
#   -> 없음 -> 직접 만들어야 하는데

#   Python에는 없지만, 각 DB 메이커에서 만들어준 게 있으니
#       cx_Oracle.py(구버전) : cx_Oracle.py + instantclient
#       oracledb.py : instantclient가 따로 없어도 되는데
#                   구버전 OracleDB는 지원이 안 되서, instantclient 따로 필요

# Python은 남의 거 잘 쓰자 -> 중앙제어시스템 pip
#################################
# 시작 - cmd
#       pip install oracledb
#################################

from oracledb import connect

# init_oracle_client(lib_dir="instantclient폴더경로") # 구버전 OracleDB라면 

con = connect("ljw100/91270290@195.168.9.124:1521/xe") # sqlplus로 접속할 때 쓰는 그 형식
# 아이디/비번@주소:포트/SID

print(con)
con.close()