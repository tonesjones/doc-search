---
title: "Configuring custom issue categories"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/configuring-custom-issue-categories.html"
content_id: "YBQ5QBduk4DadYeFLxCP4w"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:48:24.841506+00:00"
---

# Configuring custom issue categories

Coverity Connect allows you to change the impact level and category of issue types
through a custom issue (defect) category map file (JSON file). Issues are categorized by
the following criteria:

- Impact levels (High, Medium, Low, or Audit). In Coverity Connect, you can
  filter software issues by impact level, which can help you to identify the
  issues that require attention first.
- Issue description and category. For example, a C/C++ FORWARD_NULL checker can
  report Medium priority Unchecked dynamic_cast issues
  that belong to the Null pointer dereferences
  category.

For details about issue categories, see the Coverity 2026.6.0 Checker Reference.

**To customize issue categories:**

1. Navigate to Configuration > System > Issue Categorization.
2. Click Download Value File to generate a list of available
   values for "`type`" and "`impact`", along with all
   currently known category names. This information will be useful in
   editing/creating the issue categorization map.
3. If you already have an issue categorization map you want to edit, select it from
   the Issue Categorization Map Name list, and click
   Export. Then you can open and edit the file in your
   text editor. Otherwise, you will have to create a new issue categorization
   map.

   See Issue categorization map JSON format for information on
   formatting the map file.
4. Click Import and browse to the JSON file
   location.
5. Click Next. A message will be displayed to tell you
   whether the import was successful. If the import fails, an error message will be
   displayed, describing the problem.

   Note that a successful import may still return one or more warning messages,
   describing potentially unintended results.
6. Issue categorization maps are applied to issues based on their stream. Therefore,
   to apply the mapping, you must configure your desired stream to apply the newly
   created map. See Selecting an issue categorization map for a stream for
   configuration instructions.

Note: Issue categorization maps can be synchronized across a Coordinator/Subscriber cluster.
In order to work correctly, however, all subscribers should be upgraded to match the
coordinator version. Otherwise, issue categorization may not work properly on all
subscriber instances.
