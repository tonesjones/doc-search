---
title: "Adding assertions that fields are tainted or not tainted"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/adding-assertions-that-fields-are-tainted-or-not-tainted.html"
content_id: "LUrvb8qaEnBqYjyUlnDqIw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:25:59.319144+00:00"
---

# Adding assertions that fields are tainted or not tainted

In some cases, you might want to override the taint value that Coverity Analysis computes for specific class fields.

Uses of certain fields should always be considered tainted. In this case, additional
security defects will be reported if the field's values are used unsafely.
Certain other fields should *never* be considered tainted, in which case security
defects that arise from an unsafe use of the field's value will be
suppressed.

Two mechanisms are available to assert the taintedness and non-taintedness of fields:

Command-line options
:   This
    section
    introduces the command-line options, which are described in detail in the `cov-analyze`
    section of the Coverity 2026.6.0 Command Reference.

Annotations
:   Annotations for tainted or untainted fields are described in "The '@Tainted' and
    '@NotTainted' Attributes for Java Code".

Consider the following example, in which the `--tainted-field
com.coverity.examples.Table.*` command-line option is passed to assert that
the fields `com.coverity.examples.Table.title` and
`com.coverity.examples.Table.values` are tainted. This will result in
an SQLI defect being reported against the `doSqlQuery` method, regardless
of (and in addition to) any other attacker-controllable strings being assigned to the
object's title field.

```
class Table {
    String title;
    Map<int, String> values;
        int id;
        
        void doSqlQuery(Statement stmt, String where_clause) {
            stmt.executeQuery(
                "SELECT * FROM
                + this.title
                + " where "
                + where_clause
            );
        }
}
```
