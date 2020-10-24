
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
    import calendar

    monthName = {1:'January-31', 2:'February-28', 3:'March-31', 
                 4:'April-30', 5:'  May-31', 6:' June-30', 
                 7:'July-31', 8:'August-31', 9:'September-30', 
                 10:'October-31', 11:'November-30', 12:'December-31'}
    
    yearName = ' ' + str(year)
    
    feb = 28
    if isLeap(year):
        feb = 29
    
    dict1 = {}
    dict2 = {}
    dict3 = {}
    dict4 = {}
    dict5 = {}
    dict6 = {}
    dict7 = {}
    dict8 = {}
    dict9 = {}
    dict10 = {}
    dict11 = {}
    dict12 = {}
    
    for monthNum in range(1, 13):
        firstDay = calendar.weekday(year, monthNum, 1) + 1
        daysList = []   
        for row in range(6):
            for weekday in range(7):
                formula = (row * 7 + (weekday + 1 + firstDay)) - (firstDay * 2 - 1)
                daysList.append(formula)
        for x, y in zip(range(len(daysList)), daysList):
            if monthNum == 1:
                dict1[x] = str(y)
            if monthNum == 2:
                dict2[x] = str(y)
            if monthNum == 3:
                dict3[x] = str(y)
            if monthNum == 4:
                dict4[x] = str(y)
            if monthNum == 5:
                dict5[x] = str(y)
            if monthNum == 6:
                dict6[x] = str(y)
            if monthNum == 7:
                dict7[x] = str(y)
            if monthNum == 8:
                dict8[x] = str(y)
            if monthNum == 9:
                dict9[x] = str(y)
            if monthNum == 10:
                dict10[x] = str(y)
            if monthNum == 11:
                dict11[x] = str(y)
            if monthNum == 12:
                dict12[x] = str(y)

    # 1/4
    print('\n                              Calendar of' + yearName + '\n')
    print('     ' + monthName.get(1)[:-3] + yearName + '               ' + monthName.get(2)[:-3] + yearName + '                 ' + monthName.get(3)[:-3] + yearName)
    print(' M  T  W  T  F  S  S         M  T  W  T  F  S  S         M  T  W  T  F  S  S')
    print('---------------------       ---------------------       ---------------------')

    rowDict = {}
    for row in range(6):
        rowDict = {}
        rowBegin = row * 7
        rowEnd = rowBegin + 7
        for i, j in zip(range(rowBegin, rowEnd), range(7)):
            if i not in dict1.keys():
                dict1[i] = '0'
            value1 = dict1.get(i)
            if int(value1) > 31:
                value1 = '0'
            rowDict[j] = value1
        for i, j in zip(range(rowBegin, rowEnd), range(7, 14)):
            if i not in dict2.keys():
                dict2[i] = '0'
            value2 = dict2.get(i)
            if int(value2) > feb:
                value2 = '0'
            rowDict[j] = value2
        for i, j in zip(range(rowBegin, rowEnd), range(14, 21)):
            if i not in dict3.keys():
                dict3[i] = '0'
            value3 = dict3.get(i)
            if int(value3) > 31:
                value3 = '0'
            rowDict[j] = value3
        for keys, values in rowDict.items():
            if int(values) < 1:
                if (keys + 1) % 7 == 0:
                    print('   ', end = '       ')
                else:
                    print('   ', end = '')
            elif int(values) > 9:
                if (keys + 1) % 7 == 0:
                    print(values + ' ', end = '       ')
                else:
                    print(values + ' ', end = '')
            elif (keys + 1) % 7 == 0:
                print(' ' + values + ' ', end = '       ')
            else:
                print(' ' + values + ' ', end = '')
        print('\n', end = '')      
    
    # 2/4
    print('      ' + monthName.get(4)[:-3] + yearName + '                 ' + monthName.get(5)[:-3] + yearName + '                   ' + monthName.get(6)[:-3] + yearName)
    print(' M  T  W  T  F  S  S         M  T  W  T  F  S  S         M  T  W  T  F  S  S')
    print('---------------------       ---------------------       ---------------------')

    rowDict = {}
    for row in range(6):
        rowDict = {}
        rowBegin = row * 7
        rowEnd = rowBegin + 7
        for i, j in zip(range(rowBegin, rowEnd), range(7)):
            if i not in dict4.keys():
                dict4[i] = '0'
            value1 = dict4.get(i)
            if int(value1) > 30:
                value1 = '0'
            rowDict[j] = value1
        for i, j in zip(range(rowBegin, rowEnd), range(7, 14)):
            if i not in dict5.keys():
                dict5[i] = '0'
            value2 = dict5.get(i)
            if int(value2) > 31:
                value2 = '0'
            rowDict[j] = value2
        for i, j in zip(range(rowBegin, rowEnd), range(14, 21)):
            if i not in dict6.keys():
                dict6[i] = '0'
            value3 = dict6.get(i)
            if int(value3) > 30:
                value3 = '0'
            rowDict[j] = value3
        for keys, values in rowDict.items():
            if int(values) < 1:
                if (keys + 1) % 7 == 0:
                    print('   ', end = '       ')
                else:
                    print('   ', end = '')
            elif int(values) > 9:
                if (keys + 1) % 7 == 0:
                    print(values + ' ', end = '       ')
                else:
                    print(values + ' ', end = '')
            elif (keys + 1) % 7 == 0:
                print(' ' + values + ' ', end = '       ')
            else:
                print(' ' + values + ' ', end = '')
        print('\n', end = '')

    # 3/4
    print('      ' + monthName.get(7)[:-3] + yearName + '                  ' + monthName.get(8)[:-3] + yearName + '                ' + monthName.get(9)[:-3] + yearName)
    print(' M  T  W  T  F  S  S         M  T  W  T  F  S  S         M  T  W  T  F  S  S')
    print('---------------------       ---------------------       ---------------------')
   
    rowDict = {}
    for row in range(6):
        rowDict = {}
        rowBegin = row * 7
        rowEnd = rowBegin + 7
        for i, j in zip(range(rowBegin, rowEnd), range(7)):
            if i not in dict7.keys():
                dict7[i] = '0'
            value1 = dict7.get(i)
            if int(value1) > 31:
                value1 = '0'
            rowDict[j] = value1
        for i, j in zip(range(rowBegin, rowEnd), range(7, 14)):
            if i not in dict8.keys():
                dict8[i] = '0'
            value2 = dict8.get(i)
            if int(value2) > 31:
                value2 = '0'
            rowDict[j] = value2
        for i, j in zip(range(rowBegin, rowEnd), range(14, 21)):
            if i not in dict9.keys():
                dict9[i] = '0'
            value3 = dict9.get(i)
            if int(value3) > 30:
                value3 = '0'
            rowDict[j] = value3
        for keys, values in rowDict.items():
            if int(values) < 1:
                if (keys + 1) % 7 == 0:
                    print('   ', end = '       ')
                else:
                    print('   ', end = '')
            elif int(values) > 9:
                if (keys + 1) % 7 == 0:
                    print(values + ' ', end = '       ')
                else:
                    print(values + ' ', end = '')
            elif (keys + 1) % 7 == 0:
                print(' ' + values + ' ', end = '       ')
            else:
                print(' ' + values + ' ', end = '')
        print('\n', end = '')

    # 4/4
    print('     ' + monthName.get(10)[:-3] + yearName + '                ' + monthName.get(11)[:-3] + yearName + '               ' + monthName.get(12)[:-3] + yearName)
    print(' M  T  W  T  F  S  S         M  T  W  T  F  S  S         M  T  W  T  F  S  S')
    print('---------------------       ---------------------       ---------------------')
  
    rowDict = {}
    for row in range(6):
        rowDict = {}
        rowBegin = row * 7
        rowEnd = rowBegin + 7
        for i, j in zip(range(rowBegin, rowEnd), range(7)):
            if i not in dict10.keys():
                dict10[i] = '0'
            value1 = dict10.get(i)
            if int(value1) > 31:
                value1 = '0'
            rowDict[j] = value1
        for i, j in zip(range(rowBegin, rowEnd), range(7, 14)):
            if i not in dict11.keys():
                dict11[i] = '0'
            value2 = dict11.get(i)
            if int(value2) > 30:
                value2 = '0'
            rowDict[j] = value2
        for i, j in zip(range(rowBegin, rowEnd), range(14, 21)):
            if i not in dict12.keys():
                dict12[i] = '0'
            value3 = dict12.get(i)
            if int(value3) > 31:
                value3 = '0'
            rowDict[j] = value3
        for keys, values in rowDict.items():
            if int(values) < 1:
                if (keys + 1) % 7 == 0:
                    print('   ', end = '       ')
                else:
                    print('   ', end = '')
            elif int(values) > 9:
                if (keys + 1) % 7 == 0:
                    print(values + ' ', end = '       ')
                else:
                    print(values + ' ', end = '')
            elif (keys + 1) % 7 == 0:
                print(' ' + values + ' ', end = '       ')
            else:
                print(' ' + values + ' ', end = '')
        print('\n', end = '')

    return ''


fullCal(2020)



# themonth = 2
# theyear = 2004

# p = calendar.TextCalendar()
# print(p.formatmonth(theyear, themonth))

# cal(theyear, themonth)





# dn = calendar.weekday(2020,10,6)
# print(dic.get(dn))
