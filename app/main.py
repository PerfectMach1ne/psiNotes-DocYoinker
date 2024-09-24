##### main.py #####
#### psiNotes-DocYoinker core! Here be things getting launched (and dragons!). ####
###
##
#

import json
import requests as req

import gdocs
import oauth2 
import parser
from parser import args
import util.docs_ids as docs_ids
import util.jsonsaver as jdsave
import util.jsonloader as jdload
import getjdocs.posobj as get_po


def main():
    creds = oauth2.google_docs_auth()

    if args.shutup:
        print("[SkillIssueException] Dumb user tried to shut me up with --shutup, doesn't realize it's --shut-up that does the trick!")
        exit(1)
  
    if not args.shut_up:
        print(f"> args object elements: {vars(args)}")

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

    if args.test:
        pass


if __name__ == "__main__":
    main()
