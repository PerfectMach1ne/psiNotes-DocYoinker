import argparse
import util.docs_ids as docs_ids


parser = argparse.ArgumentParser(
  prog='./DocYoinker',
  description="Python interface for fetching omega Notes Google Docs \
    and converting them to HTML+CSS formatted psi Notes format.",
  epilog='Copytop Luka Vivi Starr Alice 02.2024-09.2024'
)
get_args_desc = parser.add_argument_group('GET requests', 'Fetches a Google Doc from Google Doc API in JSON doc format.')
get_args = get_args_desc.add_mutually_exclusive_group()
get_args.add_argument('-f', '--fetch', choices=docs_ids.OMEGA_IDS, nargs='+',
    help='Fetch and print a Google Doc\'s Body content (as JSON doc). WARNING: Some JSON docs are incredibly long!')
get_args.add_argument('-s', '--save', choices=docs_ids.OMEGA_IDS, nargs='+',
    help='Fetch and save a Google Doc\'s Body content to the yoinkstash directory.')
get_args.add_argument('-p', '--posobj', choices=docs_ids.OMEGA_IDS, nargs='+',
  help='Fetch PositionedObjects from a Google Doc and save them to the yoinkstash directory in correct format.')
parser.add_argument('--shut-up', action='store_true',
    help='Turn off verbose mode (on by default).')
parser.add_argument('--shutup', action='store_true',
  help='Don\'t turn off verbose mode and call out user\'s skill issue.')
parser.add_argument('--test', action='store_true',
    help='Unused argument for testing features in development.')



args = parser.parse_args()