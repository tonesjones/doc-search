---
title: "Model for a Java interface method"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/model-for-a-java-interface-method.html"
content_id: "Am78ajYaV1vkjBEPvBDtcg"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:05.524596+00:00"
---

# Model for a Java interface method

Java interface methods cannot have implementations. Because of this, to model an
interface method you need to declare the interface as if it were a class.

For example, Coverity provides the following built-in model of the
`Comparable<T>` interface:

```
public class Comparable<T> {
    public int compareTo( To ) {
        return unknownNonnegativeInt();
    }
}
```
