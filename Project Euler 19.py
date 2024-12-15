import datetime

today = datetime.datetime(1901,1,1)
SunCount = 0

while today <= datetime.datetime(2000,12,31):
    if today.weekday() == 6 and today.day == 1:
        SunCount += 1
    today += datetime.timedelta(1)
print(SunCount)