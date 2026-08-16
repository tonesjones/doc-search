---
title: "The data model: applications and projects in Polaris"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/the-data-model-applications-and-projects-in-polaris.html"
content_id: "7bEQtYTDtAfMscsxh57eQw"
product_key: "polaris-platform-latest"
section: "Understand Polaris"
scraped_at: "2026-08-12T19:55:41.072096+00:00"
content_hash: "0be04be16d17d2d253a75e2e54e56965869f66acee9c2a6820296c902a7e77e3"
---

# The data model: applications and projects in Polaris

Polaris is organized around applications and projects.

## Applications

The application can be called the organizing principle of Polaris, because projects and subscriptions are associated with an application. An application is a collection of up to five projects (although this number varies according to the subscription purchased) and up to 1 million lines of code. Its boundaries don't have to align with the boundaries of a software product, but generally all the projects in an application have the same business purpose.

## Projects

There are two types of projects in Polaris:

| Project type | Description |
| --- | --- |
| SAST & SCA | A SAST & SCA project is a discrete body of code associated with a parent application. It can contain the entire application or can be one submodule in a larger application. It might correspond to one repository, but doesn't have to. Each SAST & SCA project includes a default branch, and may include more (non-default) branches. SAST and SCA tests (including external analysis tests used to import issues from third-party tools) always run on a single branch of a project (and issues captured in tests are linked to the branch and project). |
| DAST | A DAST project is a target web application or API, which can be web-accessible or internal, that you wish to test with the fAST Dynamic analysis engine. Generally, the target uses source code from an application's SAST & SCA projects, but it doesn't have to. Note: See [Test web applications and APIs with Polaris fAST Dynamic](../how-to/test-web-applications-and-apis-with-polaris-fast-dynamic.md) for more information. |

### Branches

Add branches to a SAST & SCA project to test changes as you iterate. By default, you can add 10 branches to any SAST & SCA project. There are three types of branches in Polaris:

- Branches connected to repositories (via SCM integrations).

  Note: For more information on SCM integrations, see [Connect a Polaris project to a repository in your SCM](../how-to/connect-a-polaris-project-to-a-repository-in-your-scm.md) and Connect Polaris to Multiple SCM Repositories.
- Branches that aren't connected to repositories and only exist in Polaris.
- Branches created by Code Sight (created when you run tests from your IDE).

  Note: The names of branches created by Code Sight include `CodeSight_` and the email address of the user the branch was created for (for example, `CodeSight_user@domain.com`).

  Important: Branches created with Code Sight are not compatible with SCM integrations.

You can add all three types of branches to any SAST & SCA project, and can configure Polaris to automatically delete non-default branches that aren't tested for a period between 1 and 90 days.

Note: For more information, see Configure automatic branch deletion.

### Policies

There are three types of policies in Polaris:

- Issue policies: Use issue policies to automate actions when issues with specific properties are detected in a test.
- Pull/merge request policies: Use to have your SCM Integrations Event-Based Test Automation create PR comments including Fail PRs.
- Component policies: Use component policies to automate actions when components with specific properties are detected in an SCA test.
- Test scheduling policies: Use test scheduling policies to automate tests of SCM-integrated branches on a weekly or daily basis.

  Note: Test scheduling policies can only be used with branches connected to repositories, and cannot be assigned to DAST projects.

Default branches inherit their project's default policies. Non-default branches can use their project's default policies, or use different policies. If necessary, policies can be disabled on default and non-default branches.
