import inspect
from pymongo import Connection
from apache_log_parser import ApacheLogFile

def props(obj): 
    pr = {}
    for name in dir(obj):
        value = getattr(obj, name)
        if not name.startswith('__') and not inspect.ismethod(value):
            pr[name] = value
    return pr
  
connection = Connection('localhost', 27017)
db = connection.mydb
collection = db.logdata
alf = ApacheLogFile('example.log')
for log_line in alf:
    collection.insert(props(log_line))
alf.close()