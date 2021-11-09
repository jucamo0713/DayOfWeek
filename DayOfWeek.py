import datetime

print("let's calculate the day of week of the Date (since 1900):")
print('')
tableOfMonths=[0,3,3,6,1,4,6,2,5,0,3,5]
tableOfDaysInAMonth=[31,28,31,30,31,30,31,31,30,31,30,31]
tableOfDaysInWeek=['Sunday','Monday','Tuesday','Thursday','Wednesday','Friday','Saturday']
year=0
day=0
month=0
i=0
def IsALeapYear():
    return (year%4 == 0 and (year%100 != 0 or year%400 == 0))

def DateIsValid():
    return (year<1900 and day <1 and month<1) or (day>((tableOfDaysInAMonth[month-1])if not(IsALeapYear() and month==2) else 29))
def ValueOfYear():
    init=year-1900
    leaps=((year//4)-(year//100)+(year//400))-460
    return (init+leaps)%7
question = True
while question:
    while DateIsValid():
        if i>0:
            print('insert a valid date')
            print('')
        try:
            day = int(input('insert the day of the month: \n'))
            print('')
            month = int(input('insert the number of the month: \n'))
            print('')
            year = int(input('insert Year: \n'))
            print('')
        except:
            year=0
            day=0
            month=0
        i+=1
    else:
        if IsALeapYear():
            sum = day + tableOfMonths[month-1]+(0 if month>2 else -1)+ ValueOfYear()
        else:
            sum = day + tableOfMonths[month-1]+ ValueOfYear()
        dateInput= datetime.datetime(year, month, day)
        print(dateInput.strftime("%B")+" "+str(day)+", "+str(year)+" was a "+tableOfDaysInWeek[sum%7])
        print('You want to repeat the process')
        question=bool(int(input('1 for yes or 0 for not: \n')))
        year=0
        day=0
        month=0
else:
    print('Thanks for use this program')



