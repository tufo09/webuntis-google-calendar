import credentials as c
import webuntis
import datetime
import json


today = datetime.date.today()
monday = today - datetime.timedelta(days=today.weekday())
friday = monday + datetime.timedelta(days=4)

with webuntis.Session(
    username=c.username,
    password=c.password,
    server=c.server,
    school=c.school,
    useragent=c.useragent
).login() as s:
    table = s.my_timetable(start=monday, end=friday).to_table()
    print(table, "\n\nTable^")
    for day in table:
        print(type(day))
        print(day)
        print("\n\n\ndone\n\n\n")
"""        for period in day[1]:
            print(type(period))
            print(period)
            print("\n\n\ndone\n\n\n")"""