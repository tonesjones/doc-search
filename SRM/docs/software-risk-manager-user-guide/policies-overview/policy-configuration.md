---
title: "Policy Configuration"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/policy-configuration.html"
content_id: "8O5AqpIFOKYED0zQm484qA"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:03:24.647785+00:00"
content_hash: "b18e8966fb10bec9a87f69d70a0aa3a80081ae0fe3e81d94f664b6835560cd12"
---

# Policy Configuration

A policy consists of three parts:

- **Description.** The policy name and its purpose.
- **Rules.** The conditions that define the policy.
- **Projects.** The projects that will use the policy.

When creating, editing, or viewing policies, each part—Description, Rules, Projects—will
be displayed in a separate window. Clicking the "button" tabs along the top will switch
to that corresponding window. Click Done to close the window.

[image: image]

## Viewing Policy Configuration

Policy definitions can be displayed from the Policies page.

**To view the configuration of an existing policy:**

1. Click the Policies icon in the navigation bar to open the Policies page.

   [image: image]
2. Click a policy name to open the Policy Description window for that policy.

   [image: image]

   The Description window displays the following information:
   - **Policy Name.** The name of the policy.
   - **Description.** A description of the policy.
   - **Filter Rules.** The number of rules used to define the
     policy. Click the link to display the filter rules. (This is the
     same as clicking the Rules tab.)
   - **Projects Using this Policy.** The number of projects that
     use this policy. Click the link to display a list of projects
     that use this policy. (This is the same clicking the Projects
     tab.)

   Note: Click Done to close the window. Click Close and Edit to
   open a window where you can edit the policy's configuration. For more
   information, see Creating a
   Policy.
3. Click the Rules tab to see a list of all the rules that define the
   policy.

   [image: image]
4. Click the Projects tab to see a list of all the projects that use this
   policy.

   [image: image]

   Use the search field to search for specific
   projects.
5. Click Done to close the window.

## Additional Policy Configuration Options

Click the policy's dropdown configuration icon to display additional options:

[image: image]

- **View.** Opens the policy Description window (same as clicking a policy
  name).
- **Edit.** Opens the policy configuration page where you can edit the
  policy's configuration (see Creating a
  Policy).
- **Duplicate.** Creates a new policy with duplicate settings. This is
  useful when creating a new policy that includes many of the same rules as
  the original. Creating a policy with duplicate settings eliminates the need
  to recreate rules that have already been defined.
- **Set as default.** Specifies that the policy will be automatically
  assigned to all new projects (but not to existing ones). If a policy is a
  default policy, it will appear as part of the policy name. (A default policy
  must be "unset as the default" before it can be deleted.)
- **Delete.** Deletes the policy and all its associations with existing
  projects. Deleting a policy is irreversible. A warning pop-up window will
  list all the projects associated with the policy and ask for confirmation
  before deleting the policy.
