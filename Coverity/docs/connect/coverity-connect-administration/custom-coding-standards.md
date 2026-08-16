---
title: "Custom coding standards"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/custom-coding-standards.html"
content_id: "3Q2OZrpB3iuja3HvLfB54Q"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:50:32.722513+00:00"
---

# Custom coding standards

A Coverity Connect administrator can take an existing coding standard, such as MISRA, and modify
rules in order to create a customized standard.

For example, you might want to implement a non-default way of determining the priority of MISRA defects based on certain characteristics.
In this case, you would specify a different mapping of MISRA rules to MISRA categories.

Note:
This guide uses the term "coding standard" in a general sense. Some standards that Coverity supports,
such as OWASP, have general application; others, such as MISRA, are designed for specific industries.

A custom standard is simply a user-provided JSON file that maps types of issues, in the form
of *issue type keys,* to user-defined values. Once created, your uploaded JSON file, the new standard,
can be visible along with other standards in the Coverity Connect interface.
It appears as a new column in Issues: By Snapshot views, Issues: Project Scope views,
and in Coverity Policy Manager.

Remember:
For Coverity Connect to display the column showing issues from a custom standard, you must have enabled this column's display
in the Settings dialog.
The values that appear in this column will be the custom values you have specified.

Editing an existing standard's JSON file is not a requirement: You can also use the standards template as a guideline,
or simply create a new custom coding standard from scratch.

The custom standard becomes available in the Coverity Connect Configuration - Standards window,
which you can access by selecting Configuration > Standards.

This window contains the following buttons:

- **+Standard** enables you to add a new standard to the Coverity Connect GUI. This process includes creating, naming, and
  saving the standard on your local system, then uploading the standard to your Coverity Connect server.
- **Download Template** downloads the standards template to your
  local system. You can use this template as guidance to create your custom
  standard.

  The template lists all built-in issue type keys.
- **Download Selected** downloads the selected standard to
  your local system.
- **Update** enables you to update a custom standard, overwriting it
  with another copy.
- **Rename** enables you to rename a custom standard.
- **Hide** or **Unhide** hides or unhides the selected standard
  from the usual views: Issues: By Snapshot, Issues: Project Scope,
  and Policy Manager.
- **Delete** deletes the selected custom standard.

Notice:
You cannot update, rename, or delete a built-in standard.
