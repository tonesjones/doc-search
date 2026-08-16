---
title: "coverity.conf file format"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity.conf-file-format.html"
content_id: "thl23sSKKDlOxhma4li31w"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:47:13.257000+00:00"
---

# coverity.conf file format

The coverity.conf file format is based on
[JSON](http://www.json.org/), but with
comments allowed. Comments may begin with "//" and go to the end of the line.

The overall structure of coverity.conf is depicted in the following
diagram (note that optional fields are marked with a "?"). For a working
coverity.conf example, see Example coverity.conf file.

[image: image]

The following sub-sections describe each of the constituent elements. Several conventions
and notations are used:

- Attributes (also known as fields or properties) are named beginning with a
  lowercase letter and consist of lowercase letters and underscores.
- Classes are named beginning with an uppercase letter and consist of mixed case names.
  Class names do not actually appear anywhere in the configuration file
  because JSON does not have a notion of a class.
- Required attribute declarations are written in the following format:

  ```
  "attribute_name": type
  ```

  This format means that there must be an attribute called
  "attribute_name" and its value must be consistent
  with type.
- A type is one of the following:
  - The scalars `bool`, `int`, or `string`
  - `regex` or `path`
    (these are like `string` but have special meaning)
  - A class name (meaning the value must be an object that conforms to the structure defined for that class)
  - One of the above followed by "`[]`" (meaning the value must be an array of the indicated type)
- Optional attribute declarations are written in the following format:

  ```
  "attribute_name"?: type
  ```

  Notice the "`?`" before the
  "`:`".

  This format means that the attribute can be
  omitted. The majority of attributes in this format are optional because the
  configuration can be created by combining multiple configuration sources.
