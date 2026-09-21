---
title: "Prerequisites: GitHub Black Duck Security App"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/prerequisites-github-black-duck-security-app.html"
content_id: "71eAaBKTbMo6XPLCdtY~Jw"
version: "latest"
section: "GitHub Integrations"
scraped_at: "2026-08-08T23:47:36.965036+00:00"
---

# Prerequisites: GitHub Black Duck Security App

The prerequisites for installing and using the Black Duck Security App to deploy a generated workflow are found here. Please ensure all requirements in each section have been considered.

## GitHub organization requirements

**Organization Permissions**

You must possess **Owner** or **Admin** permissions in your GitHub organization to install the app.

To verify your permissions:

1. Navigate to your GitHub organization.
2. Go to **Settings → Member privileges**.
3. Confirm that your role is listed as **Owner** or **Admin**.

**Organization setup**

Ensure your organization has:

- At least one repository where security scans will be conducted.
- GitHub Actions enabled at the organization level.

**IP allow list configuration (if enabled)**

If your organization has IP Allow List enabled, you must add our application's IP address to the allowed list to ensure proper connectivity.

To add the IP address:

1. Navigate to **Org Settings**
2. Go to **Security → Authentication Security**
3. Locate the **Allowed IP List** section
4. Add our application's IP (34.30.9.186/32) address to the list

## Branch protection rules

The app will generate and deploy a workflow file to a configured set of repositories.

Table 1. Workflow onboarding process for branch protection rules

| Branch protection rules | Workflow onboarding process |
| --- | --- |
| Enabled | 1. Pull Request raised 2. Review and approve to enable the scan workflow and complete onboarding |
| Disabled | - **Default:** Workflow committed directly to branch as indicated on the app's summary screen. - Alternatively, an option is provided to submit the workflow as a Pull Request. |

**Learn more about GitHub branch protection:** For detailed information about configuring branch protection rules, visit: [GitHub Branch Protection Documentation](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches).

## Next steps

Once all prerequisites are satisfied, proceed to the user guide to ensure that preliminary steps have been considered and perform the installation process.
