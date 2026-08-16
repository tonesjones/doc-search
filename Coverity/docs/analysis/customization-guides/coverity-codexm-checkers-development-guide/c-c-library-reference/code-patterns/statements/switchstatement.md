---
title: "switchStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/switchstatement.html"
content_id: "UENMJ7OCR_kYmNDdUggmnA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:29:04.376981+00:00"
---

# switchStatement

Matches entire `switch` statements, including all the statements
contained in their `case` and `default` clauses.

See also caseStatement,
defaultStatement,
and breakStatement.

## Properties

`switchStatement` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `conditionExpression` | `expression` | The expression that determines which case is to be taken |
| `caseList` | `list<statement>>` | A list of the targets of this `switch` statement. A target is either a `caseStatement` or a `defaultStatement`. |
| `bodyStatement` | `statement` | The body of the `switch` statement. In most cases this is a `blockStatement`. |
| `conditionDeclaration` | `declaration?` | If a variable is declared in the `conditionExpression`, it is identified here. If no variable is declared, this property is `null`. |

**Inherits properties from:**

- astnode
- statement

## Example

A `switchStatement` CodeXM pattern matches a
target-code `switch` statement such as the following:

  
 [image: C/C++ code follows]   

```
switch( i ) {
    case 1:  return "one";
    case 2:  return "two";
    case 3:  return "three";
    default: return "unknown";
};
```

A match to the snippet above returns these values:

- `.conditionExpression` is the variable `i`.
- `.caseList` contains the four case labels
  (including the `default`).
- `.bodyStatement` contains the block
  enclosed by the `switch`.
- `.conditionDeclaration` is
  `null` since no declaration appears in the condition expression.

The following pattern identifies `switch`
statements that do have `default` cases:

  
 [image: CXM code follows]   

```
    // Switch with default statement
    pattern switchWithDefault {
        switchStatement as stms
            where exists stm in stms.caseList
                where stm matches defaultStatement
    };
```
