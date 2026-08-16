---
title: "functionType"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/functiontype.html"
content_id: "csrdS5F0FFhPnskEJ6XJlw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:29:14.701846+00:00"
---

# functionType

Matches the types of functions; for example, the type of the function being called in a function call.

## Properties

`functionType` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `declaredThrownTypeList` | `list<type>?` | The types of the exceptions that the function might directly or indirectly throw; `null` if there are none |
| `doesNotReturn` | `bool` | `true` if the function does not return |
| `hasEllipsis` | `bool` | `true` if the function's parameter list uses ellipsis ( `...` ) notation |
| `hasNoExcept` | `bool` | `true` if the function is declared with the keyword `noexcept` (since C++11) |
| `isMemberFunction` | `bool` | `true` if the function is a method in a class (C++ only) |
| `isPrototyped` | `bool` | `true` if the function has a prototype |
| `paramTypeList` | `list<type>` | The types of the function's formal parameters |
| `returnType` | `type` | The type of the value returned by the function |

## Example

The following CodeXM pattern matches a member function call whose return type is `voidType`.

  
 [image: CXM code follows]   

```
    pattern memberFcnCallWithVoidReturn {
        functionCall {
            .calledFunction.type == functionType {
                .isMemberFunction == true;
                .returnType == voidType
            }
        }
    };
```
