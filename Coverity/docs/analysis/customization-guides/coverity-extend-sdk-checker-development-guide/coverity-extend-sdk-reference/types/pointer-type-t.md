---
title: "pointer_type_t"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/pointer_type_t.html"
content_id: "YJ3wyaZzT_xh3WxaC5XUFw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:39:49.362369+00:00"
---

# pointer_type_t

This class represents a pointer, reference, or pointer to member type.

- `type_t pointed_to` — The referent type. If it is a
  member_type_t, then this type represents a pointer to
  member.
- `bool m_is_ref` — True if this type is a reference, false if
  it is a pointer or pointer to member.
