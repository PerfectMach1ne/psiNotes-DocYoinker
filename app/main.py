import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import docs_ids
import oauth2 

# The ID of a sample document.
# DOCUMENT_ID = "195j9eDD3ccgjQRttHhJPymLJUCOUjs-jmwTrekvdjFE"


def main():
  creds = oauth2.google_docs_auth()

  DOCUMENT_ID = docs_ids.DOCUMENT_IDS['0']

  try:
    service = build("docs", "v1", credentials=creds)

    # Retrieve the documents contents from the Docs service.
    document = service.documents().get(documentId=DOCUMENT_ID).execute()

    print(f"The title of the document is: {document.get('title')}")
  except HttpError as err:
    print(err)


if __name__ == "__main__":
  main()
