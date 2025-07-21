from datetime import datetime
from oracledb import connect


con = connect("ljw100/91270290@195.168.9.68:1521/xe")

sql = "select * from seoul_dust"

cur = con.cursor()
cur.execute(sql)

f = open("C:/ljw/seoulDust.csv", "w", encoding="utf-8")

for s_date, s_msrrgn_nm, s_msrste_nm, s_pm10, s_pm25, s_idex_nm in cur:
    print(s_date, s_msrrgn_nm, s_msrste_nm, s_pm10, s_pm25, s_idex_nm)
    t_date = datetime.strftime(s_date, "%Y,%m,%d,%H")
    f.write(t_date +
            "," + s_msrrgn_nm +
            "," + s_msrste_nm +
            "," + str(s_pm10) +
            "," + str(s_pm25) +
            "," + s_idex_nm + "\n"
    )

f.close()
cur.close()
con.close()