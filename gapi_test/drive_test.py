#!/usr/local/bin/python3

from __future__ import print_function
import pickle
import os.path
import pprint
import sys
import re
from urllib.parse import unquote, urlparse
from pathlib import PurePosixPath
from collections import namedtuple
from collections import defaultdict
from pprint import pformat
import numpy as np
import datetime
from gapi import GAPI


def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    gapi = GAPI().getInstance()
    drive_service = gapi.get_drive()

    files = (
        ('hello.txt', None),
        ('hello.txt', 'application/vnd.google-apps.document'),
    )

    for filename, mimeType in files:
        metadata = {'name': filename}
        if mimeType:
            metadata['mimeType'] = mimeType
        res = drive_service.files().create(body=metadata, media_body=filename).execute()
        if res:
            print(f"Uploaded {filename} ({res['mimeType']})")

    if res:
        MIMETYPE = 'application/pdf'
        data = drive_service.files().export(fileId=res['id'], mimeType=MIMETYPE).execute()
        if data:
            fn = f"{os.path.splitext(filename)[0]}.pdf"
            with open(fn, "wb") as fh:
                fh.write(data)
            print(f"Downloaded {fn} ({MIMETYPE})")

    files = drive_service.files().list().execute().get('items', [])
    for f in files:
        print(f"title={f['title']} type={f['mimeType']}")
    print('after files loop')


if __name__ == '__main__':
    main()

    # print(np.reshape(grid == 0, (81,1)))

    # print("Row sums")
    # print(45 - np.sum(grid, axis=1))

    # print("Col sums")
    # print(45 - np.sum(grid, axis=0))

    # print("Block sums")
    # for r in range(3):
    #     for c in range(3):
    #         print(45 - np.sum(grid[r*3:r*3+3,c*3:c*3+3]))

    # body = {
    #     'majorDimension': 'ROWS',
    #     'range': 'Sheet1!A1:I9',
    #     'values': grid.tolist()
    # }
    # result = service.spreadsheets().values().update(spreadsheetId=workbook_id, range="Sheet1!A1:I9", valueInputOption='RAW', body=body).execute()
