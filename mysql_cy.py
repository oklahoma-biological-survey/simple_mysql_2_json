#Simple access to MySQL with cymysql library
#Don't like that you have to create dictionary then convert to json
#Will use Django next with sqlalchamy to do Restfull Framework 
from config import host,username,password
from json_handler import handler
import cymysql, json
conn = cymysql.connect(host=host, user=username, passwd=password, db='srchdb', charset='utf8')
cur = conn.cursor()

#First query returning column names
#Added to List
columns=[]
cur.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'srchdb' AND TABLE_NAME = 'dokarrs'")
for r in cur.fetchall():
    columns.append(r[0])


#Retrieve Data
data = []
cur.execute('select * from dokarrs')
for r in cur.fetchall():
    #zip takes 2 list and creates tuples and dict to get dictionary
    data.append(dict(zip(columns,list(r))))

print json.dumps(data,default = handler,indent=4)
