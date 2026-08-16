---
title: "SCM derivation rules"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/scm-derivation-rules.html"
content_id: "sjM2uoLcvH5SZzzsJELdSw"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:50:30.586849+00:00"
---

# SCM derivation rules

Coverity Connect can apply one of a number of rules to derive the owner of an issue based
on SCM history. The rule that you choose is applied to all streams in the project that
are configured to accept SCM data for owner assignment (see Setting stream-level rules).

It is not required that you configure this property, as there is the default setting,
Set to last user to modify any line in the event tree.
However, you might find that a different rule is more appropriate for assigning owners
within your system.

The following table lists the derivation rules available for configuration in Coverity
Connect and shows the corresponding rule name used in the `cov-blame
--owner-assignment-rules` command line option. For descriptions of the
rules, see the `--owner-assignments-rules` option for
`cov-blame`
in the Coverity 2026.6.0 Command Reference.

Table 1. Automatic ownership assignment rules

| SCM rule | cov-blame rule |
| --- | --- |
| Set to last user to modify file of main event | file |
| Set to last user to modify line of main event | line |
| Set to last user to modify the function of main event | function |
| Set to last user to modify top of the event tree | top_events |
| Set to last user to modify any line in the event tree | all_events |
| Set to last user to modify any function in the event tree | all_functions |
| Set to last user to modify any file in the event tree | all_files |
