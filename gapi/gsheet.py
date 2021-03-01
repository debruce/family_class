from pprint import pprint
import numpy as np
from gapi.gauth import GAuth


def _get_cell_name(r,c):
   if c < 26:
      s = chr(65+c)
   else:
      s = chr(64+(int(c/26))) + chr(65+(c%26))
   return f"{s}{r+1}"

class GSheet:
   _api = None
   _sheet_id = None


   def __init__(self, sheet_id):
      if GSheet._api == None:
         GSheet._api = GAuth().getInstance().get_sheets()
      self._sheet_id = sheet_id


   def make_sheet(self, title, data):
      if data.dtype.kind in [ 'S', 'U' ]:
         def cell_cast(cell_value):
            return { 'stringValue': cell_value }
      elif data.dtype.kind == 'b':
         def cell_cast(cell_value):
            return { 'boolValue': cell_value }
      else:
         def cell_cast(cell_value):
            return { 'numberValue': cell_value }
      cell_range = f"{_get_cell_name(0, 0)}:{_get_cell_name(data.shape[0], data.shape[1])}"
      body = {
         'requests': [
            {
               'addSheet': {
                  'properties': {
                     'title': title,
                     'gridProperties': { 'rowCount': data.shape[0], 'columnCount': data.shape[1] }
                  }
               }
            }
         ]
      }
      response = GSheet._api.spreadsheets().batchUpdate(spreadsheetId=self._sheet_id,
         body=body).execute()
      sheetId = response['replies'][0]['addSheet']['properties']['sheetId']

      rows_to_send = []
      for row in data:
         values_to_send = []
         for cell_value in row:
            values_to_send.append({'userEnteredValue': cell_cast(cell_value)})
         rows_to_send.append({ 'values': values_to_send})

      updateCells = {
         'start': { 'sheetId': sheetId, 'rowIndex': 0, 'columnIndex': 0 },
         'fields': '*',
         'rows': rows_to_send
      }

      body = {
         'requests': [
            { 'updateCells': updateCells }
         ]
      }
      GSheet._api.spreadsheets().batchUpdate(spreadsheetId=self._sheet_id,
         body=body).execute()

   def get_sheet(self, title):
      response = GSheet._api.spreadsheets().values().get(spreadsheetId=self._sheet_id,
         range=title).execute()
      return np.asarray(response['values'])

   def get_titles(self):
      response = GSheet._api.spreadsheets().get(spreadsheetId=self._sheet_id).execute()
      return [ x['properties']['title'] for x in response['sheets'] ]