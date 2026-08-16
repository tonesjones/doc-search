---
title: "Maintaining library files"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/maintaining-library-files.html"
content_id: "~bzIak5~cr3MhfnqiicJ_w"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:36:21.789611+00:00"
---

# Maintaining library files

You can list and remove program units contained in a Coverity Fortran Syntax Analysis
library file and can compress it.

When Coverity Fortran Syntax Analysis replaces the information of program units it
actually stores the new information at the end of the library file and updates the
index. When you remove the information of program units from the library file the
librarian only removes the index entry from the library file. To retain the free space
from the library file you have to compress it.

Also when you add the information of more and more program units the index of the library
file becomes scattered and the global program unit analysis will take more time.
Compressing the library file makes the index contiguous again.
