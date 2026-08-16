---
title: "Patterns"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/patterns.html"
content_id: "bxk42p_BVb_E4lgOLFMy0Q"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:39:17.457280+00:00"
---

# Patterns

This introduction explains the
pattern matching API. It does not replace the comments in the
><install_dir>/sdk/headers/patterns/*-patterns.hpp
header files, but provides a high level overview. You should refer to
*-patterns.hpp as you read this section.

Refer to the sample pattern checker at
><install_dir>/sdk/samples/patterns/patterns.cpp,
which exercises all of the APIs described in this section.

Patterns are a mechanism for inspecting AST fragments (the AST, or Abstract Syntax Tree,
is the internal representation of the code to analyze). The basic idea is to create a
pattern object and then use its match() method to compare the pattern
to a specific AST fragment. When match() returns true, each
subpattern can be queried to obtain the AST fragment that it matched.

In addition to AST fragments (that represent code), patterns can match types and symbols.
Types are C/C++ types such as structs, classes, or typedefs. Symbols are unique
representatives for variables, functions, and class fields (as opposed to a specific
appearance of them in the code). For instance, a variable expression (which is an AST
fragment) references the symbol corresponding to the variable.

Correspondingly, there are three pattern hierarchies, with the corresponding C++ type
hierarchy that they are used to match (argument type to match() is a
rough equivalent). Note that only an ASTNodePattern (or a subclass)
can be used directly with MATCH or MATCH_TREE. For
MATCH_COND, you should use ExpressionPattern.

- ASTNodePattern (class ASTNode)
- TypePattern (class type_t)
- SymbolPattern (class symbol_t)

ASTNodePattern has two important sub-hierarchies for matching
statements (such as a `for` loop) or expressions (such as an addition).
Correspondingly, class ASTNodePattern has these subclasses:

- StatementPattern (class Statement)
- ExpressionPattern (class
  Expression)

Class ASTNode has a third subclass, Declaration
(variable declaration), that can be matched by the Decl pattern.
Since Declaration has no further subclasses, there is no hierarchy.

Next are diagrams of each of those hierarchies. In these diagrams triangles represent
inheritance. Filled triangles indicate that the superclass is abstract (not
instantiable), while the superclasses for the open triangles are concrete.

Figure 1. ASTNodePattern class hierarchy
[image: image]

Figure 2. ExpressionPattern class hierarchy
[image: image]

Figure 3. StatementPattern class hierarchy
[image: image]

Figure 4. SymbolPattern class hierarchy
[image: image]
