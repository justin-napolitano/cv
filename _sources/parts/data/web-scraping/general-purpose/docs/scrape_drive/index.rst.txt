:py:mod:`scrape_drive`
======================

.. py:module:: scrape_drive


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   scrape_drive.get_drive_service
   scrape_drive.create_folder
   scrape_drive.add_spreadsheet_to_folder



Attributes
~~~~~~~~~~

.. autoapisummary::

   scrape_drive.SCOPES


.. py:data:: SCOPES
   :annotation: = ['https://www.googleapis.com/auth/drive.metadata.readonly']

   

.. py:function:: get_drive_service(creds)

   Shows basic usage of the Drive v3 API.
   Prints the names and ids of the first 10 files the user has access to.


.. py:function:: create_folder(drive_service, title)


.. py:function:: add_spreadsheet_to_folder(drive_service, folder_id, title)


