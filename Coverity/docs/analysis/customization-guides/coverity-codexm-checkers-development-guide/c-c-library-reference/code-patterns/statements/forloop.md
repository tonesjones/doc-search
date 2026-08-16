---
title: "forLoop"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/forloop.html"
content_id: "eY8T5C0XE8iRkHY2O_aSIQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:28:57.588765+00:00"
---

# forLoop

Matches both kinds of `for` loop recognized by C++.
(C recognizes only the simple variant.)

To match only specific kinds of `for` loop, or to gain access to such a loop's properties,
see forLoopSimple
and forLoopRange.

## Properties

`forLoop` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `kind` | `enum forLoopKind` | The kind of loop; this equals either `` `simple` `` or `` `range` ``; see forLoopKind |

**Inherits properties from:**

- astnode
- statement

## Example

The following C code:

  
 [image: C/C++ code follows]   

```
for ( int i = 0; i < 10; i++ ) {
    doSomething( i );
;
```

... matches the following CodeXM pattern:

```
    forLoop {
    .kind == `simple`
};
```

Similarly, the following C++ code:

  
 [image: C++ code follows]   

```
for ( int x : intArray ) {
    doSomeOtherThing( x );
};
```

... matches the following CodeXM pattern:

  
 [image: CXM code follows]   

```
    forLoop {
        .kind == `range`
    };
```

Note:
The more specific patterns
`forLoopSimple` and `forLoopRange` are shorthand for the examples shown above.
The more specific patterns have the added benefit of exposing properties specific to the kind of loop in question.

Here is another way to express the previous CodeXM pattern:

  
 [image: CXM code follows]   

```
    for c in codes {
        where c matches forLoop{ .kind == `simple` }
    };
```

... or its alternative:

  
 [image: CXM code follows]   

```
    for c in codes {
        where c matches forLoop{ .kind == `range` }
    };
```
