---
title: "Scenario: Sharing triage data across code branches (recommended)"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/scenario-sharing-triage-data-across-code-branches-recommended-.html"
content_id: "UXj95r5GbQPMwNgiZ9GMHQ"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:50:22.557153+00:00"
---

# Scenario: Sharing triage data across code branches (recommended)

Issues share the same CID when Coverity determines that the same fix is required for
them, and most instances of a given CID are very similar issues that are found in
separate code branches.

In general, managing and tracking issues is simplified if all instances of a given CID
are triaged in the same way, regardless of the code branches in which they are found.
Historically, Coverity customers have usually triaged the same CID differently (for
example, marking the CID as a Bug in the main development branch
but as Intentional in the maintenance branch) when it was risky
to fix the CID in the maintenance branch. However, the Fix Target
attribute (introduced in version 6.0.2) diminishes the need to triage the same CID
differently (for details, see Alternative to using separate triage stores). Further, in many cases, the
same developer is the Owner of a given CID. Because of such
considerations, Coverity recommends using a single triage store (the Default Triage Store) for
all streams.

In the simplest case, where all streams across projects in a given Coverity Connect
instance share the same triage store, the triage values for a CID that occurs in these
streams will always be unified across streams in all projects.

In Figure 1, the Coverity Connect
streams share the same triage store (Default Triage Store). When a user triages CID 123
in the CodeBranch_1.0 project (by changing the classification from
Unclassified to Bug), the Default
Triage Store is updated with the new triage values for CID 123. Because the streams
rel_1.0_p1 and rel_2.0_p1 are associated with
the same triage store, they share the same triage values for CID 123.

Figure 1. Example: Updating triage value, single triage store
  
 [image: image]

The following procedure explains how to set up the scenario described in Figure 1.

**To use a single triage store:**

1. When creating a stream, always associate the stream with the Default
   Triage Store.

   For information about creating streams, see Setting up streams.
2. If any streams are currently associated with another (non-default) triage store,
   determine whether to re-associate the
   streams with the Default Triage Store. You can
   use the drop-down menu in the Streams tab to associate
   the streams with the Default Triage Store.
3. If necessary, use the Roles tab for the Default
   Triage Store to assign any necessary roles to users
   or groups.

   If a user or group needs a different set of roles, you can use the
   Edit button to select or deselect its roles.

   For example, one role might allow your developer groups to triage issues in the
   store, while another role might allow an administrative group to manage the
   Default Triage Store.
4. Click Done to save your changes and exit.
