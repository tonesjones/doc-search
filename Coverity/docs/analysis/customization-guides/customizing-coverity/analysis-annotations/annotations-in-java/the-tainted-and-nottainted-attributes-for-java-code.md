---
title: "The '@Tainted' and '@NotTainted' attributes for Java code"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-tainted-and-nottainted-attributes-for-java-code.html"
content_id: "fny2clTrv8LuO_kB1C4okQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:26:29.158720+00:00"
---

# The '@Tainted' and '@NotTainted' attributes for Java code

Marking a field as `@Tainted` indicates that security checkers should
treat that field as coming from an untrusted source (that is, as tainted). Marking a field
as `@NotTainted` indicates that analysis should treat that data as untainted,
and not report a defect when the data flows into HTML output, an SQL interpreter, or other
such sink.

## '`@Tainted`'

The following example notates that the string `untrusted` should be
considered to contain tainted data:

```
import com.coverity.annotations.*;
import java.sql.*;

class HasTaintedField {
    @Tainted String untrusted;
}

class MyController {
    void doQuery(HasTaintedField x, Statement stmt) {
        stmt.execute(
            "SELECT * FROM user WHERE name='"
            + x.untrusted
            + "'"
        );
    }
}
```

## '`@NotTainted`'

Although a `@NotTainted` annotation suppresses error reports when the
identified field flows into a sink, it *does report* a TAINT_ASSERT defect if
it identifies tainted data flowing into the sink

For more information, see the description of "TAINT_ASSERT" in the Coverity 2026.6.0 Checker Reference.
