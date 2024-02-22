##### main.py #####
#### psiNotes-DocYoinker core! Here be things getting launched (and dragons!). ####
###
##
#
import json

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import oauth2 
import util.docs_ids as docs_ids
import jsondocs.jsonsaver as jdsave
import jsondocs.jsonloader as jdload


def get_all_ntb_ids():
  existing_ntb_ids = {omega_id: gdoc_id for omega_id, gdoc_id in docs_ids.DOCUMENT_IDS.items() if gdoc_id != ""}

  return existing_ntb_ids


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


def main():
  creds = oauth2.google_docs_auth()

  # Is this a bit unnecessary...? Yeah!
  notebooks = get_all_ntb_ids()
  omega_ids = list(notebooks.keys())
  ntb_0 = get_ntb(creds, omega_ids[omega_ids.index("0")])

  # print(f"The title of the document is: {ntb_0.get('title')}")
  print(json.dumps(ntb_0.get('body'), indent=' ' * 4))


if __name__ == "__main__":
  main()
