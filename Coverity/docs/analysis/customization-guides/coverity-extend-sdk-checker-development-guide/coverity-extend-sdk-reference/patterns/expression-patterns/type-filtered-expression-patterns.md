---
title: "Type-filtered expression patterns"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/type-filtered-expression-patterns.html"
content_id: "bmEdRzqWO_FoJCHoikWtEw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:39:25.273122+00:00"
---

# Type-filtered expression patterns

Several patterns match expressions with certain types:

- `Array` — Match an expression with array type.
- `Const_obj` — Match an expression whose type has the
  `const` qualifier.
- `ExprWithType (TypePattern &)`— Matches an expression whose type is matched by
  the given TypePattern. For example,

  ```
  Integer integer
  ```

  is equivalent to:

  ```
  IntegralType itype;
  ExprWithType integer(itype);
  ```
- `Float`— Matches an expression with a floating point type
  (such as `float` or `double`). Same as
  `ExprWithType (FloatType)`.
- `FloatType`— Matches a floating point type (float, double, or long double). For
  example, you can pass this as a parameter to `ExprWithType`'s
  constructor.
- `FunctionPointer` — Match an expression with pointer to
  function type.
- `Integer` — Matches an expression with an integral type. Same
  as `ExprWithType (IntegralType)`.
- `IntegralType`— Matches an integral type, for instance `int`,
  `char` or `bool` but not
  `float` or `double`.
- `NonConstAddr` — Like `Addr` (match a use of the address-of
  operator), except it does not match if the object whose address is taken has
  the `const` type qualifier (for instance, when using a const
  reference function argument).
- `Pointer` — Match an expression with pointer or reference
  type.
- `Reference` — Match an expression with a C++ reference
  type.
- `Scalar` — Matches an expression with a scalar type. Same as
  `ExprWithType (ScalarType)`.
- `ScalarType` — Matches any scalar type (integral or floating point).
- `Struct`— Match an expression with `struct` or
  `class` type.
- `Union`— Match an expression with union type.
