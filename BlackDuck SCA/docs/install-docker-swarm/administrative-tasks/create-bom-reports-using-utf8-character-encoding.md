---
title: "Create BOM reports using UTF8 character encoding"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/create-bom-reports-using-utf8-character-encoding.html"
content_id: "GeU_4fDcN3qTtzPYgBAydg"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-10-04T23:32:25.241788+00:00"
content_hash: "baea2a7ee32e7b712ae5462433f19eda6ffde1fd85a7360d4c94e40cfc7d4071"
---

# Create BOM reports using UTF8 character encoding

To enable support for UTF8 character encoding in BOM reports when using non-Western characters, add the following to the `blackduck-config.env` file:

```
USE_CSV_BOM=true
```
