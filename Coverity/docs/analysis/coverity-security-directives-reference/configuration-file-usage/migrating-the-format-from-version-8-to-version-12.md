---
title: "Migrating the format from Version 8 to Version 12"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/migrating-the-format-from-version-8-to-version-12.html"
content_id: "uTKuuakTvmx0Hyc9ktUTPA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:44:06.335912+00:00"
---

# Migrating the format from Version 8 to Version 12

We don't recommend that you follow these steps unless it is necessary to support legacy code.
See "Migrate DC custom checkers to CodeXM"
in the Coverity 2026.6.0 Checker Reference.

To migrate away from using the deprecated fields to the `new_issue_type`
field that replaces them, proceed as follows:

1. Ensure that your directives file has a `format_version` of
   `8` or greater.
2. Add a `new_issue_type` field containing a JSON object to your
   checker definition.
3. Move your `category`, `cwe`,
   `impact`, `local_effect`,
   `long_description`, and `type` fields into
   this new object, but rename `long_description` to
   `description` and rename `type` to
   `name`. If you omitted any of these fields (and thus used the
   default values), there’s no need to create them: The defaults remain the
   same.
4. Set the `quality_kind` and `security_kind` fields
   of `new_issue_type` according to your old `kind`
   field.

   - `"kind"` : `"quality"` translates to
     `"quality_kind": "true"`, `"security_kind":
     "false"`
   - `"kind"` : `"security"` translates to
     `"quality_kind": "false"`, `"security_kind":
     "true"`
   - `"kind"` : `"both"` translates to
     `"quality_kind": "true"`, `"security_kind":
     "true"`
5. Remove your old `kind` field.
6. Optionally, add a `type` field of
   `new_issue_type`.
