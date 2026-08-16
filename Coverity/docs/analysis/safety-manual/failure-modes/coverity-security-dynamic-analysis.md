---
title: "Coverity Security Dynamic Analysis"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-security-dynamic-analysis.html"
content_id: "OO1Yq5tERdWmOmIxmEo7sw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:35:36.190884+00:00"
---

# Coverity Security Dynamic Analysis

Coverity Security Dynamic Analysis (DA) normally runs as part of the
*emit* capture step in the Coverity Analysis workflow, when
the project being captured includes either Java or .NET (C# or Visual Basic) bytecode.
It is invoked as a separate process by the `cov-build` command, and runs
just before the execution of either of those commands completes.

Because Security DA executes some of the captured bytecode on the platform used to perform the capture step, there is
a small risk that the state of that machine can be affected. Depending on the code executed, any of the machine's resources,
including filesystems and other processes, might be affected. However, steps have been taken to minimize this risk, as described here:

- The methods of interest to Security DA are those which have a single in/out parameter of type `string`,
  and those which have a single input parameter of type `string` and a return value of type `string`.
  Only those methods of interest are subjected to Security DA; all other methods are ignored.
- When tested by Security DA, the methods of interest are invoked with a small list of stereotyped inputs. These inputs consist of short strings
  no longer than two characters in length. No interesting (malicious) behavior could be encoded in such small strings. Any malicious behavior detected
  is thus an essential characteristic of the method being called.
- To further limit the possibility of causing undesirable effects, Security DA begins with a list of routines that are known to be good.
  By examining the call tree of the method being tested, Security DA can determine whether all of the callees (defined recursively) of that method
  are known to be good. If one is not, that method is not analyzed.

  There is also a list of routines that are known to be bad. This list is used to shorten the search.
- When analyzing Java bytecode, each method under test is executed in a system-supplied sandbox.
  This further limits the risks involved in running Java Scurity DA.

## See also

Coverity Template Dynamic Analysis
