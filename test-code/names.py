#!/usr/bin/env python
#-*- conding:utf-8 -*-

from name_function import get_formatted_name
print "Enter 'q' at any time to quit ."
while True:
    first = raw_input("input first name")
    if first == 'q':
        break
    last = raw_input("input last name")
    if last == 'q':
        break
    formatted_name = get_formatted_name(first,last)
    print ("\t Neatly formatted name: " + formatted_name + ' ')


