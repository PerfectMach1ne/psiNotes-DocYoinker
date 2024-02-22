import os.path
import json

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
    print(json.dumps(document.get('body'), indent="  "))
    ###### master plan pipeline:
    # >put JSON in a .json
    # >make stash of functions to handle different parts of it
    # >first, the hard part - search for all images and their positions
    # >download all of the images to ../yoinkstash/pos_objs/rawposobjs.json
    # >then grab all the text and tables
    # > >put tables in a ../yoinkstash/tables/tables.json
    # > >rest goes to ../yoinkstash/text/rawtext.json
    # > >develop some system to identify your headers and etc
    # > > >different for 0, different for other notebookies.
    # > > >split rawtext.json into segtext.json (segmented text)
    # ! everything stores its position!
    # >the first hellish attempt at trying to convert everything to XML or even HTML...
    # > >....but maybe converting the JSON data into a very decent XML format i can engineer is a better idea?

  except HttpError as err:
    print(err)


if __name__ == "__main__":
  main()
