---
title: "C# and Visual Basic concurrency primitives"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/c-and-visual-basic-concurrency-primitives.html"
content_id: "MmQbqGtCD7y86hDqN~~Atg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:25:49.345323+00:00"
---

# C# and Visual Basic concurrency primitives

These primitives represent conditions for managing concurrent execution.

## `Concurrency.Lock( System.Object o )`

Simulates acquiring a lock on the object provided.

Parameters:

`o`
:   The object to be modeled as a lock being locked

See also:

- `Concurrency.Unlock( System.Object )`

## `Concurrency.LockByMonitor( System.Object o )`

Simulates acquiring a lock (by a monitor) on the object provided.

Typically, `Concurrency.Lock( System.Object )`
is the preferable means of representing lock semantics, as
`LockByMonitor()` models subtly different behavior, and is
applicable only to Monitor objects.

Parameters:

`o`
:   The object to be modeled as a monitor lock being locked

## `Concurrency.ThreadUnsafeFunction()`

A call to this primitive in the model for a function indicates that calling the function from multiple concurrent contexts is an error.
This issue will be reported by the UNLOCKED_ACCESS checker.

## `Concurrency.TimedWait( System.Object o )`

Simulates a *wait* operation on the object provided. The *wait* might
return after a timeout and before a *pulse* on the object.

Parameters:

`o`
:   The object subject to the *wait* operation

See also:

- `Concurrency.Wait( System.Object )`

## `Concurrency.Unlock( System.Object o )`

Simulates releasing a lock on the object provided.

Parameters:

`o`
:   The object to be modeled as a lock being unlocked

See also:

- `Concurrency.Lock( System.Object )`

## `Concurrency.UnlockByMonitor( System.Object o )`

Simulates releasing a lock (by a monitor) on the object provided.

Typically, `Concurrency.Unlock( System.Object
)` is the preferable means of representing unlock semantics, as
`UnlockByMonitor()` models subtly different behavior, and is
applicable only to Monitor objects.

Parameters:

`o`
:   The object to be modeled as a monitor lock being unlocked

## `Concurrency.Wait( System.Object o )`

Simulates a *wait* operation on the object provided, which can block
indefinitely waiting for a *pulse* on the object.

Parameters:

`o`
:   The object subject to the wait operation

See also:

- `Concurrency.TimedWait( System.Object )`
