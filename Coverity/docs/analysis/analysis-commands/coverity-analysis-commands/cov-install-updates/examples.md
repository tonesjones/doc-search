---
title: "Examples"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/examples.html"
content_id: "0UTTEh2MIRbiJcu7tKiccg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:41:34.130253+00:00"
---

# Examples

The following examples illustrate the use of the `cov-install-updates`
command.

This command checks the number of updates available:

```
C:\Users\thildeb>cov-install-updates check --url=https://emmett:14111 --user=userName --password=aPassword

5 updates are available.
```

This command checks the content of available updates:

```
C:\Users\thildeb>cov-install-updates list --url=https://emmett:14111 --user=userName --password=aPassword

5 updates are available.

Updates available for product: Coverity Static Analysis
------------------------------
**> 2018.03-1
User documentation errata and updates.
------------------------------
**> 2018.03-2
Add a script to simplify model extraction from JavaScript frameworks.
------------------------------
**> 2018.03-3
Expanded Japanese documentation.
------------------------------
**> 2018.03-4
Improvement and expansion of selected security checkers.
------------------------------
**> 2018.03-5
Selected new QA checkers are now enabled for the Swift language.
------------------------------
```

This command displays the version number:

```
C:\Users\thildeb>cov-install-updates version
2018.03
```

This example shows the installation of updates up to the specified version number:

```
C:\Users\thildeb>cov-install-updates install --url=https://emmett --port=14111 --user=userName --password=aPassword 
   --end-version=2018.03-1
[STATUS] Downloading updates list
[INFORMATION] 1 update to install.
[STATUS] Downloading cov-analysis-win64-2018.03-1-update.zip
[STATUS] Unpacking cov-analysis-win64-2018.03-1-update.zip
[INFORMATION] Selected installers:
------- 2018.03 ==> 2018.03-1
[STATUS] Validating installers
[STATUS] Listing backup files from cov-analysis-win64-2018.03-1-update.zip
[STATUS] Installing cov-analysis-win64-2018.03-1-update.zip
[STATUS] Verifying current installation.
[STATUS] Done.
```

This example illustrates the use of the `rollback` subcommand:

```
C:\Users\thildeb>cov-install-updates rollback --force
[STATUS] Rolling back from C:\Program Files\Coverity\Coverity Static Analysis\.coverity\rollback
[STATUS] Done.
```
