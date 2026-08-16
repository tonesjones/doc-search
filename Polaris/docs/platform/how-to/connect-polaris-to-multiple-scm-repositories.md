---
title: "Connect Polaris to Multiple SCM Repositories"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/connect-polaris-to-multiple-scm-repositories.html"
content_id: "aFTyAon711OJf4p16_5g~A"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:57:07.151989+00:00"
content_hash: "d494cf2ad9f0a988995bc7b1c8a6b1f1a242a60a975aed7140e9d32a3b148dc3"
---

# Connect Polaris to Multiple SCM Repositories

## Overview

Bulk onboarding into Polaris features include:

- Using your Source Code Management (SCM) repository to create new application(s) and project(s), or add multiple repositories to existing applications in Polaris.
  - Automatic mapping: Polaris creates an application for each organization/group that can be accessed using the access token, and it creates a project for each repository.
  - Customizable mapping: Manually select the organization/group and repositories you wish to add to Polaris. Use this option to create multiple repositories to be imported to a new application(s) or existing application(s).
- Assign roles while onboarding.
- Ability to update the connection credentials for all the projects under an application.
- Import SCM repositories as projects into an existing application.
- Access to:
  - Synchronizing your SCM provider with Polaris
  - Event-Based Test Automation
  - PR comments including Fail and Fix PRs

Note: Projects created during bulk onboarding automatically inherit your organization's default policies. To customize policies assigned to applications, projects, and branches, see [Create and manage Policies](create-and-manage-policies.md).

## General Prerequisites

**The following roles can initiate bulk onboarding:**

- Organization Admin
- Organization Application Manager
- Application Admin (limited to bulk onboarding projects and SCM connections for applications they are the admin for).

**Assumptions and constraints**

- A concurrent subscription (in Polaris) is required to use this feature.
- Users can only import repositories from organizations they are a member of; they cannot import repositories from public orgs that they are not a member of.
- Only 100 repositories per hour will be onboarded. The access token provided will be subject to rate-limits on SCM. If the rate limit is reached, the system does not automatically retry the operation.
- You cannot import repositories that do not belong to a supported SCM or SCM organization.
- Only one active bulk onboarding job is allowed per tenant.
- Access token must be created by an Organization Owner in the SCM organization and have specific requirements/scopes:
  - Azure Tokens for SCM Bulk Integration and/or Monitoring.
  - Bitbucket Tokens for SCM Bulk Integration and/or Monitoring.
  - GitHub Tokens for SCM Bulk Integration and/or Monitoring.
  - GitLab Tokens for SCM Bulk Integration and/or Monitoring.
- Some SCMs require additional settings for Block PRs. See [Fail Pull Requests (Fail PR)](fail-pull-requests-fail-pr.md).
- On-premise SCMs require a secure tunnel. See [Add and manage secure tunnels in the Polaris UI](add-and-manage-secure-tunnels-in-the-polaris-ui.md) for more information.

### Support

Within the Polaris UI, SCM repository bulk integration is supported for:

- Azure Repos
- Bitbucket Cloud (Premium)
- GitHub and GitHub Enterprise
- GitHub Enterprise Server
- GitLab SaaS (Premium and Ultimate)

### Update your SCM connections within an application

Update or add new access token to your SCM provider. If your token has expired or you need to update the scope in order to setup synchronization or event-based testing, follow these steps.

1. On the Portfolio page, select an application by clicking on its name.
2. Click Settings > Integrations.
3. Click Edit icon next to Connected SCM.
4. Enter the updated access token created in the SCM under Repository Access Token.
5. Click the Connect button.

   You should receive a Connection Successful message. If your connection test is unsuccessful, check the following:

   - Your network connection is stable.
   - Check the Repository Access Token to make sure it is accurate.
   - Check that the Repository Access Token is still valid and has not expired.
   - Check that you selected the correct provider for your source repository.
   - Check that you have authorized use of access token outside SSO (if applicable).
6. If connection is successful, click Save.
