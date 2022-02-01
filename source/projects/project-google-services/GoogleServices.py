from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google.oauth2 import service_account
from googleapiclient.http import MediaIoBaseDownload, MediaFileUpload


class GoogleAPI:
    def __init__(self):
        self.GoogleCredentials = self.load_google_creds()
        self.SheetsApp = self.instantiate_sheets_app()
        self.DriveApp = self.instantiate_drive_app()
        self.DriveApp.test_call()
    def load_google_creds(self):
        #file_path = "credentials.json"
        return creds(file_path = "credentials.json")

    def instantiate_sheets_app(self):
        return SheetsApp(self.GoogleCredentials.credentials)

    def instantiate_drive_app(self):
        drive_app = DriveApp(self.GoogleCredentials.credentials)
        return drive_app



class SheetsApp:

    def __init__(self,creds):
        self.SheetService = self.get_sheet_service(creds)
       
        
    def get_sheet_service(self,creds):
        service = build('sheets', 'v4', credentials=creds)
        return service.spreadsheets()



class DriveApp:
    
    def __init__(self,creds):
        self.SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']
        self.DriveService = self.get_drive_service(creds)
        #self.test_call()

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
        return service

    def test_call(self):

        # Call the Drive v3 API
        results = self.DriveService.files().list(
            pageSize=10, fields="nextPageToken, files(id, name)").execute()

        items = results.get('files', [])

        if not items:
            print('No files found.')
        else:
            print('Files:')
            for item in items:
                print(u'{0} ({1})'.format(item['name'], item['id']))

        
        
        

    def create_folder(self,title):
        file_metadata = {
            'name': '{}'.format(title),
            'mimeType': 'application/vnd.google-apps.folder'
        }
        file = self.DriveService.files().create(body=file_metadata,
                                            fields='id').execute()
        print('Folder ID: %s' % file.get('id'))
        return file


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
        #print(res)

        return res



class creds:

    def __init__(self,file_path = "credentials.json"):
        self.credentials = self.get_creds(file_path)

    def get_creds(self,file_path):
        """Shows basic usage of the Sheets API.
        Prints values from a sample spreadsheet.
        """
        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
                print("no creds")
            else:
                creds = service_account.Credentials.from_service_account_file(file_path)
                #creds = ServiceAccountCredentials.from_json_keyfile_name('add_json_file_here.json', SCOPES)
                #flow = InstalledAppFlow.from_client_secrets_file(
                #    'credentials.json', SCOPES)
                #creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            #with open('token.json', 'w') as token:
            #    token.write(creds.to_json())
        return creds
