import json
import requests as req

import util.jsonloader as jdload
from parser import args
import util.docs_ids as docs_ids
import util.jsonsaver as jdsave
import util.jsonloader as jdload


def get_posobjs(creds, omega_id: str) -> dict:
    doc_id = docs_ids.OMEGA_IDS[docs_ids.OMEGA_IDS.index(omega_id)]
    doc = gdocs.get_ntb(creds, doc_id)
    return_posobjs = dict()    

    if not args.shut_up:
        print(f"> Fetching PositionedObjects...")
    pos_objs = doc.get('tabs')[0].get('documentTab').get('positionedObjects')

    paragraph_list = jdload.load_jsondoc(doc_id)
    pos_objs_pars = list()
    for par in zip(range(len(paragraph_list)), paragraph_list):
        pos_obj_id = par[1].get('paragraph')
        if pos_obj_id != None :
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
    
    
    return []


def download_posobjs():
    pass


def save_posobjs():
    pass
