---
title: "Configuring custom checker descriptions"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/configuring-custom-checker-descriptions.html"
content_id: "OEYReUNuteATpYIc1xCYcw"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:48:24.212088+00:00"
---

# Configuring custom checker descriptions

Note: Note the following:

- If Coverity Connect is deployed in the cloud, this section does not apply.
- The features described in this section are deprecated as of version 7.6.0. This
  functionality will be removed completely in a future release.

  Custom checker
  properties are now reported during the commit process automatically, so
  importing checker descriptions via a CSV file is no longer necessary.
  Coverity Connect continues to support custom issue categories and impact -
  see Configuring custom issue categories

Coverity Connect allows you to add issue descriptions and information that will be
displayed in the UI when a custom checker discovers an issue. The information you add
can appear in various locations in the Coverity Connect UI, such as:

- In the issue filters for checkers, categories, and types.
- In the CWE listing and Information tab in the Triage pane.
- In the Source browser as event descriptions.

All unrecognized checkers, developed with the Extend SDK or some other custom solution,
are categorized as Miscellaneous (a `category`
value) and as type Other violation (a `name`
value) in the UI unless you specify the checker descriptions in a CSV file (for example,
customCheckers.csv) and then import the file to Coverity
Connect. Alternatively, you can create a custom categorization map that recategorizes
the defect type (see Configuring custom issue categories).

Note: Note that all custom checkers will initially
be assigned an impact of "Low". If you wish to change the impact value for a custom
checker, create an Issue
Categorization Map to map the checker `type` to your desired
`impact` value.

The CSV file accepts the following values:

domain
:   Represents the programming language that the checker analyzes or the type of
    analysis. The following values are allowed:

    - STATIC_C - C/C++ language.
    - STATIC_JAVA - Java language.
    - STATIC_CS - C# language.
    - DYNAMIC_JAVA - Dynamic Analysis.
    - OTHER - Denotes another language that might be used with
      importing third-party issues. See "Using the Third Party Integration Toolkit" in the Coverity Analysis 2026.6.0 User and Administrator Guide for more
      information.

    This is a required field.

Name
:   The display name of the checker. This is a required field.

subcategory
:   A checker subcategory, describing the issue produced by the checker. Checkers
    can have multiple subcategories. This is an optional field.

    Extend SDK checkers do not support subcategories, so all issues will have a
    subcategory of none.

category
:   A string used to describe the nature of the issue. This must be a string
    between 2 and 256 characters long, and can be a previously known category or
    a custom category.

    This a required field.

type
:   A short description of a checker that will be displayed under the
    Type filter in the issue view. For more
    information abut the checker filters, see Coverity Connect usage.

    This is a required field.

CWE
:   The number that corresponds to an issue description in the Common Weakness
    Enumeration (CWE). The CWE provides further information and examples of the
    issue type.

long description
:   The description that will appear in the upper section of the triage
    pane.

local effect
:   The description that will appear under the Information tab in the triage
    pane.

event set 0 caption
:   Describes the event(s) that leads to the issue as found by your checker. This
    description is displayed in the Occurrences tab of
    the Triage pane.

    You can specify multiple events with event set 1
    caption and event set 2
    caption.

The file is simply a list of comma separated values. For example:

```
STATIC_C,checker1,*,apiUsageErrors,C API usage error,382,long description,local effect,event set 0 caption,event set 1 caption,event set 2 caption
STATIC_C,checker2,subcategoryA,buildSystemIssues,C build system issue,,long description,local effect,,,
STATIC_C,checker2,subcategoryB,controlFlowIssues,C control flow issue,398,long description,local effect,,,
STATIC_JAVA,checker1,*,apiUsageErrors,Java API usage error,382,long description,local effect,event set 0 caption,event set 1 caption,event set 2 caption
```

Be sure to format the CSV fields precisely, with no additional spacing or quoting around
field values. Each entry should be typed on a single line.

Note: Wildcards ("`*`") are accepted in the following places in the CSV
file:

1. After the period ("`.`") in a checker name. For example,
   `CustChkr.*` will return `CustChkr.1`,
   `CustChkr.2`, `CustChkr.3`, and so on
   (assuming they exist).
2. In the place of a subcategory name. The wildcard
   indicates that the specified category,
   cwe, short description,
   and so forth, should be applied to all subcategories of the specified
   checker.

**To import the CSV file:**

1. Edit and save the CSV file with your custom checker descriptions.
2. Navigate to Configuration > System > Custom Checkers.
3. Click the Import button and browse to the location of the
   CSV file.
   - If the structure of the file is valid, you will receive a Success
     notification.
   - If it is not valid, you will receive a Failure notification. In this
     case, you need to check your file for errors. You can also search
     for errors in cim.log.

   After the file is successfully imported, the checker name, description, and
   language (domain) are displayed in the custom checker table. The custom checkers
   will also be added to all of your category maps, under the categories specified
   in the imported CSV.

**To remove all custom checkers:**

1. Create an empty CSV file.
2. Click the Import button to import the empty CSV file.

   This action will remove any existing custom checker settings.

**To remove an individual custom checker:**

1. Click the Export button and save the
   customCheckers.csv file.
2. Open the customCheckers.csv file.
3. Remove the line or value (if it is not required) of the checker that you want to
   delete.
4. Save the customCheckers.csv file.
5. Click the Import button to import the new CSV
   file.
