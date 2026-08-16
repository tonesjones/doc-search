---
title: "Finding a literal argument value"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/finding-a-literal-argument-value.html"
content_id: "sqfrBTRi~4MMoqnBzk87Hw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:26:42.617165+00:00"
---

# Finding a literal argument value

With the `functionCall` pattern, available for all supported target languages,
you can detect a literal value being passed to a function.

**Use case:**
:   Find an argument that has a particular value, or that does not have a desired value.

    You might want to detect an illegal value being passed, a mandatory value, or an inappropriate usage.
    For example, legacy code might specify a cryptographic standard that is no longer considered secure.

The following example simply checks for a mandatory value. The `functionCall` pattern's `argumentList` property
lets your checker inspect what is being passed to a speficied function.

[image: CXM code follows]

```
checker {
    name = "BAD_ARGUMENT_VALUE";
    reports = for node in globalset allFunctionCode where 
                  node matches functionCall {
                      .calledFunction.identifier == "setIterations"
                  } as fc
                  && fc.argumentList[1] matches intLiteral { .value != 256 } : {
                      events = [
                          {
                              tag = "testArgValue";
                              description = "The 'steps' parameter"
                                            + " must equal 256.";
                              location = node.location;
                          }
                      ];
                  }
};
```
