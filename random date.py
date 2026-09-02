import random 
import time 
def getrandomdate(StartDate, Enddate):
    print("Generating random date between", StartDate, "and", Enddate)
    randomGenerator = random.random()
    dateformat =  '%d/%m/%Y'
    startTime = time.mktime(time.strptime(StartDate, dateformat))
    endTime = time.mktime(time.strptime(Enddate, dateformat))
    randomTime = startTime + randomGenerator * (endTime - startTime)
    randomDate = time.strftime(dateformat, time.localtime(randomTime))
    return randomDate
print("Random date = ", getrandomdate("01/01/1401", "12/12/3000"))