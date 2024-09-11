##### main.py #####
#### psiNotes-DocYoinker core! Here be things getting launched (and dragons!). ####
###
##
#

import argparse
import json

import oauth2 
import gdocs
import jsondocs.jsonsaver as jdsave
import jsondocs.jsonloader as jdload


def main():
  creds = oauth2.google_docs_auth()

  notebook_ids = gdocs.get_all_ntb_ids()
  omega_ids = list(notebook_ids.keys())

  parser = argparse.ArgumentParser(
    prog='DocYoinker',
    description="Python interface for fetching omega Notes Google Docs \
     and converting them to HTML+CSS formatted psi Notes format.",
    epilog='Copytop Luka Vivi Starr Alice 02.2024-09.2024'
  )
  parser.add_argument('-f', '--fetch', choices=omega_ids,
    help='Fetch and print a Google Doc\'s content (as JSON doc). WARNING: Some JSON docs are incredibly long!')
  parser.add_argument('-s', '--save', choices=omega_ids,
    help='Fetch and save a Google Doc to the yoinkstash directory.')
  parser.add_argument('-v', '--verbose', action='store_true',
    help='Toggle verbose mode (on by default).')

  args = parser.parse_args()

  if args.fetch != None:
    doc_id = omega_ids[omega_ids.index(args.fetch)]
    doc = gdocs.get_ntb(creds, doc_id)
    print(f"The title of the fetched document is: {doc.get('title')}")
    print(json.dumps(jdload.load_jsondoc(doc_id), indent=' ' * 4))
  elif args.save != None:
    doc_id = omega_ids[omega_ids.index(args.save)]
    doc = gdocs.get_ntb(creds, doc_id)
    print(f"The title of the fetched document is: {doc.get('title')}")
    jdsave.save_ntb(doc, doc_id)

if __name__ == "__main__":
  main()
