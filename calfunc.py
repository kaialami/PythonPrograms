
def cal(year, month):
    import calendar
    
    monthName = {1:'January-31', 2:'February-28', 3:'March-31', 
                 4:'April-30', 5:'  May-31', 6:' June-30', 
                 7:'July-31', 8:'August-31', 9:'September-30', 
                 10:'October-31', 11:'November-30', 12:'December-31'}
    
    name = monthName.get(month)
    
    print('   ' + name[:-3] + '  ' + str(year))
    print(' M  T  W  T  F  S  S ')
    print('--------------------')
    
    firstDay = calendar.weekday(year, month, 1) + 1
    
    daysInMonth = int(name[-2:])
    
    if isLeap(year) and month == 2:
        daysInMonth = daysInMonth + 1
    
    
    for row in range(6):
        for weekday in range(7):
            formula = (row * 7 + (weekday + 1 + firstDay)) - (firstDay * 2 - 1)
            
            print(monthDays(formula, daysInMonth), end = '')
        print('')
    return ''
        
    
def monthDays(formula = 0, daysInMonth = 31):
    
    ret = ''
    strFormula = str(formula)
    
    if formula < 1:
	    ret = '   '
    elif formula < 10:
	    ret = ' ' + strFormula + ' '
    elif formula >= 10 and formula <= daysInMonth:
        ret = strFormula + ' '
        
    return ret


def isLeap(year):
    myLeapYear = 2020
    if abs(myLeapYear - year) % 4 == 0 or myLeapYear == year:
        return True
    else:
        return False
        

def fullCal(year):
    print(str(cal(year, 1)), str(cal(year, 2)), str(cal(year, 3)), 
          str(cal(year, 4)), str(cal(year, 5)), str(cal(year, 6)), 
          str(cal(year, 7)), str(cal(year, 8)), str(cal(year, 9)), 
          str(cal(year, 10)), str(cal(year, 11)), str(cal(year, 12)))

fullCal(2002)
#cal(2002, 1)


#themonth = 2
#theyear = 2004

#p = calendar.TextCalendar()
#print(p.formatmonth(theyear, themonth))

#cal(theyear, themonth)





# dn = calendar.weekday(2020,10,6)
# print(dic.get(dn))
