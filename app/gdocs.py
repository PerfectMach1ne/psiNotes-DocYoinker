##### gdocs.py #####
#### Functions handling the fetched raw Google Document object ####
###
##
#
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import util.docs_ids as docs_ids


def get_all_ntb_ids() -> dict[str, str]:
  existing_ntb_ids = {omega_id: gdoc_id for omega_id, gdoc_id in docs_ids.DOCUMENT_IDS.items() if gdoc_id != ""}

  return existing_ntb_ids


def get_ntb(creds, omega_id: str) -> object:
  DOCUMENT_ID = docs_ids.DOCUMENT_IDS[omega_id]
  document = None

  try:
    service = build("docs", "v1", credentials=creds)

    # Retrieve the documents contents from the Docs service.
    document = service.documents().get(documentId=DOCUMENT_ID).execute()
  except HttpError as err:
    print(err)

  return document