##### gdocs.py #####
#### Functions handling the fetched raw Google Document object ####
###
##
#
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import parser
from parser import args
import util.docs_ids as docs_ids


def get_ntb(creds, omega_id: str) -> object:
  DOCUMENT_ID = docs_ids.DOCUMENT_IDS[omega_id]
  document = None

  try:
    if not args.shut_up:
      print("> Retrieving Google Doc...")
      print(f"\-> GET https://docs.googleapis.com/v1/documents/{docs_ids.DOCUMENT_IDS[omega_id]}")
    service = build("docs", "v1", credentials=creds)

    # Retrieve the documents contents from the Docs service.
    document = service.documents().get(documentId=DOCUMENT_ID, includeTabsContent=True).execute()
  except HttpError as err:
    if not args.shut_up:
      print("> Google Doc retrieval failed (HttpError)!")
      print(f"\-> {err}")
    else:
      print(err)

  return document