---
title: "Example: sign2"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/example-sign2.html"
content_id: "4jdotWDzzVj1SxS6Ozidew"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:38:42.122068+00:00"
---

# Example: sign2

The error output routines are demonstrated in the sign2.cpp checker
(see <install_dir>/sdk/samples/sign2/sign2.cpp or sign2 checker), which is an extension of the
sign.cpp checker discussed previously (see Example: tracking the sign of expressions).

The main difference between the sign.cpp and
sign2.cpp checkers is that in sign2.cpp
every call to SET_STATE is followed by a call to
ADD_EVENT. There are also some calls to
CLEAR_STATE, used to remove previously-associated events in cases
where a new value is being stored. COPY_STATE is used to copy events
from one expression to another, to reflect the history of each value.

The whatis query now uses COMMIT_ERROR to output
the events associated with the expression being queried, or
OUTPUT_ERROR if nothing is known about the expression.

The print_store query uses an ostringstream to
construct a big string, which it then sends to OUTPUT_ERROR.

Finally, this checker has some true defect detection because it recognizes typecasts from
signed to unsigned where the source might be negative. Though these potential defects
include many false positives at first, the premise for this checker is to suppress them
by adding assertions. However, in order to respond to assertions, the checker needs to
handle conditionals, which is the subject of the next section.
