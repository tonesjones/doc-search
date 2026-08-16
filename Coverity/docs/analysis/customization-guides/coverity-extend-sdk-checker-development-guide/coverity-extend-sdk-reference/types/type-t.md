---
title: "type_t"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/type_t.html"
content_id: "8ANAZyeZCznVO3jq1Fs58Q"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:39:45.307453+00:00"
---

# type_t

This class is the superclass of all type representation classes. It does not have any
data members.

It has a number of virtual functions that can be used to determine which
type_t subclass that an object is. This information is also
available using standard run-time type identification, but these methods are sometimes
more convenient. For each subclass SUB, there are methods:

- `const SUB &as_SUB() const` — If this object has dynamic
  type SUB, returns a reference to it as such. Otherwise,
  throws invalid_type_exception.
- `SUB &as_SUB()` — Same as previous, but accepts/returns a
  non-constant reference.
- `const SUB *as_SUB_p() const` — If this object has dynamic
  type SUB, returns a pointer to it as such. Otherwise,
  returns NULL.
- `SUB *as_SUB_p()` — Same as previous, but accepts/returns a
  non-constant pointer.
