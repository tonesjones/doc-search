---
title: "I see a header file error: expected an identifier"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/i-see-a-header-file-error-expected-an-identifier.html"
content_id: "Ckfh~u~TLDkPQWCmp5X~~w"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:35:21.982299+00:00"
---

# I see a header file error: expected an identifier

**Error:**

```
"tasking/c166v86r3/include/stdio.h", line 21: error: 
expected an identifier 
#ifndef#define#endif
"/tasking/c166v86r3/include/stdio.h", 
line 14: error: the #endif for this directive is missing #ifndef _STDIO_H
```

**Solution:**

There are missing macros. Look at the stdio.h file to identify the macro
in title. The macro could be removed through a number of reasons. The first to check is
the compiler macro and compat files to see if the string has been #define'd to nothing.
The next is to check in the coverity_config.xml file for the compiler. The directory to
look in, for the file, will be shown in the `cov-emit` line that
failed. There will be a preinclude option followed by a path to the
coverity-compiler-compat.h. All the files used are in the same
directory. Please note that Microsoft Visual Studio compilers may use "response" files.
These are a list of files and options in an external file that is passed to
`cov-translate` as an 'rsp' file. If this is the case, you may not
see the complete `cov-emit` line. To work out which configuration that
was being used, you would manually have to work out which compiler was being used and
look that up at the top of the build-log.txt file.
