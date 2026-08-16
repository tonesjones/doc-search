---
title: "Java Android primitives"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/java-android-primitives.html"
content_id: "J43kBxaeMnKPGT4sRfxhMA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:26:06.197982+00:00"
---

# Java Android primitives

These primitives model Android state transitions.

## `void add_action( java.lang.Object o, java.lang.String p )`

Adds a new *intent* action, `p`, to match against the *IntentFilter* object `p`.

## `void build_componentName( java.lang.Object o )`

Models adding a *ComponentName* object that is used to change an *intent* from implicit to explicit and also to decide whether the *intent* can be safely broadcast or not.

## `void build_context( java.lang.Object o )`

Models adding a *Context* object that is used to change an *intent* from implicit to explicit and also to decide whether the *Intent* can be safely broadcast or not.

## `void build_intent( java.lang.Object o )`

Marks the parameter `o` as containing an operation *intent* to be performed.

## `void build_intentFilter( java.lang.Object o )`

Creates an *IntentFilter* instance with a specified filter object `o`, where `o` can be 1) an action, 2) an *IntentFilter* instance, or 3) null.

## `void build_safe_context()`

Models the constructor for a *context* object.
Changes the context's *intent* from implicit to explicit and also decides
whether the intent can be safely broadcast or not.

## `void build_safe_packageName()`

Models the constructor for a *package* object.
Changes the package's *intent* from implicit to explicit and also decides
whether the intent can be safely broadcast or not.

## `void implicit_intent_sink( java.lang.Object o )`

Models *bindService, start Activity, startActivities, startIntentSender, startService, stopService, startActivityForResult* actions, and so on as implicit *intent* sinks.

The parameter `o` specifies the *intent* object being started or bounded by another activity.

## `void make_intent_explicit( java.lang.Object o, java.lang.Object p )`

Models changing an implicit *intent* into an explicit *intent* by function calls such as `setPackage()`, `setClass()`,
`setClassName()`, and `setComponent()`.

The parameter `o` is the *intent* object being made explicit.

The parameter `p` can equal `packageName`, `ComponentName`, or `Context`.

## `void register_receiver( java.lang.Object o, java.lang.String p )`

Registers a receiver of broadcasts, `p`, with an *IntentFilter*, `o` and broadcast permission.

The parameter `o` specifies the *IntentFilter*.

The parameter `p` specifies the broadcast permission.

## `void send_broadcast( java.lang.Object o, java.lang.String p )`

Simulates broadcasting the parameter `o`.

The parameter `o` specifies the object to broadcast.

The parameter `p` specifies the broadcast permission.

## `void set_class( java.lang.Object o, java.lang.Object p )`

Used by the IMPLICIT_INTENT checker
to detect the use of implicit intents.

The parameter `o` specifies the *intent* object, and
`p` should be a `className`.

## `void set_component( java.lang.Object o, java.lang.Object p )`

Used by the IMPLICIT_INTENT checker
to detect the use of implicit intents.

The parameter `o` specifies the *intent* object, and
`p` should be a `componentName`.

## `void set_package( java.lang.Object o, java.lang.Object p )`

Used by the IMPLICIT_INTENT and MISSING_PERMISSION_FOR_BROADCAST checkers to
to detect the use of implicit intents.

The parameter `o` specifies the *intent* object, and
`p` should be a `packageName`.
