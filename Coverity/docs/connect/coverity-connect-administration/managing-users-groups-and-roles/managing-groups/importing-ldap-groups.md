---
title: "Importing LDAP groups"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/importing-ldap-groups.html"
content_id: "vFSK0vTvxPyD3gvxE9KceQ"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:49:43.488149+00:00"
---

# Importing LDAP groups

You can import one or more LDAP groups at once.

Note: The Group Filter can now be applied to either top-level and nested groups, or just
top-level groups. By default it applies to both.

To import only top-level groups, go
to Configuration > System > LDAP Configuration > ldap and uncheck **Retrieve group members from nested
groups**.

1. Navigate to Configuration > Users & Groups.
2. Click Import to open the Import LDAP
   Groups window.
3. Import one or more groups:

   1. If multiple domains appear in a drop-down list, select the correct
      domain, and then click Next.

      If not, proceed to the next step.
   2. Select one or more groups to import, and then click
      Next.
   3. Confirm the list of groups by clicking Next. A
      table that lists all of your group memberships should appear.
   4. If you receive an error notification, click Back
      and fix these problems, or click Next to continue
      the import without these groups.
   5. Select any of the following options:

      - Lock accounts (users must use recover password to
        unlock)
      - Disable accounts (users cannot sign
        in)
      - Email sign in instructions to users after
        adding
      - Refresh LDAP group membership
        nightly

      Note: For the Lock accounts and Email sign
      in instructions to be enabled, it is necessary for
      Coverity Connect e-mail to be enabled. For details, see Configuring Email notification and delivery.
   6. Click Finish.
   7. Click Done.
4. Click Done.
