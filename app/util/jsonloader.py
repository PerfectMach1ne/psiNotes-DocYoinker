##### jsonsaver.py #####
#### Open a "JSON doc" and load it into memory, then do stuff with it. ####
###
##
#
import json
from os import path

import parser
from parser import args


YOINK_PATH = path.abspath('../yoinkstash')


# Loads the whole JSONdoc into memory and returns it
def load_jsondoc(omega_id: str) -> list:
    if not args.shut_up:
        print(f"> Opening file /yoinkstash/jsondoc_{omega_id}.json ...")
    with open(YOINK_PATH + '/jsondoc_' + omega_id + '.json', 'r', encoding='UTF-8') as jsondoc:
        read_jsondoc = json.load(jsondoc)
  
    if jsondoc.closed == False:
        raise Exception('File hasn\'t been closed properly.')

    jsondoc.close()

    json_content = read_jsondoc
    if not args.shut_up:
        print("> Paragraphs contained in the locally saved Notebook: " + str(len(json_content)))

    return json_content
