#!/usr/local/bin/python3

from __future__ import print_function
import os.path
import pprint
import sys
from gapi import GAPI


def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    gapi = GAPI().getInstance()
    #drive_service = gapi.get_drive()
    sheets_service = gapi.get_sheets()

    body = {
        "properties": {
            "title": "My first spreadsheet"
        },
        "sheets": [
            {
                "properties": {
                    "title": "sheet one"
                }
            },
            {
                "properties": {
                    "title": "sheet two"
                }
            }
        ]
    }
    result = sheets_service.spreadsheets().create(body=body).execute()
    pprint.pprint(result)
    workbook_id = result['spreadsheetId']

    body = {
        "valueInputOption": "RAW",
        "data": [
            {
                "range": "sheet one!A1:I9",
                "majorDimension": "ROWS",
                "values": [["goodbye", "world"], ["this", "is", "line", "two"]]
            },
            {
                "range": "sheet two!A1:I9",
                "majorDimension": "ROWS",
                "values": [["hello", "world"], ["this", "is", "line", "two"]]
            }
        ]
    }
    result = sheets_service.spreadsheets().values().batchUpdate(spreadsheetId=workbook_id, body=body).execute()

if __name__ == '__main__':
    main()
