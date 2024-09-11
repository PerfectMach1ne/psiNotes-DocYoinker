##### main.py #####
#### psiNotes-DocYoinker core! Here be things getting launched (and dragons!). ####
###
##
#

import json

import gdocs
import oauth2 
import parser
from parser import args
import util.docs_ids as docs_ids
import jsondocs.jsonsaver as jdsave
import jsondocs.jsonloader as jdload


def main():
  creds = oauth2.google_docs_auth()
  
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

  elif args.save != None:
    doc_id = None
    doc = None
    for fetched_doc in args.save:
      doc_id = docs_ids.OMEGA_IDS[docs_ids.OMEGA_IDS.index(fetched_doc)]
      doc = gdocs.get_ntb(creds, doc_id)
      print(f"> Fetched JSON doc title: {doc.get('title')}")
      jdsave.save_ntb(doc, doc_id)


if __name__ == "__main__":
  main()
