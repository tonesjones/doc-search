---
title: "Adding the bin directory to your PATH"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/adding-the-bin-directory-to-your-path.html"
content_id: "ut38pywtMk62TpPD6p3aaQ"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:46:44.114821+00:00"
---

# Adding the bin directory to your PATH

In order to run `cov-run-desktop` from the command line, it is recommended
(although not required) to add the bin directory of the
`cov-analysis` installation directory to your PATH.

**On Windows:**

1. Go to Control Panel > System Properties > Advanced > Environment Variables.
2. Select PATH and click Edit.
3. Append a semi-colon (;) followed by the "bin" directory path.
4. Click OK twice to save.
5. Start a new command shell window.

On Unix, edit your shell startup file (for example, "$HOME/.bashrc")
and add a line like:

```
PATH=$PATH:/path/to/cov-analysis/bin
```

where `/path/to/cov-analysis` is the directory where you chose to install the
Coverity Analysis tools. Then save that file and start a new shell.
