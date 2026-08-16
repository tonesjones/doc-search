---
title: "Creating a policy rule"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/creating-a-policy-rule.html"
content_id: "JI4Om2oJrP4Tysiesa8lng"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:31:12.460654+00:00"
---

# Creating a policy rule

Create rules to ensure that your projects do not have an open source component, component
version, or vulnerability that violates your policies.

You can create multiple rules and rules can have multiple conditions giving you the
flexibility to create generic or highly specific global policy rules.

Note: Only users with the Policy Manager role can
create policy rules.

## Creating a policy

1. Log in to Black Duck SCA as a user with the Policy Manager
   role.
2. Click [image: image] and select **Policies**.
3. Click **Create Policy Rule** to display the Create Policy Rule dialog
   box.
4. Complete the following:

   - **Name**. Required. Name of this policy.
   - **Category**. Optional. Assign one of the following categories for
     this policy:

     - Uncategorized. This is the default value.
     - Component.
     - License.
     - Operational.
     - Security.

     Black Duck SCA provides a filter in the project
     version BOM (to view policy violations by category) and the Policy
     Management pages (to view policies by category).
   - **Description**. Optional. This description appears when you
     select **>** on the Policy Management page.
   - **Severity**. Optional. The severity level of this policy. You can
     use this option with build integrations to indicate what should
     happen when a policy violation occurs. For example, all policy
     violations with a severity of Blocker should fail the build.

     Select one of the following values: **Blocker**, **Critical**,
     **Major**, **Minor**, or **Trivial**.
   - **Scan Modes**. Select whether this policy rule applies to Full
     Scans (default value), Rapid Scans, or both.
   - **Enabled**. Clearing this option disables this rule. BOMs will
     not be evaluated until the rule is enabled.

     Clear the option if you want to create draft policy rules.

     You can enable
     or disable the rule after it is created.
   - Select whether to allow manual overrides for this rule.

     Users
     with the Policy Manager role can override a disapproved component in projects in which
     they are a member or have project-group privileges.
   - Select whether this policy rule applies to all projects or a subset
     of filtered projects – projects with specific properties.

     Selecting filtered projects displays the policy filters, as described
     above, that you can select for this policy rule. Select a project
     filter, an operator, and specify a value.
5. For a project condition: ensure you have the **A Subset of Projects,
   filtered by...** option is enabled, select an attribute from the
   Project Conditions list, select an operator, and specify a value.

   Click **+ Project Condition** to specify additional project
   conditions.
6. For a component condition: select an attribute from the **Component
   Conditions** list, select an operator, and specify a value.

   Click **+ Component Condition** to specify additional component
   conditions.
7. For a vulnerability condition: select an attribute from the **Vulnerability
   Conditions** list, select an operator, and specify a value.

   Click **+ Vulnerability Condition** to specify additional vulnerability
   conditions.
8. To remove a condition, click [image: Delete icon] in the row of the condition you wish to remove.
9. Click **Create**.

   If the rule is enabled, existing BOMs are evaluated to determine if they are
   in violation of this rule. For any components that are in violation of
   component or vulnerability conditions, the Policy Violation icon ( [image: image] ) appears
   next to component name.

## Policy conditions

Creating the condition(s) for a policy rule consists of selecting the projects that
this rule applies to (all or specific project attributes) and then selecting:

1. A component and/or vulnerability attribute

   You can create a policy rule for a component, a
   vulnerability, or for a
   component and vulnerability combination.
2. An operator (such as equals or greater than)
3. A value (depending on the option you selected)

Components that meet the conditions will violate the policy rule. For vulnerability
conditions, components that have vulnerabilities that meet the vulnerability
conditions violate the policy rule.

You can create multiple conditions for a policy rule: *all* conditions must be
true for a component to be in violation.

When evaluating components with multiple licenses for policy rules created using one
or more of these license conditions: license, license status, license family and/or
license expiration date, each license is evaluated and *all* license conditions
must be true for a policy violation. If license risk is included as a policy
condition, license risk is evaluated independently: all licenses for the component
are evaluated, not just the license that met the other license policy conditions.
Therefore, a policy violation can be triggered if one license meets the policy rule
for multiple conditions while another license for that component meets the license
risk condition.

Note: All attributes appear for you to select, including attributes for those modules for which
you are not licensed.

The table below shows the project filters you can select and the values you can
specify.

### Project Conditions filters

The Project Conditions filter is displayed when the **A Subset of Projects,
filtered by...** option is enabled.

  
 [image: image]   

Project Condition filters are divided into these categories:

- Properties
- Project Custom Fields
- Project Version Custom Fields

Table 1. Properties

