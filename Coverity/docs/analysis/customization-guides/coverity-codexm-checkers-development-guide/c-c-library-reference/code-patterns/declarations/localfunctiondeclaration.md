---
title: "localFunctionDeclaration"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/localfunctiondeclaration.html"
content_id: "Z~22Illv_BZ8n7kLMo0VKg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:29:07.269586+00:00"
---

# localFunctionDeclaration

Matches function declarations within a function (as opposed to outside of a function, as is frequently done in headers).

This pattern does not match actual function *calls*.
To find function calls, see functionCall.

See also: functionType.

## Properties

`localFunctionDeclaration` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `declaredFunction` | `functionType` | Information for the declared function |

**Inherits properties from:**

- astnode
- declaration

## Example

Consider the following snippet of C code:

  
 [image: C/C++ code follows]   

```
int tryme( int i ) {
    void me( void );      /* A declaration: there is a function
                             named me(). */
                
    me();                // An actual call to that function
};
```

The `functionDeclarationLocal` pattern matches
`void me(void);` in the first line of `tryme()`,
since `me()` is declared locally.

However, this pattern does not match the actual call to `me()`.
To match the function call itself, use the `functionCall` pattern.
