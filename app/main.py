##### main.py #####
#### psiNotes-DocYoinker core! Here be things getting launched (and dragons!). ####
###
##
#

import json
import requests as req

from googleapiclient.discovery import build

from chi.chinotes import refresh_from_template
import gdocs
import oauth2 
import tableofcontents as toc
import util.docs_ids as docs_ids
import util.jsonsaver as jdsave
import util.jsonloader as jdload
import getjdocs.posobj as get_po
from parser.parsercore import args


def main():
    creds = oauth2.google_docs_auth()

    if args.shutup:
        print("[SkillIssueException] Dumb user tried to shut me up with --shutup, doesn't realize it's --shut-up that does the trick!")
        exit(1)

    if not args.shut_up:
        print(f"> args object elements: {vars(args)}")

    #
    # Docs exclusive features
    #
    if args.fetch != None:
        doc_id = None
        doc = None
        for fetched_doc in args.fetch:
            doc_id = docs_ids.OMEGA_IDS[docs_ids.OMEGA_IDS.index(fetched_doc)]
            doc = gdocs.get_ntb(creds, doc_id)
        if not args.shut_up:
            print(f"> Serializing JSON object for Ntb {doc_id}...")
        print(f"> Fetched JSON doc title: {doc.get('title')}")
        json_content = doc.get('tabs')[0].get('documentTab').get('body').get('content')
        print(json.dumps(json_content, indent=4))
    # This CAN be an elif, bc --fetch & --save are MUTUALLY EXCLUSIVE!!!
    elif args.save != None:
        doc_id = None
        doc = None
        for fetched_doc in args.save:
            doc_id = docs_ids.OMEGA_IDS[docs_ids.OMEGA_IDS.index(fetched_doc)]
            doc = gdocs.get_ntb(creds, doc_id)
            print(f"> Fetched JSON doc title: {doc.get('title')}")
            jdsave.save_ntb(doc, doc_id)
    elif args.posobj != None:
        doc_id = None
        doc = None
        for fetched_doc in args.posobj:
            doc_id = docs_ids.OMEGA_IDS[docs_ids.OMEGA_IDS.index(fetched_doc)]
            doc = gdocs.get_ntb(creds, doc_id)
            doc_posobjs = get_po.get_posobjs(creds, doc_id)
            get_po.save_posobjs(doc_posobjs)

    #
    # Table of Contents & psi/chi Notes features
    #
    if hasattr(args, 'subcommand'):
        print(args.subcommand)
        if args.subcommand == 'toc':
            file = toc.get_toc(creds)
            sheets_service = build('sheets', 'v4', credentials=creds)

            # Slop code to just test if it works:
            spreadsheet_info = sheets_service.spreadsheets().get(
                spreadsheetId=toc.TOC_ID
            ).execute()
            sheet_title = spreadsheet_info['sheets'][2]['properties']['title']

            result = sheets_service.spreadsheets().values().get(
                spreadsheetId=toc.TOC_ID,
                range=sheet_title
            ).execute()

            values = result.get('values', [])

            found = False
            for row_id, row in enumerate(values):
                for col_id, cell in enumerate(row):
                    if cell == "4.1.2.Empty set":
                        print(f"woo woo woo '{sheet_title}' bwoo bwoo {row_id + 1}:{col_id + 1} found me a {cell}")
                        found = True
        
        elif args.subcommand == 'chi':
            refresh_from_template(args.refresh)
            pass


    if args.test:
        pass


if __name__ == "__main__":
    main()
