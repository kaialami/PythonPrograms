def word_count(string):
    lst = string.split()
    return len(lst)


def char_count(string):
    lst = [char for char in string if char != " "]
    return len(lst)

