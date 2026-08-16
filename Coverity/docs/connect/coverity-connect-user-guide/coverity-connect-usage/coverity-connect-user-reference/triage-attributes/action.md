---
title: "Action"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/action.html"
content_id: "KwjlAfTzwj8AeXwiyOZ0AQ"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:47:39.892253+00:00"
---

# Action

You use these options to describe and track an issue:

Undecided
:   Default for a new issue. Indicates that there is no decision yet whether to
    fix or ignore it.

Fix Required
:   Indicates that the issue requires a fix.

Fix Submitted
:   Indicates that the issue has been fixed. Note that issues will continue to
    appear in snapshots until they are absent from the source code, as
    determined by the analysis based on the checkers that are enabled and the
    checker options they use.

Modeling Required
:   Indicates that incorrect modeling (or the absence of modeling) is confusing
    the analysis. You can address this issue by fixing or creating the model,
    which will help the analysis in generating the correct result.

Ignore
:   Indicates that the issue can be ignored. This designation might be
    appropriate for some bugs of minor severity.

Note that a Coverity Connect administrator can add, delete, and rename these attributes.
For more information, see Configuring triage attributes.
