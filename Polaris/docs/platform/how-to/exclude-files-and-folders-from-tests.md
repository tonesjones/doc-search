---
title: "Exclude files and folders from tests"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/exclude-files-and-folders-from-tests.html"
content_id: "hHirShI09y6gPlkrfsUZWw"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:56:10.847072+00:00"
content_hash: "fb601fa7cbd0a47ed4fd9eb1a231dabe04e0f3edf658093d70c6d229bec98684"
---

# Exclude files and folders from tests

Learn how to exclude SAST issues associated with specific files and folders in your projects from test results.

## Overview

You can set up file and folder exclusion rules for your organization, for specific applications, and for specific projects. Up to 30 exclusion rules can be defined for your organization, each application, and each project. Once configured, SAST issues (including SAST issues imported from third-party tools) found in excluded files:

- Are hidden in the Polaris user interface, without affecting issue metadata.

  Note: This means each issue's metadata (triage status, first detected date, ... etc.) can be restored when exclusion rules change.
- Do not count as policy violations.

Additionally, pull request (PR) comments will not be applied to excluded files.

Tip: Although issues associated with excluded files are hidden in the Polaris user interface, hidden issues are returned in responses to `GET /api/findings/issues/{id}` and `GET /api/findings/issues` endpoints in the [Findings](https://polaris.blackduck.com/developer/default/documentation/findings) API (and can be easily identified when the `_includeIssueExclusion` parameter is set to `true`).

### Processing exclusions

Polaris evaluates and applies exclusions:

- At the end of SAST tests, before test results appear in Polaris.

  Note: This means all the files in your project are still available and evaluated during tests, and ensures the exclusion rules you configure don't affect test quality.
- At the end of external analysis tests, before issues you import from third-party tools appear in Polaris.
- When file and folder exclusion rules are modified.

  Note: A banner appears at the top of the Issues tab (Portfolio > select an application > select a SAST & SCA project > Issues) while Polaris processes changes.

  [image: code exclusion banner]

### Exclusion inheritance

File and folder exclusion rules set at the organization-level serve as defaults for all the applications and projects in your portfolio. However, exclusion rules assigned to applications and projects take precedence; an application's rules override organization-level rules, while a project's exclusion rules override both application and organization-level rules.

To check the active exclusion rules for an application or project, open the Analysis tab.

- For an application, go to Portfolio > select an application > Settings > Analysis.
- For a project, go to Portfolio > select an application > select a project > Settings > Analysis.

When Inherited appears at the top of the Code Exclusions panel, the exclusion rules that apply to the application (example below) or project are inherited.

[image: Screenshot of the Code Exclusions panel for an application.]

### Regular expression reference

Exclusion rules are regular expressions (regex), and each rule can include a comment.

```
Rule #Comment
Rule #Comment
Rule #Comment
```

Table 1. Key regex operators

| Type | Operator | Description |
| --- | --- | --- |
| Anchors | `^` | Matches the start of a path or file name. |
| `$` | Matches the end of a path or file name. |
| Path separator | `/` | Separates directories in a path. |
| Escape | `\` | An escape character that precedes literals. For example, use `\.` to select a period. |
| Quantifiers | `*` | Zero or more occurrences of the preceding element. |
| `+` | One or more occurrences of the preceding element. |
| `?` | Zero or one occurrence of the preceding element. |
| `{n}` | A specific number (`n`) of occurrences of the preceding element. |
| `{n,}` | A minimum number (`n`) of occurrences of the preceding element. |
| `{n,m}` | A range (between `n` and `m`) of occurrences of the preceding element. |
| Character classes | `\d` | Any digit. |
| `\D` | Any non-digit. |
| `\w` | Any word character. |
| `\W` | Any non-word character. |
| `\s` | Any whitespace character. |
| `\S` | Any non-whitespace character. |
| Character ranges | `[abc]` | Any of the characters in the brackets. |
| `[^abc]` | Anything but the characters in the brackets. |
| `[a-z]` | Letters of the alphabet from a to z. |

### Example exclusion rules

Example Python project structure:

```
project/
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── utils.py
│   └── config.py
│
├── tests/
│   ├── __init__.py
│   ├── test_main.py
│   └── test_utils.py
│
├── venv/
│   ├── lib/
│   └── bin/
│
├── .git/
├── README.md
└── requirements.txt
```

Table 2. Example exclusion rules

| Example exclusion rule | Effect |
| --- | --- |
| `^.*test_[\w_-]*\.py$` | Excludes all Python files with names that start with "test\_" (and allows filenames to include additional underscores and dashes). |
| `^venv/.*$` | Excludes the entire venv directory and its contents. |
| `^tests/.*\.py$` | Excludes all Python files in the tests directory. |
| `^src/config\.py$` | Excludes only the config.py file in the src directory. |

## Create or update organization-level exclusion rules

To create organization-level exclusion rules, follow these steps:

Note: Only Organization Administrators can manage organization-level exclusion rules.

1. Go to My Organization > Analysis.
2. Under Code Exclusions, select Edit.
3. Modify your organization's exclusion rules, as required.

   You can create up to 30 organization-level exclusion rules, and each rule can include a comment.

   ```
   Rule #Comment
   Rule #Comment
   Rule #Comment
   ```
4. Select Save.

   Important: It can take several minutes for Polaris to process changes you make. It can take up to an hour for changes to affect reports and dashboards.

## Create or update application-level exclusion rules

To create application-level exclusion rules, follow these steps:

Note: Organization Administrators, Organization Application Managers, and other users with permissions to manage application settings can manage application-level file and folder exclusion rules.

1. Go to Portfolio and open an application.
2. Go to Settings > Analysis.
3. Under Code Exclusions, select Edit.
4. Modify the application's exclusion rules, as required.

   You can assign up to 30 exclusion rules to each application in your portfolio, and each rule can include a comment.

   ```
   Rule #Comment
   Rule #Comment
   Rule #Comment
   ```

   Important: After exclusion rules are assigned to an application, organization-level rules no longer apply to the application and its projects.
5. Select Save.

   Important: It can take several minutes for Polaris to process changes you make. It can take up to an hour for changes to affect reports and dashboards.

## Create or update project-level exclusion rules

To create project-level exclusion rules, follow these steps:

Note: Organization Administrators, Organization Application Managers, Application Administrators, Application Contributors, and other users with permissions to manage project settings can manage project-level file and folder exclusion rules.

1. Go to Portfolio, open an application, and open a project.
2. Go to Settings > Analysis.
3. Under Code Exclusions, select Edit.
4. Modify the project's exclusion rules, as required.

   You can assign up to 30 exclusion rules to each project in your portfolio, and each rule can include a comment.

   ```
   Rule #Comment
   Rule #Comment
   Rule #Comment
   ```

   Important: After exclusion rules are assigned to a project, organization and application-level exclusion rules no longer apply to the project.
5. Select Save.

   Important: It can take several minutes for Polaris to process changes you make. It can take up to an hour for changes to affect reports and dashboards.

## Reset application and project-level exclusion rules

After you customize application or project-level exclusion rules, you can select Reset (at the top of the Code Exclusions panel) to delete the application or project-level rules. When you reset an application's exclusion rules, the application will inherit your organization-level rules. When you reset a project's exclusion rules, the project will inherit application (if set) or organization-level rules.

1. Open the application or project's settings:
   - For an application, go to Portfolio > select an application > Settings > Analysis.
   - For a project, go to Portfolio > select an application > select a project > Settings > Analysis.
2. Select Reset (at the top of the Code Exclusions panel).
