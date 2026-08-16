---
title: "Model for a Java interface method"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/model-for-a-java-interface-method.html"
content_id: "Am78ajYaV1vkjBEPvBDtcg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:25:56.661982+00:00"
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
