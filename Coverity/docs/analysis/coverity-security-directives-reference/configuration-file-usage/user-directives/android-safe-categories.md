---
title: "android_safe_categories"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/android_safe_categories.html"
content_id: "_NcTiigkV82PvMDwIkT4Lg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:43:35.709197+00:00"
---

# android_safe_categories

**Languages: Java Android**

The `android_safe_categories` directive specifies categories within
Android `Intent` objects to treat as safe.

If an `Intent` object contains a category that the analysis deems safe,
the analysis will also assume that the `Intent` object comes from a
trusted source. If each `intent-filter` of an Android application
component either contains a `safe` category or contains only protected `Intent` actions, the analysis considers that the
component can only receive `Intent` objects from trusted sources.

By default, the analysis considers the following categories to be safe:

- ```
  android.intent.category.HOME
  ```
- ```
  android.intent.category.LAUNCHER
  ```

This directive can be used to extend the list of categories that the analysis considers
to be safe.

If multiple `android_safe_categories` directives are specified, the
analysis considers the union of all the categories specified in all the
`android_safe_categories` directives.

## Fields

This directive uses the following field:

`android_safe_categories`
:   Specifies a JSON array of strings. Each string is the name of a safe
    category.

## See also

The android_protected_intent_actions
directive.
