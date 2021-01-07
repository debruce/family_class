#!/usr/local/bin/python3

from __future__ import print_function
import os.path
import sys
from pprint import pprint
from gapi import GAPI


def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    gapi = GAPI().getInstance()
    drive_service = gapi.get_drive()

    pageToken = None
    while True:
        lst = drive_service.files().list(pageSize=1000, pageToken=pageToken).execute()
        for f in lst['files']:
            pprint(f)
            print('####')
            # myfile = drive_service.files().get(fileId=f['id'], fields='*').execute()
            # pprint(myfile)
            # print('####')
            if f['mimeType'] == 'text/plain':
                print("try to dump it")
                mydata = drive_service.files().get_media(fileId=f['id']).execute()
                pprint(mydata)
            print('\n\n\n')
        if 'nextPageToken' not in lst:
            break
        pageToken = lst['nextPageToken']
    # lst = drive_service.files().list().execute()

    # files = (
    #     ('hello.txt', None),
    #     ('hello.txt', 'application/vnd.google-apps.document'),
    # )

    # for filename, mimeType in files:
    #     metadata = {'name': filename}
    #     if mimeType:
    #         metadata['mimeType'] = mimeType
    #     res = drive_service.files().create(body=metadata, media_body=filename).execute()
    #     if res:
    #         print(f"Uploaded {filename} ({res['mimeType']})")

    # if res:
    #     MIMETYPE = 'application/pdf'
    #     data = drive_service.files().export(fileId=res['id'], mimeType=MIMETYPE).execute()
    #     if data:
    #         fn = f"{os.path.splitext(filename)[0]}.pdf"
    #         with open(fn, "wb") as fh:
    #             fh.write(data)
    #         print(f"Downloaded {fn} ({MIMETYPE})")

    # files = drive_service.files().list().execute().get('items', [])
    # for f in files:
    #     print(f"title={f['title']} type={f['mimeType']}")
    # print('after files loop')


if __name__ == '__main__':
    main()
