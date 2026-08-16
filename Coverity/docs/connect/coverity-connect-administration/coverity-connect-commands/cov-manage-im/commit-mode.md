---
title: "Commit mode"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/commit-mode.html"
content_id: "0CbpuCaxEupzXiVGlx4Lgg"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:51:36.037010+00:00"
---

# Commit mode

Gets, enables, and disables the commit gate, which permits or prevents commits to the
Coverity Connect database.

## Synopsis

```
--mode commit --update --set status:<enabled>|<disabled> [<OTHER>]
```

## Commit mode options

In general, you can specify options in any order.

The OTHER option listed in the synopsis refers to sets of command
line options that are common to all modes. The options are:

- Common OUTPUT options
- CONNECTION options
- Shared
  options

OPERATION options
:   Specify exactly one OPERATION option in commit mode.

    --update
    :   Updates the commit gate status.

SET options
:   The SET options apply changes to the commit gate. Use `--update` to update the
    commit gate. At least one SET option is required with
    `--update`.

    --set status:{enabled | disabled}
    :   Opens the commit gate (enabled) or closes the commit gate
        (disabled).

## Commit mode examples

The first example shows the four connection options that must contain values either
on the command line, or in the XML configuration file (host, port, user, password).
These connection options are intentionally dropped from most of the subsequent
examples to reduce the length of the command lines. When the connection options are
not specified, assume that the values are retrieved from the default XML
configuration file.

**Update examples**

Enable the commit gate.

```
> cov-manage-im --mode commit --update --set status:enabled
```

Disable the commit gate.

```
> cov-manage-im --mode commit --update --set status:disabled
```
