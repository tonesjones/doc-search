---
title: "'null' and 'NonNull'"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/null-and-nonnull-.html"
content_id: "mSJzDN24unsMODDaBTuOzg"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:12.798902+00:00"
---

# 'null' and 'NonNull'

The keywords `null` and `NonNull` are complementary.

`null`
:   The keyword `null` represents an optional value that has not been defined, as shown in the following snippet of code:
    [image: CXM code follows]

    ```
        somethingNullable != null
    ```

`NonNull`
:   The keyword `NonNull` matches any nullable value that *has* been defined, as the following code sample shows:
    [image: CXM code follows]

    ```
        somethingNullable matches NonNull as myNotNullThing
    ```

For more information, see Handling null values.
