---
title: "Customized filters"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/customized-filters.html"
content_id: "dizcbjw3y9GOkoHEgmrQPg"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:49:28.999895+00:00"
---

# Customized filters

Customized filters enable you to configure one or more filters to restrict the number of issues
you wish to be displayed in the Issues view.

To construct your filter settings, select the edit filter...
option from the Filter
drop-down menu. This launches
the Filter Manager
window.

Figure 1. Filter Manager window
[image: image]

To create a new filter, click the Add button and enter the name of
the filter in the Name field. This is the name that will display
in the Filter list in the Issues view. If there is a pre-defined
or an existing saved filter that you want to be the basis for a new filter, highlight it
and select the Copy button to edit the filter's
configuration.

Filters are made up of one or more filter expressions. A Filter expression consists of
the following:

Attribute
:   Describes an aspect of the analysis results for the issue. For example, you can specify
    user-defined triage states, a checker or issue type, and so forth. The
    attributes that you can define for a filter are described in the Filter attributes and values table.

    Note: The attribute and value table does
    not include any custom attributes that might exist if they were
    created in Coverity Connect.

Qualifier
:   Defines the criteria for how the value, related to its attribute, appears
    in the search. Each attribute will have a unique list of possible
    qualifiers from which you can choose, but each qualifier is described in
    the Filter qualifiers table.

Value
:   Represents a specific aspect of an attribute. Attribute values are
    described in the Filter attributes and values table.

For example, the following filter expression, when saved and applied as a filter,
will return only the issues that have a Classification of Bug:

Figure 2. Simple filter example
[image: image]

Coverity Desktop enables you to construct more complex filters. The filter
edit buttons enable you to add multiple filter expressions and nested filter expressions.
The controls are explained next.

Table 1. Filter edit buttons

| Button | Action | Description |
| --- | --- | --- |
| [image: image] | Add | Adds a filter expression at the current level. There are two levels at which you can add a filter, the top level and the nested level. New filter expressions created at the top level are AND operators, so results are returned if they match all of filter expressions that you add at that level. Top-level filter expressions have to contain a unique filter value. The Add button also creates new nested expressions at the same level as the previous nested expression (if one exists). |
| [image: image] | Remove | Removes the current filter expression. If you remove a top level expression that contains nested expressions, all of those expressions are deleted. |
| [image: image] | Add nested | Adds a new nested expression one level under the current top level expression. Nested expressions are OR operators, so results are returned for the current top level expression if the results match the top-level and any of the nested levels. All nested level expressions that belong to the same top level expression must filter on the same attribute. You can change the qualifiers and values. |

For example, the following filter expressions, when saved and applied as a filter, return
any issues that match the following:

- Any Classification value that is Unclassified

  AND
- Any Impact rating of High Impact

  that has any of the following Action values:
  - Undecided

    OR
  - Fix Required

    OR
  - Modeling Required

Figure 3. Complex filter example
[image: image]

The following table lists the default attributes and possible values that you can use in a
given filter expression. Note that this table does not include custom attributes and
values that can be created in Coverity Connect:

Table 2. Filter attributes and values

| Attribute | Description | Values |
| --- | --- | --- |
| Action | The action to be taken on the issue. | Undecided, Fix Required, Fix Submitted, Modeling Required, or Ignore. For definitions of the action values, see Action. |
| Category | Represents a description of the type of issues that one or more checkers might find during analysis. | A checker category chosen from a pick list. |
| Checker | The name of the checker that reported the issue. | A checker name chosen from a pick list or a full or partial name of a checker entered by the user. |
| CID | The CID (unique numerical representation) of the issue. | A number or range of numbers. |
| Classification | The classification of the issue. | Unclassified, Pending, False Positive, Intentional, or Bug. For definitions of classification values, see Classification. |
| Component | Displays issues that are contained in one or more components to which you have access. Component filtering is CID-based, so an issue is included even if only one of its occurrences happens to be in the included component. Components that are invisible to users (through Access Control or exclusion) do not appear in the filter. For more information about components, see the Coverity Platform 2026.6.0 User and Administrator Guide. | A component name chosen from a pick list (if there is more than one) or a full or partial name of a component entered by the user. |
| External Reference | An identifier (such as an issue number in a different database) specified by your company. | An external reference value chosen from a pick list or a full or partial external reference value entered by the user. |
| File | The name of the file that contains the issue. | A full or partial file name entered by the user. |
| First Detected | The date of the analysis in which the issue was first detected. | A date or a number of hours, days, weeks, or years. |
| Fix Target | The targeted time frame in which the issue should be fixed. | Untargeted, or any custom value set by an administrator. |
| Function | The name of the function that contains the issue. | A full or partial function name entered by the user. |
| Impact | Impact is a rating of how the issue will affect your code or program. Some issue types have a greater impact on software stability than others. Filtering by impact enables you to view high impact issues first. | High, Medium, Low, or Audit. |
| Issue Kind | Specifies the type of issue found. | Quality, Security |
| Language | Programming language associated with the issue. | A Coverity supported programming language (C++, Java, etc.) |
| Legacy | Specifies whether the CID is a *Legacy* issue. | True or False. |
| Local Issue Status | Specifies whether the CID exists locally and/or in the reference stream. This attribute only applies to local analysis results. | "Missing locally", "Local only", or "Present in reference". |
| MISRA Category | The classification for MISRA issues | Mandatory, Required, or Advisory (If this choice is left blank, it is set to None.) |
| Occurrences | The number of issues that have this CID. | A number or range of numbers. |
| Owner | The owner of the issue. Coverity Desktop gives you a drop-down list of all available users on the Coverity Connect instance to which the plug-in is connected. By default, the owner is the current user. | A Coverity Connect username chosen from a pick list or a full or partial username entered by the user. |
| Present in Reference | Indicates whether a CID is present in your reference stream. | True or False. |
| Severity | The severity assigned to the issue. | Unknown, Major, Moderate, or Minor. For definitions of the severity categories, see Severity. |
| Type | Issue type. For example, *Resource leak*, *Out-of-bounds write*. | An issue type chosen from a pick list. |

The following table lists the qualifiers that are available to you when you construct
your filter expressions. This table is a comprehensive list of the qualifiers.
Attributes will only contain a certain subset of these qualifiers (based on the type of
attribute):

Table 3. Filter qualifiers

| Qualifier | Action |
| --- | --- |
| is | Includes the value for the attribute in the filter. |
| is not | Includes all other values (excluding the value that is specified) for the attribute in the filter. |
| contains | Include the value for the attribute if the value contains the characters entered in the text field. |
| matches glob | Include the value if it matches any part of the entered glob pattern. For example, if you choose the Checker attribute and add `FB.*NW*`, the filter will return all available checkers that contain "FB." and the characters "NW", such as FB.UWF_UNWRITTEN_FIELD or FB.NP_UNWRITTEN_FIELD. |
| starts with | Include the value for the attribute if the value starts with the exact characters entered in the text field. |
| ends with | Include the value for the attribute if the value ends with the exact characters entered in the text field. |
| is in the range | Select a range of two dates or numbers. |
| is greater than | A range that is greater than the number you enter. |
| is less than | A range that is less than the number you enter. |
| is after | Select a single date. Returns values that occur after the specified date. |
| if before | Select a single date. Returns values that occur before the specified date. |
| is today | Returns the values that match the current date. |
| in the last | Returns the values that match the specified number of hours, days, weeks, or months. |
| not in the last | Returns the values that do not match the specified number of hours, days, weeks, or months. |
