---
title: "Overriding Severity Levels"
source_url: "https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/overriding-severity-levels.html"
content_id: "o8RNDgwuUneKtXvPdyR3Kw"
version: "2026.8.0"
section: "Sigma User Guide"
scraped_at: "2026-08-13T00:25:11.473797+00:00"
---

# Overriding Severity Levels

Note: Configuring Sigma with a `.sigma-config.yml`
file is deprecated. For more information, see Configuring Sigma with coverity.yml.

Every issue found by a Sigma check has an associated severity level. This level is
calculated by Sigma and can have one of the following values:

- Unspecified
- Info
- Low
- Medium
- High
- Critical

You can display the severity level associated with a given check by running the
command

```
sigma explain <check_name>
```

By configuring the severity level of a check from its default of "Medium" to "High" or
"Critical," you can control how the issues are rendered in GitHub, GitLab or in an IDE.
This can affect how a company operates, because a company might have a policy of not
releasing a product if there are any errors in GitHub Code Scanning Alerts or GitLab
Security Vulnerabilities.

When Sigma is configured with the output format of `github` or
`gitlab`, Sigma severity levels are converted to severity levels that
control how GitHub Code Scanning Alerts or GitLab Security Vulnerabilities are rendered.

Below is a mapping of Sigma severities to GitHub and GitLab severities.

| Sigma | GitHub | GitLab |
| --- | --- | --- |
| Unspecified | Note | Unknown |
| Info | Note | Info |
| Low | Note | Low |
| Medium | Warning | Medium |
| High | Error | High |
| Critical | Error | Critical |

Unless they are overridden, Sigma severity levels are calculated from a check's
`impact` and `likelihood` levels.

Impact and likelihood generally have similar but different values, the computed value and
the default value. Every check will have a default impact and likelihood assigned,
however, when a check finds an issue, it can dynamically change the impact, the
likelihood, or both, to a different value according to the context.

For impact and likelihood, it is possible to overwrite both the default value and the
computed value:

- When changing the default attribute, the new customized value will be used when the
  check does not dynamically re-assign the impact or likelihood.
- When changing the computed attribute, the new customized value will always be
  used.

| Severity Level | Default Impact | Default Likelihood |
| --- | --- | --- |
| Info | Low | Low |
| Low | Low | Medium |
| Low | Medium | Low |
| Medium | Low | High |
| Medium | Medium | Medium |
| Medium | High | Low |
| High | Medium | High |
| High | High | Medium |
| Critical | High | High |
