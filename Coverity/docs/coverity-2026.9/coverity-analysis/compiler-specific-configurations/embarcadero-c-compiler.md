---
title: "Embarcadero C++ compiler"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/embarcadero-c-compiler.html"
content_id: "i4~Bj1ABH163qXu2MZGpxg"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:33:25.771909+00:00"
---

# Embarcadero C++ compiler

Use a template configuration
for the Embarcadero C++ compiler:

```
cov-configure --template --compiler bcc32 --comptype bcc:32
cov-configure --template --compiler bcc32x --comptype bcc:32x_64
cov-configure --template --compiler bcc64 --comptype bcc:32x_64
```
