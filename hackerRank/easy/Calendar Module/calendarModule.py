#time started 12:30
import calendar
print(dir(calendar))
calendario = calendar.TextCalendar(firstweekday=0).formatyear(2015)
print(calendario)
print(type(calendario))

import sys

# for line in sys.stdin:
# date = [04, 05, 2024]
# for character in calendario:
#     print(character)

# calendario2 = calendar.Calendar.firstweekday
# print(calendario2.itermont)

class calendar.Calendar(firstweekday=0)

    