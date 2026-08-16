---
title: "Incompatible #import attributes"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/incompatible-import-attributes.html"
content_id: "eyc_texx4xju1IFwS3TUlA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:35:32.946504+00:00"
---

# Incompatible #import attributes

The Microsoft Visual C++ `#import` directive is used to incorporate
information from a type library. The extracted information is then converted into valid
C++ code and fed into the compiler. The Coverity compiler also uses this generated code.
The code, however, can be generated incorrectly if during a single compilation a type
library is included multiple times with different attributes. The Coverity compiler
generates the following warning when this happens:

```
"t.cpp", line 2: warning: incompatible #import attributes (previous import at
    line 1)
#import "t.tlb" no_namespace
```

To avoid this issue, you need to add guards around every `#import`, for
example:

```
#ifndef __import_MSVBBM60_dll
#define __import_MSVBBM60_dll
#import "MSVBVM60.dll" raw_native_types raw_interfaces_only
#endif

#ifndef __import_MSVBBM60_dll
#define __import_MSVBBM60_dll
#import "MSVBVM60.dll" raw_native_types
#endif
```
