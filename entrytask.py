from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/admin.directory.user']

def main():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('admin', 'directory_v1', credentials=creds)

    firstname = input('Введите имя сотрудника: ')
    lastname = input('Введите фамилию сотрудника: ')
    mail = input('придумайте почту для сотрудника: ')
    if mail.rfind('@') == -1:
        print('Вы забыли ввести домен почты')
        mail = mail + '@' + input('введите домен (например example.com): ')
    passw = input('придумайте и введите пароль: ')
    newuser = {
        'primaryEmail': mail,
        'name': {
            'familyName': firstname,
            'givenName': lastname
        },
        'password': passw
    }
    service.users().insert(body = newuser).execute()  
if __name__ == '__main__':
    main()
