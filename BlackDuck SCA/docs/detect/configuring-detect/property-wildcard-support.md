---
title: "Property wildcard support"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/property-wildcard-support.html"
content_id: "ZEbYbgeoSK2QRMNlhfLw2g"
version: "11.5.1"
section: "Configuring Detect"
scraped_at: "2026-08-08T23:44:22.516970+00:00"
---

# Property wildcard support

When providing input values for the following Detect properties, you can utilize filename globbing-style wildcards.

| General | Gradle | Lerna | Maven | pnpm |
| --- | --- | --- | --- | --- |
| detect.binary.scan.file.name.patterns | detect.gradle.included.configurations | detect.lerna.excluded.packages | detect.maven.included.scopes | detect.pnpm.included.packages |
| detect.excluded.directories | detect.gradle.excluded.configurations | detect.lerna.included.packages | detect.maven.excluded.scopes | detect.pnpm.excluded.packages |
|  | detect.gradle.included.projects |  | detect.maven.included.modules |  |
|  | detect.gradle.excluded.projects |  | detect.maven.excluded.modules |  |

| Wildcard | Effect | Example |
| --- | --- | --- |
| Asterisk (*) | matches any sequence of zero or more characters | `*.jpg` matches `someimage.jpg`, but not `somedocument.doc` |
| Question mark (?) | matches any single character | `*.???` matches `someimage.jpg` and `somedocument.doc`, but not `somedocument.docx` |

Note: Wildcard evaluation in these values is similar to Linux command line file globbing, and different from regular expression matching.Detect uses the
[Apache Commons IO FilenameUtils.wildcardMatch()](https://commons.apache.org/proper/commons-io/javadocs/api-release/org/apache/commons/io/FilenameUtils.html#wildcardMatch-java.lang.String-java.lang.String-) method to determine whether a string matches the given pattern.
