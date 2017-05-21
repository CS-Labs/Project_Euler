import datetime

def problemNineteen():
    iNumSundays = 0
    for iYear in range(1901,2001):
        for iMonth in range(1,13):
            # The weekday function returns a 6 when the date provided is 6.
            if(datetime.date(iYear,iMonth,1).weekday() == 6):
                iNumSundays +=1
    return(iNumSundays)


print(problemNineteen())
