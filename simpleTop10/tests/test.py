#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Six
#defines the old array list, the list of lists
oldArr = ([1,2,3,4],['a','b','c','d'],['A','B','C','D'])
#takes the size of the old array list
size = len(oldArr[1])
#defines the new list we will be adding information into
newArr = []
#append blank new arrays to the old array
for i in range(size):
    newArr.append([])

#loops through to add elements to this new array
for i,val in enumerate(oldArr):
    for index,value in enumerate(val):
        newArr[index].append(value)

#tuple is ordered and unchangeable
newTuple = tuple(newArr)
print (newTuple)

