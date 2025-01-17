import webuntis
import datetime
import json



credentials = json.load(open("credentials.json", "r"))
print(credentials["username"])


username=credentials["username"]
password=credentials["password"]
server=credentials["server"]
school=credentials["school"]
useragent=credentials["useragent"]


today = datetime.date.today()
monday = today - datetime.timedelta(days=today.weekday())
friday = monday + datetime.timedelta(days=4)

with webuntis.Session(
    username=username,
    password=password,
    server=server,
    school=school,
    useragent=useragent
).login() as s:
    table = s.my_timetable(start=monday, end=friday).to_table()
    print(table, "\n\nTable^")
    for day in table:
        print(type(day))
        print(day)
        print("\n\n\ndone\n\n\n")
