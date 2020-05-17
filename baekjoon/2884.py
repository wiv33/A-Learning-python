import datetime

hour, minute = map(int, input().split())

split = str(datetime.timedelta(hours=hour, minutes=minute) - datetime.timedelta(hours=0, minutes=45)).split(":")
print("{} {}".format(split[0].replace("-1 day, ", ""), split[1]))

if minute >= 45:
    print(hour, minute - 45)
elif minute <= 44 and hour >= 1:
    print(hour - 1, minute + 15)
else:
    print(23, minute + 15)
