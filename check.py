def int_check(num):
    try:
        int(num)
        return True
    except:
        return False

def range_check(num, lower, upper):
    if num >= lower and num <= upper:
        return True
    else:
        return False