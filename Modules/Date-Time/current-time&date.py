from datetime import date
import time

current_date = date.today()
print(current_date)


t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print(current_time)