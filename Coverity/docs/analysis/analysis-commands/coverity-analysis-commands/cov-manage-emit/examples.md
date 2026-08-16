---
title: "Examples"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/examples.html"
content_id: "W1_GMzzQfRqnbB9uhsxNVQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:41:53.429170+00:00"
---

# Examples

List build information from an intermediate directory:

```
> cov-manage-emit --dir apache_2111 \
    list-builds
```

List all translation unit information from an intermediate directory:

```
> cov-manage-emit --dir apache_2111 \
    list
```

List information from an intermediate directory for the translation unit with the ID
6:

```
> cov-manage-emit --dir apache_2111 --tu 6 \
    list
```

List all information on all entities:

```
> cov-manage-emit --dir apache_2111 \
    find  '.*'
```

List only callee information for all entities:

```
> cov-manage-emit --dir apache_2111 \
    find --print-callees  '.*'
```

List all information for entity `uninit`:

```
> cov-manage-emit --dir apache_2111 \ 
    find  '^uninit$'
```

List the definition of entity `uninit`:

```
> cov-manage-emit --dir apache_2111 \ 
    find  '^uninit$' --print-definitions
```

List the source files of TU 1:

```
> cov-manage-emit --dir apache_2111 \ 
    --tu 1 print-source-files
```

List TUs where bar.cc or foo.cc is the primary
source file:

```
> cov-manage-emit --dir apache_2111 \ 
    --tu-pattern "file('bar.\cc$') || file('foo.\cc$')" list
```

List TUs using patterns specified in the file files:

```
> cov-manage-emit --dir apache_2111 \ 
    --tu-pattern @files list
```

Recompile the TUs in the emit database:

```
> cov-manage-emit --dir apache_2111  recompile
```

Recompile and put diagnostic information in the 211_log.txt file:

```
> cov-manage-emit --dir apache_2111 \
    recompile --compilation-log 211_log.txt
```

Recompile only TU 1:

```
> cov-manage-emit --dir apache_2111 \
    --tu 1 recompile --compilation-log 211_log.txt
```

Recompile translation units where test.c is the primary source
file:

```
> cov-manage-emit --dir apache_2111 \
        --tu-pattern "file('test\.c$')" recompile
```

List source files missing SCM annotations from the intermediate directory:

```
> cov-manage-emit --dir apache_2111 \
    list-scm-unknown --output files-without-scm-age-data.txt
```

List source files under /builds missing SCM annotations from the
intermediate directory:

```
cov-manage-emit --dir apache_2111 list-scm-unknown  \
       --output files-without-scm-annotation-data.txt \
       --filename-regex '^/builds/'
```

List source files with existing SCM annotations in the intermediate directory:

```
> cov-manage-emit --dir apache_2111 \
    list-scm-known --output files-with-scm-age-data.txt
```

List source files under /builds with existing SCM annotations from
the intermediate directory:

```
 cov-manage-emit --dir apache_2111 \
       list-scm-known --output files-with-scm-annotations.txt \
       --filename-regex '^/builds/'
```

Count the source files under /builds with existing SCM annotations
from the intermediate directory:

```
cov-manage-emit --dir apache_2111 \
      list-scm-known --output count-files-with-scm-annotations.txt \
      --filename-regex '^/builds/' --count
```

Add SCM annotations for source files in the intermediate directory:

```
> cov-manage-emit --dir apache_2111 \
     add-scm-annotations --input scm-age-data.txt
```

Dump SCM annotations for source files in the intermediate directory:

```
> cov-manage-emit --dir apache_2111 \
    dump-scm-annotations --output scm-age-data.txt
```

Remove all SCM annotations from the intermediate directory:

```
cov-manage-emit --dir apache_2111 delete-scm-annotations
```
