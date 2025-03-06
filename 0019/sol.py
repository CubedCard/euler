from datetime import date
from dateutil.relativedelta import relativedelta

current = date(1901, 1, 1) 
end = date(2000, 12, 31) 

sundays = 0
while current < end:
    if current.strftime('%A').title() == 'Sunday':
        sundays += 1
    current = current + relativedelta(months=1)

print(sundays) 
