---
title: "Editing a Project Group"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/editing-a-project-group.html"
content_id: "eE8D3Ksoca83z0NsHLRDeA"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:31:19.491971+00:00"
---

# Editing a Project Group

Once you have created a project group, you can add project and project group children,
individual members, and/or user groups. You can also change the project group's name or
description as well as set the option to validate the generation of SBOM reports against
policies for projects belonging to specific project groups.

To do so, follow the steps listed below:

1. Log in to Black Duck.
2. Click [image: Administration icon] .
3. Select **Project Groups** to display the Project Group Management page.

     
    [image: image]

## Editing the name or description

By default the root level project group is called "Black Duck Project Groups" but it
can be renamed.

1. Click [image: image] and select **Settings** from the dropdown menu.
2. Edit the name of the project group in the **Group Name** field. This field
   is mandatory.
3. Edit the description for the project group in the **Description** field.
   This field is optional.
4. Click **Save**. The Project Group Management page updates to display the
   new group.

## Adding project sub-groups

1. Click [image: image] and select **Groups and Projects** from the dropdown menu.
2. Click [image: image] and
   select **Create New...** from the dropdown menu.
3. In the Create New Project Group dialog box:

   1. Type the name of the project group in the **Group Name** field.
      This field is mandatory.
   2. Type a description for the project group in the **Description**
      field. This field is optional.
   3. Click **Save**. The Project Group Management page updates to
      display the new group.

## Removing project sub-groups

1. Select the desired project group from the project group tree in the left-hand
   panel. This displays all child project groups in the right-hand panel.
2. Click [image: image]
3. Select **Delete** from the dropdown menu.
4. Click **Delete** from the confirmation dialog box.

If the project group is a child of a parent group:

1. Select the parent of the desired project group from the project group tree in
   the left-hand panel. This displays all project sub-groups for that project
   group in the right-hand panel.
2. Click [image: image]
3. Select **Delete** from the dropdown menu.
4. Click **Delete** from the confirmation dialog box.

## Moving a project group to a different project group

1. Select the parent of the desired project group from the project group tree in
   the left-hand panel. This displays all child project groups for that project
   group in the right-hand panel.
2. Click [image: image]
3. Select **Move**
4. Select a project group game from the Group Name dropdown menu presented in
   the **Move Selected Group to...** dialog box.
5. Click **Save** to confirm the move.

## Moving another project group into the selected group

1. Select the project group from the project group tree in the left-hand panel.
   This will display the details for the project group itself.
2. Click [image: image] .
3. Select **Move existing...**
4. Select a project group game from the Group Name dropdown menu presented in
   the **Move Selected Group to...** dialog box. Please note, a project
   group cannot be moved into the selected project group if it is an ancestor
   of the selected project group.
5. Click **Save** to confirm the move.

## Adding a member to a project group

1. Select the desired project group from the project group tree in the left-hand
   panel.
2. Click [image: image] and select
   **Users** from the dropdown menu.
3. Click [image: image] .
4. Type or select a user name from the Users dropdown menu to open a list of
   members.
5. Select any role(s) that user will have for that project group. For more
   details regarding user roles, see Understanding roles.
6. Click **Save**.

## Removing a member from a project group

1. Select the desired project group from the project group tree in the left-hand
   panel.
2. Click [image: image] and select
   **Users** from the dropdown menu.
3. Click [image: image] .
4. Select **Delete Direct Access**.
5. Click **Delete** from the confirmation dialog box.

## Editing a member's roles in a project group

1. Select the desired project group from the project group tree in the left-hand
   panel.
2. Click [image: image] and select
   **Users** from the dropdown menu.
3. Click [image: image] .
4. Select **Edit Direct Access**.
5. Add or remove any role(s) that user will have for that project group. For
   more details regarding user roles, see Understanding roles.
6. Click **Save**.

## Adding a user group to a project group

1. Select the desired project group from the project group tree in the left-hand
   panel.
2. Click [image: image] and select **User Groups** from the dropdown menu.
3. Click [image: image] .
4. Type or select a user name from the User Group dropdown menu to open a list
   of user groups.
5. Select any role(s) that user group will have for that project group. For more
   details regarding user roles, see Understanding roles.
6. Click **Save**.

## Removing a user group from a project group

1. Select the desired project group from the project group tree in the left-hand
   panel.
2. Click [image: image] and select **User Groups** from the dropdown menu.
3. Click [image: image] .
4. Select **Delete Direct Access**.
5. Click **Delete** from the confirmation dialog box.

## Enabling or disabling SBOM report validation

When setting is enabled, the ability to generate SBOM
reports will be disabled if the project has policy violations.

1. Select the desired project group from the project group tree in the left-hand
   panel.
2. Click [image: image] and select
   **Settings** from the dropdown menu.
3. Scroll to the **Reports** section.
4. Check or uncheck the **Don't generate SBOM reports for projects with policy violations**
   checkbox.
5. Select either:

   - **Apply setting to all projects in this group only**: Selecting this
     option will make it so that only this specific project group will have
     validation enabled when generating a SBOM report.
   - **Apply setting to all projects in this group and child groups**:
     Selecting this option will make it so this project group and all its
     child groups will have validation enabled generating a SBOM report.

## Editing SBOM and VEX fields

These are additional fields that can be included in the SBOM report.

1. Select the desired project group from the project group tree in the left-hand
   panel.
2. Click [image: image] and select
   **SBOM & VEX fields** from the dropdown menu.
3. Edit any of the following fields:

   - **Creator**: Replaces default creator information with the person(s) or organization(s)
     that created the SBOM file.
   - **Namespace**: The Namespace is a URL that is under control of your organization and
     can be used as a globally unique identifier for the VEX document
     issuing party. E.g., "https://www.mycompanyname.com"
   - **Creator Comments**: An optional field for creators of the SBOM
     file to provide general comments about the creation of the SPDX file
     or any other relevant comment not included in the other fields.
   - **VEX Legal Disclaimer**: An optional field to define your organization's legal
     disclaimer for VEX documents. If populated, this text will be
     automatically included in all generated VEX reports and
     cannot be excluded.
   - **Propagate field values to all child groups**: When enabled, all project groups under
     this group will inherit the field values, but they can be overriden
     in each group.
