---
title: "Using Policies to Define a Quality Gate"
source_url: "https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/using-policies-to-define-a-quality-gate.html"
content_id: "Y5pQ6Wd~t5l1cl5l8hHcGA"
version: "2026.8.0"
section: "Sigma User Guide"
scraped_at: "2026-08-13T00:25:26.682469+00:00"
---

# Using Policies to Define a Quality Gate

Note: Using a policy file to define a quality gate is deprecated.

To use Sigma as a quality gate, you create a YAML policy file that specifies the
conditions under which a build should fail. This policy file can be one of the
following:

- Sigma's default policy file (.sigma-policy.yml), if it
  exists.

  This file should be in the directory where you run the `sigma`
  command.
- A file you specify using the `--policy` option to the
  sigma command.

Sigma reads policy definitions from the file and uses these to select the exit code and
the message shown the user when a given condition is met.

If the pipeline fails, Sigma will not send results to be triaged by issue management; it
will display results for issues that caused the failure, and you can take action to fix
or dismiss the issues.

You can use policy to fail Sigma (and your build) in the following cases:

- If an issue is found by a particular check or set of checks.
- If an issue is found by checks of a given severity; for example, fail if a
  critical issue is found.
