---
title: "How does Coverity Analysis work?"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/how-does-coverity-analysis-work-.html"
content_id: "Z4_H~CdrbA6ajrr5LlkRfA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:27:08.839756+00:00"
---

# How does Coverity Analysis work?

To fully answer the question posed by the title of this topic would require a lot of detail.
This topic isn't a thorough description, just a birds-eye view of what Coverity Analysis does.
If you understand the methods described here, you will have an easier time writing CodeXM checkers.

For a compiled, procedural language, one of the first steps the compiler does is to parse the source code and construct a syntax tree.
You might already be familiar with how these look.

For example, the source code `x - y*2 + 1` can be expressed in tree form, as the following illustration shows:

  
 [image: Code expressed as a tree of nodes]   

Constructing a syntax tree is also one of the first steps taken when you run `cov-analyze`.

A code compiler proceeds to traverse the syntax tree and use it to generate object code.

The `cov-analyze` program also traverses the syntax tree, but in this case it does not generate code.
Instead it searches for the patterns specified by the checkers it is running.
Those checkers can be provided off-the-shelf, as components of Coverity, or they can be custom checkers written using either
CodeXM or the Extend SDK. When a checker finds a target pattern, it generates a report—an *event*.

A standard compiler generates a tree that accurately represents the source code. Coverity, on the other hand, applies some optimizations and simplifications, to facilitate the work of static analysis. (It would be possible to analyze literal source, but that would be much, much slower.) Because of this, the structure built by Coverity is known as an *abstract* syntax tree, or AST.

To use Coverity, you don't need to know details about the AST structure or how analysis works. If you are writing checkers of your own, it can help to bear in mind that the checker is not analyzing the original source code, but a representation of it that is built of node objects organized into a tree.

In terms of CodeXM code, each of the nodes shown in the tree shown above is an `astnode` object.
There are various types of these. Some nodes represent binary operators such as assignment, addition, and multiplication.
Other nodes represent variables; still others represent literals such as integers or strings.

**Note:** There are no `astnode` objects for white space or comments.

A pattern you specify in CodeXM, for example, can look for instances of addition—this would locate
the `y*2 + 1` expression in the tree illustrated above,
or any other occurrence of the `+` operator).
A pattern can look for multiplication of a variable and a constant—as in `y*2`.
It can also look for binomial expressions such as instances of addition (or subtraction) used with multiplication—such a pattern would match
`y*2+1` or `z*3-4`, but would *not* match `1+2`.

A pattern you write can be as specific and as thorough as you need it to be.

Every CodeXM language library has an `astnode` object, and each
`astnode` has a specific set of properties.
In addition, there are various types of `astnode` objects:
Each type has specific properties of its own, as well as the ones it inherits from the parent `astnode` object. See any of the language library references for the details.

Once it has constructed the abstract syntax tree, `cov-analyze`
inspects all possible execution paths. This is one of the advantages of static analysis:
It is fast enough to comprehensively look at what the code will do—unlike dynamic
analysis, which has to execute the target program, and so to be efficient has to rely on
a sampling of behaviors.

Not that we recommend you use *only* static analysis. A robust testing strategy should employ both techniques, as appropriate.
