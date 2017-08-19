#!/usr/local/bin/python3
from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

scopes = ['https://www.googleapis.com/auth/calendar']

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    '/path/to/keyfile.json', scopes=scopes)
gcal = build('calendar', 'v3', http=http_auth)

