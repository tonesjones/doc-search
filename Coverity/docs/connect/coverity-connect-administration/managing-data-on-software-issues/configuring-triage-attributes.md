---
title: "Configuring triage attributes"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/configuring-triage-attributes.html"
content_id: "kGpoazMhf33gw3vG2JeUIg"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:50:11.897435+00:00"
---

# Configuring triage attributes

Developers use these attributes to triage software issues through the
Triage panel in Coverity Connect. The
Attributes menu allows you to edit some of the built-in
attributes and to create and edit custom attributes.

There are many conceivable scenarios for using a custom attribute. The following scenario
uses a custom attribute to identify the version (or branch) of the code base in which a
bug should be fixed.

Assume that developers are working on multiple branches of the same code base and that
issue data from each branch is submitted to separate streams in a Coverity Connect
project (Project 1):

- Branch 1 of the code base is analyzed and committed to streamV1 in Coverity
  Connect.
- Branch 2 of the code base is analyzed and committed to streamV2 in Coverity
  Connect.

In such a case, you might use the built-in Fix Target attribute to
list all versions (or releases) in which bugs might be fixed (for example, v1 and v2).
Developers can then mark the version in which the bug should be fixed. For example,
assume that both code branches contain the same issue (CID 123). If CID 123 is a bug,
developers might set the Fix in attribute to Version 2 (v2), for
example, if there is no time to fix it in Version 1, or if the bug is of lower priority
than others. However, if time permits, they might reset the Fix
in attribute for the CID to Version 1 (v1). Both branches will share the
same setting for the CID if the stream for each branch is associated with the same
triage store (see Managing triage stores). Note that after creating the
appropriate values for the Fix in attribute, you also need to
select the Show in triage panel option. For details, see Editing triage attributes.
