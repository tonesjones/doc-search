---
title: "Windows limitations"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/windows-limitations.html"
content_id: "LWtunpYyow~53LVNMcR~ng"
version: "2026.9"
section: "Coverity Connect"
scraped_at: "2026-10-04T23:33:19.672755+00:00"
---

# Windows limitations

Limitations for PostgreSQL on Windows include the following:

- `shared_buffer` cannot exceed 1GB.
- `effective_io` cannot be used to improve performance. Enabling
  this feature under Windows will prevent PostgreSQL from starting.
