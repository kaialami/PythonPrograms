# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 21:11:40 2020

@author: Kai
"""

# import myClass type
import myClass

# create an INSTANCE of myClass and call it o (o for object)
o = myClass.myClass

# call the Object's "sayHello" method
hello = o.sayHello()

# call the Object's "upperCaseName" method
myUpper = o.upperCaseName('asdf asdfa asdf')

print(hello)
print(myUpper.lower())

print(o)

# i have another object called cheese
# cheese.getCheeseByUpperCaseName(o.upperCaseName('blue cheese'))




import time

# seconds since Jan 1st 1970 00:00:00
1601862144
print (time.time())