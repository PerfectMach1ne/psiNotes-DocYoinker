##### main.py #####
#### psiNotes-DocYoinker core! Here be things getting launched (and dragons!). ####
###
##
#

import oauth2 
import gdocs
import jsondocs.jsonsaver as jdsave
import jsondocs.jsonloader as jdload


def main():
  creds = oauth2.google_docs_auth()

  # Is this a bit unnecessary...? Yeah!
  notebooks = gdocs.get_all_ntb_ids() # Only contains the dict with IDs, not actual Document objects
  omega_ids = list(notebooks.keys())
  ntb_0_omega_id = omega_ids[omega_ids.index("0")]
  ntb_0 = gdocs.get_ntb(creds, ntb_0_omega_id)

  jdsave.save_ntb(ntb_0, ntb_0_omega_id)

  # print(f"The title of the document is: {ntb_0.get('title')}")
  # print(json.dumps(ntb_0.get('body'), indent=' ' * 4))


if __name__ == "__main__":
  main()
