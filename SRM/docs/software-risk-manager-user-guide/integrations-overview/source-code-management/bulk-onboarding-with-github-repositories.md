---
title: "Bulk Onboarding with GitHub Repositories"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/bulk-onboarding-with-github-repositories.html"
content_id: "EGGw3BuIMNyIwgUStf_EyA"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:03:34.428866+00:00"
content_hash: "ebec19a0b2f07a903b295c2138f6d2c322d376d2fa067af44a3e93a694009b32"
---

# Bulk Onboarding with GitHub Repositories

Software Risk Manager can automatically create projects based on existing GitHub
repositories.

Click the Integrations icon in the navigation bar and select SCM to open the Source Code
Management page.

[image: image]

## Configuring the Connection to a GitHub Repository

To configure the connection to a GitHub repository:

1. Click the Integrations icon in the navigation bar and select SCM to display
   the GitHub option.

   [image: image]
2. Click the configuration icon for GitHub, then select the Connections tab
   from the top menu.

   [image: image]
3. Click Add Connection.

   [image: image]
4. Enter a Connection Name and Access Token.

   Use the Test Connection button
   to verify proper configuration.
5. Click Save.

   With a saved connection, you can create projects from your
   GitHub repositories as well as associate GitHub repositories with
   existing projects.

## Synching GitHub Repositories with SRM

To sync GitHub repositories with SRM:

1. Click the Integrations icon in the navigation bar and select SCM to display
   the GitHub option.

   [image: image]
2. Click the configuration icon for GitHub, then select the Repositories tab
   from the top menu.

   [image: image]
3. Select a connection from the dropdown menu.
4. Use the checkboxes to select which repositories to sync with Software Risk
   Manager.
5. Click Create Projects.

   [image: image]
6. Specify the following parameters:
   - **Naming Convention.** The template is a
     https://handlebarsjs.com/ expression. The available fields are as follows:
     - `organization`. The organization name.
     - `repository`. The repository name.
     - `isPrivate`. Specifies whether the repository
       is private.
     - `isArchived`. Specifies whether the
       repository is archived.
     - `isFork`. Specifies whether the repository is
       a fork.
     - `languages`. A list of languages in the
       repository.

     Note: When the name (chosen by the naming convention) for a
     repository corresponds to an existing SRM Project, SRM will
     associate the repository with the existing project rather than
     creating a new project, but only if the user has the
     `manage` role for that project.
   - **Parent Projects.** Enables you to specify a parent project for
     the projects you are creating.
   - **Analyses.** Instructs SRM to run an analysis after creating the
     new projects.
7. Click Create Projects.

   The new projects will appear on the Projects
   page.

   [image: image]

   Clicking the git branch icon opens the SCM Configuration
   window, which displays the connection name and repository URL.

   [image: image]

   To delete the repository, click the Delete Configuration
   button.

For projects that are set up with a git configuration, SRM will automatically create
a ZIP archive of the files from that git repo and include it in the analysis prep
area as a "source from" item, as shown in the example below.

[image: image]
