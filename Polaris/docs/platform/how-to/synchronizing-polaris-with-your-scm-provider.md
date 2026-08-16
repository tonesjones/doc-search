---
title: "Synchronizing Polaris with your SCM Provider"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/synchronizing-polaris-with-your-scm-provider.html"
content_id: "OzPZQ6qmRGHPymcZvTHo0A"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:57:13.389987+00:00"
content_hash: "0cd73ea6fcdbbce14cfb068fb5bba90113d77438c665905dd373cf0b761ac392"
---

# Synchronizing Polaris with your SCM Provider

## Overview

Polaris provides seamless synchronization with your SCM provider. These settings can be enabled either during the onboarding process or for an existing organization or application. You can customize these settings at both the organization and application levels.

These settings allow automatic tracking and monitoring which will:

- Onboard a repository created on the SCM provider to Polaris which will create a project with a default branch. When onboarding a branch from the SCM provider, Polaris will create a corresponding branch for the specified project.
- Update a project or branch name whenever the repository or branch name is
  modified on the SCM provider (not available for GitLab).
- Update the default branch whenever changes are made to it on the SCM provider.
- Delete a project and its associated branches when the repository is deleted from the SCM Provider.
- Delete a branch when it is deleted on the SCM Provider.
- Import and sync non-default branches by using matching substrings (default branches are automatically included).

Note: Editing or deleting synced projects and branches in Polaris is not allowed.

## Prerequisites and limitations

- Azure Repos, Bitbucket Cloud (Premium), GitHub, GitHub Enterprise, or GitLab
  SaaS (Premium or Ultimate).
- On-prem deployments will need to allow IPs for Polaris.
- An SCM integration that supports synchronization (see [Connect a Polaris project to a repository in your SCM](connect-a-polaris-project-to-a-repository-in-your-scm.md) or Connect Polaris to Multiple SCM Repositories).
- The access token used for integration must fit token requirements:
  - Azure Tokens for SCM Bulk Integration and/or Monitoring
  - Bitbucket Tokens for SCM Bulk Integration and/or Monitoring
  - GitHub Tokens for SCM Bulk Integration and/or Monitoring
  - GitLab Tokens for SCM Bulk Integration and/or Monitoring

**The following roles can manage synchronization:**

- Organization Admin
- Organization Application Manager
- Application Admin (only for applications they are the admin for)

## Synchronizing Polaris with your SCM Provider

1. Select the appropriate level to sync. 

   You can configure synchronization at two levels:

   - During onboarding: Use either Automatic or Custom Matching. Custom matching does not allow for importing new repositories for the whole organization.
   - Application: Select Application name > Settings > Integrations.  
    [image: Mapping bulk import]
2. Select Edit (if existing integration).
3. Select appropriate boxes.

   1. Keep repositories and branches synchronized with
      SCM: Polaris will actively monitor repository
      updates, deletions, renames, and branch modifications, including
      updates, deletions, and renames, on the SCM provider. It will then
      implement the necessary changes to the corresponding Projects and
      Branches.

      Important: If this is selected without the
      additional branches option below, this will apply only to
      default branches.

      Note: Monitoring
      and updates for renaming is not supported for GitLab.
   2. Continue to import new repositories for above organization: For example, if you create a new repository in GitHub, Polaris will create a new project in Polaris. This is not available when you use custom matching during bulk onboarding.
   3. Import additional branches matching
      substrings: Default branches are automatically
      imported but this allows you to import/sync non-default branches.
      1. When selected, a new input field will appear. Enter
         substrings separated by commas (for example:
         `-release`, `-demo`)
      2. When selected, a checkbox is available if you want to
         Continue to import new branches matching
         substrings after the initial integration.
         Polaris will monitor for branch creation events on all the
         repos under the organization/application that match the
         specified substrings.

      Note: Organization Admins will receive failure notifications for
      project/branch creation/update operations as part of auto
      onboarding. They can monitor project/branch create/update/delete
      events in audit logs (My Organization > Audit
      Logs).

      CAUTION:

      After synchronization is disabled, projects and
      branches can be edited as usual at the user's discretion. This
      is not advised if synchronization will be enabled again
      later.
4. Select Save or Import Repository.

   Your synchronization settings are saved and applied.
5. Now, you can set up event-based test automation.

   See [Event-Based Test Automation in Polaris for SCM Integrations](event-based-test-automation-in-polaris-for-scm-integrations.md) for more information.
