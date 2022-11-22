from datetime import datetime

date_time = datetime(2022,11,23,12,0,0)
print(date_time)
print(date_time.year)
print(date_time.month)
print(date_time.hour)
print(date_time.minute)

# current date and time

d_t = datetime.now()
print(d_t)

date_time = datetime(2022,11,23)
print(date_time)
print("----------------------------")
# change format of datetime

now = datetime.now()
new_date = now.strftime("%d %b %y %I:%M:%S")
print(now)
print(new_date)

print("-------------------------------")

new_date = now.strftime("%d %B %Y  %H:%M:%S")
print(now)
print(new_date)




