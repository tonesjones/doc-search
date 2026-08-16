---
title: "The when Node"
source_url: "https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/the-when-node.html"
content_id: "GrASSLXa~AW_zKxU7xZWYw"
version: "2026.8.0"
section: "Sigma User Guide"
scraped_at: "2026-08-13T00:25:27.941457+00:00"
---

# The when Node

The `when` node lists the conditions that define rule violations. If the
condition criteria defined in this node matches the issues found in your code, the
policy is violated.

You may define conditions based on the checks that flag issues or on the severity of *any*
check that flags issues. If you specify both check names and severity levels, the build
might fail for either case, but the severity condition takes precedence.

- **To match checks, use this structure:**

  ```
  when:
  	checks:
  		- <CHECK_NAME_1>
  		- <CHECK_NAME_2>
                                      ....
  		- <CHECK_NAME_N>
  ```

  The first check name that matches the found issue is the one causing the policy
  violation.
- **To match checkers, use this structure:**

  ```
  when:
  	checkers:
  		- <CHECKER_NAME_1>
  		- <CHECKER_NAME_2>
                                      ....
  		- <CHECKER_NAME_N>
  ```

  The first checker name that matches the found issue is the one causing the policy
  violation.
- **To match severity, use this structure:**

  ```
  when:
  	severity:
  		- <SEVERITY_LEVEL>
  ```

  Severity values can be one of the following:

  ```
  -- Unspecified
  -- Info
  -- Low
  -- Medium
  -- High
  -- Critical
  ```
