---
title: "Managing deep licenses"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/managing-deep-licenses.html"
content_id: "J5F2uSRagh7tw0WoEHuv7w"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:56:45.555576+00:00"
content_hash: "22b0c5521f94b34c70ae8f9e7dcab0338ded7de0804ce937cf2e991735b65bf9"
---

# Managing deep licenses

An overview of deep license data in Polaris, including how to enable or disable it, and where to view embedded license information in open source components.

As part of your license workflows to help meet your legal use cases, Polaris provides deep licenses (also known as sub-licenses or embedded licenses) information that may exist in your open source components. Deep license data allows access to embedded licenses which may exist beyond declared licenses. Managing this deep license data reduces the risk of license infringement and makes it easier to understand and report on deep licenses and their risks in the open source being used.

Deep license data is:

- Disabled by default.
- The branch level will inherit the project settings.
- The following roles can enable or disable it:
  - Org Admin for the organization-level.
  - Application Admin for the application and project level.
- Can be monitored via Component Policies.

## Deep license data setting inheritance

Organization-level deep license data settings serve as defaults for all applications and projects in your portfolio. However, settings at the application and project levels take precedence:

- An application's settings override organization-level settings for that application.
- A project's settings override both application and organization-level settings for that project.

To check the active deep license data settings for an application or project, open the **Licenses** tab in **Settings**.

- For an application, go to **Portfolio** > select an application > **Settings** > **Licenses.**
- For a project, go to **Portfolio** > select an application > select a project > **Settings** > **Licenses**.

At the top of the **Deep License Data** panel:

- **Inherited** — the settings that apply to the application or project are inherited.
  - For applications, it is inherited from the organization-level setting.
  - For projects, it can be inherited from the organization-level or application settings.
- **Modified** — the settings have been edited at this level. **Reset** returns them to **Inherited**.

## Viewing deep license data

Deep license data in the locations below is available only when deep license data is enabled.

| Location | Action | Details |
| --- | --- | --- |
| **Portfolio** > (Select an application) > (Select a project) > **Components** tab | Use filter to view components with deep license data. |  |
| **Portfolio** > (Select an application) > (Select a project) > **Components** tab > Click gavel icon in component's row > **Deep License Data** page | View individual component's deep license information.  NOTE: Only a component with the gavel icon has deep license data. | The **Deep License Data** page:   - List of all the component's licenses with the following information:   - License Name   - License Family - Filter or search licenses. - Click on <name of license> to view copyright. - Click on arrow to the left of name to see **Component Origins** and find **View Files** button.   - Shows if the license has multiple origins and allows you to view them. - Click **View Files** for the **Reference files** page   **Reference files** includes:   - Complete text for the embedded license. - Highlights text to show where the deep license data is coming from. |
| **Reporting > Notices File** | Option to include deep license data in Notices File Reports. | See [Create a report](create-a-report.md). |
| **Policy > Component Policies** | Add a rule for Deep License Family to include all or specific families and set action (Send Notification or Attempt Build Break). | See [Component policies](create-and-manage-policies/component-policies.md). |
