#Simple access to MySQL with MySQLdb library
#Will use Django next with sqlalchamy to do Restfull Framework 
from config import host,username,password
from json_handler import handler
from MySQLdb import connect
from MySQLdb.cursors import DictCursor
import json


def get_json(database='srchdb',table='dokarrs'):
    conn = connect(host=host, user=username, passwd=password, db=database, charset='utf8',cursorclass=DictCursor)
    cur = conn.cursor()

    #Retrieve Data
    data = []
    cur.execute('select * from %s' % (table))
    for r in cur.fetchall():
        data.append(r) 
    return json.dumps(data,default = handler,indent=4)


if __name__ == "__main__":
    
    print get_json()
