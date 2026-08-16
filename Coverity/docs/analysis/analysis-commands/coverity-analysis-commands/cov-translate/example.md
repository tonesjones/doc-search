---
title: "Example"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/example.html"
content_id: "z88Fh1Z9vZHAssEi8Dt4pA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:42:47.906708+00:00"
---

# Example

Suppose you have a single file t.c that is compiled with gcc as:

```
> gcc -DFOO=BAR -c t.c
```

In this case, invoking this command with `cov-translate` in front will
call `cov-emit` in the appropriate way to compile
t.c, assuming that gcc has been configured with
`cov-configure`:

```
> cov-translate --dir /tmp/emit gcc -DFOO=BAR -c t.c
```

Output of the `cov-translate` example:

```
cov-emit --dir /tmp/emit ... --gcc -w -DFOO=BAR t.c
Emit for file 't.c' complete.
```

In the previous example, `...` represents other arguments that are added
to provide system include directories, preinclude files, and other command-line
arguments that `cov-translate` adds to make `cov-emit`
imitate gcc more precisely.
