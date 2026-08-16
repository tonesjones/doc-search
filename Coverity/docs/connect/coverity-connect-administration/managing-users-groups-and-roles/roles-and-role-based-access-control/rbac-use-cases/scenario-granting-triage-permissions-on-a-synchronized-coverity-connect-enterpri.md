---
title: "Scenario: Granting triage permissions on a synchronized Coverity Connect enterprise cluster"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/scenario-granting-triage-permissions-on-a-synchronized-coverity-connect-enterprise-cluster.html"
content_id: "OLWH1eWpAXax0xn_s3GA5w"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:49:51.107700+00:00"
---

# Scenario: Granting triage permissions on a synchronized Coverity Connect enterprise cluster

**Goal:** To grant permissions for groups of users to be able to triage issues on a
specific stream on a subscriber instance of Coverity Connect.

In order to accomplish this, the group must have appropriate triage permissions at the
following levels:

- Triage store level (set on the coordinator)
- Component level (set on the coordinator)
- Stream level (set on a subscriber)

Note: If this scenario were to be deployed on a standalone instance of Coverity Connect, the
procedures are basically the same. Instead of performing these steps on a coordinator or
subscriber, respectively, they would be performed on the single Coverity Connect
instance.

**Scenario assumptions:** The organization has two product lines in their code base,
represented as ProductA and ProductB.

Coverity Connect is deployed as an enterprise cluster as follows:

- coordinator is the name of the installed coordinator for the
  system.
- subscriber1 is a configured subscriber of
  coordinator and contains the analysis streams for
  ProductA.
- subscriber2 is a configured subscriber of
  coordinator and contains the analysis streams for
  ProductB.

On coordinator, the following users and entities exist:

- Users and groups:

  - SysAdmin possesses one or more roles that contain
    the Manage users and groups, Manage
    component maps, Manage triage
    stores, and Manage streams
    permissions (for example, the System Administrator role).
  - The users group contains all users on the
    system.
  - Users who are a group of engineers that belong to
    DevGroupA. This group represents the engineers
    that develop ProductA.
  - Users exist on the system, some of which are a group of engineers that
    belong to DevGroupB. This group represents
    engineers that develop ProductB.
  - Some users that belong to DevGroupA and
    DevGroupB belong to a group
    calledSecurityGroup.

- Triage stores:

  - ProductAStore is the triage store that contains all
    of the development streams that represent ProductA;
    ProdAVer1.0, ProdAVer2.0,
    ProdAVer3.0 (see subscriber 1, below).
  - ProductBStore is the triage store that contains all
    of the development streams that represent ProductB; ;
    ProdBVer1.0, ProdBVer2.0,
    ProdBVer3.0 (see subscriber 2, below).

- Components:

  - Default contains component maps that are associated
    with streams pertaining to ProductA and ProductB.
  - 3rdParty contains a component map of the same name
    that is associated with third-party libraries that are to be viewed by
    select users.

On subscriber1, the following entities exist:

- ProjectA exists and contains the following streams, which
  represent release versions of ProductA.

  - ProdAVer1.0 - This stream has been marked as EOL
    (End of Life). No development or bug fixes occur on the code represented
    by this stream.
  - ProdAVer2.0 - This stream represents code that is
    currently supported, but no new features are under development. Bug
    fixes are expected.
  - ProdAVer3.0 - This stream represents code that is
    under active development.

On subscriber2, the following entities exist:

- ProjectB exists and contains the following streams, which
  represent release versions of ProductB.

  - ProdBVer1.0 - This stream has been marked as EOL
    (End of Life). No development or bug fixes occur on the code represented
    by this stream.
  - ProdBVer2.0 - This stream represents code that is
    currently supported, but no new features are under development. Bug
    fixes are expected.
  - ProdBVer3.0 - This stream represents code that is
    under active development.

**Scenario procedures:**

1. On coordinator, SysAdmin assigns the
   Developer role at the global level.

   SysAdmin accesses Configuration > Users & Groups, selects DevGroupA, and in the
   Roles tab assigns the Developer role at the global
   level. SysAdmin then repeats the role assignment for
   DevGroupB and SecurityGroup.

   - At this point, all groups have the Developer role assigned to them at the
     global level. Because there are currently no roles assigned at any of
     the "lower" roles levels, the members of the group will have the
     Developer role permissions defined for every level on the system to
     which the group will be assigned.
   - For triage purposes, the permissions that are of most interest are
     View issues, View
     source, and Triage
     issues.
