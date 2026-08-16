---
title: "Create BOM reports using UTF8 character encoding"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/create-bom-reports-using-utf8-character-encoding.html"
content_id: "654w5rJtBVO3M9E46K5BNw"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:34:02.574904+00:00"
---

# Create BOM reports using UTF8 character encoding

To enable support for UTF8 character encoding in BOM reports when using non-Western
characters, add the following to the `blackduck-config.env` file:

```
USE_CSV_BOM=true
```
