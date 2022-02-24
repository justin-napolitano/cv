:py:mod:`GoogleServices`
========================

.. py:module:: GoogleServices


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   GoogleServices.GoogleAPI
   GoogleServices.SheetsApp
   GoogleServices.DriveApp
   GoogleServices.creds




.. py:class:: GoogleAPI

   .. py:method:: load_google_creds(self)


   .. py:method:: instantiate_sheets_app(self)


   .. py:method:: instantiate_drive_app(self)



.. py:class:: SheetsApp(creds)

   .. py:method:: get_sheet_service(self, creds)



.. py:class:: DriveApp(creds)

   .. py:method:: get_drive_service(self, creds)

      Shows basic usage of the Drive v3 API.
      Prints the names and ids of the first 10 files the user has access to.


   .. py:method:: test_call(self)


   .. py:method:: create_folder(self, title)


   .. py:method:: add_spreadsheet_to_folder(self, folder_id, title)



.. py:class:: creds(file_path='credentials.json')

   .. py:method:: get_creds(self, file_path)

      Shows basic usage of the Sheets API.
      Prints values from a sample spreadsheet.



