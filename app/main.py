import os.path
import json

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import util.docs_ids as docs_ids
import oauth2 


def get_ntb(creds, omega_id):
  DOCUMENT_ID = docs_ids.DOCUMENT_IDS[omega_id]
  document = None

  try:
    service = build("docs", "v1", credentials=creds)

    # Retrieve the documents contents from the Docs service.
    document = service.documents().get(documentId=DOCUMENT_ID).execute()
  except HttpError as err:
    print(err)

  return document


def get_all_ntb_ids():
  existing_ntb_ids = {omega_id: gdoc_id for omega_id, gdoc_id in docs_ids.DOCUMENT_IDS.items() if gdoc_id != ""}

  return existing_ntb_ids
  # print(existing_gdoc_ids)


def main():
  creds = oauth2.google_docs_auth()

  # Is this a bit unnecessary...? Yeah!
  notebooks = get_all_ntb_ids()
  omega_ids = list(notebooks.keys())
  ntb_0 = get_ntb(creds, omega_ids[omega_ids.index("0")])

  # print(f"The title of the document is: {ntb_0.get('title')}")
  print(json.dumps(ntb_0.get('body'), indent=' ' * 4))
  
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
  


if __name__ == "__main__":
  main()
