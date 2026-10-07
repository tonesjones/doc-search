---
title: "argList"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/arglist.html"
content_id: "XR03I8YDQkVyLOouZjICkQ"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:27.232257+00:00"
---

# argList

Matches the use of `__arglist`.

In C#, you can use `__arglist` as an argument to a new `ArgIterator` object.
This allows you to later call that object using `__arglist(args)`
and specify an arbitrary number of arguments in place of "`args`".

In other words, `__arglist` behaves somewhat like the `...`
construct for "tuple" arguments in C++.

This pattern only matches nodes of type `expression`.

## Properties

`argList` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| Name | Type | Description |
| `type` | `type` | The type of the expression |

**Inherits properties from:**

- astnode
- expression

## Example

Here is an example of using `__arglist` in a `new` declaration:

  
 [image: C# code follows]   

```
    ArgList(__arglist)
    {
        var iterator = new System.ArgIterator(__arglist);
        // ...
```
