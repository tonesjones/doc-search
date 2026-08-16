---
title: "Setting Sigma Policy Files"
source_url: "https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/setting-sigma-policy-files.html"
content_id: "fUpEUp5I9BAbzL02rQuh3g"
version: "2026.8.0"
section: "Sigma User Guide"
scraped_at: "2026-08-13T00:25:21.397286+00:00"
---

# Setting Sigma Policy Files

By default, Sigma searches for the .sigma-policy.yml file in the
directory where Sigma is being executed. This file defines the policy rules that control
whether Sigma identifies policy violations during execution.

If you want Sigma to use a policy file different than the default, add the
`--policy` option to the Command Line field
with the correct path to the policy rules file in the build workspace.

The command syntax is as follows:

```
--policy <PATH_TO_POLICY_FILE_IN_WORKSPACE> analyze --format jenkins
```

In the following example, the `--policy` parameter specifies that the file
sigma-policy.yml is located in the config
directory in the workspace.

```
--policy config/sigma-policy.yml analyze --format jenkins
```
