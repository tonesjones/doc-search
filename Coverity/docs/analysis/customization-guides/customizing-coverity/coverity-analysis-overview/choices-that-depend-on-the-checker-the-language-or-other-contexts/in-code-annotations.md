---
title: "In-code annotations"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/in-code-annotations.html"
content_id: "zEGl9loeLgt0kdevW3cZlQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:25:12.011175+00:00"
---

# In-code annotations

Another way to adjust analysis behavior is to add *analysis annotations* to the
source code being analyzed. These annotations, like models, provide Coverity Analysis with hints about function behavior.

For C/C++, annotations can also suppress reports of code patterns that have an
intentional purpose in the source code being analyzed.

Note: The standard Coverity workflow never requires any tool-specific code modifications.
The use of in-code analysis annotations is purely optional.

**Use case:** Override the default TAINT_ASSERT checker report of a tainted value, but
for specific class members only.

For example, a user has certain class members that are known to be either trusted or not
trusted. In the following sample of Java code, the entries `@NotTainted`
and `@Tainted` are analysis annotations that tell TAINT_ASSERT to always
treat `name` values as trustworthy and `selfDescription`
values as tainted:

```
import com.coverity.annotations.*;
            
    class UserData {
        @NotTainted String           name;
        @Tainted    StringBuffer     selfDescription;
    }
```

**Limitations and alternatives:**

- Analysis annotations are available only for C/C++, C#, Java, and Visual Basic.
- The properties that can be described by in-code annotations are limited and apply
  only to certain syntax.

**Suggestion:** If analysis annotations are not compatible with your project source,
or if the situation you want to adjust for is out of their scope, look at the
documentation on security analysis directives (introduced in the section that follows)
to see if these provide the functionality you are looking for.

**Learn more:** See Analysis annotations.
