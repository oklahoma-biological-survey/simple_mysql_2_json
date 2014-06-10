#Simple access to MySQL with cymysql library
#Don't like that you have to create dictionary then convert to json
#Will use Django next with sqlalchamy to do Restfull Framework 
from config import host,username,password
from json_handler import handler
import cymysql, json


def get_json(database='srchdb',table='dokarrs'):
    conn = cymysql.connect(host=host, user=username, passwd=password, db=database, charset='utf8')
    cur = conn.cursor()

    #First query returning column names
    #Added to List
    columns=[]
    cur.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = '%s' AND TABLE_NAME = '%s'" % (database,table))
    for r in cur.fetchall():
        columns.append(r[0])


    #Retrieve Data
    data = []
    cur.execute('select * from %s' % (table))
    for r in cur.fetchall():
        #zip takes 2 list and creates tuples and dict to get dictionary
        data.append(dict(zip(columns,list(r))))
    return json.dumps(data,default = handler,indent=4)


if __name__ == "__main__":
    
    print get_json()
