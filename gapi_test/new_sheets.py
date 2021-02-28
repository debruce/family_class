#!/usr/bin/env python3

from __future__ import print_function
import sys
from gapi import GSheet

my_sheet = GSheet('198I2bfQZlT3j43GGXU-WS7TuVlr8RekcyCJ7HcwpT_A')

data = [
    [ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]
]

my_sheet.set_sheet('data', data)


# my_sheet.set_sheet('new_data', data)