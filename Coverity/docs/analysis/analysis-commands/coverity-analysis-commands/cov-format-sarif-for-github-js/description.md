---
title: "Description"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/description.html"
content_id: "~14SqInvmhtK~V1m5WD2qg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:40:57.089952+00:00"
---

# Description

GitHub can display Coverity Analysis results formatted using a particular subset of the
SARIF 2.1.0 JSON schema.

The `cov-format-sarif-for-github.js` script converts Coverity Analysis
results into SARIF format customized for GitHub.

The script is located in

```
<install_dir>/SARIF/cov-format-sarif-for-github.js
```

You can run it using the Node.js installation located in

```
<install_dir>/node/bin/node
```

The resulting SARIF will not contain source code, but relies on GitHub hosting the source
code in a repository.

The --githubUrl and --checkoutPath option values
are used to convert analyzed filepaths into GitHub URLs that hold the corresponding
source code.

For more information about SARIF support in GitHub, see <https://docs.github.com/en/github/finding-security-vulnerabilities-and-errors-in-your-code/sarif-support-for-code-scanning>.