| Project Filters | Value |
| --- | --- |
| Project Name | Begin typing to view possible values. |
| Project Group Name | Begin typing to view possible values. |
| Project Tags | Enter the tag name. |
| Project Tier | Enter one of the following values: 0 - 5. |
| Project Phase | Select one of the following values:   - Deprecated - In Development - In Planning - Pre-Release - Released |
| Project Distribution Type | Select one of the following values:   - External - Internal - Open Source - SaaS |

Table 2. Project Custom Fields

| Project Filters | Value |
| --- | --- |
| Project Custom Field Name | Available for Boolean, Date, Drop Down, Multiple Selections, Single Selection, and Text field types.  Select a value. |

Table 3. Project Version Custom Fields

| Project Filters | Value |
| --- | --- |
| Project Version Custom Field Name | Available for Boolean, Date, Drop Down, Multiple Selections, Single Selection, and Text field types.  Select a value. |

### Component conditions

Component conditions are divided into these categories:

- Properties
- Operational
- Vulnerabilities
- Licenses
- Custom Fields: BOM Component, Component, and Component Version

Table 4. Properties

| Component Condition | Value |
| --- | --- |
| Component | Begin typing to view possible component values.  After selecting a component, the version field appears whereby you can enter a version number. **Any Version** is the default value if you do not enter a specific version. |
| Component Usage | Select one of the following values:   - Dev. Tool / Excluded - Dynamically Linked - Source Code - Statically Linked - Separate Work - Implementation of Standard - Prerequisite - Merely Aggregated - Unspecified |
| Review Status | Select one of the following values:   - Not Reviewed - Reviewed |
| Match Type | Select one of the following values:   - Files Added/Deleted - File Dependency - Direct Dependency - Transitive Dependency - Exact Directory - Exact File - Files Modified - Manually Added - Manually Identified - Partial - Snippet - Binary - Direct Dependency Binary - Transitive Dependency Binary |
| Component Purpose | Select either Yes or No.  Indicates whether information was added in the **Purpose** field when manually adding or editing a component. |
| Component Modified | Select either Yes or No.  Indicates whether the **Modification** option was selected when manually adding or editing a component. |
| Component Modification | Select either Yes or No.  Indicates whether information was added to the **Modification** field when manually adding or editing a component. |
| Component Approval Status | Select one of the following values:   - Unreviewed - In Review - Reviewed - Approved - Limited Approval - Rejected - Deprecated |
| Component Version Approval Status | Select one of the following values:   - Unreviewed - In Review - Reviewed - Approved - Limited Approval - Rejected - Deprecated |
| Unknown Component Version | Select **True** or **False**.  If you select **True**, any component that has a ? as the version will trigger a policy violation. |
| Unconfirmed Snippets | Select **True** or **False**.  If you select **True**, any snippet that has not been reviewed will trigger a policy violation. |

Table 5. Operational

| Component Condition | Value |
| --- | --- |
| Component Release Date | Select a date. |
| Component Release Age | Enter a number value in days. |
| Newer Versions Count | Enter a number. |
| Commits in the past year | Enter a number. |
| Contributors in the past year | Enter a number. |

Table 6. Vulnerabilities

| Component Condition | Value |
| --- | --- |
| Critical Severity Vulnerability Count | Enter a number. |
| High Severity Vulnerability Count | Enter a number. |
| Medium Severity Vulnerability Count | Enter a number. |
| Low Severity Vulnerability Count | Enter a number. |
| Highest Vulnerability Score | Enter a number between 0 and 10, including decimal numbers. |

Table 7. Licenses

