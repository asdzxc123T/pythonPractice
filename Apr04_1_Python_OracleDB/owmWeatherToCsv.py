from datetime import datetime
from oracledb import connect


con = connect("ljw100/91270290@195.168.9.68:1521/xe")

sql = "select * from weather"

cur = con.cursor()
cur.execute(sql)

f = open("C:/ljw/owmWeather.csv", "w", encoding="utf-8")

for w_date, w_desc, w_temp, w_feels_like, w_humi in cur:
    t_date = datetime.strftime(w_date, "%Y,%m,%d,%H")
    f.write(t_date +
            "," + w_desc +
            "," + str(w_temp) +
            "," + str(w_feels_like) +
            "," + str(w_humi) + "\n"
    )

f.close()
cur.close()
con.close()