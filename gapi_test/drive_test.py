#!/usr/local/bin/python3

from __future__ import print_function
import os.path
import sys
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
