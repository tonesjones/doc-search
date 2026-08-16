---
title: "Extended example: Using the 'languages' and 'files' options together"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/extended-example-using-the-languages-and-files-options-together.html"
content_id: "~QQtP8O9LI4ZqaJAqu_2Dg"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:45:56.177916+00:00"
---

# Extended example: Using the 'languages' and 'files' options together

Here is a full example that combines both `languages` and `files`:

```
capture:
    languages:
        include:
            - java
            - csharp
    files:
        exclude-glob: "*Test.java"
        include-dirs:
            - vendor
```

This sample configuration:

- Captures only Java and C# files.
- Excludes files whose name has the suffix Test.java; for example, a file called whateverTest.java would be excluded.
- Overrides the default exclusions so as to include files in vendor/ directories.
