#!/usr/bin/python
# -*- coding: utf-8 -*-
#

__author__ = 'xukai.ken@gmail.com(Kai.XU)'

import httplib2

from apiclient.discovery import build
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import run

CLIENT_SECRETS = 'client_secrets.json'

TOKEN_FILE_NAME = 'analytics.dat'

MISSING_CLIENT_SECRETS_MESSAGE = '%s is missing' % CLIENT_SECRETS

FLOW = flow_from_clientsecrets(CLIENT_SECRETS, scope = 'https://www.googleapis.com/auth/analytics.readonly', message = MISSING_CLIENT_SECRETS_MESSAGE)

def main():
  
  
  
  pass


if __name__ == '__main__':
  main()