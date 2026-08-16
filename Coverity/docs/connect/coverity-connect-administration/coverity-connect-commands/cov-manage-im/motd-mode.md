---
title: "MOTD mode"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/motd-mode.html"
content_id: "2s4aHPQFjXhJRKaF_9Bs5Q"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:51:35.405075+00:00"
---

# MOTD mode

Sets and gets a message of the day for a Coverity Connect instance.

## Synopsis

```
--mode motd --show [<OUTPUT>] [<OTHER>]

--mode motd --update <SET> [<OTHER>]
```

## MOTD mode options

In general, you can specify options in any order.

The OTHER option listed in the synopsis refers to sets of command
line options that are common to all modes. The options are:

- Common OUTPUT options
- CONNECTION options
- Shared
  options

OPERATION options
:   Specify exactly one OPERATION option in motd mode.

    --show
    :   Outputs the current message of the day.

    --update
    :   Updates the message of the day.

OUTPUT options
:   OUTPUT options are optional and are valid only with the `--show` option.

    -no-headers
    :   Displays the message of the day without a header if
        enabled is specified.

SET options
:   The SET options apply changes the message of the day. Use `--update` to update the
    message of the day. At least one SET option is required with
    `--update`.

    --set message:"message"
    :   Specify a message. For example

        `--set message:"this is the message of the
        day"`

## MOTD mode examples

The first example shows the four connection options that must contain values either
on the command line, or in the XML configuration file (host, port, user, password).
These connection options are intentionally dropped from most of the subsequent
examples to reduce the length of the command lines. When the connection options are
not specified, assume that the values are retrieved from the default XML
configuration file.

**Show examples**

Show message of the day.

```
> cov-manage-im --host cim.company.com --port 8080 --user test \
    --password secret --mode motd --show -no-headers
```

**Update example**

Change the message of the day.

```
> cov-manage-im --mode motd --update --set message:"hello, Hello, HELLO"
```
