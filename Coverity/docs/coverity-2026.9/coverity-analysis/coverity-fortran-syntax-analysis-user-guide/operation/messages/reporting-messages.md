---
title: "Reporting messages"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/reporting-messages.html"
content_id: "~g7d2EBHb9ycSiQTNBYlhg"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:33:34.685878+00:00"
---

# Reporting messages

The maximum number of messages that will be presented in a statement, argument list, or
common list is 6 by default. This number can be changed by specifying:

```
max msg = n
```

in the [VARIOUS] section of the configuration file.

During subprogram analysis a message is presented in the listing file after the relevant
source code statement. In the report file, or if no listing file has been requested the
message is generally preceded by the source code statement. You can suppress the source
code statement in the report file by specifying:

```
source stm = ’no’
```

in the [VARIOUS] section of the configuration file. You also can suppress only the line
or statement number of this source code statement:

```
source linstm number = ’no’
```

When presenting a message Coverity Fortran Syntax Analysis adds a line with the filename
and line number. The format of this line can be specified, e.g.:

```
file line format = ’("(file: ",a,", line: ",i0,")")’
```

The output of the filename and line can me made gnu-conforming by specifying:

```
file line format = ’(a,":",i0,":")’
```

If you replace the i0 edit descriptor by an x the line number will be suppressed.
