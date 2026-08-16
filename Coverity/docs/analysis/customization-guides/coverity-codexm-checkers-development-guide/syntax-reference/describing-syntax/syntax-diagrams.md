---
title: "Syntax diagrams"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/syntax-diagrams.html"
content_id: "wHht8o0rf5n6HsnzApxLPQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:27:06.032460+00:00"
---

# Syntax diagrams

Syntax diagrams (often called "railroad diagrams") have long been used to visually illustrate the syntax of various programming languages.
Because they are easy to read, we use them in this document, too.

In case you've never seen these before and are unfamiliar with how to read them, the notion is that you follow the path from left to right.
If an item lies on the path, it must be part of the code. If the path branches, you can choose one of the options that are shown.
The path can even loop back to indicate a repeating element, but you *cannot* reverse direction to go against the
overall movement from left to right.

When you reach the right end of the diagram, you have constructed an example of the portion of syntax that the diagram describes.

Syntax diagrams use a few visual conventions to help you see what the diagram is describing.
In addition to the "railroad-track" path, the diagrams can include the following three elements:

- A box with round corners represents a literal, such as a keyword, that you must enter character-for-character, as the diagram shows.
- A box with square corners represents another syntax rule.
  In this case, the rule in the box should have a diagram of its own, elsewhere in this reference.
- A box with angles at each end represents a character sequence that can vary, such as an identifier.
  These boxes use the conventions described in the following description of *regular expressions,*
  which are described in the section Extended Backus-Naur form, which follows.

The following text and graphics show some examples of syntax diagrams.

The syntax requires `keyword` to introduce another portion of syntax:

  
 [image: Syntax diagram, sequential elements]   

The syntax requires one of two choices. You can pick one or the other, but you have to make a choice:

  
 [image: Syntax diagram, alternative elements]   

The syntax allows an option. You can include the option, or omit it:

  
 [image: Syntax diagram, optional element]   

The syntax allows the `something` element to repeat an indefinite number of times:

  
 [image: Syntax diagram, repeating element]   

The syntax allows the `something` element to repeat an indefinite number of times, but each
*additional* `something` must be preceded by a plus sign:

  
 [image: Syntax diagram, repeating element with plus-sign delimiter]   

As you see, syntax diagrams are easy to follow, but they are versatile enough to fully describe the syntax of
any [context-free grammar](https://en.wikipedia.org/wiki/Context-free_grammar).
