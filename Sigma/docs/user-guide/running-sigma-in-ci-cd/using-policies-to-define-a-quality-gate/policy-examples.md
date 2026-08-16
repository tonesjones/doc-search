---
title: "Policy Examples"
source_url: "https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/policy-examples.html"
content_id: "gxidhxwRO5Sz7YyLwXvYow"
version: "2026.8.0"
section: "Sigma User Guide"
scraped_at: "2026-08-13T00:25:29.207587+00:00"
---

# Policy Examples

The following example shows how to define a policy that causes the build to fail if an
issue is reported by the `BACKUPS_ALLOWED_ANDROID`
check.

```
version: 1
policies:
  - id: EXAMPLE_POLICY_CHECK:backups_allowed_android
    when:
      checks:
        - backups_allowed_android
    result:
      exit-code: 1
      message: >
        EXAMPLE_POLICY_CHECK:backups_allowed_android / 
        Defect from backups_allowed_android check caused failure
```

The following example shows how to define a policy that causes the build to fail if an issue
is reported by the `BACKUPS_ALLOWED`
checker.

```
version: 1
policies:
  - id: EXAMPLE_POLICY_CHECKER:backups_allowed
    when:
      checkers:
        - backups_allowed
    result:
      exit-code: 1
      message: >
        EXAMPLE_POLICY_CHECKER:backups_allowed / 
        Defect from backups_allowed_android checker caused failure
```

The following example shows a policy definition that causes builds to fail when defects
are reported for medium-severity checks.

```
version: 1
policies:
  - id: EXAMPLE_POLICY:medium-severity
    when:
      severity: medium
    result:
      exit-code: 1
      message: >
        EXAMPLE_POLICY:medium-severity message / 
        Defect from a medium severity checker caused this failure.
```
