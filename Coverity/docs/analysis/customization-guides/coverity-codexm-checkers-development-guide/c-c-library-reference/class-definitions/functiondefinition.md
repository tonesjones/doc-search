---
title: "functionDefinition"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/functiondefinition.html"
content_id: "fZz_ZHYGgb18NsdTaIQv_w"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:28:32.332573+00:00"
---

# functionDefinition

Describes a function definition.

## Properties

`functionDefinition` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `body` | `statement` | A `blockStatement` of the function body. |
| `constructorInitializerList` | `list<ctor>?` | If this function is a constructor, this list describes how the base classes and members of the current class are initialized. For example, this is comparable to the list that comes after the ":" in the definition of a C++ constructor: though in the case of CodeXM, this list also includes implicit initialization that uses default constructors.  If this function is not a constructor, this property is `null`. |
| `formalParameterList` | `list<symbol>` | A list of `parameterSymbol` objects, one for each parameter to the function |
| `functionSymbol` | `symbol` | The `functionSymbol` that represents this function |

**Inherits properties from:**

- functionOrStaticVariableDefinition
