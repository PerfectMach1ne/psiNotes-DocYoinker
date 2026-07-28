##### parser/parsercore.py #####
#### Core features for the parser based on the argparse module. ####
###
##
#

import argparse

from parser.dualpoolaction import DualPoolAction
import util.docs_ids as docs_ids


GREEN = "\033[32m" # ourple on my machine
RED = "\033[33m" # also red on my machin
RESET = "\033[0m"


parser = argparse.ArgumentParser(
	prog='./app/DocYoinker',
	description="Python interface for fetching omega Notes Google Docs \
    and converting them to HTML+CSS formatted psi Notes format.",
	epilog='Copytop Luka Vivi Starr Alice & TSoRE 02.2024-07.2026'
)

get_args_desc = parser.add_argument_group('GET requests', 'Fetches a Google Doc from Google Doc API in JSON doc format.')
get_args = get_args_desc.add_mutually_exclusive_group()
get_args.add_argument('-f', '--fetch', choices=docs_ids.OMEGA_IDS, nargs='+',
    help='Fetch and print a Google Doc\'s Body content (as JSON doc). WARNING: Some JSON docs are incredibly long!')
get_args.add_argument('-s', '--save', choices=docs_ids.OMEGA_IDS, nargs='+',
    help='Fetch and save a Google Doc\'s Body content to the yoinkstash directory.')
get_args.add_argument('-p', '--posobj', choices=docs_ids.OMEGA_IDS, nargs='+',
	help='Fetch PositionedObjects from a Google Doc and save them to the yoinkstash directory in correct format.')

# subcommands = parser.add_subparsers(title='Subcommands')

subcom = parser.add_subparsers(
	title='Available DocYoinker subcommands',
	description="View and edit the Table of Contents Google Sheet and use features for chi Notes integration.",
	dest='subcommand',
	help=f"See '{GREEN}toc -h{RESET}' or '{GREEN}toc --help{RESET}' for subcommand arguments."
	f" There are two available subcommand groups: '{RED}[toc|tableofcontents, chi|chinotes]{RESET}'"
)
toc_args = subcom.add_parser('toc', aliases=['tableofcontents'])
toc_args.add_argument('-la', '--listall', action='store_true',
	help="List a \'prettyformatted\' list of all Notebook series tables of contents")
toc_args.add_argument('-s', '--select', choices=docs_ids.SERIES_IDS, nargs=1, default='0',
	help="Select a Notebook series' table of contents sheet into the working memory.")
# TODO: default should be a variable loaded from a data file!!
toc_args.add_argument('-l', '--list', choices=docs_ids.SERIES_IDS, nargs='?', default='0',
	help="List ALL chapters & subchapters from EVERY Notebook series.")
toc_args.add_argument('-lc', '--listchapters', choices=docs_ids.SERIES_IDS, nargs='?', default='0',
	help="List all chapters of a selected Notebook series")
toc_args.add_argument('-lsc', '--listsubchapters', action=DualPoolAction, nargs='+',
	choices=docs_ids.SERIES_IDS,
	metavar=(docs_ids.SERIES_IDS, 'chapter_number'),
	help="List all subchapters under a selected Notebook series' chapter.")
# TODO: These r 'store_true's for now until i will feel like implementing them lol
toc_args.add_argument('-i', '--insert', action='store_true',
	help="Insert a chapter or a subchapter.")
toc_args.add_argument('-d', '--delete', action='store_true',
	help="Manually delete a chapter or a subchapter.")
toc_args.add_argument('-u', '--update', action='store_true',
	help="Update a chapter or a subchapter.")
# toc_args= parser.add_argument_group('Table of Contents operations', '')
# toc_args.add_argument('-t', '--toc', choices=docs_ids.OMEGA_IDS, nargs='+',
# 	help='Load the Table of Contents of a specified Notebook series.')

# TODO: default should be a variable loaded from a data file!!
chi_args = subcom.add_parser('chi', aliases=['chinotes'])
chi_args.add_argument('--refresh', '-r', choices=docs_ids.OMEGA_IDS, default='0',
	help="Refresh the core structure of a selected chi Notes notebook from the `main.tex` template.")

parser.add_argument('--shut-up', action='store_true',
    help='Turn off verbose mode (on by default).')
parser.add_argument('--shutup', action='store_true',
	help='Don\'t turn off verbose mode and call out user\'s skill issue.')
parser.add_argument('--test', action='store_true',
    help='Unused argument for testing features in development.')


args = parser.parse_args()
