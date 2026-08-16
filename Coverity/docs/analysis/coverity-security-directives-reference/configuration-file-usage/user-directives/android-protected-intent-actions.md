---
title: "android_protected_intent_actions"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/android_protected_intent_actions.html"
content_id: "eziU8XWm84CmmnbXucKObA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:43:35.056232+00:00"
---

# android_protected_intent_actions

**Languages: Java Android**

The `android_protected_intent_actions` directive specifies Android
`Intent` actions to treat as protected.

The Android analysis considers some `Intent` actions to be protected
because `Intent` objects that contain such an `Intent`
action can only come from a trusted source (for example, from the Android system). If
each `intent-filter` of an Android application component either contains
a safe
category or contains only protected `Intent`
actions, the analysis assumes that the component can only receive
`Intent` objects from trusted sources.

Examples of `Intent` actions that the analysis considers to be
protected:

- `android.intent.action.AIRPLANE_MODE`
- `android.intent.action.BATTERY_CHARGED`
- `android.intent.action.BATTERY_LOW`

If multiple `android_protected_intent_actions` directives are specified,
the analysis considers the union of all the `Intent` actions specified in
all the `android_protected_intent_actions` directives.

## Fields

This directive uses the following field:

`android_protected_intent_actions`
:   Specifies a JSON array of strings. Each string is the name of a protected
    `Intent` action.

## See also

The android_safe_categories
directive.
