---
title: "Scenario: Component configuration"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/scenario-component-configuration.html"
content_id: "Lhv3vrHb794lzOL~P0eV3w"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:50:19.604534+00:00"
---

# Scenario: Component configuration

**User:**
busybox_owner

**Goal:** To create and configure a component map called busybox
that contains the following components:

core_libs
:   This component represents a section of core library files that exist in the following
    directories:

    - libbb

    - include

    The devA group is the team of developers that primarily
    works on this section of code. The devC group
    occasionally works on this section of the code.

IO
:   This component represents input and output utilities that exist in the
    archival directory. The devB
    group is the team of developers that primarily work on this code. The
    devA group occasionally works on this section of
    the code.

util
:   This component represents a series of utilities located in the following
    directories:

    - util
    - util-linux

    The devB group is the team of developers that work on
    this section of code.

3rd_party_code
:   This component represents sections of the code developed by a third party.
    The files and issues contained in this component are not to be exposed to
    Coverity Connect users.

**Configuring components:**

1. busybox_owner creates a component map.

   1. Goes to Configuration >  Component Maps.

      Coverity Connect automatically creates the Default
      component map. This component map can be copied or edited, but not
      deleted.
   2. Clicks Add to create a new component map.
   3. Enters busybox as the component map name.
   4. Adds a description of the component map (this step is optional).
   5. Instead of adding a new component each time,
      busybox_owner can use the
      Duplicate button to copy an existing
      component map and then edit it.
2. Adds the first component definition for the busybox
   component map (more components are added later in this scenario).

   1. While the busybox component map is selected,
      busybox_owner clicks Add
      to add a new component and names it
      core_libs.
   2. Selects core_libs to edit it.
3. Defines file rules in the File Rules tab.

   1. Uses a regular expression pattern to match files that belong to a
      component. File rules are added by using the Insert
      Rule... button.

      busybox_owner adds the following file rules:

      `/libbb/.*`
      :   Maps all files and issues contained in the
          /libbb directory to this
          component.

      `/1_9_2/include/.*`
      :   Maps all files and issues contained only in the
          /1_9_2/include/ directory to this
          component. This file rule specifies the
          /1_9_2 because other
          /include subdirectories exist, but
          the files contained within them are not applicable to the
          development groups associated with this component.
   2. For each file rule added, busybox_owner selects and
      assigns core_libs from the
      Components auto-complete field.
4. (This step is optional) - In the Default Owner tab,
   busybox_owner chooses to define
   user1 as the default owner for the
   core_libs component.
5. Goes to the Components tab to add access control for the
   development groups working on the files and issues defined in the component.

   1. Clicks Add open the RBAC selection list.
   2. Enters devA in the Group/User
      field.
   3. Assigns the Developer role to the group.
   4. busybox_owner enters devC and
      assigns the Developer role.
6. busybox_owner associates streams with the component map.

   1. Goes to Configuration > Projects & Streams.
   2. Selects the allnoconfig stream and adds the
      busybox component map to it.
   3. Selects the allyesconfig stream and adds the
      busybox component map to it.
   4. Clicks Done to finalize the changes and exit the
      screen.

   Note: If busybox_owner copies a stream (for example,
   allyesconfig), the copied stream is associated with the
   same component map (busybox).
7. Repeats the Add Component procedure for the IO component
   with the following configuration:

   **File Rules:**
   `/archival/.*`

   **default owner:**
   `user6`

   **Access Control:**
   `devB - Developer`, `devA - Developer`
8. Repeats the Add Component procedure for the util component
   with the following configuration:

   **File Rules:**
   `/runit/.*\.c`

   `/util-linux/.*\.c`

   These files rules return files with the `.c` suffix in the
   designated directories.

   **default owner:**
   `user6`

   **Access Control:**
   `devB - Developer`
9. Repeats the Add Component procedure for the 3rd_party_code
   component. This component is defined so that third party code, and its
   associated issues, are not exposed. In this scenario, header
   (.h) files that exist in directories other than those
   defined in the previous components represent third-party code. The configuration
   is:

   **File Rules:**
   `\.h`

   **default owner:** Not set (no action required).

   **Access Control:**
   `devC - Developer`, `devA - Developer`
10. Establishes the file rule order in the File Rules tab.

    If a file matches multiple component specifications, it is assigned to the first
    component in the list (from top to bottom). busybox_owner
    changes the order of components as follows:

    1. Selects the file rule, and then clicks the up or
       down buttons.
    2. Repeats this process (if necessary) to get the desired ordering.
    3. Clicks Done to finalize the changes and exit the
       screen.

       Figure 1. File Rules tab
         
        [image: image]
11. Observes the effects of changes to the component rules in the configuration area
    prior to applying the changes.
12. Clicks Done to update all changes in the system.
