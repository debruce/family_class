#!/usr/bin/env python3
from __future__ import print_function
from __future__ import absolute_import

from gapi.gsheet import GSheet
import numpy as np

my_sheet = GSheet('198I2bfQZlT3j43GGXU-WS7TuVlr8RekcyCJ7HcwpT_A')

# arr = np.array([[1.1, 2.2, 3.3], [4.4, 5.5, 6.6]])
# my_sheet.make_sheet('new_data', arr)

arr = np.array([[1.1, 2.2, 3.3], [4.4, 5.5, 6.6]])
my_sheet.make_sheet('float_data', arr)


arr = np.array([["hello", 'world', 'the rain']])
my_sheet.make_sheet('string_data', arr)

# my_sheet.set_sheet('data', arr)

# print(my_sheet.get_titles())
# data = my_sheet.get_sheet('data')
# print(data)