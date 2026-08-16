---
title: "Functions"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/functions.html"
content_id: "jrbTJBGzFsnQs~ka5EaWBA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:26:59.971871+00:00"
---

# Functions

Unless the line becomes too long (>100 characters), put the function's name, argument list, and optional return type
on a single line, and close the line with the `->` arrow that introduces the function body.

If the entire function fits on a single line, that is OK. Here is an example:

[image: CXM code follows]

```
function addOne ( num : int ) -> num + 1 ;
```

If the function arguments don't all fit on one line, give each argument after the first one a line of its own,
aligned with the first argument, as the following example shows:

[image: CXM code follows]

```
function manyArguments ( aArg: aArgType,
                               bArg: bArgType,
                               // ...
                               xArg: xArgType ) ->
    
    // ... function body ...
    
;
```

If the function requires more than one line, place the semicolon ( `;` ) that closes the function body on a line of its own,
at the same indentation level as the keyword `function`.
This is shown in the previous example and in the one that follows.

If a return type fits on the same line as the `function` keyword, that is OK.
Otherwise, put the return type on a line of its own and align the colon ( `:` ) that introduces it
with the name of the function.
Here is an example:

[image: CXM code follows]

```
function manyArguments ( aArg: aArgType,
                               bArg: bArgType,
                               // ...
                               xArg: xArgType )
         : longReturnType  ->
    
    // ... function body ...
    
;
```
