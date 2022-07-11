from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import pandas as pd

#https://docs.google.com/spreadsheets/d/1han67G0Pa0M8pkAw8vfP19FNNNbzzTWgrOlPwZR-8rs/edit?usp=sharing

# Initializing a GoogleAuth Object
def auth():
    gauth = GoogleAuth()

    # client_secrets.json file is verified
    # and it automatically handles authentication
    gauth.LocalWebserverAuth()

    # GoogleDrive Instance is created using
    # authenticated GoogleAuth instance
    drive = GoogleDrive(gauth)

    # Initialize GoogleDriveFile instance with file id
    file_obj = drive.CreateFile({'id': '1han67G0Pa0M8pkAw8vfP19FNNNbzzTWgrOlPwZR-8rs'})
    file_obj.GetContentFile('Internship Fair (Responses).xls',
        mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

    dataframe = pd.read_excel('Internship Fair (Responses).xls')
    #dataframe.to_csv('Internship Fair (Responses).csv')
    return dataframe
