---
title: "Fix Pull Requests (Fix PR)"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/fix-pull-requests-fix-pr-.html"
content_id: "XUOflzc228XydyNCLuBjuA"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:56:35.999037+00:00"
content_hash: "b2eca9fef827d6371af236ef19a2b2dc92a6da493d5ef30f36b6d85b7cb6dbca"
---

# Fix Pull Requests (Fix PR)

A guide to creating Fix PRs automatically or manually to resolve open-source vulnerabilities detected by SCA scans in SCM-integrated projects.

Fix PRs are created on your SCM integration — either automatically or manually — to help resolve direct dependency vulnerabilities detected by SCA scans. There are two ways to create Fix PRs:

- **Automatic:** Polaris automatically generates Fix PRs for qualifying issues once a test completes, and they appear immediately on the SCM side. The workflow is: create a policy → apply it to the project → run a test → Fix PRs appear on the SCM.
- **Manual:** After a test has run, navigate to the Components tab, select a component, and, if it meets the criteria, manually create a Fix PR. The Fix PR will appear on the SCM side.

## Requirements

- An SCM integration connected to Polaris. Source uploads and CLI-based projects are not supported.
- An SCA entitlement, or a bundled test type that includes SCA.
- For automatic Fix PRs, a component policy with the Fix PR action configured and applied at the project or application level.

## Overview

- A Fix PR can only be created for a component with a direct dependency that has short-term or long-term upgrade guidance associated with it.
- Automatic Fix PRs are created for each component with a direct dependency that matches the criteria in the component policy rule, and within the limits and upgrade guidance set at the organization, application, project, or branch level.
- Component policies are triggered on any SCA test.
- Component policies can be applied to SCM onboarding.
- When new vulnerabilities are associated with a component, the Knowledge Base is updated and Fix PRs are created as soon as possible.
- When short-term or long-term fix suggestions are created or updated, existing Fix PRs are updated with the new information.
- Only one Fix PR can exist at a time for a given component version. If an open Fix PR already exists, even on another branch, a new one will not be created.
- All roles can create and manage Fix PRs except the Application Observer role. Any custom application role created by a user will have this permission unchecked by default, but it can be added.

## Restrictions

An SCA Fix PR will not be created in the following cases:

- Not a direct dependency
- There is already an open PR
- No security vulnerabilities found
- No upgrade guidance available
- Number of PRs has exceeded the allowed limit for automatic Fix PR (see [Create and manage automatic Fix PRs](fix-pull-requests-fix-pr/create-and-manage-automatic-fix-prs.md))

## Automatic Fix PRs Inheritance

Fix PR component policy can be customized at all levels (organization, application, project, and branch). Organization-level Fix PR settings serve as defaults for all applications and projects in your portfolio. Settings at lower levels take precedence:

- An application's settings override organization-level settings for that application.
- A project's settings override both application and organization-level settings for that project.
- A branch's settings override project, application, and organization-level settings for that branch.

## Checking Active Fix PR Settings

To check the active Fix PR settings at each level:

- **Organization:** My Organization > Integrations
- **Application:** Portfolio > select an application > Settings > Integrations
- **Project:** Portfolio > select an application > select a project > Settings > Integrations
- **Branch:** Portfolio > select an application > select a project > Branches tab > select a branch

## Settings Status

At the top of the Fix Pull Request Settings panel, the settings status is shown as one of the following:

Inherited
:   The settings that apply to the application or project are inherited.

    - For applications, settings are inherited from the organization level.
    - For projects, settings can be inherited from the organization or application level.
    - For branches, settings can be inherited from the organization, application, or project level.

Modified
:   The settings have been edited at this level. Selecting Reset returns them to Inherited.

**Related tasks**  

- Create and manage automatic Fix PRs
- Create a manual Fix PR
- Disable a Fix PR for a component
