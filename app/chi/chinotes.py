##### main.py #####
#### chiNotes-core, for now just a testing thing ####
###
##
#

from pathlib import Path
import re

from pylatex import Document, NoEscape

from util.docs_ids import SERIES_IDS


WORK_DIR = Path(__file__).resolve().parent
TEMPLATE_PATH = WORK_DIR / ".." / ".." / ".." / "chi_Notes_LaTeX" / "main.tex" 
CHINOTES_DIR = WORK_DIR / ".." / ".." / ".." / "chi_Notes_LaTeX" / "ntb_series"


doc = Document()


def refresh_from_template(omega_id: str):
    series = '0'
    for s in SERIES_IDS:
        if omega_id.startswith(s):
            series = s
            break

    ntb_filename = omega_id + '.tex'
    ntb_path = CHINOTES_DIR / series / ntb_filename
    
    # TODO: temporary testing garbogargbage
    code_phrase = "PREAMBLE" # there's also HEADER
    
    templ_latex = TEMPLATE_PATH.read_text(encoding='utf-8')
    ntb_latex = ntb_path.read_text(encoding='utf-8')

    extract_pattern = (
        rf"%%\s*BEGIN\s+{re.escape(code_phrase)}%?\s*\n"
        rf"(.*?)"
        rf"\n?\s*%%\s*END\s+{re.escape(code_phrase)}"
    )
    match_specialcomments = re.search(extract_pattern, templ_latex, flags=re.DOTALL)
    if not match_specialcomments:
        raise ValueError(f"Could not find comment block '%% BEGIN {code_phrase}' in {TEMPLATE_PATH}")

    extracted_latex = match_specialcomments.group(1).strip()

    inject_pattern = rf"(%%\s*BEGIN\s+{re.escape(code_phrase)}%?\s*\n)"

    if not re.search(inject_pattern, ntb_latex):
        raise ValueError(f"Target comment block '%% BEGIN {code_phrase}' missing in {ntb_path}")

    new_latex = rf"\1{extracted_latex}\n"
    updated_latex = re.sub(
        inject_pattern,
        lambda match: match.group(1) + extracted_latex + "\n",
        ntb_latex,
        count=1
    )

    ntb_path.write_text(updated_latex, encoding='utf-8')

