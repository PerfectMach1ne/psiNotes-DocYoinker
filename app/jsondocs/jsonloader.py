##### jsonsaver.py #####
#### Open a "JSON doc" and load it into memory, then do stuff with it. ####
###
##
#
import json
from os import path


YOINK_PATH = path.abspath('yoinkstash')


# Loads the whole JSONdoc into memory and returns it
def load_jsondoc(omega_id: str) -> list:
  with open(YOINK_PATH + '/jsondoc_' + omega_id + '.json', 'r', encoding='UTF-8') as jsondoc:
    read_jsondoc = json.load(jsondoc)
  
  if jsondoc.closed == False:
    raise Exception('File hasn\'t been closed properly.')

  jsondoc.close()

  content = read_jsondoc["content"]
  print("Objects contained in the unpacked Notebook: " + str(len(content)))

  return content
