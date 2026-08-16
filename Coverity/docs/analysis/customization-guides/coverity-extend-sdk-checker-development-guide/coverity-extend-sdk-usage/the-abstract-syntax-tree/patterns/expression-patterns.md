---
title: "Expression patterns"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/expression-patterns.html"
content_id: "5d2EpreTIDy~E9zSFqyD3g"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:38:30.177654+00:00"
---

# Expression patterns

The expression patterns are, in most cases, constructed using C++ operator overloading.
For an example, see
<install_dir>/sdk/samples/patterns/patterns.cpp.

```
Expr a, b;
if (MATCH_TREE( a + b , CURRENT_TREE)) {
  cout << "  matched an addition; a=" << a << ", b=" << b << endl; 
}
```

This checker fragment declares two pattern variables (*holes*) called
a and b, with type Expr.
The Expr pattern type matches any expression; there are other pattern
types that are more restrictive. For convenience, there is a predefined pattern variable
called "_" (underscore) that matches anything.

The previous code then constructs a pattern expression:

```
a + b
```

The `+`
here is actually an overloaded operator that constructs a pattern. The pattern matches
input ASTs that use the binary operator `+`.

It then uses MATCH_TREE to compare the constructed pattern to
CURRENT_TREE (which is the AST passed to
ANALYZE_TREE). This returns true when the input matches the
pattern. For example, when given the following line of input syntax:

```
z = x + y;
```

the checker fragment prints out:

```
matched an addition; a="x", b="y"
```

because there is
exactly one subexpression in the input file that matches the pattern.

When the line of code:

```
cout << "matched an addition; a=" << a  << ", b=" << b << endl;
```

prints
a pattern variable (such as `a`), it prints the AST fragment that the
pattern variable matched. This AST fragment can also be obtained explicitly by calling
the Pattern::get_tree() method.

Since it is common to use MATCH_TREE with CURRENT_TREE,
the MATCH macro is available as a shortcut:

```
MATCH(<pattern>) is equivalent to MATCH_TREE(<pattern>, CURRENT_TREE)
```

To
match a function call expression, create a pattern of type CallSite:

```
CallSite bar("bar");   // match call to bar()
if (MATCH( bar ))
   cout << "call to bar: " << CURRENT_TREE << endl;
```

When the
CallSite pattern matches, you can inspect its arguments using the
nargs and get_arg methods:

```
for (int i=0; i  < bar.nargs(); i++) {
   cout <<  "  arg "  << (i+1) << ": "  << bar.get_arg(i)  << endl;
}
```

To match a call site with specific patterns for the arguments, simply pass the
argument patterns to CallSite::operator():

```
Const_int ci;
if (MATCH( bar(ci) ))
    cout << "  single literal integer argument: " << ci.llval() << endl;
```

The
previous fragment utilizes the Const_int pattern, which matches an
expression that is an integer literal.

See Expression patterns for
more information.
