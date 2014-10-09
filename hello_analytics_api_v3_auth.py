#!/usr/bin/python
# -*- coding: utf-8 -*-
#

__author__ = 'xukai.ken@gmail.com(Kai.XU)'

from apiclient.discovery import build
import httplib2
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import run


CLIENT_SECRETS = 'client_secrets.json'

TOKEN_FILE_NAME = 'analytics.dat'

MISSING_CLIENT_SECRETS_MESSAGE = '%s is missing' % CLIENT_SECRETS

FLOW = flow_from_clientsecrets(CLIENT_SECRETS, scope = 'https://www.googleapis.com/auth/analytics.readonly', message = MISSING_CLIENT_SECRETS_MESSAGE)


def prepare_credentials():
  storage = Storage(TOKEN_FILE_NAME)
  credentials = storage.get()
  
  if credentials is None or credentials.invalid:
    credentials = run(FLOW, storage)
  return credentials



def initialize_service():
  http = httplib2.Http()

  #Get stored credentials or run the Auth Flow if none are found
  credentials = prepare_credentials()
  http = credentials.authorize(http)

  #Construct and return the authorized Analytics Service Object
  return build('analytics', 'v3', http = http)  
  
  
