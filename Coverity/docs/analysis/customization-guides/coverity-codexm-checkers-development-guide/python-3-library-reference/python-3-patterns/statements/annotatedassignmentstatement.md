---
title: "annotatedAssignmentStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/annotatedassignmentstatement.html"
content_id: "k3ZiaelVSE1DCkDGbIIFDw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:38:10.996548+00:00"
---

# annotatedAssignmentStatement

Matches Python 3 annotated assignment statements.

CAUTION:

This pattern does not appear in pattern decomposition:
Use assignmentStatement instead.
For more about decomposition, see Decomposing a pattern to match specific properties.

An annotated assignment has the form,
`<variable> : <annotation> = <value>`.
(The assignment operator can be augmented as well as simple.)
In abstract syntax, Coverity Analysis represents an annotated assignment as follows:

```
    {
        variable = value;
        __annotations__[ "variable" ] = annotation;
    }
```

This pattern only matches nodes of type `statement`.

## Properties

`annotatedAssignmentStatement` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `annotation` | `expression` | The annotation itself (`<annotation>`) |
| `annotationAssignment` | `expression` | The assignment expression (`__annotations__[ "variable" ] = annotation;`) |
| `sourceExpression` | `expression` | The source expression (`<value>`) |
| `targetExpression` | `expression` | The target expression (`<variable>`) |
| `valueAssignment` | `assignmentOperator` | The operator used for the assignment |

**Inherits properties from:**

- astnode
- statement

## See also

assignmentKind,
assignmentStatement
