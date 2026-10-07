---
title: "classParent"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/classparent.html"
content_id: "8OmTWYArfdbWLyoMiW9bzw"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:15.636875+00:00"
---

# classParent

Describes the parent of a given C++ class.

## Properties

`classParent` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `isVirtual` | `bool` | `true` if this is a virtual parent |
| `parent` | `classDefinition` | The definition for the parent class |

## Example

A class definition (that is, `classDefinition`)
includes a list of its parent classes via the `.parentList` field.
