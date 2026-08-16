---
title: "Models for source code that is unavailable"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/models-for-source-code-that-is-unavailable.html"
content_id: "fhXIUWoZB9r_omfJ2NOdmg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:25:26.560736+00:00"
---

# Models for source code that is unavailable

Sometimes the source code for called functions is not available, and cannot be
analyzed. For example, third-party library functions are typically linked in by using their
object-code form, and the source code for the library is not accessible.

Examples of third-party libraries include the standard C and C++ libraries, the UNIX® system-call API, and the Windows® API.

When interfaces that are perhaps critical to the system's behavior are linked in
from code that is not compiled locally, this code cannot be analyzed unless you create
custom models to specify the behavior of those interfaces.

For example, if your application links to a new memory-allocation interface from a
third-party API, writing custom models of the interface can enable Coverity Analysis to detect and report defects in the uses of that
allocator.

As another example, if your application uses an abort-like function that relies on an
assembly routine to exit, analysis might be incapable of detecting that calls to this
function cannot return. In this case, false positives occur because of the imperfect
understanding of the code. Writing a custom model of the abort routine can correct this
problem.
