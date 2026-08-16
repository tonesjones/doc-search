---
title: "Migrate Polaris to the Black Duck domain"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/migrate-polaris-to-the-black-duck-domain.html"
content_id: "GoviOv1mz19~IVoa4mOUvg"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:55:57.981648+00:00"
content_hash: "acce12d751f62b64d3b0c07049b38416268af5b3fbba0ffe810b1a5147ebb58a"
---

# Migrate Polaris to the Black Duck domain

The Synopsys Software Integrity Group (SIG) is now [Black Duck](https://www.blackduck.com/), and Polaris is the Black Duck Polaris® Platform. Follow the instructions on this page to migrate your Polaris tenant to the new Black Duck domain. We strongly recommend you complete this migration as soon as possible.

## Before you run the migration

Before you run the migration, you will need to:

- Update your allow list
- Plan and schedule your migration
- If you use single sign-on to manage access to Polaris, an additional step is required before you run the migration.

Each one of these steps is described in greater detail below.

### Update your allow list

To ensure Polaris continues to function as expected, update your allow list.

See [Polaris IP ranges](../reference/polaris-ip-ranges.md) and Polaris IP ranges for Bridge CLI for more information.

### Plan and schedule your migration

The migration can run for up to 15 minutes, but typically runs much faster. Running the migration won't impact any tests that are already in progress, and won't prevent you from running new tests. While the migration runs, users in your organization will not be able to sign into Polaris.

Running the migration will invalidate links in the welcome emails Polaris sends to new users. Please avoid inviting new users to Polaris during the 24-hour window before you run the migration.

Note: Once the migration is complete, Organization Administrators can reset a new user's password (My Organization > Users > select a user > Reset Password) to send the new user another email with a valid link they can use to sign into Polaris.

By now, you should have already completed the following actions:

- Added <https://repo.blackduck.com> to your allow list.
- Updated to the latest versions of the Bridge CLI, Black Duck Security Scan Extension for Azure DevOps, Black Duck Security Scan Action, Black Duck Security Scan Template, and Black Duck Security Scan Plugin for Jenkins. For more information, see:
  - [Polaris: Migrating to the new Bridge CLI](https://community.blackduck.com/s/article/integrations-black-duck-migration-instructions#Polaris)
  - [Azure DevOps: Migrating to Black Duck Security Scan](https://community.blackduck.com/s/article/integrations-black-duck-migration-instructions#PolarisAzure)
  - [GitHub: Migrating to Black Duck Security Scan](https://community.blackduck.com/s/article/integrations-black-duck-migration-instructions#PolarisGithub)
  - [GitLab: Migrating to Black Duck Security Scan](https://community.blackduck.com/s/article/integrations-black-duck-migration-instructions#PolarisGitlab)
  - [Jenkins: Migrating to Black Duck Security Scan](https://community.blackduck.com/s/article/integrations-black-duck-migration-instructions#PolarisJenkins)
- Updated trusted certificates for Polaris.

  See [Scheduled Certificate Updates for Coverity on Polaris and Polaris on March 5, 2025](https://community.blackduck.com/s/question/0D5Uh00000UlyuKKAR/operational-announcement-scheduled-certificate-updates-for-coverity-on-polaris-and-polaris-on-march-5-2025) for more information.

Table 1. Polaris domain migration, key dates

| Key date | Milestones |
| --- | --- |
| January 13, 2026 | Domains for Polaris (and its services) that include "synopsys" will stop functioning. Pipelines that haven't been updated will fail, and certificate errors will prevent users from accessing Polaris in browsers. CAUTION:  If you use single sign-on to manage access to Polaris, the automatic migration may prevent the users in your organization from accessing Polaris. Complete the migration by January 13, 2026 to avoid issues. |
| November 24, 2026 | Media types (used in Polaris APIs) that include "synopsys" will no longer function. Tip: Several endpoints will be sunset on this date, too.  Versions of the Bridge CLI older than 3.6.0 will not function as expected. Upgrade to Bridge CLI 3.6.0 or newer to avoid failures.  Versions of Code Sight older than 2025.4.0 will not function as expected. Upgrade to Code Sight 2025.4.0 or newer to avoid failures. |

### If you use single sign-on

CAUTION:

If you use single sign-on to manage access to Polaris, there are additional steps you'll need to perform before and after you run the migration. See [Migrate your tenant to Black Duck (with single sign-on)](migrate-polaris-to-the-black-duck-domain/migrate-your-tenant-to-black-duck-with-single-sign-on.md) for more information.

## Running the migration

To run the migration, follow these steps:

1. Go to My Organization > General.

   Note your Organization Name, listed near the top of the page. You'll need this in a later step.
2. Under Black Duck Migration, select Start Migration.

   A confirmation appears.
3. Enter your organization name and select Start Migration.

   Note: While the migration runs, users in your organization will not be able to sign into Polaris.
4. When the migration is complete, select Reload.

   The Sign in page opens.
5. Sign in to Polaris.

## After you run the migration

After you run the migration, users in your organization can sign into Polaris from the new Black Duck URL:

- North America: <https://polaris.blackduck.com>
- POC: <https://poc.polaris.blackduck.com>
- European Union: <https://eu.polaris.blackduck.com>

Note: Other users in your organization who were signed into Polaris when the migration started will need to close Polaris and sign in again. They can still sign in to Polaris from the old URLs (<https://polaris.blackduck.com>, <https://poc.polaris.blackduck.com>, and <https://eu.polaris.blackduck.com>). During sign in, they will be redirected to the Black Duck domain automatically.

After you run the migration, you will need to:

- Generate new access tokens
- Update your pipelines
- Update API scripts
- Upgrade Code Sight
- Update your bookmarks

Each one of these steps is described in greater detail below.

### Generate new access tokens

While not required, we recommend you make new access tokens and use them when you update your pipelines and API scripts. See [Make an access token](make-an-access-token.md) for more information.

### Update your pipelines

Minimally, in addition to replacing the token(s) your pipelines use, please update the Polaris server URL your pipelines reference.

- Replace <https://polaris.synopsys.com> with <https://polaris.blackduck.com>
- Replace <https://poc.polaris.synopsys.com> with <https://poc.polaris.blackduck.com>
- Replace <https://eu.polaris.synopsys.com> with <https://eu.polaris.blackduck.com>

See [Complete List of Bridge Arguments > Polaris](https://docs.blackduck.com/access?ft:originId=cba15d77e1e0a5989f94dbbae8f7dd44/104e9b8ad79809821c6b1e50bb52508d.topic) for more information.

Important: Older versions of the Bridge CLI will stop functioning on November 24, 2026. Upgrade Bridge CLI to version 3.6.0 or newer before November 24 to avoid failures.

### Update API scripts

In addition to replacing the token(s) your API scripts use, please update:

- The Polaris server URL your API scripts reference.
  - Replace <https://polaris.synopsys.com> with <https://polaris.blackduck.com>
  - Replace <https://poc.polaris.synopsys.com> with <https://poc.polaris.blackduck.com>
  - Replace <https://eu.polaris.synopsys.com> with <https://eu.polaris.blackduck.com>
- Media types referenced in your scripts. Find new media types in API references:
  - [Audit](https://polaris.blackduck.com/developer/default/documentation/audit)
  - [Identity and Access Management](https://polaris.blackduck.com/developer/default/documentation/identity-and-access-management)
  - [Bug Tracking Integration](https://polaris.blackduck.com/developer/default/documentation/bug-tracking-integration)
  - [Notification](https://polaris.blackduck.com/developer/default/documentation/notification)
  - [Findings](https://polaris.blackduck.com/developer/default/documentation/findings)
  - [Policies](https://polaris.blackduck.com/developer/default/documentation/policies)
  - [Portfolio](https://polaris.blackduck.com/developer/default/documentation/portfolio)
  - [Reports](https://polaris.blackduck.com/developer/default/documentation/reports)
  - [Repos Integration](https://polaris.blackduck.com/developer/default/documentation/repos-integration)
  - [Tests](https://polaris.blackduck.com/developer/default/documentation/tests)
  - [Tools](https://polaris.blackduck.com/developer/default/documentation/tools)

### Upgrade Code Sight

If you use Black Duck®
Code Sight™ with Polaris, we recommend you upgrade Code Sight after you run the migration.

1. Follow the instructions in Black Duck Community to uninstall older versions of Code Sight and then install the latest version of Code Sight: [HOW TO: Migrating existing Synopsys Code Sight users to the new Black Duck Code Sight](https://community.blackduck.com/s/article/code-sight-black-duck-migration-instructions).
2. Open the [Polaris tab](https://docs.blackduck.com/access?ft:originId=e5be419b9a362d8c0118eeab3a8ee157/597c4b57b9cf5751d2bbcce1b81a0318.topic&Version=latest) (found in Code Sight's [Authentication preferences](https://docs.blackduck.com/access?ft:originId=e5be419b9a362d8c0118eeab3a8ee157/34dc2f1ddf4312b3c8ca7ac8f9c496b7.topic&Version=latest)).
3. Replace the token Code Sight uses and update your Polaris server URL:
   - Replace <https://polaris.synopsys.com> with <https://polaris.blackduck.com>
   - Replace <https://poc.polaris.synopsys.com> with <https://poc.polaris.blackduck.com>
   - Replace <https://eu.polaris.synopsys.com> with <https://eu.polaris.blackduck.com>

Important: Older versions of Code Sight will stop functioning on November 24, 2026. Upgrade Code Sight to version 2025.4.0 or newer before November 24 to avoid errors.

### Update your bookmarks

We recommend you update your bookmarks to Polaris after you perform the migration.

After you sign into Polaris on the new Black Duck domain, bookmarks to pages in Polaris (that use the old domain) may direct you to a Sign In page. If this occurs, follow these steps:

1. Enter your Email Address and select Next.

   The Portfolio page opens.
2. Select your bookmark again.

   Now, whenever you select an old bookmark (a bookmark that uses the old domain), you will automatically be redirected to the Black Duck domain.

   Important: Your browser's cookie settings may prevent automatic redirection from working as expected. Each time you clear your browser's cookies, you will need to repeat these steps. Additionally, redirection will only work until January 13, 2026; update your bookmarks before then to avoid issues.

   Tip: Most browsers allow you to export your bookmarks to a text file, which can be modified in a text editor (think, find and replace), and reimported.

## Need support?

To request support, follow these steps:

1. Select the Help [image: help icon] icon (near the upper-right corner of Polaris).

   The search panel opens.
2. Select Need additional help or support? (near the bottom of the panel).

   The How Can We Help You? page opens.
3. Select Submit a Case.
4. When Black Duck Community opens, create a support case.

   See [Submit a support ticket](https://community.blackduck.com/s/article/Support-Guide#SubmitaSupportTicket) for more information.

### If you can't access Polaris

If you need support and cannot access Polaris, sign in to [Black Duck Community](https://community.blackduck.com/s/contactsupport), go to [Submit a Support Case](https://community.blackduck.com/s/contactsupport), and create a support case. Otherwise, request support via email. See [Contact Support > Email support (language specific)](https://community.blackduck.com/s/article/Support-Guide#ContactSig) for more information.

## Additional information

Find additional information on the [Black Duck Domain Change FAQ](https://community.blackduck.com/s/article/Black-Duck-Domain-Change-FAQ).
