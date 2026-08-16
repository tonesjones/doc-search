---
title: "Function call site expression patterns"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/function-call-site-expression-patterns.html"
content_id: "OLcEOzct7bxgc7Yy9YBnFA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:39:23.973634+00:00"
---

# Function call site expression patterns

There are a variety of patterns to match function call sites:

- `CallSite` — Match function calls. This pattern is used to
  implement all the other ones below, which are only provided for backwards
  compatibility and convenience. A `CallSite` pattern can be
  set up to match function pointers, direct function calls or both (using
  `setCalledExpression)`. It can also include or exclude
  method/non-method calls (using `setReceiverObject`). It also
  has an `operator()` method that allows specifying call
  arguments.

  Note: See bullet items below for uses of `CallSite` that replace deprecated
  `Fun` patterns.
- `Fun()` — Match a call to any function, including calls
  through function pointers. Equivalent to:

  ```
  CallSite()
  ```

  For
  backwards compatibility, note that using `operator()` with no
  arguments has no effect (but using `CallSite` with no
  arguments matches a call with no arguments).

  Note: This function is deprecated as of version
  5.5.0.

  Use
  `CallSite` instead. For example:

  - You can replace the following:

    ```
    Fun f;
    ```

    With the following:

    ```
    CallSite f;
    ```
- `Fun(char const *name, fun_options flags = NONE)` — Match a
  call to a function, restricted as follows:

  - If the call is through a function pointer, match if and only if
    `flags` includes FUNCTION_POINTERS_ALLOWED.
  - If the call is to a named function (including class methods):

    - If `name` is NULL, then match.
    - Otherwise, if `flags` includes UNMANGLE_NAME,
      match if the unmangled name of the called function equals
      `name`.

      Name mangling is a technique used by compilers to encode the
      type of an entity in its linker symbol name. For more
      information, see Name mangling.
    - Otherwise, match if the mangled name of the called function
      equals `name`.

  Note: This function is deprecated as of version
  5.5.0.

  Use
  `CallSite` instead. For example:

  - You can replace the following:

    ```
    Fun f(name);
    ```

    With the following:

    ```
    CallSite f(name, /*unmangle*/false);
    ```

    Note that `MATCH(f())` is equivalent to
    `MATCH(f)` when `f` is a
    `Fun`. However, if `f` is a
    `CallSite`, `MATCH(f())` will
    only match a call with no arguments, so Coverity recommends
    using `MATCH(f)` in this case.
  - You can replace the following:

    ```
    Fun f(NULL, Fun::FUNCTION_POINTERS_ALLOWED);
    ```

    With the following:

    ```
    CallSite f;
    ```
  - You can replace the following:

    ```
    Fun f(name, Fun::FUNCTION_POINTERS_ALLOWED);
    ```

    With the following:

    ```
    FunctionDecl fnDecl(name, /*unmangle*/false);
    CallSite f(Or(fnDecl, *_));
    ```
  - You can replace the following:

    ```
    Fun f(NULL, Fun::FUNCTION_POINTERS_REQUIRED);
    ```

    With the following:

    ```
    CallSite f(*_);
    ```
  - You can replace the following:

    ```
    Fun f(NULL, Fun::FUNCTION_POINTERS_DISALLOWED);
    ```

    With the following:

    ```
    FunctionDecl fnDecl; 
    CallSite f(fnDecl);
    ```
- `Fun(MultipleNamesTag mntag, const char **fnames, fun_options flags =
  NONE)` — Similar to the previous pattern, except for a call to a
  named function, match if the name equals any of the strings in the
  NULL-terminated `fnames` array. If `fnames`
  begins with NULL, match regardless of the called function's name.

  Note: This function is deprecated as of version
  5.5.0.

  Use
  `CallSite` instead. For example:

  - You can replace the following:

    ```
    Fun f(Fun::matchMultipleNames, names);
    ```

    With the following:

    ```
    CallSite f(namedSymbols(names));
    ```
- `MemberFun` — Match a call to a nonstatic member function, and
  provide patterns for the arguments. At a minimum, a pattern must be provided
  for the receiver object (the *instance*). Optionally, a sequence of
  argument patterns may be specified using `operator()`.

  Note: This function is deprecated as of version
  5.5.0.

  Use
  `CallSite` instead. For example:

  - You can replace the following:

    ```
    MemberFun f(receiver);
    ```

    With the following:

    ```
    CallSite f;
    f.setReceiverObject(receiver);
    ```
- `Constructor` — Match a call to a constructor.
- `CopyConstructor` — Match a call to a copy constructor, which
  is a special case of what `Constructor` matches.
- `Destructor` — Match a call to a destructor.
- `Anyfun` — Match a call to any function (there is no filtering
  based on function name). If you specify an argument pattern, the pattern
  matches if *any* argument at the call site matches the argument
  pattern. For example, `Anyfun()(Const_int)` matches any call
  where a literal int is among the arguments.

  Note: This function is deprecated as of version
  5.5.0.

  Use
  `CallSite` instead. For example:

  - You can replace the following:

    ```
    Anyfun f;
    MATCH(f(pat));
    ```

    With the following:

    ```
    CallSite f;
    f.setAnyArg(pat);
    ```
