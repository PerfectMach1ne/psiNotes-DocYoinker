##### parser/dualpoolaction.py #####
#### Custom parser Action for  ####
###
##
#

import argparse
from util.docs_ids import SERIES_IDS


class DualPoolAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        if len(values) > 2:
            parser.error(f"{option_string} accepts at most 2 values, got {len(values)}.")

        req_arg = values[0]
        opt_arg = values[1] if len(values) == 2 else 0 # Go for chapter 0 by default.

        if req_arg not in SERIES_IDS:
                parser.error(
                    f"invalid choice for first argument: '{req_arg}' "
                    f"(choose from {sorted(CHOICES_A)})"
                )

        if not isinstance(opt_arg, int):
                parser.error(
                    f"invalid choice for second argument: '{req_arg}' "
                    f"(only provide integer values)"
                )

        # Set the attributes of the Action (I think)
        settattr(namespace, self.dest, (req_arg, opt_arg))
