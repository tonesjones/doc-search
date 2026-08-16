---
title: "Examples"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/examples.html"
content_id: "~_2k09MaWZKqzbaNa~5Bpg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:41:38.718840+00:00"
---

# Examples

Create a link file based on an existing emit repository:

```
> cov-link --dir . --collect -of /usr/foo/all.link
```

Create a link file based source files with apache in the
pathname:

```
> cov-link --dir . -s  /apache/ -of /usr/foo/link_reports/apache.link  \
    all.link
```

Create a link file based on the source files with apache_1.3.33 in
the pathname, include only the files that were compiled with the `DEBUG`
macro defined on the command line, and then create an intermediate directory with an
emit repository:

```
> cov-link --dir . -a -DDEBUG  -s /apache_1.3.33/   \
    -of /usr/foo/link_reports/apache1333_DEBUG.link  all.link
> cov-link  --dir .  --output-dir emit_apache1333_DEBUG \
    /usr/foo/link_reports/apache1333_DEBUG.link
```

Create a new emit repository based on the source files with
apache_1.3.33 in the pathname, and include only the files that
were compiled with the `DEBUG` macro defined on the command line (same as
previous example, but without creating the intermediary link file):

```
> cov-link --dir . --collect -a -DDEBUG -s /apache_1.3.33/   \
    --output-dir emit_apache1333_DEBUG
```
