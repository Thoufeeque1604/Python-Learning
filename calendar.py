import datetime
#from datetime import date

date_time = "2015-08-05"
format = "%mm %dd %yyyy"
datetime_str = datetime.datetime.strptime(date_time, format)

print(datetime_str)