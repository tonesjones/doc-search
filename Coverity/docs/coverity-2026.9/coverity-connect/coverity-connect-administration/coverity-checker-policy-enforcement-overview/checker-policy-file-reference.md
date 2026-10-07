---
title: "Checker policy file reference"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/checker-policy-file-reference.html"
content_id: "Efimdt_41w4iGicUqmkdzw"
version: "2026.9"
section: "Coverity Connect"
scraped_at: "2026-10-04T23:33:14.716567+00:00"
---

# Checker policy file reference

A checker policy file is a YAML or JSON file that defines the analysis settings a
scan must satisfy. This topic describes the supported top-level keys, their structure, and
examples of each approach.

## Top-level structure

A policy file must contain at least one of the following top-level keys:

`versions`
:   Defines the analysis versions allowed to run. See versions.

`require`
:   Defines the analysis settings that must be present in the scan. All policy
    requirements are nested under `require.analyze`. See require.
:   All settings valid in the scan configuration file
    (`coverity.yaml`) analyze section are also valid in the
    policy's `require.analyze` section, with certain exceptions
    (for example, settings that take file path values).

Both keys can coexist in the same file.

## versions

The `versions` key restricts which Coverity Static Analysis versions
are allowed. You can specify an exact list of versions or a version range.

**Exact version list**

```
versions:
  - 2026.9.0
  - 2026.12.0
```

**Version range**

```
versions:
  min: 2026.12.0
```

```
versions:
  min: 2026.9.0
  max: 2026.12.0
```

If `min` is specified without `max`, all versions at or
above the minimum are allowed. If `max` is specified without
`min`, all versions at or below the maximum are allowed.

## require

The `require` key defines analysis settings the scan configuration
must satisfy. All requirements are nested under `require.analyze`.

The following approaches can be used individually or in combination.

**aggressiveness-level**

Requires a specific analysis aggressiveness level.

```
require:
  analyze:
    aggressiveness-level: high
```

**cov-analyze-args**

Requires analysis options that map to `cov-analyze` arguments. Each
entry under `subsequences` is a list representing one argument or an
argument with its value.

```
require:
  analyze:
    cov-analyze-args:
      subsequences:
        - [--enable-virtual]
        - [--enable-constraint-fpp]
        - [--max-loop, 16]
```

**enable-check-set**

Requires predefined checker sets. This is useful for enforcing broad security or
standards-based coverage without enumerating individual checkers.

```
require:
  analyze:
    enable-check-set:
      - cwe-top-25-2023
      - owasp-web-top-10-2025
```

Note: Available checker set names depend on the analysis vocabulary supported by the
release. Examples include `cwe-top-25-2023` and
`owasp-web-top-10-2025`.

**checkers**

Requires individual checkers to be explicitly enabled.

```
require:
  analyze:
    checkers:
      checker-config:
        FORWARD_NULL:
          enabled: true
        XSS:
          enabled: true
```

**coding-standards**

Requires coding-standard analysis. Use the coding standard identifier as the key and
set `pre-canned` to specify the rule set.

```
require:
  analyze:
    coding-standards:
      misrac20212:
        pre-canned: all
      autosarcpp14:
        pre-canned: all
```

## Supported constraint types

Instead of a literal scalar value, a setting under `require.analyze`
can specify one of the following constraint types to allow a range of acceptable
values.

**equals**

Requires an exact literal match. This is semantically identical to specifying the
scalar directly.

```
require:
  analyze:
    aggressiveness-level:
      equals: high
```

**oneOf**

Requires an exact match against one of the listed literal values. This is
functionally equivalent to the sequence shorthand but may be preferred for clarity
in complex constraint objects.

```
require:
  analyze:
    aggressiveness-level:
      oneOf:
        - high
        - medium
```

**matches**

Requires the configured value to match the specified regular expression. The
regular expression is not implicitly anchored, so it can match a substring rather
than the entire string. The regular expression must be valid and must match at
least one valid value for the setting.

```
require:
  analyze:
    aggressiveness-level:
      matches: "^(low|high)$"
```

**range**

Requires the configured value to be numeric. This constraint type applies to
numeric settings only. If `min` is specified, the value must be at
or above the minimum. If `max` is specified, the value must be at
or below the maximum. At least one of `min` or `max`
must be specified.

```
require:
  analyze:
    replay-processes:
      min: 1
      max: 10
```

**fullSequence**

Requires the configured value to be a sequence that exactly matches the listed
constraints, in order, with no additional elements permitted.

The corresponding scan configuration setting must be present, and its value must be
a sequence of scalars. Each value in the sequence must satisfy the corresponding
element listed in the policy constraint. Scalar constraints include
`equals` (or a literal value), `oneOf` (or a list
of literal values), `matches`, and `range`.

```
require:
  analyze:
    cov-analyze-args:
      fullSequence:
        - --max-loop
        - 16
        - --max-mem
        - 64
```

This requires `cov-analyze-args` to be present and to be exactly
`--max-loop 16 --max-mem 64`.

```
require:
  analyze:
    cov-analyze-args:
      fullSequence: [--max-loop, 16, --max-mem, 64]
```

This is equivalent to the previous example. Commas are required to separate the
elements of the sequence.

```
require:
  analyze:
    cov-analyze-args:
      fullSequence:
        - --max-loop
        - range:
            min: 16
            max: 32
        - --max-mem
        - 64
```

This is similar to the previous example, but specifies a `range`
constraint for the second element of the sequence.

**subsequences**

Requires the configured sequence to include each listed subsequence of constraints,
in order within each subsequence, while permitting additional elements elsewhere
in the sequence.

The corresponding scan configuration setting must be present, and its value must be
a sequence of scalars. The configured sequence must include each subsequence
listed in the policy constraint, and each value in a subsequence must satisfy the
corresponding element listed in the policy constraint. Scalar constraints include
`equals` (or a literal value), `oneOf` (or a list
of literal values), `matches`, and `range`.

```
require:
  analyze:
    cov-analyze-args:
      subsequences:
        - - --max-loop
          - 16
        - - --max-mem
          - 64
```

This requires `cov-analyze-args` to be present and to include
`--max-loop 16` and `--max-mem 64`, in either
order, allowing other elements as well.

```
require:
  analyze:
    cov-analyze-args:
      subsequences:
        - [--max-loop, 16]
        - [--max-mem, 64]
```

This is equivalent to the previous example. Commas are required to separate the
elements of each subsequence.

```
require:
  analyze:
    cov-analyze-args:
      subsequences:
        - - --max-loop
          - range:
              min: 16
              max: 32
        - [--max-mem, 64]
```

This is similar to the previous example, but specifies a `range`
constraint for the second element of the first subsequence.

## Combined example

A single policy file can combine a version constraint with multiple requirement
approaches.

```
versions:
  min: 2026.12.0
require:
  analyze:
    aggressiveness-level: high
    enable-check-set:
      - cwe-top-25-2023
    cov-analyze-args:
      subsequences:
        - [--enable-constraint-fpp]
        - [--enable-virtual]
    checkers:
      checker-config:
        FORWARD_NULL:
          enabled: true
```
