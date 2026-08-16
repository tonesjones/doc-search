---
title: "Issue categorization map JSON format"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/issue-categorization-map-json-format.html"
content_id: "KNi1d3Q52kak5NZvSe9zDQ"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:48:25.468097+00:00"
---

# Issue categorization map JSON format

An imported issue categorization map must match a defined JSON format. Each map must
contain a "`name`" object, along with a list of "`types`".
Each individual `type` object consists of a type name, and an associated
"`category`" value, "`impact`" value, or both. This
will map the specified `category` and/or `impact` value
with all issues of the given `type`.

For example, the following JSON file creates an issue categorization map called "My
default map". It maps all issues of type "Allocation size error" to the "Memory -
corruptions" category and "High" impact. It also maps all issues of type "Calling
deprecated method" to the "Code maintainability issues" category. The built-in impact
for "Calling deprecated method" type issues remains unchanged.

```
{
    "name": "My default map",
    "types": {
        "Allocation size error": {
            "category": "Memory - corruptions",
            "impact": "High"
        },
        "Calling deprecated method": {
            "category": "Code maintainability issues"
        }
    }
}
```

Please note the following when creating or editing an issue categorization map:

- To override built-in "category" or "impact" values for any "types", import a
  map that only provides the new values. This is shown in the example
  above.
- It is not an error to use type names that Coverity Connect does not
  recognize, however a warning will be raised upon importing the file. This is
  to ensure that the issue type is a valid value and not a typo.

  Once imported, those type names will be recognized by Coverity Connect. In
  future commits, any issues with a matching type will be mapped
  accordingly.

  Note: A custom categorization can be tied to either a snapshot or stream. Each
  stream and snapshot also has its own categorization. Therefore, we recommend
  that you tie the categorization to a stream, so that the categorization
  persists for both the snapshot and stream. New changes will be seen only
  after a commit has been made to that stream, or when a new snapshot has been
  created.
- The value for "`category`" must be a string between 2 and 256
  characters long. You can use a previously known category, or create a custom
  category.
- Impact value must be "High", "Medium", "Low", or "Audit".
- "`category`" and "`impact`" are both optional,
  but at least one must be specified for each type.
- Null values are not valid for any field.
- The name shown for each issue type corresponds to a checker shown in the Coverity 2026.6.0 Checker Reference.
