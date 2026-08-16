---
title: "Scenario: Separating triage data by code branch"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/scenario-separating-triage-data-by-code-branch.html"
content_id: "6T1Ei5naH1XUcidBleSK5w"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:50:23.330288+00:00"
---

# Scenario: Separating triage data by code branch

A company might decide to create separate triage stores for the currently active (main)
and maintenance (for example, hotfix or patch) code branches so that users can triage
the same CID differently depending on the code branch. Figure 1 shows an example of
such a case. Here, there is a single Coverity Connect project for streams that contain
issue data from active branches and maintenance branches of the code base. This setup
allows users (with the appropriate permissions) to triage instances of a CID (for
example, CID 123) in both triage stores (the default) or only in one of them by
selecting the triage stores. For example, users might decide to ignore an instance of a
CID in the maintenance branch (setting the Action attribute to
Ignore) but fix the CID in the main branch (setting the
Action attribute to Fix Required).

Figure 1. Example: Updating triage value, multiple triage stores
  
 [image: image]

**To complete the scenario:**

1. When setting up Coverity Connect for the first time, the administrator uses the
   Add button to create the triage store
   that is intended for streams that contain issues from the active code
   branch.

   The example calls this triage store the Main store for convenience only. A
   company could give it any name that fits its naming conventions. Here, an active
   code branch is the branch for an upcoming release of the products.
2. The administrator makes sure that the streams are associated with the correct
   triage store:

   - When creating a stream for the active code base (here, release branch
     2.0), the administrator associates the stream with Main triage
     store.

     For information about creating streams, see Setting up streams.
   - When putting a branch of the code base into maintenance, the
     administrator creates a branch of the Main triage store, then associates the streams that contain issues for the
     maintenance release (here, rel_1.0_p1 and
     rel_1.0_p2) with this copy (here, named the
     Maintenance store for convenience).

     This action creates a triage store that contains the current triage
     history of the Main triage store. The administrator associates the
     *_1.0_* streams with the Maintenance triage store so that users will be
     able use the Advanced Triage feature to update
     CIDs in the Main triage store without triaging CIDs in the Maintenance
     triage store (and vice versa).

     Note: **Alternative to using separate triage stores**

     To avoid using separate triage stores for the streams shown in
     the example, you could use a single triage store along with a
     Fix Target attribute that identifies
     the releases (for example, `rel_1.0` or
     `rel_2.0`) in which a given CID could be
     fixed. In this way, a user who triages CID 123 could set the
     Fix Target attribute to
     `rel_2.0` and set the
     Action attribute to Fix
     Required. Though the CID would be marked as
     Fix Required for both branches, the
     Fix Target attribute would tell
     developers to fix the CID only in the active
     (`rel_2.0`) code branch, not in the
     maintenance branch. Such a scenario might be required to
     minimize the testing of the maintenance branch that is required
     prior to releasing a hotfix or patch.

     With this
     configuration, users no longer need to use advanced triage to triage
     the Action attribute of the CID differently
     in two triage stores. For more about issue attributes, see Configuring triage attributes.
3. To provide or restrict access to the Maintenance streams, the administrator can
   use the Roles menu for the Maintenance store to assign
   any necessary roles to users or groups.

   If a user or group requires a particular role, the administrator can use the
   Edit button to select that role. For example, in some
   cases, a company might not want users to triage CIDs in the Maintenance store.
   In such a case, the administrator could assign a role that gives the a developer
   group permission to view (View issues) but not triage (or
   see the triage history of) the CIDs in the maintenance streams, or that prevents
   the group from viewing or triaging instances of CIDs that are in the maintenance
   streams. For details about roles and permissions, see Roles and role-based access control.
4. Click Done to save your changes and exit.

Note: In Figure 1, streams for
the different code branches are stored in the same project so that users can take
advantage of advanced triage. However, if there is no need for advanced triage, the set
of streams for each release could be in separate project. Assuming the same triage store
associations, such a configuration would keep the triage data for each set of streams
separate. However, triaging instances of a CID that occur in both projects would require
triaging the CID twice, once in the 2.0 project, another time in the 1.0 project.
