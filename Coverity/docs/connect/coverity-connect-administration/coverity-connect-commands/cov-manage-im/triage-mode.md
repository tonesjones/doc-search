---
title: "Triage mode"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/triage-mode.html"
content_id: "g4X3l_Pho0kNFbUyySttqA"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:51:34.802852+00:00"
---

# Triage mode

Query, add, delete, and update triage stores in Coverity Connect.

## Synopsis

```
--mode triage --show [<FILTER>][<OUTPUT>] [<OTHER>]

--mode triage --add <SET> [<OTHER>]

--mode triage --delete <FILTER> [<OTHER>]

--mode triage --update <FILTER> <SET> [<OTHER>]
```

## Triage mode options

In general, you can specify options in any order. The exception is when you add more
than one triage store within a single command. In this case, you must specify the
options for the properties of each new triage store at the same time.

The OTHER option listed in the synopsis refers to sets of command
line options that are common to all modes. The options are:

- Common OUTPUT options
- CONNECTION options
- Shared
  options

OPERATION options
:   Specify exactly one OPERATION option in Triage mode.

    --show
    :   Output a comma separated value (CSV) list of triage stores and their descriptions that match the
        filter criteria. Use the --fields option to control the display of the
        triage store fields and their order. FILTER options are not
        required with `--show`.

    --add
    :   Add new triage stores. A minimum of one triage store name is
        required for each triage store that you add.

        You can add multiple triage stores with a single command by
        specifying groups of SET options for each new triage
        stores.

    --delete
    :   Delete the triage stores that match the name you specify.

    --update
    :   Update the name or description of the triage store that match
        the filter criteria. At least one FILTER option and one SET
        option is required.

FILTER options
:   FILTER options focus the set of triage stores that are operated on. You
    can specify multiple instances of each filter.

    --name glob
    :   Operate on a triage store, or triage stores, that match the
        name.

SET options
:   The SET options apply changes to triage store names and descriptions. Use `--add`
    to create a new triage store or description, or
    `--update` to update the triage store. At least one
    SET option is required with `--update`.

    --set name:name
    :   Specify a name for a new triage store with the `--add OPERATION` option. This
        option is required for each triage store added with
        `--add`. For example

        `--add --set name:triagestore1`

        Update the name of an existing triage store using the `--update
        OPERATION` option. For example:

        `--update --name triagestore1 --set
        name:triagestore2`

        Names must be between 1 and 256 characters and are case
        sensitive. Names can not contain the following characters:

        - `:` (colon)
        - `*` (asterisk)
        - `/` (forward slash)
        - `\` (backslash)
        - `` ` `` (backtick)
        - `'` (single quote)
        - `"` (double quote)

    --set {description|desc}:description
    :   Specify an optional description for a new triage store using the `--add OPERATION`
        option, or update the description of a triage stream using
        the `--update OPERATION` option.

## Triage mode examples

The first example shows the four connection options that must contain values either
on the command line, or in the XML configuration file (host, port, user, password).
These connection options are intentionally dropped from most of the subsequent
examples to reduce the length of the command lines. When the connection options are
not specified, assume that the values are retrieved from the default XML
configuration file.

**Show examples**

Show all triage stores and descriptions.

```
> cov-manage-im --host cim.company.com --port 8080 --user test \
    --password secret --mode triage --show
```

Show individual triage store named mytriagestore .

```
> cov-manage-im --mode triage --show --name mytriagestore
```

**Add examples**

Add a new triage store and description.

```
> cov-manage-im --mode triage --add \
    --set name:mytriagestore \
    --set desc:"This is my new triage store"
```

**Update examples**

Change a triage store name and its description.

```
> cov-manage-im --mode triage --update --name mytriagestore \
    --set name:yourtriagestore \
    --set desc:"This is your new triage store"
```

**Delete example**

Delete the store triage named yourtriagestore (it can only be
deleted if it does contain any streams)

```
> cov-manage-im --mode triage --delete --name yourtriagestore
```
