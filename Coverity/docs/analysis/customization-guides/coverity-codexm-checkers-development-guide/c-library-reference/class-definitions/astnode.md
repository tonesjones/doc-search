---
title: "astnode"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/astnode.html"
content_id: "u5kiy9j3LEX8lnx1P28lDA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:30:27.850072+00:00"
---

# astnode

Every target-code object that Coverity inspects is a node in an abstract syntax tree.

For a brief overview of how Coverity uses these syntax trees,
see How does Coverity Analysis work?.

## Properties

Every `astnode` has the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `location` | `sourceloc` | The location of this code construct in the source files |
| `children` | `list<astnode>` | A list of child nodes that are sub-parts of this code construct |
| `parent` | `astnode?` | The `astnode` that is the parent of the current node, if there is one. For example, in the case of a `blockstatement`, which contains a list of substatements, the `blockstatement` node is the parent of each statement in the list.  This field is `null` if the current node has no parent. |
| `implicit` | `bool` | Indicates whether the node is the result of compiler intervention, as opposed to being explicitly stated in the source code. For example, `if ( x )` in the source code is interpreted as `if ( x != 0 )` by the compiler. The not-equals binary operator and the literal constant zero are *implicit*. |

The `astnode` elements are further classified as `statement`,
`expression`, `initializer` and
`ctorinit` (constructor initializer),
and `declaration` elements (`declaration` elements
declare symbols).
Various kinds of elements have their own set of properties in addition to the `astnode` properties shown here.
