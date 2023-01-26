import sqlite3

conn=sqlite3.connect('db.sqlite3')
cursor=conn.cursor()
query="""CREATE TABLE IF NOT EXISTS BASE(district TEXT,otg TEXT,np TEXT,street TEXT,buildings TEXT," \
"poweroff_type TEXT,poweroff_cause TEXT,poweroff_time TEXT,poweron_time TEXT)"""
'''query="SELECT * FROM BASE"
cursor = conn.cursor()
cursor.execute(query)
res = cursor.fetchall()

print(res)
for r in res:
    print("District:", r[0])
    print("otg:", r[1])
    print("city:", r[2])
    print("street:", r[3])
    print("house:", r[4])
    print("type_off:", r[5])
    print("cause:", r[6])
    print("time_off:", r[7])
    print("time_on:", r[8])
    print(res)
#headers=['District','Otg','City',"Street","House","type_off","Cause","Time_off","Time_on"]
#headers.extend(data[0]['teches'].keys())


conn.close()'''
