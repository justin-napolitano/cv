from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google.oauth2 import service_account
from googleapiclient.http import MediaIoBaseDownload, MediaFileUpload


class SheetsApp:

    def __init__(self,creds):
        self.SheetService = self.get_sheet_service(creds)
       
        
    def get_sheet_service(creds):
        service = build('sheets', 'v4', credentials=creds)
        return service.spreadsheets()



class DriveApp:
    
    def __init__(self,creds):
        self.SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']
        self.DriveService = self.get_drive_service(creds)

    def get_drive_service(self,creds):
        """Shows basic usage of the Drive v3 API.
        Prints the names and ids of the first 10 files the user has access to.
        """
        SCOPES = []
        #creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.

        service = build('drive', 'v3', credentials=creds)

        # Call the Drive v3 API
        results = service.files().list(
            pageSize=10, fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])

        if not items:
            print('No files found.')
        else:
            print('Files:')
            for item in items:
                print(u'{0} ({1})'.format(item['name'], item['id']))

        return service
        
        

    def create_folder(self,title):
        file_metadata = {
            'name': '{}'.format(title),
            'mimeType': 'application/vnd.google-apps.folder'
        }
        file = self.DriveService.files().create(body=file_metadata,
                                            fields='id').execute()
        print('Folder ID: %s' % file.get('id'))


    #def share_folder(drive_service, )


    def add_spreadsheet_to_folder(self,folder_id,title):
        #folder_id = '0BwwA4oUTeiV1TGRPeTVjaWRDY1E'
        #file_metadata = {
        #    'name': 'photo.jpg',
        #    'parents': [folder_id]
        #}

        file_metadata = {
        'name': '{}'.format(title),
        'parents': [folder_id],
        'mimeType': 'application/vnd.google-apps.spreadsheet',
        }

        #media = MediaFileUpload('photo.jpeg',
        #                        mimetype='image/jpeg',
        #                        resumable=True)

        res = self.DriveService.files().create(body=file_metadata).execute()
        print(res)

        return res
