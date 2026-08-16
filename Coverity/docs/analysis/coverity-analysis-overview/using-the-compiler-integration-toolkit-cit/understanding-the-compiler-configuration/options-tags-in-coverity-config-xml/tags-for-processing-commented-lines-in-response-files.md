---
title: "Tags for processing commented lines in response files"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/tags-for-processing-commented-lines-in-response-files.html"
content_id: "KqMXOX7Gsa9DuVqLE3mqQQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:35:07.793502+00:00"
---

# Tags for processing commented lines in response files

You can specify tags to control whether or not comments should be removed for response
files. If you do not specify these tags, the compiler considers everything (including
the comments) to be a switch.

These tags are child tags to <expand> and<post_expand>. Acceptable arguments
are `yes` or `no`, where `yes` enables the
processing of the commented line.

<response_file_merge_lines>
:   Merges lines that end with backslashes in the response file.

<response_file_strip_comments>
:   Enables all of the comment filters.

<response_file_strip_poundsign_comments>
:   Strips a single commented line that begins with the pound sign (#). This filter respects
    line merges for lines that end with a backslash (\).

<response_file_strip_semicolon_comments>
:   Strips a single commented line that begins with an unquoted, un-escaped semicolon (;). This
    filter respects line merges for lines that end with a backslash (\).

<response_file_strip_slashslash_comments>
:   Strips a single commented line that begins with double slashes (//). This filter respects
    line merges for lines that end with a backslash (\).

<response_file_strip_slashstar_comments>
:   Strips all commented lines that begin with a slash star (/*) and end with a star slash
    (*/).

For example:

```
<post_expand>
   <options>
      <response_file_strip_comments>yes</response_file_strip_comments>
      <response_file_merge_lines>yes</response_file_merge_lines>
   </options>
</post_expand>
```

Will strip the following (example) commented lines:

```
/*
* Add switches to compiler command line
*/
// This one is especially \
     important
-DDEFINE_ME=1
# So is this one
-UUNDEFINE_ME
```