| Component Condition | Value |
| --- | --- |
| Unfulfilled License Terms | Select **True** or **False**.  If you select **True**, any component that has unfulfilled license terms will trigger a policy violation.  Note: The **Legal** tab must be enabled for a user to indicate that a term is fulfilled. If the **Legal** tab is disabled, a user will be unable to indicate that a term is fulfilled, and policy violations cannot be cleared. |
| License Conflict with Project Version | Select **True** or **False**.  If you select **True**, a policy violation is triggered when a component's license conflicts with the license for a project version. |
| License Risk | Select one of the following values:   - None - Low - Medium - High |
| License (Declared) | Begin typing to view possible declared license values. |
| License Family (Declared) | Select one of the following KB license families (Permissive, Reciprocal, Weak Reciprocal, AGPL, or Unknown) or a custom license family for the declared license. |
| License Status (Declared) | Select one of the following values:   - Unreviewed - In Review - Reviewed - Approved - Limited Approval - Rejected - Deprecated |
| License Expiration Date (Declared) | Select an expiration date for the declared license. |
| License Expiration Date Comparison (Declared) | Use this condition to compare the declared license expiration date of a component to the project version release date. Specify a number which equals the number of days to *add to* the project version release date for the comparison. Black Duck triggers a policy violation if the date is less than or greater than that date.   - Use 'before' to trigger a policy violation when the   license expiration date is more than X number of   days before (or less than), the project version   release date. - Use 'after' to trigger a policy violation when the   license expiration date is more than X number of day   after (or greater than), the project version release   date.   The following are examples using 'before.' The project version release date is the 10th.   - Number of days = 0: triggers a policy violation when   the license expiration date is the day before the   project version release date (the 9th) or   earlier. - Number of days = 1: triggers a policy violation when   the license expiration date is the same day as the   project version release date (the 10th) or   earlier. - Number of days = 2: triggers a policy violation when   the license expiration date is the 11th or earlier.   (the   10th plus 2 days equals the 12th. : trigger a   violation for 4/11 and earlier) - Number of days = -2: triggers a policy violation when   the license expiration date is the 7th and earlier.   (the   7th - 4/10 -2 = 4/8. Trigger a violation for 4/7   and earlier)   The following are examples using 'after.' The project version release date is the 10th.   - Number of days = 0: triggers a policy violation when   the license expiration date is the day after the   project version release date (the 11th) or   later. - Number of days = -1: triggers a policy violation when   the license expiration date is the same as the   project version release date (the 10th) and   later. - Number of days = 2: triggers a policy violation when   the license expiration date is the 13th and later.    (10   +2 = 4/12.) - Number of days is -2: triggers a policy violation   when the license expiration date is the 9th and   later. (10 -2 = 8: policy violation for 9 and   later) |
| License (Deep License) | Begin typing to view possible deep (embedded) license values. |
| License Family (Deep License) | Select one of the following KB license families (Permissive, Reciprocal, Weak Reciprocal, AGPL, or Unknown) or a custom license family for the deep (embedded) license. |
| License Status (Deep License) | Select one of the following values for the deep (embedded) license:   - Unreviewed - In Review - Reviewed - Approved - Limited Approval - Rejected - Deprecated |
| License Expiration Date (Deep License) | Select an expiration date for the deep (embedded) license. |
| License Expiration Date Comparison (Deep License) | Use this condition to compare the deep license expiration date of a component to the project version release date. Specify a number which equals the number of days to *add to* the project version release date for the comparison. Black Duck triggers a policy violation if the date is less than or greater than that date.   - Use 'before' to trigger a policy violation when the   license expiration date is more than X number of   days before, or less than, the project version   release date. - Use 'after' to trigger a policy violation when the   license expiration date is more than X number of day   after, or greater than, the project version release   date.   The following are examples using 'before.' The project version release date is the 10th.   - Number of days = 0: triggers a policy violation when   the license expiration date is the day before the   project version release date (the 9th) or   earlier. - Number of days = 1: triggers a policy violation when   the license expiration date is the same day as the   project version release date (the 10th) or   earlier. - Number of days = 2: triggers a policy violation when   the license expiration date is the 11th or earlier.   (the   10th plus 2 days equals the 12th. : trigger a   violation for 4/11 and earlier) - Number of days = -2: triggers a policy violation when   the license expiration date is the 7th and earlier.   (the   7th - 4/10 -2 = 4/8. Trigger a violation for 4/7   and earlier)   The following are examples using 'after.' The project version release date is the 10th.   - Number of days = 0: triggers a policy violation when   the license expiration date is the day after the   project version release date (the 11th) or   later. - Number of days = -1: triggers a policy violation when   the license expiration date is the same as the   project version release date (the 10th) and   later. - Number of days = 2: triggers a policy violation when   the license expiration date is the 13th and later.    (10   +2 = 4/12.) - Number of days is -2: triggers a policy violation   when the license expiration date is the 9th and   later. (10 -2 = 8: policy violation for 9 and   later) |

Table 8. BOM Component Custom Fields

| Component Condition | Value |
| --- | --- |
| BOM Component Custom Field Name | Available for Boolean, Date, Drop Down, Multiple Selections, Single Selection, and Text field types. Select a value. |

Table 9. Component Custom Fields

| Component Condition | Value |
| --- | --- |
| Component Custom Field Name | Available for Boolean, Date, Drop Down, Multiple Selections, Single Selection, and Text field types. Select a value. |

Table 10. Component Version Custom Fields

| Component Condition | Value |
| --- | --- |
| Component Version Custom Field Name | Available for Boolean, Date, Drop Down, Multiple Selections, Single Selection, and Text field types. Select a value. |

The table below shows the vulnerability attributes that you can select and the
values you can specify.

### Vulnerability conditions

When configuring policy rules with vulnerability conditions, it is important to
understand how remediation status affects policy evaluation.

#### Vulnerability Score and Remediation

Policy rule vulnerability conditions do not automatically exclude remediated
vulnerabilities from results. Vulnerabilities retain their original overall
score even after remediation actions have been taken. This means that if a
policy is based on vulnerability score, the policy condition will not be
automatically cleared when a vulnerability is remediated.

