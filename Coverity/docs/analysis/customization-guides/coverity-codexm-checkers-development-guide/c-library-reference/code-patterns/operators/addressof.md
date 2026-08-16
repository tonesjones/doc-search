---
title: "addressOf"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/addressof.html"
content_id: "1taO_OSHHxe6ZqMsIoAq_Q"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:32:01.827481+00:00"
---

# addressOf

Matches instances of the address-of ( `&` ) operator.

This pattern only matches nodes of type `expression`.

## Properties

`addressOf` produces a record that contains the following property.

| Name | Type | Description |
| --- | --- | --- |
| `kind` | `enum intKind` | The type to find the address of: one of `` `bool` ``, `` `byte` ``, `` `char` ``, `` `decimal` ``, `` `double` ``, `` `dynamic` ``, `` `enum` ``, `` `float` ``, `` `int` ``, `` `object` ``, `` `sbyte` ``, `` `short` ``, `` `string` ``, `` `uint` ``, `` `ulong` ``, or `` `ushort` ``; see intKind |

**Inherits properties from:**

- astnode
- expression

## Example

The following pattern matches operations that obtain the address of `int` variables:

[image: CXM code follows]

```
    pattern addressOfInt {
        addressOf {
            .operandType == integralType {
                .kind == `int`
            }
        }
    };
```
