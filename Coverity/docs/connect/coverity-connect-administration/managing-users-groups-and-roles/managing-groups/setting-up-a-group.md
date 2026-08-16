---
title: "Setting up a group"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/setting-up-a-group.html"
content_id: "6FQieU6exawa76XhiaVBsw"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:49:40.997772+00:00"
---

# Setting up a group

Additional groups are useful if you need to assign specialized roles or LDAP properties
to a group of users.

Note: You can also import groups from external files or an LDAP server. See Importing LDAP groups.

**To add a new group:**

1. Select Configuration > Users & Groups.
2. In the Groups tab, click Add to
   create a new group.
3. Specify a unique Name for the group.
4. Specify one of the following group types:

   - Local
   - LDAP

     Select the LDAP domain, if available. The LDAP group must exist on the
     LDAP server before you add it.
5. Click Create.
6. If you selected LDAP for the Group Type, click
   Edit in Group Details to
   select the following options:

   **Refreshing LDAP group membership**

   Refresh LDAP group membership nightly
   :   There are 2 separate jobs that run to sync and delete LDAP
       Users/Groups:

       **Job #1.** nightly refresh (runs at 2 a.m.)—which just removes those users from the
       LDAP groups and moves them to default USER Group in Connect.

       **Job #2.** midnight job—disables all those users that are removed from LDAP in job
       #1.

       Since job #2 runs after job #1 by default, deleted LDAP users go to
       the Default User group until job #2 runs. Job #2 then disables those
       users. If admins want to remove these users sooner, then they can
       reschedule this job to run after 2 a.m.

   Refresh LDAP group membership now
   :   This option synchronizes members of the LDAP group with users on the
       system immediately after you apply this setting to the group
       membership.

   In both cases, new group members are added as users, and users who are no longer members of
   the group are disabled at midnight.

   To change the default schedule from 12am every night, you can add the
   `ldap.users.disabled.sync.cron.schedule` property to the
   `cim.properties` file. This property accepts a cron string in the
   same format as cron schedules in the policy manager. For example, the following string
   disables users every night at 3 a.m.: `ldap.users.disabled.sync.cron.schedule= 0
   0 3 * * *`
7. Use the Members tab to assign users to the new group.

   For guidance, see Assigning one or more users to a group.
8. Use the Roles tab to assign one or more roles to the
   group.

   For guidance, see Managing roles for a group
9. Select Done.
