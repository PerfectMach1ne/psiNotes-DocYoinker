from os import path

YOINK_PATH = '../../yoinkstash'

print(YOINK_PATH + '/jsondoc_' + 'M1' + '.json')
paffwayy = path.relpath('yoinkstash')
print(path.abspath(paffwayy))