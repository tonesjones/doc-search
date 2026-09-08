---
title: "Creating and Editing Policies"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/creating-and-editing-policies.html"
content_id: "JIW_DHLIa~D2yPGHkp4sPA"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:03:25.622567+00:00"
content_hash: "8262afa11937a3d36fb3b1b9c6aaddd8370817dce423e3159eca4dda379ee80e"
---

# Creating and Editing Policies

Policies are created and updated from the Policies page. (Note that there are often
alternative ways to perform the same task. The most common are detailed below.)

- Creating a Policy
- Editing a Policy
- Deleting a Policy

Note: Policy functionality is role-based: users assigned to the "Manager" role are limited to assigning and removing
projects.

## Creating a Policy

**To create a new policy:**

1. Click the Policies icon in the navigation bar to open the Policies page.

   [image: image]
2. Click Add Policy to open the policy description window.

   [image: image]
3. Enter a name (required) and description for the policy

   The
   policy name must be unique. A description is not required, but it is
   recommended.
4. Configure the sharing settings for the policy, then click Next.

   By default, a policy can only be viewed and edited by
   the user who creates it. Once projects are associated to the policy, any users who can view at least
   one of those projects will be able to view the policy.

   [image: image]
5. Click Add Rule to assign rules to the new policy.

   Clicking Add Rule opens a
   dialog where you can configure new rules.

   [image: image]
6. Use the dropdown options to configure the policy rule.

   Creating a rule includes
   configuring the following elements:
   - **On/Off toggle.** Allows individual rules to be temporarily
     deactivated.
   - **Threshold.** Sets the minimum number of findings needed to trigger
     the rule.
   - **Filter.** Defines which filters the policy will use. Select filters
     from the dropdown list. (**Note:** Private saved filters must be
     shared before they can be applied. For more information, see Saving Filters.) Use
     the search field to search for existing filters.

     [image: image]

     Note: Regarding the use of the Policy Violations and
     Policy Violation Urgency filters in saved private filters, if either
     (or both) of these filters are added to a saved filter, those
     options will be ignored when using that filter as a Policy
     rule.
   - **Fix by.** Sets the number of days before the violation status
     changes to overdue. Select the number of days from the dropdown list.
     Select "Not Required" if no date is necessary.

     [image: image]
   - **Action.** Specifies what action should be taken when the rule is
     violated. The options are "Nothing," "Create ticket(s)," and "Break
     Build."

     [image: image]
7. Click Next to open the Projects window.

   [image: image]
8. Click Add Project to open the Add Projects to Policy window.

   [image: image]
9. Select the projects to associate with this policy and click Add Projects.

   Use the
   checkboxes to select projects. You can search for projects using the search
   field. The Current Policies column shows the number of policies that have
   already been assigned to that project.
10. Click Finish.

## Editing a Policy

**To edit an existing policy:**

1. Click the Policies icon in the navigation bar to open the Policies page.

   [image: image]
2. Click the policy's dropdown configuration icon and select Edit.

   [image: image]
3. Make changes as necessary.

   For field definitions, see the descriptions in
   the Creating Policies section.
4. Click Finish.

## Deleting a Policy

**To delete an existing policy:**

1. Click the Policies icon in the navigation bar to open the Policies page.

   [image: image]
2. Click the policy's dropdown configuration icon and select Delete.

   [image: image]
3. Click Delete to confirm.
