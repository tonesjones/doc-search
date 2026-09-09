---
title: "Advanced Field Configuration"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/advanced-field-configuration.html"
content_id: "XNSl~TT7w0~OCjLBjPg6jw"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:03:15.218198+00:00"
content_hash: "0fc7b1b24c56346cef00af3c3629e699bcf1dbbe4dc86a9147c3922f67a60d2a"
---

# Advanced Field Configuration

When creating an issue or work item from Software Risk Manager, several standard fields
are provided (e.g., summary, description). However, many issue trackers provide more
than just a few fields for issues or work items and can be configured to require these
additional fields when creating an issue or work item. Issue trackers can also allow the
creation of custom fields on a per-project or per-server basis. Software Risk Manager
provides for this situation through "Advanced Fields." Jira users should note that while
Software Risk Manager supports all of Jira's "Standard" custom fields as well as many of
Jira's "Advanced" custom fields, some are implemented via third-party plugins and are
not fully supported. These fields will still appear and can be used if the correct
format is known, but they should be left empty otherwise.

You can create template expressions for any of the available fields when creating an
issue or work item for the configured issue tracker server. These expressions will be
applied to the relevant Software Risk Manager finding (or findings) when you create an
issue or work item, which allows Software Risk Manager to pre-populate the field with
data from the finding, according to your specification. More technical users should be
advised that the template language is the [JavaScript Handlebars library](https://handlebarsjs.com/) and that all of
the template expressions are Handlebars Expressions.

Software Risk Manager will use its own default values for the Description (Azure DevOps, GitHub,
GitLab, Jira, ServiceNow) and Due Date (Azure DevOps, GitLab, Jira, ServiceNow) fields
if none are specified. If auto-create is enabled, Software Risk Manager will also use its
own default values for the Summary (Jira), Title (Azure DevOps, GitHub, GitLab) and
Short Description (ServiceNow) fields if none are specified.

Note: Users should note that by default, the Due Date fields are based on the Software
Risk Manager finding Fix By Date. The finding Fix By Date value is just a date; some issue trackers
like Azure DevOps and ServiceNow also expect a time component in the Due Date value. So, SRM
sends its local midnight as the time component value for these trackers, which may be rendered
differently on the respective UI depending on the instance's timezone settings.

Users should also note that because fields can be given template expressions, which won't
be evaluated until a finding is available, the validation that can be done on the fields
is limited. The issue tracker field mappings are an advanced feature, and it is up to
the user to make sure that the default values and expressions entered will produce valid
values for the relevant issue tracker field types.

For more information on field configuration, see the following topics:

- Expression Basics
- Expression Logic
- Helpers
- Enumerable Fields
