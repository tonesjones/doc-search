---
title: "The 'Tainted' and 'NotTainted' attributes for .NET code"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-tainted-and-nottainted-attributes-for-.net-code.html"
content_id: "eqa1SFoVoBzIvDZdV9Q4eg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:26:26.520157+00:00"
---

# The 'Tainted' and 'NotTainted' attributes for .NET code

Marking a field as `Tainted` indicates that security checkers should
treat that field as coming from an untrusted source (that is, as tainted). Marking a field
as `NotTainted` indicates that analysis should treat that data as untainted,
and not report a defect when the data flows into HTML output, an SQL interpreter, or other
such sink.

## The '`[Tainted]`' or '`<Tainted()>`' attribute

Security checkers (such as XSS, SQLI, and OS_CMD_INJECTION) report a defect when a field that
is annotated as `Tainted` (`[Tainted]` for C# and
`<Tainted()>` for Visual Basic) flows to HTML output, an SQL
interpreter, or to another such sink.

Here is an example of using `[Tainted]` in C# code:

```
using Coverity.Attributes;
using System.Web;
using System.Web.Mvc;

class HasTaintedField {
    // Here is a class member annotated as being tainted.
    [Tainted] string Untrusted;
}
    
// An MVC controller
class MyController : Controller {

    private HasTaintedField SomeData;

    // A controller request handler
    public ActionResult GetSomeHtml() {
        // The annotated member is used in an unsafe way.
        // A cross-site scripting defect is reported.
        return Content(
            "<html>"+SomeData.Untrusted+"</html>"
        );    // XSS Defect
    }
}
```

Here is an example of using `<Tainted()>` in Visual Basic code:

```
Imports Coverity.Attributes
Imports System
Imports System.Web
Imports System.Web.Mvc

Class HasTaintedField
    ' Here is a class member annotated as being tainted.
    <Tainted()> Untrusted as String
End Class
        
' An MVC controller
Class MyController
    Inherits Controller

    Private SomeData As HasTaintedField

    ' A controller request handler
    Public Function GetSomeHtml() As ActionResult
        ' The annotated member is used in an unsafe way.
        ' A cross-site scripting defect is reported.
        Return Content(
            "<html>" & SomeData.Untrusted & "</html>"
        )    ' XSS Defect
    End Function
End Class
```

## The '`[NotTainted]`' or '`<NotTainted()>`' attribute

Although a `NotTainted` (`[NotTainted]` for C# and
`<NotTainted()>` for Visual Basic) annotation suppresses error
reports when the identified field flows into a sink, it *does report* a
TAINT_ASSERT defect if it identifies tainted data flowing into the sink.

For more information, see the description of "TAINT_ASSERT" in the Coverity 2026.6.0 Checker Reference.