#### **Remediation Status in Component Vulnerability Conditions**

Unlike Vulnerability Conditions, **Component Conditions** automatically
exclude vulnerabilities with remediated statuses from evaluation. For
example, when using the Component Condition **Highest Vulnerability
Score**, remediated vulnerabilities are not considered in the score
calculation.

This behavior makes Component Conditions a preferred option for customers who
want policy rules that automatically account for remediation without
requiring additional expressions. For instance, customers may choose to use
the Component Condition **Highest Vulnerability Score** instead of
combining the Vulnerability Condition **Overall Score** with a
**Remediation Status** expression.

#### Best Practice: Include Remediation Status

To ensure that your policy rules accurately reflect the current state of vulnerabilities in
your project:

- Consider including an expression for **Remediation Status** in
  your policy conditions. This allows you to create more precise
  policies that account for remediation actions and avoid false
  positives from vulnerabilities that have already been addressed.
- **Use Vulnerability Conditions** when you need granular control
  over vulnerability evaluation and want to explicitly define how
  remediation status should be handled.
- **Use Component Conditions** when you want remediated
  vulnerabilities to be automatically excluded from policy
  evaluation.

| Vulnerability condition | Value |
| --- | --- |
| Overall Score | Enter a number from 0 to 10. |
| Vulnerability IDs | Enter a specific vulnerability ID (CVE or BDSA). |
| CWE IDs | Enter a Common Weakness Enumeration (CWE) number. |
| Solution Available | Select either Yes or No.  Indicates whether there is a solution for the vulnerability. |
| Workaround Available | Select either Yes or No.  Indicates whether there is a workaround available for the vulnerability. |
| Exploit Available | Select either Yes or No.  Indicates whether there is an exploit for the vulnerability. |
| Reachable from Source | Select either Yes or No.  Indicates whether the vulnerability is reachable from the source code. |
| Remediation Status | Select one or more of the following values:   - Duplicate - Ignored - Known Affected - Known Affected: Mitigation - Known Affected: No fix planned - Known Affected: None available - Known Affected: Vendor fix - Known Affected: Workaround - Known Not Affected - Known Not Affected: Component not present - Known Not Affected: Vulnerable code not present - Known Not Affected: Vulnerable code cannot be   controlled by adversary - Known Not Affected: Vulnerable code not in execute   path - Known Not Affected: Inline mitigations already   exist - Mitigated - Needs Review - New - Patched - Remediation Complete - Remediation Required |
| Vulnerability Tags | Select one or more of the following values:   - AI Assisted - Zero-click Remote Code Execution - Malicious Code Identified - Embargoed Vulnerability Details - Unconfirmed Vulnerability - Automated Security Advisory - CISA Known Exploited Vulnerability - Rapid Review |
| Published Age | Allows you to define a policy based on how recently a vulnerability was published.  Enter a number value in days. |

### Operators in Black Duck SCA Policies

In Black Duck SCA, operators are essential for defining rules and
conditions within policy management. They allow users to create precise and
effective policies for managing open source components, vulnerabilities, and
compliance requirements.

This section outlines the different types of operators available, including
logical, comparison, membership, string, and existence operators. Understanding
how to use these operators is crucial for formulating policies that align with
your organization's security and compliance objectives.

#### Types of Operators

- **Comparison Operators**: Compare values to establish conditions
  for policy enforcement.

  - **Equals**: Checks if two values are equal.
  - **Not Equal To**: Checks if two values are not equal.
  - **Less Than**: Checks if a value is less than another value.
  - **Greater Than**: Checks if a value is greater than another value.
  - **Less Than or Equal To**: Checks if a value is less than or equal to another value.
  - **Greater Than or Equal To**: Checks if a value is greater than or equal to another value.
- **Membership Operators**: Determine whether a value exists within
  a specified set.

  - **In**: Checks if a value exists within a specified list
    or set.
  - **Not in**: Checks if a value does not exist within a
    specified list or set.
- **Time Operators**: Used to filter and assess vulnerabilities or
  components based on their timestamps.

  - **Before**: Checks if a specified date or time occurs
    before another date or time.
  - **After**: Determines if a specified date or time occurs
    after another date or time.
  - **Older than**: Compares a date or time against a
    specified duration, checking if a record is older than the
    given time frame (e.g., older than 30 days).
  - **Younger than**: Compares a date or time against a specified duration, checking if a
    record is younger than the given time frame (e.g., younger
    than 30 days).
- **Other Operators**

  - **Included**: Checks if a component is part of a defined list or collection based on
    the criteria specified in the policy. It can be used to
    determine whether certain components are explicitly included
    in a project or BOM (Bill of Materials) for the purposes of
    vulnerability assessment, licensing compliance, or other
    related evaluations.
  - **Matches**: Used to determine if the value matches a specified pattern.
