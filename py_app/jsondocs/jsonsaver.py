##### jsonsaver.py #####
#### Save a Google Document object to a JSON ("JSON doc"); also save changes I guess! ####
###
##
#
import json
from os import path


YOINK_PATH = path.abspath('yoinkstash')


# Takes in a notebook Document object & its omega_id, and saves it into a properly named "JSONdoc" file.
def save_ntb(ntb_obj: object, omega_id: str) -> object:
  serialized_str = json.dumps(ntb_obj.get('body'), indent=' ' * 4)

  with open(YOINK_PATH + '/jsondoc_' + omega_id + '.json', 'w', encoding='UTF-8') as jsondoc:
    jsondoc.write(serialized_str)
  
  if jsondoc.closed == False:
    raise Exception('File hasn\'t been closed properly.')
  
  jsondoc.close()
