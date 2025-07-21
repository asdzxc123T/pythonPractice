
from oracledb import connect


con = connect("ljw100/91270290@195.168.9.124:1521/xe")

sql = "select s_msrrgn_nm, avg(s_pm10 + s_pm25) "
sql += "from seoul_dust "
sql += "group by s_msrrgn_nm "
sql += "order by avg(s_pm10 + s_pm25) desc"

cur = con.cursor()
cur.execute(sql)

for mn, avg in cur:
    print(mn, avg)

cur.close()
con.close()