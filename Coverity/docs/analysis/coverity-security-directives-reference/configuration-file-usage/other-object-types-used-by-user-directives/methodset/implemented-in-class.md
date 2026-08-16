---
title: "implemented_in_class"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/implemented_in_class.html"
content_id: "~dVQ0xFcThdlP3p_lVnKyQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:44:28.424399+00:00"
---

# implemented_in_class

An `implemented_in_class MethodSet` uses a `ClassSet` to
identify methods.

## Fields

The `implemented_in_class MethodSet` has a single field:

`implemented_in_class`
:   A ClassSet value. The
    `implemented_in_class MethodSet` matches any method
    that is a member of this set, including constructors and static
    initializers but *not including* any methods inherited from
    super-classes.

## Examples

For example, given the class `A` below, the
`implemented_in_class MethodSet` that follows the class
declaration would match these objects:

- The method `A.getX()int`
- The `A` constructor
  `A.<init>(int)void`
- The implicitly created, static initializer of `A`

It *would not* match methods that `A` inherits, such as
`java.lang.Object.hashCode()int`.

```
class A {
  int x;
  int getX() { return x; }
  A(int x0) { x = x0; }
}]]
```

```
{ "implemented_in_class": { "named": "A" } }
```
