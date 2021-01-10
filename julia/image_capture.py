#!/usr/local/bin/python3

import cv2
from gapi import GAPI

gapi = GAPI().getInstance()
drive_service = gapi.get_drive()

camera = cv2.VideoCapture(0)
for i in range(1):
    return_value, image = camera.read()
    cv2.imwrite('opencv'+str(i)+'.png', image)
del(camera)

files = (
    ('opencv0.png', 'image/png'),
)

for filename, mimeType in files:
    metadata = {'name': filename}
    if mimeType:
        metadata['mimeType'] = mimeType
    res = drive_service.files().create(body=metadata, media_body=filename).execute()
    if res:
        print(f"Uploaded {filename} ({res['mimeType']})")

