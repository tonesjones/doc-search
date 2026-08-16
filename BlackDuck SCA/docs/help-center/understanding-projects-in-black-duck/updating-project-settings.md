---
title: "Updating project settings"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/updating-project-settings.html"
content_id: "2Cps47PSYFEifTbtkWuN~Q"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:14:03.099718+00:00"
---

# Updating project settings

Project team members can view and update project settings, such as:

- Project
  Details
- SCM
  Repository. This field is visible only if this feature is enabled in
  your environment.
- Users
- Groups
- Custom
  Fields
- SBOM Fields
- Activity

To configure a project's settings:

1. Log in to Black Duck SCA.
2. Select the project name using the **Watching** or **My Projects**
   dashboard. The *Project Name* page appears.
3. Select the **Settings** tab.

## Updating project details

From the project **Overview** tab, you can perform the following tasks:

- Update the Project Name, Description, Owner, URL, or Tier.

  If you remove a project owner, the user remains a member of the project. If you add a
  project owner who is not already a project member, Black Duck adds the user as a member.
- Configure the ability to
  apply edits to all versions of a project.
- Configure snippet
  adjustments.
- Update project version cloning settings.
- Configure custom scan signatures.
- Configure your project's unmatched files
  data retention.
- Set how deep
  license data applies to your BOMs or snippet component matches.
- Set an Application ID. This field is used to store an external mapping ID for the
  project to an external system, such as an asset management system or application
  catalog.
- Clone this project.
- Delete this project.
- Enable license conflicts to apply
  license conflicts data to your components

## Setting a project's SCM Repository

Projects can be associated with a single SCM Repository. Once mapped, then each version can be
associated with a branch in the repository. Select an SCM repository, or manually
enter a repository URL.

To update the project's SCM repository, click [image: image]
and select from the following options:

- Select New Repository. Choose from the list of configured SCM
  providers and repositories.
- Manually Enter Repository. Enter the desired repository URL.
- Clear Repository. Remove the project's linked SCM repository.

## Updating project members

Manage the users and groups
associated to this project.

## Updating a project's custom fields

If there are custom fields created for
projects, you can provide the requested details here.

## Updating a project's SBOM fields

These are additional fields that can be included in the SBOM report. These field values will
propagate when this project is used as subproject, you can override them at the BOM
level. See SBOM Project fields for more information.

## Viewing a project's activity audit trail

The Activity Audit Trail retains
the activity audit records of user actions and key events, such as project version,
component, and vulnerability records, that affect a project or project version.

Note: Audit records are only available for activities that occur while audit tracking
is enabled. If audit tracking is enabled after a project has already been created or
modified, earlier activities are not backfilled and will not appear in the audit
trail.
