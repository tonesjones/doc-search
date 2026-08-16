---
title: "Configuring components"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/configuring-components.html"
content_id: "ciWblxA0KzfowUn2c6nrBQ"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:50:16.045502+00:00"
---

# Configuring components

Configuring and using the Coverity Connect components feature requires multiple
procedures and options over several areas of the interface. This section provides
procedures for setting up components. Subsequent sections provide more detailed User Scenarios that provide examples of
component configuration and user interaction.

**To configure a component:**

1. Create a component map.

   A user with configuration privileges creates a component map that describes how
   to map source code files and analysis issues into components.

   UI Location: Configuration > Component Maps

   Figure 1. Component map settings
     
    [image: image]

   To create a new component map, select Add. To copy an
   existing component map, select a component map from the list and click
   Duplicate. The Delete button
   removes a selected component map.

   After you have added or duplicated a component map, you define the following:

   - Name - Uniquely identifies the component
     map.
   - Description - Optional description of the
     component map.
   - Stream
     associations
   - Components
   - File
     Rules
   - Default
     owner

   The Default component map is a Coverity Connect-created
   component map that consists of a single rule that maps to the catch-all
   Other component. Newly created streams and streams that
   have no component map associations are automatically associated with
   Default. Default can be edited
   or copied, but cannot be removed. When an existing component map is removed, the
   streams associated with it are re-associated to the
   Default component map.
2. Create the component.

   UI Location: Configuration > Component Maps > Components

   Figure 2. Component settings
     
    [image: image]

   To add a new component, click +. To remove an existing
   component, select one and click -. The
   Other component cannot be removed.

   After you add a new component, you define the following:

   1. **Name**

      Uniquely identifies the component.
   2. **Roles**

      The access control feature allows you to restrict users to viewing and
      triaging issues contained in a component. You define access privileges
      for users based on users and/or groups through the Coverity Connect RBAC
      feature.

      Each component can be associated with an ordered list of user or groups,
      in which each group can be assigned RBAC roles to limit or grant usage
      permissions. Any role can be assigned to a user or group within a
      component, but the only permissions that effectively limit or grant
      access are:

      - View issues
      - View source
      - Triage issues

      Coverity Connect ships with a number of pre-defined roles that contain
      these permissions, but you can create your own customized rules to limit
      or grant access. For more information about RBAC, see Roles and role-based access control.

      For example, suppose that your system contains the following groups:

      - Users contains all users on your
        system.
      - offshore contains users that represent a
        part of the engineering department that are in a different
        locale from the local developers.

      Within a component, you grant access for code and issues at the component
      level for the users group, but wish to restrict
      access to offshore:

      `Users` - Assign a global role, such as Developer, that
      includes permissions for viewing and triaging issues.

      `offshore` - Assign a role, such as No Access on a given
      component.

      Alternatively, you could grant a global No Access role for the
      User group, and grant a Developer role for
      Offshore at the component level.
3. Specify file rules.

   UI Location: Configuration > Component Maps > File Rules

   Figure 3. File Rules settings
     
    [image: image]

   To add a file rule:

   1. Click Insert Rule....

      This displays the file rules edit dialog:

        
       [image: image]   

      Insert Rule... add a new rule expression
      immediately after the selected rule (if a rule is selected). If there is
      no selection, the new rule is added at the end of the list.
   2. Enter a regular expression to map source files (see the notes below for
      more information).
   3. Add the file rule to an existing component.
   4. Click OK.

   A file represents a source file in your code. It is identified by its
   fully-qualified file path. You can exclude path prefixes for file names during
   the commit process by using the `cov-commit-defects
   --strip-path` option. For more information, see the
   `cov-commit-defects`
   documentation in the Coverity 2026.6.0 Command Reference.

   File rules contain path patterns to establish which files are mapped to the
   component. Use regular expressions to match a component's set of file names. For
   example, the following path pattern for component1 matches
   any file contained in any directory named /temp within your
   directory structure:

   `/temp/.*` (component1)

   However, /temp might exist in multiple subdirectories, so
   for component2, you might want to match only a set of
   specific file types that exist under a specific directory. The following file
   rule returns only files with the .c extension in the
   /subdir/temp directory:

   CAUTION:

   Avoid using a leading `.*` in these regular
   expressions. This can make the search considerably slower.

   `/subdir/temp/.*\.c` (component2)

   Coverity Connect maps each file to a component using the first regular expression
   that matches the entire absolute path of that file. Coverity Connect allows you
   to add multiple file rules per component map, and to set the order of precedence
   in which the file rules are executed.

   Continuing with the example, if you set the following file rule order by
   selecting the rule and using the Up or
   Down buttons:

   `/subdir/temp/.*\.c` (component2)

   `/temp/.*` (component1)

   component2 will contain only .c files
   contained in the /subdir/temp/ path, while
   `component1` will contain any file under any
   /temp directory, *except* for `.c`
   files that exist under /subdir/temp/.

   If you select Ignore lettercase in regex evaluation, all
   regular expressions will be evaluated without regards to case. If this option is
   not selected, all regular expressions will be evaluated with regards to case
   sensitivity.
4. Assign the default owners.

   UI Location: Configuration > Component Maps > Default Owners

   Figure 4. SCM system settings for automatic owner assignment
     
    [image: image]

   This optional step allows you to assign an owner to issues upon a commit based on
   the first issue component that matches the rule. Any user that is permitted to
   access a component can be designated as the default owner for all issues within
   the component. This feature is one of the configuration options for Automatic owner
   assignment.

   To assign a default owner, select a component name, click Assign
   Owner..., and then type a user name in the Default
   owner field.
5. Assign roles to the users.

   UI Location:  Configuration > Component Maps > Roles

   Figure 5. Role-assignment settings
     
    [image: image]

   Use the Roles tab to assign and manage roles for the users
   of this component map.
6. Associate streams with your component map.

   UI Location: Configuration > Projects & Streams

   Note: The Streams tab under Components
   only displays the stream that are currently assigned to the component map.
   Stream association is configurable in the location listed above.

   Figure 6. Stream settings
     
    [image: image]

   To associate a stream:

   1. Select a stream from the Projects & Streams list.
   2. Enter a component map name in the Component Map
      field.
   3. To allow a user to view the component map associated with the stream,
      make sure the user has View Component Maps permission for that component
      map.
   4. Click Done.

   When you associate a stream with a component map, it maps the source files in
   that stream into a component.

   A given stream can only be associated with exactly one component map. However, a
   component map can contain multiple streams. If a component map is not specified,
   the stream is associated with the Default component
   map.
