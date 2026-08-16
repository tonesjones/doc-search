---
title: "Go concurrency primitives"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/go-concurrency-primitives.html"
content_id: "FwDuz1ygTzeF_vS7bdTT0w"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:25:54.645602+00:00"
---

# Go concurrency primitives

These primitives represent conditions for managing concurrent execution.

## `Lock( lock interface{} )`

Simulates acquiring a lock on the object provided.

**Parameters:**

`lock`
:   The object to be modeled as a lock being locked

**See Also:**
`Unlock()`

## `Sleep`

Indicates that the calling function might take a long time to complete, or might
otherwise block execution.

## `Unlock( lock interface{} )`

Simulates releasing a lock on the object provided.

**Parameters:**

`lock`
:   The object to be modeled as a lock being unlocked.

**See Also:**
`Lock()`
