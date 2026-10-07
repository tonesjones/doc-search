---
title: "Suppressing defect reports on a method"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/suppressing-defect-reports-on-a-method.html"
content_id: "8rczMDNtHaZ5QOChi0SscQ"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:05.732430+00:00"
---

# Suppressing defect reports on a method

An empty model overrides the behaviors derived by Coverity Analysis. You can use such
a model to suppress false positives when executing the CSRF checker.

In the following sample code, the call inside the model has been commented out, which
suppresses defect reports from CSRF:

```
package com.example;

class MyDAO {
    void permissibleUnprotectedDatabaseUpdate(String value) { 
        /* Empty model suppresses derived CSRF protection obligation:
               SecurityPrimitives.csrf_check_needed_for_db_update();
        */
    }
}
```

To generate models for Web application security checkers only, see Generating Java Web application security models.
