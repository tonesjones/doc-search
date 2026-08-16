---
title: "Syntax reference"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/syntax-reference.html"
content_id: "NZjpB6LJhAkDH35rG528Pw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:27:04.630444+00:00"
---

# Syntax reference

This part of the reference describes the CodeXM language.

CodeXM is all of the following things:

- A domain-specific language expressly designed to examine code and detect certain (typically undesired) patterns in that code
- A [functional](https://en.wikipedia.org/wiki/Functional_programming) programming language
- A language that is meant to be quick to learn and easy to use, yet powerful enough to provide sophisticated code-checking capabilities

In CodeXM, as in Coverity Analysis, the central element is a *checker:*
a portion of code that describes what you're looking for, and what to do when you find it.
A CodeXM file can define any number of these checkers, along with supporting functionality.
Each checker can examine code in order to look for different kinds of patterns.

A number of predefined utilities are provided to support CodeXM checkers.
These include both language-specific predefined patterns and functions, and general-purpose functions for use with any supported language.

As mentioned above, CodeXM is a *functional* programming language.
A functional language is slightly different from most programming languages commonly employed in production environments today:
These languages are variously described as being *procedural* or *imperative* languages.

In those other languages, you typically define a set of steps: first do this; when that is complete, do the next thing; and so on.
In CodeXM, as in other functional languages, the logic is expressed in expressions, not statements.
Using a functional language is more like defining the formulas in a spreadsheet, than it is like programming a procedural language such as C or Java.

In CodeXM you specify *where* you're looking, and *what* you're looking for.
You also describe *how* to present the results when a CodeXM checker finds the pattern you've defined

Though it uses expressions rather than statements, CodeXM should still be easy to learn if you have programmed before.
Most of the inner workings of code analysis are left unexposed, and what does show through is revealed in ways that ought to be
familiar to developers who use typical programming languages.
If you're looking for a `goto` statement or an `if` statement,
you will write a CodeXM checker that use a `gotoStatement` or an `ifStatement` pattern
to find—or, in CodeXM parlance, to *match*—these statements in the target code.

This syntax reference only describes the grammar of CodeXM: the rules of the CodeXM language.
When you write a checker, as the QuickStart shows,
you will also need to work with the patterns that are provided by the libraries for the various supported languages:
Each such library has a reference of its own.
