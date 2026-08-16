---
title: "Queries on the current function"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/queries-on-the-current-function.html"
content_id: "9XSihPr74aluKTvaBZHwlg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:39:33.185180+00:00"
---

# Queries on the current function

Since the analysis works one function at a time, several functions return information
about the current function being analyzed.

- `current_function_get_mangled_name` — Returns the full, mangled name of the
  current function.
- `current_function_get_name` — Returns the identifier for the
  current function, for example `foo`. This name is never
  mangled.
- `current_function_get_signature` — If the function's name is mangled (that is, a
  C++ function, but not mixed code using `extern "C"`), returns the
  result of de-mangling. This includes scope and parameter type information, for
  example `N::foo(int)`. Otherwise, this returns the identifier of
  the function, for example, `printf`.
- `current_function_get_class_name` — Returns the scope in which the
  current function is defined, for example `N`. For a function in
  the global scope, returns the empty string (`""`).
- `current_function_is_ctor` — Returns true if the current function
  is a constructor.
- `current_function_is_dtor` — Returns true if the current function
  is a destructor.
- `current_function_is_pure_virtual` — Returns true if the current function is a
  pure virtual function. Note that a pure virtual function is defined as follows:

  ```
  class MyClass {
  ...
    virtual void pureDefined() = 0;  // combining pure and inline NOT allowed
  };
  void MyClass::pureDefined() { /* but this IS allowed */ }
  ```
- `current_function_is_virtual` — Returns true if the current
  function is a virtual function.
