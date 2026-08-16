---
title: "Tuning the output"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/tuning-the-output.html"
content_id: "OM6tlp1_R7JIWjSFZ6tVWQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:36:31.555717+00:00"
---

# Tuning the output

The output options as described in Options determine which parts of
the analysis are displayed in the listing file. Moreover using the miscellaneous options
you can specify if you want to create a report file and if you want to present the
internal table usage.

Beside using these command line options you can specify what information is sent to
`stdout`, is stored in the listing file, and in the report file. You
can do this by setting keywords in the [OUTPUT] section of the configuration file. In
the following table the keywords that can be applied are listed with their meaning and
default value. Acceptable keyword values are ’`TRUE`’ and
’`FALSE’`.

| `STDOUT MSGSUM` | send message summary to stdout | true |
| `STDOUT METRICS` | send metrics to stdout | false |
| `STDOUT USAGE` | send internal table usage to stdout | false |
| `LISTING MSGSUM` | display message summary in listing file | true |
| `LISTING METRICS` | display metrics in listing file | true |
| `LISTING USAGE` | display internal table usage in listing file | false |
| `REPORT MSGSUM` | store message summary in report file | true |
| `REPORT METRICS` | store metrics in report file | true |
| `REPORT USAGE` | store internal table usage in report file | true |

For example, if you want to see the message summary on your screen and the metrics not,
you specify the following lines in the [OUTPUT] section of the configuration file:

```
STDOUT MSGSUM = ’TRUE
STDOUT METRICS = ’FALSE’
```

Note that the keyword value has to be placed within apostrophes. You can concatenate a
supplied configuration file with a private configuration file as described in the
section Redefinition and suppression of messages.
