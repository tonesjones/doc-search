---
title: "Import file format examples"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/import-file-format-examples.html"
content_id: "2nyvVMzGT8~LMxMIc6Smvg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:35:27.585463+00:00"
---

# Import file format examples

This section describes the format and attribute values of the JSON file that you must
construct in order to import third-party issues into Coverity Connect, including:

- A sample import file
- Sample source files
  that the import file references
- Import file reference that describes the
  elements used in the import file

Any field preceded by a question mark (?) is optional.

## JSON file - example.json

```
{
"header" : {
    "version" : 1,
    "format" : "cov-import-results input"
},
"sources" : [{
        "file" : "/projects/cov-import-test/doc_example/missing_indent_source.c",
       ? "encoding" : "ASCII",
       ? "language" : string
    },
    {
        "file" : "/projects/cov-import-test/doc_example/too_many_characters.c",
        "encoding" : "ASCII"
    }
],
"issues" : [{
    "checker" : "bad_indent",
    "extra" : "bad_indent_var",
    "file" : "/projects/cov-import-test/doc_example/missing_indent_source.c",
  ? "function" : "do_something",
    "subcategory" : "small-mistakes",
  ? "domain" : string
    
  ? "properties" : {
      ? "type" : "Type name",
        "category" : "Category name",
        "impact" : "Medium",
      ? "cwe" : 123,
        "longDescription" : "long description",
        "localEffect" : "local effect",
        "issueKind" : "QUALITY"
    },    
    "events" : [{
        "tag" : "missing_indent",
        "description" : "Indent line with 8 spaces (do not use Tab)",
      ? "linkUrl" : "http://www.blackduck.com/",
      ? "linkText" : "Black Duck Software, Inc Web page",  
        "line" : 19,
      ? "main" : true
        }
    ] },
{
    "checker" : "line_too_long",
    "extra" : "line_too_long_var",
    "file" : "/projects/cov-import-test/doc_example/too_many_characters.c",
    "function" : "do_something_else",
    "subcategory" : "small-mistakes",
    "events" : [
        {
        "tag" : "long_lines",
        "description" : "This line exceeds the 80 character limit",
     ?  "linkUrl" : "http://www.blackduck.com/",
     ?  "linkText" : "Black Duck Software, Inc Web page",
        "line" : 4,
     ?  "main" : true
        }
    ] }
] }
```

**Source file 1 - missing_indent_source.c**

```
#include <stdio.h>

int main(int argc, const char * argv[])
{
    int limit=10;
    int res = 0;

    res = do_something (limit);

    printf ("The final count for l was %d\n",res);

    return 0;
}

int do_something (int limit) {
    int i=0, l=0;

    for (i=0;i<limit;i++){
        l+=i;
    }

    return l;
}
```

**Source file 2 - too_many_characters.c**

```
#include  <stdio.h>

int do_something_else () {
	printf("This is an example of a pretty long line, which will exceed the 80 character rule"); 
}
```
