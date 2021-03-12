#!/usr/bin/env python3
from __future__ import print_function
from __future__ import absolute_import

from gapi.gsheet import GSheet

GSheet.show()

my_sheet = GSheet(openTitle='my created sheet')

titles = my_sheet.get_titles()

print(titles)

for title in titles:
    print(f"title is {title}")
    print(my_sheet.get_sheet(title))
    print()

