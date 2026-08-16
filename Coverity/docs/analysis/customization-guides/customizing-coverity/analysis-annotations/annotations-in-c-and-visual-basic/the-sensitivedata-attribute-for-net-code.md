---
title: "The 'SensitiveData' attribute for .NET code"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-sensitivedata-attribute-for-.net-code.html"
content_id: "uONizjeRjrEiF5cqLk7UUw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:26:27.192719+00:00"
---

# The 'SensitiveData' attribute for .NET code

The `SensitiveData` attribute (`[SensitiveData]` for C#
and `<SensitiveData()>` for Visual Basic) notates sources of sensitive
data.

In the following examples, if the return value of `GetMyLocation` or
the argument passed to `RetrieveAccountNumbers` passes to a sink that
exposes information, the SENSITIVE_DATA_LEAK checker will report a defect.

Here is an example of using `[SensitiveData]` in C# code:

```
using Coverity.Attributes;
using Coverity.Primitives;

class SensitiveDataExample {

    [SensitiveData(SensitiveDataType.Geographical)]
    string GetMyLocation() {
        return "This is considered sensitive geographical data.";
    }

    void RetrieveAccountNumbers(
    [SensitiveData(SensitiveDataType.Account)] string[] accts) {
        // The parameter arg1 will be treated as sensitive account
        // data inside of this method and in the caller after passing
        // it through this method.
    }
}
```

Here is an example of using `<SensitiveData()>` in Visual Basic code:

```
Imports Coverity.Attributes
Imports Coverity.Primitives
Imports System

Class SensitiveDataExample
    <SensitiveData(SensitiveDataType.Geographical)>
    Function GetMyLocation() As String
        Return "This is considered sensitive geographical data."
    End Function

    Sub RetrieveAccountNumbers(
    <SensitiveData(SensitiveDataType.Account)> accts() as String)
        ' The parameter arg1 will be treated as sensitive account
        ' data inside of this method and in the caller after passing
        ' it through this method.
    End Sub
End Class
```

You can specify multiple sensitive data types by passing an array argument to the
attribute. In the following examples, the field `LoginInfo` is
considered as both user-identifier and password data.

Here is an example of specifying multiple sensitive data types in C# code:

```
class LoginService {
    [SensitiveData(new[]{SensitiveDataType.UserId,SensitiveDataType.Password})]
    List<string> LoginInfo;
}
```

Here is an example of specifying multiple sensitive data types in Visual Basic
code:

```
Class LoginService
    <SensitiveData({SensitiveDataType.UserId,SensitiveDataType.Password})>
    Dim LoginInfo As List(Of String)
End Class
```
