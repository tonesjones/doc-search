---
title: "CodeXM checkers"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/codexm-checkers.html"
content_id: "oSaabhFY4D1WWMAKJJA5lg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:25:14.621098+00:00"
---

# CodeXM checkers

*CodeXM* is short for *Code eXaMination*. It is an interpreted language
used to write customized checkers that run using the Coverity engine. It allows you to
define problematic patterns that you want to find in your source code.

CodeXM exposes the underlying abstract syntax tree (AST) that analysis generates, and
lets you scan this directly for matches. CodeXM can also detect certain conditions based
on program states; for example, an execution path.

**Use case:** A development team wants to enforce a coding policy that C++ code should
not use the `goto` statement. They build the following CodeXM checker to
report any occurrences of `goto` in their code:

```
include `C/C++`;
            
            
checker { 
    name = "NO_GOTO";
    reports =
        for c in globalset allFunctionCode
            where c matches gotoStatement : 
                {
                    events = [ {
                        // ... Messages to describe what you found
                    } ];
                };
};
```

**Limitations and alternatives:** CodeXM rules are primarily intended for matching
syntax patterns in source code.

- CodeXM, like Lisp, is a *functional* programming language, as opposed to a
  *procedural* language such as C++ or Java. If you are used to coding
  procedurally, which these days is how most programs are written, then getting used
  to the functional model can take some time.
- CodeXM is not always sufficient for deeply reasoning about program behavior; for
  example, tracing runtime call resolution, or comprehensively tracking runtime
  values. These are difficult program analysis problems!

  In cases like these, it might be more appropriate to interact with the analysis engines by using API
  modeling, custom dataflow checkers, or security directives.

**Learn more:**

- "Learning to write CodeXM checkers"
  in the Coverity
  CodeXM Checkers Development Guide introduces the CodeXM environment
  and demonstrates a number of ways to use the language. It includes a style guide,
  too.
- The "Syntax reference" Coverity
  CodeXM Checkers Development Guide describes the language itself.
- Several chapters describe the libraries that are provided with CodeXM.
  For the most part, each library supports the analysis of a particular target source
  language (certain functions are common to all libraries).
  There is also chapter for the "common library", which provides general-purpose utility functions.
