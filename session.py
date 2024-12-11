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
    print("done")