2. SysAdmin assigns groups and access roles at the Triage Store
   level.

   1. SysAdmin accesses Configuration > Triage Stores.
   2. SysAdmin selects
      ProductAStore.
   3. On the Roles tab, SysAdmin
      clicks Add, starts typing in the Group
      / User box and selects DevGroupB to
      associate that group with ProductAStore.
   4. SysAdmin selects the Observer role to
      DevGroupB, and clicks
      OK.
   5. SysAdmin repeats the process but for
      ProductBStore and
      DevGroupA, respectively.
   - Access is now starting to be restricted at lower levels.
     DevGroupA has triage access only to the streams
     that are associated with ProductAStore, while
     DevGroupB has triage access only to the streams
     that are associated with ProductBStore. Each group
     has Observer permissions on the triage store of the other
     groups.
3. On coordinator, SysAdmin assigns groups
   and roles at the component level.

   1. SysAdmin accesses Configuration > Component Maps.
   2. SysAdmin selects the Other
      component (under the Default component map,
      Components tab), and in the
      Group/Users selects
      DevGroupA and DevGroupB to
      associate those groups with the component map. The groups inherit the
      Developer role on Other by virtue of the global
      Developer role assignment.
   3. SysAdmin selects the 3rdParty
      component map and under Group/Users, adds
      SecurityGroup to associate that group with
      3rdParty.
   4. SysAdmin clicks Edit and
      applies the Observer role to SecurityGroup. This
      role does not contain triage permissions, but allows the members of the
      group to view issues.
   5. SysAdmin adds DevGroupA and
      DevGroupB to the 3rdParty
      component map and assigns them the No Access role.
   - Users in DevGroupA and
     DevGroupB have triage permissions at the
     component-level role because the Developer role is inherited by virtue
     of that role's global assignment.
   - Users in SecurityGroup are the only users on the
     system that can view issues in the streams that are associated with that
     component. Furthermore, because the Observer role is assigned to the
     group at the component level, the permissions in that role take
     precedence over the permissions that are assigned to the Developer role
     at the global level. So, the members of the group can view issues and
     the source, but not triage issues in the streams that are associated
     with the component map.
4. On subscriber1, SysAdmin assigns groups
   and roles at the stream level.

   1. SysAdmin accesses Configuration > Projects & Streams, and selects ProjectA.
   2. In both ProdAVer2.0 and
      ProdAVer3.0, SysAdmin
      associates DevGroupA to them in
      Group/Users.
   3. In both ProdAVer2.0 and
      ProdAVer3.0, SysAdmin
      associates the users group to them in
      Group/Users and then assigns the No Access
      role to the users group. This ensures that no users
      on the system can access these two streams, unless explicitly given
      access permissions.
   4. In ProdAVer1.0, SysAdmin
      associates DevGroupA to it in
      Group/Users.
   5. In the Roles tab for
      ProdAVer1.0, SysAdmin
      assigns the No Access role to the group.
   - DevGroupA now has the Developer role on the
     ProdAVer2.0 and
     ProdAVer3.0 streams because the role is
     inherited from the levels above it. The members of the group can now
     view and triage the issues that exist in each stream.
   - In the ProdAVer1.0 stream,
     DevGroupA has the No Access role assigned.
     Because Coverity Connect evaluates the role defined at the most granular
     level (in this case, the stream level) and because the role definition
     does NOT contain the View issues, View
     source, and Triage issue
     permissions, the members of the group cannot view or triage issues in
     the stream.
5. On subscriber2, SysAdmin assigns groups
   and roles at the stream level.

   SysAdmin performs the same procedures described in the
   previous step for DevGroupB and users
   as they apply to the ProBAVer1.0,
   ProdBVer2.0, and ProdBVer3.0. The
   results are similar:

   - The members of DevGroupB can view and triage issues
     in the ProdAVer2.0 and
     ProdAVer3.0 streams.
   - The members of DevGroupB can not view or triage
     issues in the ProdBVer1.0 stream.
