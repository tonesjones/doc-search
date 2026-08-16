---
title: "Windows limitations"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/windows-limitations.html"
content_id: "LWtunpYyow~53LVNMcR~ng"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:52:13.266597+00:00"
---

# Windows limitations

Limitations for PostgreSQL on Windows include the following:

- `shared_buffer` cannot exceed 1GB.
- `effective_io` cannot be used to improve performance. Enabling
  this feature under Windows will prevent PostgreSQL from starting.
