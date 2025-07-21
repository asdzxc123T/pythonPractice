from pymongo import ASCENDING, DESCENDING, MongoClient


con = MongoClient("195.168.9.68")
db = con.ljw

snacks = db.apr14_snack.find().sort([("s_price", DESCENDING), ("s_name", ASCENDING)])

for s in snacks:
    print(s["s_name"])
    print(s["s_price"])
    print("-----")

con.close()