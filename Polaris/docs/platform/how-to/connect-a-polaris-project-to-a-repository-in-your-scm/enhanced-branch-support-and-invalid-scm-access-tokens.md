---
title: "Enhanced branch support and invalid SCM access tokens"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/enhanced-branch-support-and-invalid-scm-access-tokens.html"
content_id: "f~7hpA9G~60wMENqoH68_w"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:57:25.293218+00:00"
content_hash: "0cd319893ad4f784dd676e7a93abccfb90001acfa733b9747ff0915ebcb9a6b4"
---

# Enhanced branch support and invalid SCM access tokens

When branching features are enabled in Polaris, your projects are upgraded automatically. When upgrading a project connected to an SCM repository, Polaris retrieves the default branch name from the repository and creates the project's default branch (using the name retrieved from the repository).

Note: If the project's SCM access token is invalid, Polaris creates a default branch called `scm_token_invalid`. If this occurs, follow the steps below to create a new SCM access token and reestablish the project's SCM integration.

## Create a new SCM access token

If, after the branching features are enabled in Polaris, you find a project with a default branch called `scm_token_invalid`, follow these steps:

1. Open your SCM service and create a token.
   1. Azure DevOps tokens require Read access to the Code scope.
   2. Bitbucket app passwords require Read permissions for Projects and Repositories.
   3. GitHub tokens require repo scope.
   4. GitLab tokens require read\_repository and read\_api scopes.
2. In Polaris, go to Portfolio, open an application, and open the project with the `scm_token_invalid` branch.
3. Go to Settings > Integrations.
4. Enter your new token in the Repository Access Token field.
5. Select Test your connection.
6. Select Save.
7. Go to Branches and select the `scm_token_invalid` branch.
8. Select the repository's default branch with the SCM Branch pulldown menu and select Save.
9. Repeat steps 2-9 for other projects, as required.
