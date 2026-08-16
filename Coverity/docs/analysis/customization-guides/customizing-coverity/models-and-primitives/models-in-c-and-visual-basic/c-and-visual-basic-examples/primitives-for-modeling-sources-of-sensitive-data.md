---
title: "Primitives for modeling sources of sensitive data"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/primitives-for-modeling-sources-of-sensitive-data.html"
content_id: "YTcIZHXJsZr289_ucdKkeA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:25:45.877839+00:00"
---

# Primitives for modeling sources of sensitive data

Detecting unsafe uses of sensitive data is built in to Coverity Analysis, but you can add models of additional,
application-specific sources in order to detect additional, and possibly more accurate,
defects.

Coverity Analysis reports defects—for example
`SENSITIVE_DATA_LEAK`,
`UNENCRYPTED_SENSITIVE_DATA`, or
`WEAK_PASSWORD_HASH`—when it detects unsafe uses of
sensitive data.

Methods that return sensitive data can be modeled using the
`Security.SensitiveSource` primitive. There are two versions of
this primitive: One takes a single argument, and the other takes two arguments. See
C# and Visual Basic primitives.

## Modeling a Login Method

The following C# model indicates that the `GetLoginInfo()` method
returns both sensitive user identifier and password information:

```
using Coverity.Primitives;
using System.Collections.Generic;
    
List<string> GetLoginInfo() {
    Security.SensitiveSource(SensitiveDataType.Password);
    Security.SensitiveSource(SensitiveDataType.UserId);
    return new List<string>();
}
```

The following Visual Basic model accomplishes the same thing:

```
Imports Coverity.Primitives
Imports System
Imports System.Collections.Generic
    
Function GetLoginInfo() As List(Of String)
    Security.SensitiveSource(SensitiveDataType.Password)
    Security.SensitiveSource(SensitiveDataType.UserId)
    Return New List(Of String)()
End Function
```
