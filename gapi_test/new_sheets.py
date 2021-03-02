#!/usr/bin/env python3
from __future__ import print_function
from __future__ import absolute_import

from gapi.gsheet import GSheet
import numpy as np

# my_sheet = GSheet(openId='198I2bfQZlT3j43GGXU-WS7TuVlr8RekcyCJ7HcwpT_A')

createInfo={
    'title': 'my created sheet',
    'users': [
        {'role': 'reader', 'emailAddress': 'julia.v.bruce@gmail.com'},
        {'role': 'writer', 'emailAddress': 'david.e.bruce@gmail.com'}
    ]
}

my_sheet = GSheet(createInfo=createInfo)

# # arr = np.array([[1.1, 2.2, 3.3], [4.4, 5.5, 6.6]])
# # my_sheet.make_sheet('new_data', arr)

arr = np.array([[1.1, 2.2, 3.3], [4.4, 5.5, 6.6]])
my_sheet.make_sheet('float_data', arr)


arr = np.array([["hello", 'world', 'the rain']])
my_sheet.make_sheet('string_data', arr)

# my_sheet.set_sheet('data', arr)

titles = my_sheet.get_titles()

print(titles)

for title in titles:
    print(f"title is {title}")
    print(my_sheet.get_sheet(title))
    print()

