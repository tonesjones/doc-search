---
title: "HANDLE_OPTION"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/handle_option.html"
content_id: "3GDe1OfJ7Xx8xH1tu2ng7w"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:39:09.276085+00:00"
---

# HANDLE_OPTION

**Synopsis**

```
HANDLE_OPTION() { <code> }
```

**Description**

This handler is called for every command-line argument to the
`cov-analyze` command of the form:

`(--checker_option|-co) checker_name:option_name[:option_value]`

where `checker_name` is the same as the argument to `START_EXTEND_CHECKER`.

The following macros can be used in `HANDLE_OPTION` to determine the argument:

- `CHECK_OPTION(opt) { <code> }`— Executes
  `code` if the `option_name` on the command
  line equals `opt`.
- `OPTION_VALUE — <option_value>` (as a `char const
  *`) passed on the command line, or NULL if no value was
  passed.
- `OPTION_HANDLED()`— Tells Coverity Analysis that the
  command-line option has been recognized and processed. Calling this function
  causes a return from `HANDLE_OPTION`.
- `OPTION_NOT_HANDLED()`— Tells Coverity Analysis that the
  option has *not* been recognized. Calling this function causes a return
  from `HANDLE_OPTION`.

For example:

```
// The following member variables are located between 
// the checkers START_EXTEND_CHECKER and END_EXTEND_CHECKER.
int mode;
bool use_mangled;
// called at program startup
INIT_OPTIONS()
{
    mode = 0;
    use_mangled = false;
}
// called for each --checker_option command-line argument
HANDLE_OPTION()
{
    CHECK_OPTION( "mode" ) {
        mode = atoi( OPTION_VALUE );
        OPTION_HANDLED();
    }
    CHECK_OPTION( "use_mangled" ) {
        use_mangled = true;
        OPTION_HANDLED();
     }
     OPTION_NOT_HANDLED();
}
// You can now use mode and use_mangled in ANALYZE_TREE.
```
