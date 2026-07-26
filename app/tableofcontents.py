##### gdocs.py #####
#### For loading the Table of Contents Google Sheet ####
###
##
#
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import parser
from parser import args


TOC_ID = "15nSuKrllBI4PdawNSxqVGMqnc-CjYMN8A3c6kASYd9Y"


def get_toc(creds) -> object:
    tableofcontents = None

    try:
        if not args.shut_up:
            print("> Retrieving Table of Contents...")
            print(f"\\-> GET https://docs.googleapis.com/v1/documents/")
        service = build("drive", "v3", credentials=creds)

        # Retrieve the Table of Contents sheet from the Drive service.
        sheet = service.files().get(fileId=TOC_ID).execute()

    except HttpError as err:
        if not args.shut_up:
            print("> Table of Contents retrieval failed (HttpError)!")
            print(f"\\-> {err}")
        else:
            print(err)

    return tableofcontents
