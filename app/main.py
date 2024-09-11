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
    # This CAN be an elif, bc --fetch & --save are MUTUALLY EXCLUSIVE!!!
    elif args.save != None:
        doc_id = None
        doc = None
        for fetched_doc in args.save:
            doc_id = docs_ids.OMEGA_IDS[docs_ids.OMEGA_IDS.index(fetched_doc)]
            doc = gdocs.get_ntb(creds, doc_id)
            print(f"> Fetched JSON doc title: {doc.get('title')}")
            jdsave.save_ntb(doc, doc_id)

    if args.test:
        print("> Running testing code! Good luck!!!")
        doc_id = docs_ids.OMEGA_IDS[docs_ids.OMEGA_IDS.index('0')]
        doc = gdocs.get_ntb(creds, doc_id)

    if not args.shut_up:
        print(f"> Fetched JSON doc title: {doc.get('title')}")

    pos_objs = doc.get('tabs')[0].get('documentTab').get('positionedObjects')
    
    # Find the Paragraphs with positionedObjectIds property.
    paragraph_list = jdload.load_jsondoc(doc_id)
    pos_objs_pars = list()
    for par in zip(range(len(paragraph_list)), paragraph_list):
        pos_obj_id = par[1].get('paragraph')
        if pos_obj_id != None:
            if 'positionedObjectIds' in pos_obj_id.keys():
                pos_objs_pars.append(pos_obj_id)

    if not args.shut_up:
        print(f"> PositionedObject paragraphs in NtB {doc_id}: {len(pos_objs_pars)}")
        print("> PositionedObject IDs: ")
        for obj in pos_objs_pars:
            print(json.dumps(obj.get('positionedObjectIds')[0], indent=4))

    img_uris = list()
    for obj in pos_objs_pars:
        img_uris.append(pos_objs.get(obj.get('positionedObjectIds')[0])
        .get('positionedObjectProperties')
        .get('embeddedObject')
        .get('imageProperties')
        .get('contentUri'))

    if not args.shut_up:
        print("> PositionedObject image URIs:")
        for zt in zip(img_uris, pos_objs_pars):
            print("\"" + zt[1].get('positionedObjectIds')[0] + "\": " + zt[0])
    
    for img_uri in img_uris:
        url = img_uri
        res = req.get(url)
        print(res.headers['content-type'])



if __name__ == "__main__":
    main()
