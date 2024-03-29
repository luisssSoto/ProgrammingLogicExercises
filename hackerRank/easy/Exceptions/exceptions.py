# Enter your code here. Read input from STDIN. Print output to STDOUT
#Time started 11:10

import sys
count = 0
for line in sys.stdin:
    if count > 0:
        valuesList = line.split()
        try:
            dividend = int(valuesList[0])
            divisor = int(valuesList[1])
            result = dividend // divisor
            strResult = str(result)
            sys.stdout.write(strResult)
            sys.stdout.write('\n')
        except ValueError:
            strValue = valuesList[1]
            if valuesList[0].isnumeric() is False:
                strValue = valuesList[0]
            sys.stdout.write('Error Code: invalid literal for int() with base 10: \'')
            sys.stdout.write(strValue)
            sys.stdout.write('\'')
            sys.stdout.write('\n')
        except ZeroDivisionError:
            sys.stdout.write('Error Code: integer division or modulo by zero')
            sys.stdout.write('\n')
    count += 1
        
        
