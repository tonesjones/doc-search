---
title: "Remove old Sigma (SAST) processes"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/remove-old-sigma-sast-processes.html"
content_id: "OynYcWQsqvD9yzU_TNY5AA"
version: "2026.9.0"
section: "Code Sight Release Notes and Known Issues"
scraped_at: "2026-10-06T23:40:00.211593+00:00"
---

# Remove old Sigma (SAST) processes

If you run Code Sight in VS Code and you upgraded from Code Sight 2021.8.0 or 2021.8.1 to Code Sight 2022.1.0, 2022.1.1, or 2022.4.0, you need to
make sure out-of-date Sigma (SAST) processes are no longer running.

**After you upgrade, do one of the following:**

- (Recommended) Restart your system.
- If you don’t wish to restart your system, then use Operating System controls to stop the lingering processes.

  In macOS or Linux, the Sigma process appears as `sigma`.
  In Windows, the Sigma process appears as `sigma.exe`.
