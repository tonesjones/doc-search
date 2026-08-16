---
title: "Suppressing macro expansion to improve modeling"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/suppressing-macro-expansion-to-improve-modeling.html"
content_id: "xqu~y65clczkuwYxkJUDVA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:33:20.115103+00:00"
---

# Suppressing macro expansion to improve modeling

Complex macros sometimes cause Coverity Analysis to misinterpret parts of the code. Most
commonly, this issue occurs when a model of a library function, such as
`strcpy`, is incorrectly defined as a macro by the native compiler.
In this case, it is necessary to suppress macro expansion so that Coverity Analysis can
identify the model as a function call.

Macro expansion can be suppressed by using the `#nodef` syntax of the
Coverity compiler:

- `#nodef macroname`

  This form can be used, for example, to convert a macro
  implementation of a standard C library function into a function
  call:

  ```
  #nodef strcpy
  ```

  For a more complete example, see
  "A sample `user nodefs.h` file."
- `#nodef macroname value`

  This form is useful if you need to model a macro
  using a function name that differs from the name of the macro, thereby
  preventing your model function from conflicting with another function that might
  exist in your code base. For example:

  ```
  #nodef strcpy model_strcpy
  char *model_strcpy(char *, const char *);
  ```

  Note that the function
  declaration can appear in this file or elsewhere.
- `#nodef macroname(x,...) value`

  In addition to allowing for a different
  function name, this form allows you to model a macro (such as `#define
  my_assert(int) { ... }` ). For
  example:

  ```
  #nodef my_assert(x) my_assert_model(x);
  void my_assert_model(int x);
  ```

  Then you can provide a model for
  `my_assert_model`.

The last two examples suppress the definition of a macro, while providing an alternative
definition of the macro. The alternative overrides all future definitions of the
macro.

Note: A commented, but otherwise empty template is provided
at:

```
<install_dir>/config/user_nodefs.h
```

If you insert
company-specific `#nodef` directives in this file, the
`cov-configure` command ensures that compilations with the
Coverity Analysis compiler (which is invoked when you run
`cov-build`) will include the configuration directives in
user_nodefs.h.

Figure 1. A sample user_nodefs.h file

```
#nodef strpbrk
#nodef memset
#nodef strstr
#nodef free
#nodef snprintf
#nodef memcpy
#nodef gets
#nodef fgets
#nodef strcpy
#nodef setjmp
#nodef strdup
#nodef memcmp
#nodef strrchr
#nodef sigsetjmp
#nodef strcmp
#nodef vsprintf
#nodef puts
#nodef vprintf
#nodef strcpy
#nodef freopen
#nodef printf
#nodef vfprintf
#nodef fread
#nodef realloc
#nodef fclose
#nodef fopen
#nodef sprintf
#nodef vsnprintf
#nodef fprintf
#nodef strncmp
#nodef fwrite
#nodef malloc
#nodef strchr
#nodef calloc
#nodef KASSERT
#nodef assert
#nodef BUG
#nodef BUG_ON
```
