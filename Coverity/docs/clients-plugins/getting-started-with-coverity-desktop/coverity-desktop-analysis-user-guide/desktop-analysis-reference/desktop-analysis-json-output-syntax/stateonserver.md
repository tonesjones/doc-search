---
title: "StateOnServer"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/stateonserver.html"
content_id: "DtoxAH6MjN1zb8srMLZ8pw"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:47:06.522856+00:00"
---

# StateOnServer

This object represents information about the issue that is only known to the Coverity
Connect server. This object is `null` in disconnected mode.

cid: int
:   The numeric Coverity ID (CID) of the merged issue. The CID is found in the triage store for
    the stream specified in the `cov-run-desktop` command.

triage: Triage
:   An object containing the current values of the *built-in* triage attributes for this
    defect. These values are described in the Triage section.

customTriage: CustomTriage
:   An object containing the current values of the *user-defined* triage attributes for
    this defect.

presentInReferenceSnapshot: boolean
:   True if the issue is present in the reference snapshot specified in the
    `cov-run-desktop` command, false if not.

firstDetectedDateTime: string
:   The date and time when the issue was first detected in the stream. It expresses the date
    and time with the granularity of seconds in the time zone where the
    producing program is invoked, and includes that time zone expressed as a
    positive or negative offset from GMT.

    For example:
    `2013-05-04T19:47+07:00`

stream: string
:   The name of the stream specified in the `cov-run-desktop` command.

components: [string]
:   A list of components in which the issue occurrences with the same merge key appear.

componentOwners: [string]
:   A pair of strings for the component's `componentDefaultOwner` and
    `componentDefaultOwnerLdapServer`. The values of the two
    fields will be null if the component does not have a default owner.

cached: boolean
:   True if `cov-run-desktop` was run in disconnected mode and the state was
    cached from a previous connected run. If false,
    `cov-run-desktop` was able to obtain up-to-date triage
    data by connecting to Coverity Connect.

retrievalDateTime: string
:   The date/time when the state was last retrieved. If `cached` is
    `false`, this is the time that
    `cov-run-desktop` was run. Otherwise, it is the
    invocation time of the last `cov-run-desktop` process that
    successfully retrieved data from Coverity Connect.

ownerLdapServerName: string
:   The LDAP server of the defect owner. An empty string indicates that the
    `ownerLdapServerName` is null. Added in version 3.
