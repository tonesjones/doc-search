---
title: "What is the AST?"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/what-is-the-ast-.html"
content_id: "CfL_B8cLZyIRafoSBtGlKw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:38:28.223404+00:00"
---

# What is the AST?

An Abstract Syntax Tree (AST) is a tree-shaped data structure that represents the phrase of the
concrete input syntax of the source code. For example, the input `1+2*3`
has a corresponding AST that looks like this:

```
         +
        / \
       1   *
          / \
         2   3
```

From this AST fragment, you can infer that the multiplication of 2
and 3 happens first (even though `*` occurs textually after the
`+`), and the result is added to 1. If the input is instead
`(1+2)*3`, then the AST is:

```
         *
        / \
       +   3
      / \
     1   2
```

Note that the grouping parentheses has affected the AST by changing
the order of operations. The parentheses are not explicitly present in the AST, since
the tree structure is sufficient to represent their effect.

In Coverity Analysis, the AST is the output of the parser, and the input to the
checker.

AST fragments can be grouped into several categories:

- Expressions, such as the examples shown previously.
- Statements, such as `x = 3;` or `while (true) { ...
  }`.
- Type identifiers, such as `int` or `class C { ...
  }`.
- Function definitions as a whole.

Although there are a few other categories, these are the main ones that most
checkers use.
