import json
import requests as req
from io import BytesIO
from os import path
from PIL import Image

import gdocs
import util.jsonloader as jdload
from parser import args
import util.docs_ids as docs_ids
import util.jsonsaver as jdsave
import util.jsonloader as jdload


type PosObj = list[dict[dict[list, str, str]]]


YOINK_PATH = path.abspath('../yoinkstash')


def get_posobjs(creds, omega_id: str) -> PosObj:
    doc_id = docs_ids.OMEGA_IDS[docs_ids.OMEGA_IDS.index(omega_id)]
    doc = gdocs.get_ntb(creds, doc_id)
    return_posobjs = list()    

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
                return_posobjs.append(
                    dict(
                        placeholder=
                            dict(paragraph_data=[], uri="", mime_type="")
                        )
                    )

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
        stupid_counter = 0
        for zt in zip(img_uris, pos_objs_pars):
            url = zt[0]
            res = req.get(url)
            content_type = res.headers['content-type']
            posobj_id = zt[1].get('positionedObjectIds')[0]

            print("\"" + posobj_id + "\": " + url)
            print("Content-Type: " + res.headers['content-type'])

            local_obj = return_posobjs[stupid_counter][posobj_id] = return_posobjs[stupid_counter].pop('placeholder')
            local_obj['uri'] = url
            local_obj['mime_type'] = content_type
            stupid_counter = stupid_counter + 1

    
    return return_posobjs


def image_to_bytearr(image: Image) -> bytes:
    image_byte_array = BytesIO()
    image.save(image_byte_array, format=image.format)
    image_byte_array = image_byte_array.getvalue()
    return image_byte_array


def download_posobjs(posobj: PosObj):
    res_tuples = list()

    for po_list in posobj:
        for po_key in po_list:
            uri = po_list[po_key]['uri'] 
            res = req.get(uri)
            mime_type = po_list[po_key]['mime_type'] 
            img = Image.open(BytesIO(res.content))
            content = image_to_bytearr(img)
            res_tuples.append(tuple(
                (po_key, content, mime_type)
                ))
            
    return res_tuples    


def save_posobjs(posobj: PosObj):
    # Rough draft of the function so far:
    tuples = download_posobjs(posobj)
    for tup in tuples:
        posobjkey = tup[0]
        img_bytes = tup[1]
        mime_type = tup[2]

        file_type = None
        match mime_type:
            case "image/jpeg":
                file_type = ".jpg"
            case "image/png":
                file_type = ".png"
    
        if not args.shut_up:
            print("> Saving file: " + YOINK_PATH + '/pos_objs/' + posobjkey + file_type + " ...")
        with open(YOINK_PATH + '/pos_objs/' + posobjkey + file_type, 'wb') as local_img:
            print(type(img_bytes))
            local_img.write(img_bytes)
        if local_img.closed == False:
            raise Exception('File hasn\'t been closed properly.')

        local_img.close()
