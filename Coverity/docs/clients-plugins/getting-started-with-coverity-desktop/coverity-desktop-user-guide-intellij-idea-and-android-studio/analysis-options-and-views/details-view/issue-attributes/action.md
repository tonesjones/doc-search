---
title: "Action"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/action.html"
content_id: "Mw9_GRb5MSP8O6EDM_npVg"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:48:46.333087+00:00"
---

# Action

Actions describe what should be done about the issue in question. Coverity Connect enables you to add, delete, and rename action issue attribute values. Coverity Desktop displays these customized attributes if they exist in
the most current snapshot. For more information, see the Coverity Platform 2026.6.0 User and Administrator Guide. The default action attributes are:

Undecided
:   This attribute is the default when a new issue is inserted. It reflects that
    no decision about fixing or ignoring has been made.

Fix Required
:   The issue is outstanding and requires a fix; such an issue will continue to
    appear in future commits.

Fix Submitted
:   The issue is fixed in the source code, but the fix has not been identified as
    Fixed through the build, analysis, and commit processes.

Modeling Required
:   An investigation is required of each method in the application that is used
    for interprocedural analysis, created as each function is analyzed. For
    example, the model shows which arguments are dereferenced, and whether the
    function returns a null value. This can be a form of false positive in which
    after the modeling is corrected, the analysis will no longer report this
    issue.

Ignore
:   The issue can be ignored. This might be an appropriate action for a bug of
    minor severity.
