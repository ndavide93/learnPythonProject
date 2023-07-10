from datetime import date
from datetime import datetime
import time
d1= datetime(2020, 11, 4, 14, 53, 0)
#https://docs.python.org/3/library/time.html



""" 2020/11/04 14:53:00 """
print(d1.strftime("%Y/%m/%d %H:%M:%S"))
""" 20/November/04 14:53:00 PM """
print(d1.strftime("%y/%B/%d %H:%M:%S %p"))
""" Wed, 2020 Nov 04 """
print(d1.strftime("%A ,%Y %B %d "))
""" Wednesday, 2020 November 04 """
print('Weekday: '+d1.strftime("%w"))
""" Weekday: 3 """
print(d1.strftime('Day of the Year : %j'))
""" Day of the year: 309 """
print(d1.strftime('Week number of the Year : %W'))
""" Week number of the year: 44 """