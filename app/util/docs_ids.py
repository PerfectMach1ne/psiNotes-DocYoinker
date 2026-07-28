#### docs_ids.py #####
#### Literally just a list of Google Doc IDs lol ####
###
##
#

DOCUMENT_IDS = {
	"0": "1HBPgLziAX2HG9rgtShM1pq2n710qmQi9DLZTZBAU25E",
	"A&M": "1xvy_JRqsYY-qSEcwylL_5nBubLNtkDJb5otq_C_03hY",
	"B1": "1zWZL0GyYb_uM2vJaP384nmyajioygD1viWTZuCSl5sU",
	"B2": "",
	"C1": "1X2yIsOxmf8Ic6RYuAG5ZV9Ru9OOH3aloRcAKSjDRkGM",
	"C2": "1fLyzY6NaSRK1DbRcdNZOQK3fufGBCBDGdtRs6qczpfw",
	"CS": "1bJfCXJYjRITR9V7hJwZ2iaY7Leld8PIdRR4h51N8nCU",
	"EE1": "1ystzIw9OHbofu2B4iGF6gWu2fW9T4bQYbCz05yY1KxY",
	"EE2": "",
	"M1": "1fz6j5w-gRXjCB6A2YbGQ8nM6YWFTutaRBLvcFss0ZpI",
	"M2": "1atUiihcPNvC6ZJ6zaNojDx4xlyAYLdFpMfhGF_0AS8A",
	"M3": "1B3wYPnc0o-pXTQ9-VUc_LiJ6paK7evIwy9SeTKGXFDc",
	"M4G": "",
	"P1": "1Rd4AC_L55x6gUJv-PJml873m1Dfjos9FKvycyKInA8U",
	"P2": "1RSSwYydFolNc4p4JK-naT1SZMQHPtWL2R5GO0KgQIp0",
	"P3P": "",
}

NTB_SERIES = {
	"0": "Zero",
	"A&M": "Astronomy && Meteorology",
	"B": "Biology",
	"C": "Chemistry",
	"CS": "Cognitive Sciences",
	"EE": "Electrical Engineering",
	"M": "Mathematics",
	"P": "Physics",
}

# NOTE: This IGNORES ALL notebooks that DON'T have a pre-existing omega Notes GDoc!!
def get_all_ntb_ids() -> dict[str, str]:
    existing_ntb_ids = {
		omega_id: gdoc_id for omega_id, gdoc_id
		in DOCUMENT_IDS.items() if gdoc_id != ""
	}

    return existing_ntb_ids


NOTEBOOK_IDS = get_all_ntb_ids()
SERIES_IDS = list(NTB_SERIES.keys())
OMEGA_IDS = list(NOTEBOOK_IDS.keys())