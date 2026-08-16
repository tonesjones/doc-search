---
title: "Coverity Extend SDK checker file structure"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-extend-sdk-checker-file-structure.html"
content_id: "O3z89Q4RiFaQ8u8xoP0I8w"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:39:05.718436+00:00"
---

# Coverity Extend SDK checker file structure

An Coverity Extend SDK checker source file is organized as follows:

```
// checker_name.c
// (comment about what the checker does)
      
#include "extend-lang.hpp"        // Coverity Extend SDK API
      
(1) 
      
START_EXTEND_CHECKER( checker_name, checker_type );
      
(2) 
      
END_EXTEND_CHECKER();
      
MAKE_MAIN( checker_name )
```

In section (1) you can define arbitrary C/C++ functions
and data structures. Syntactically, it is in the global scope.

In section (2) you define the checker handler functions. Syntactically, section (2) is
inside a class definition.

You can define member variables inside section (2); doing so is somewhat cleaner than
defining them as global variables in section (1), but either method works. However,
member variables cannot be initialized at the declaration site (see INIT_OPTIONS).
