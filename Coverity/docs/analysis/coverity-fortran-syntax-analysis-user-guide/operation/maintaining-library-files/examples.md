---
title: "Examples"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/examples.html"
content_id: "z8hfQd9C_sHGOs5B8Lnwsg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:36:23.089863+00:00"
---

# Examples

```
fcklib -remove sub1,sub2,sub3 tstlib
```

This command will remove the program units `SUB1`, `SUB2`,
and `SUB3` from the Coverity Fortran Syntax Analysis library file
`tstlib.flb`.

```
fcklib -compress tstlib
```

This command will create a new, compressed, library `tstlib.flb` out of
the existing library `tstlib.flb`.

You can combine the `-remove` and `-compress` options in
one command:

```
fcklib -remove sub1,sub2,sub3 -compress tstlib
```

The names of the program units are converted to upper case before usage because in the
library file all names are stored in upper case characters.
