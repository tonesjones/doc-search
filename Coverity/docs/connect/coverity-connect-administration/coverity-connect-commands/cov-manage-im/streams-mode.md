---
title: "Streams mode"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/streams-mode.html"
content_id: "MTY6fP8~4Ldfh2HYJB6n2w"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:51:34.109377+00:00"
---

# Streams mode

Query, add, delete, and update streams in Coverity Connect.

## Synopsis

```
--mode streams --show [<FILTER>] [<OUTPUT>] [<OTHER>]

--mode streams --add <SET> [<OTHER>]

--mode streams --delete <FILTER> [<OTHER>]

--mode streams --update <FILTER> <SET> [<OTHER>]
```

## Streams mode options

In general, you can specify options in any order. The exception is when you add more
than one stream within a single command. In this case, you must specify the options
for the properties of each new stream at the same time.

The OTHER option listed in the synopsis refers to sets of command
line options that are common to all modes. The options are:

- Common OUTPUT options
- CONNECTION options
- Shared
  options

OPERATION options
:   Specify exactly one OPERATION option in Streams mode.

    --show
    :   Output a comma separated value (CSV) list of streams that
        match the filter criteria. Use the --fields option to control the display of the
        stream fields and their order. FILTER options are not
        required with `--show`.

    --add
    :   Add new streams. A minimum of one stream name is required for
        each stream that you add.

        You can add multiple streams with a single command by
        specifying groups of SET options for each new stream.

    --delete
    :   Delete the streams that match the filter criteria. At least
        one FILTER option is required.

    --update
    :   Update the name or description of the streams that match the
        filter criteria. A stream's language can not be updated
        after a stream has been created. At least one FILTER option
        and one SET option is required.

FILTER options
:   FILTER options focus the set of streams that are operated on. You can
    specify multiple instances of each filter, except for
    `--name` and `--description`.

    If you specify multiple instances of the same filter, the values are
    effectively ORed together. Different filter options are effectively
    ANDed together. For example, `--project a --project b --language
    c --language d` matches streams of the criteria
    `(project = a OR b) AND (language = c OR d)`.

    --name glob
    :   Operate on a stream, or streams, whose name matches the glob
        pattern.

    --language|--lang lang
    :   Operate on a stream, or streams, based on language. lang can
        be one of:

        - `C/C++, cpp`
        - `Java, java`
        - `C#, cs`
        - `dynamic_java`
        - `Mixed, mixed`
        - Other, other

    --description|--desc glob
    :   Operate on a stream, or streams, whose description matches
        the glob pattern.

    --stream glob
    :   Operate on a stream, or streams, whose name matches the glob
        pattern.

    --project glob
    :   Operate on streams that are associated with projects whose
        name matches the glob pattern.

OUTPUT options
:   OUTPUT options are optional and are valid only with the `--show` option.

    --output fields
    :   Display the list of valid field names for this mode. These
        field names can then be used with the --fields option.

    Output Options
    :   You can also specify Output options that are common to all modes.

SET options
:   The SET options apply changes to stream attributes. Use `--add` to set the
    attributes of new streams, or `--update` to update the
    attributes of existing streams. At least one SET option is required with
    `--update`.

    --set {component-map|cmap}:component-map
    :   Specify a component map to associate with a stream using the
        `--add OPERATION` option.

    --set {description|desc}:description
    :   Specify a description for a new stream using the
        `--add OPERATION` option, or update the
        description of a stream using the `--update
        OPERATION` option.

    --set desktopAnalysis:{disabled|enabled}
    :   This option allows (or prohibits) the stream to provide data
        for Desktop Analysis. Only streams that have specifically
        enabled Desktop Analysis can be used as reference streams
        for Desktop Analysis users.

        To set this option for newly created streams, use
        `--add`, for example `--mode
        streams --add --set
        desktopAnalysis:enabled`.

        To set this option for existing streams use
        `--update`, for example `--mode
        streams --update --set
        desktopAnalysis:enabled`.

        These options are disabled by default.

        For more information, see the Coverity Platform 2026.6.0 User and Administrator Guide.

    --set expiration:{disabled|enabled}
    :   This option allows you to set Coverity Connect to
        automatically delete streams after a period of inactivity.
        Only streams that are specifically configured for this
        feature are eligible for automatic deletion.

        To set this option for newly created streams, use
        `--add`, for example `--mode
        streams --add --set expiration:enabled`.

        To set this option for existing streams use
        `--update`, for example `--mode
        streams --update --set expiration:enabled`.

        These options are disabled by default.

        For more information, see "Designating a stream for auto-deletion of expired streams" in the Coverity Platform 2026.6.0 User and Administrator Guide.

    --set {language|lang}: lang
    :   Specify a language for a new stream using the `--add
        OPERATION` option. `--set
        language` can be used for each stream you add.
        If you do not set a language for the stream, it defaults to
        `mixed`. You can not update the language
        of an existing stream with this option. You should choose
        the default (mixed) for each new stream that you create. The
        other languages are provided for backward compatibility for
        previously released Coverity Connect versions (in which
        implicitly designated languages were required for streams).
        The valid languages are:

        - `Mixed, mixed`
        - `C/C++, cpp`
        - `Java, java`
        - `C#, cs`
        - `dynamic_java`
        - `Other, other`

          Note: `Other` can be used when
          creating a stream with the
          `--add` option.
          `Other` is among the languages that
          may be shown when displaying a stream with the
          `--show` option.

    --set name:name
    :   Specify a name for a new stream with the `--add
        OPERATION` option. This option is required for
        each stream added with `--add`. For
        example

        `--add --set name:Stream1`

        Update the name of an existing stream using the
        `--update OPERATION` option. For
        example:

        `--update --name A --set name:B`

        Important: Stream names are
        case-sensitive and must be 1 - 256 characters. Stream names
        can NOT contain the following special characters:

        - `:` (colon)
        - `*` (asterisk)
        - `/` (forward slash)
        - `\` (back slash)
        - `` ` `` (backtick)
        - `'` (single quote)
        - `"` (double quote)

    --set ownerAssignmentOption:{default_component_owner|scm|none}
    :   This option allows you to set owner assignment options for a
        stream. If you do not set the
        `ownerAssignmentOption` for the stream,
        it defaults to default_component_owner.
        You can update this value to any of the entries mentioned
        above.

    --set triage:triage-store
    :   Specify a triage store to which the stream will belong. If
        the triage store is not specified, it defaults to the
        default triage store.

## **Streams mode examples**

The first example shows the four connection options that must contain values either
on the command line, or in the XML configuration file (host, port, user, password).
These connection options are intentionally dropped from most of the subsequent
examples to reduce the length of the command lines. When the connection options are
not specified, assume that the values are retrieved from the default XML
configuration file.

**Show examples**

Show all streams.

```
> cov-manage-im --host cim.company.com --port 8080 --user test \
	--password secret --mode streams --show
```

Show all streams whose name starts with "linux-".

```
> cov-manage-im --mode streams --show --name "linux-*"
```

Show all streams whose language is Java.

```
> cov-manage-im --mode streams --show --lang Java
```

List the fields that can be passed to `--fields` in streams mode.

```
> cov-manage-im --mode streams --show --output fields
```

Control the fields that are shown by specifying some of these fields with the
`--fields` option.

```
> cov-manage-im --mode streams --show  \
	--fields stream,language,desktop-analysis
```

Displays the attributes of stream mystream, including the
stream's language, `other`.

```
> cov-manage-im --mode streams --show  \
	--name mystream
```

**Add examples**

Add a new C/C++ stream with minimal attributes specified.

```
> cov-manage-im --mode streams --add \
	--set name:HelloWorld \
	--set lang:mixed \
	--set triage:mytriagestore
```

Add a new stream with all attributes specified, and desktop analysis enabled.

```
> cov-manage-im --mode streams --add \
	--set name:HelloWorld \
	--set lang:mixed \
	--set triage:mytriagestore \
	--set "desc:My stream" \
	--set desktopAnalysis:enabled
```

Add two new streams at the same time

```
> cov-manage-im --mode streams --add \
	--set name:stream1 \
	--set lang:mixed \
	--set desc:"My new stream" \
	--set triage:mytriagestore \
	--set name:stream2 \
	--set desc:"My other new stream" \
	--set triage:mytriagestore
```

Associate the stream1 stream with the
component1 component map.

```
> cov-manage-im --mode streams --update --name stream1 \
	-- set component-map:component1
```

Adds a new stream with `other`.

```
> cov-manage-im --mode streams --add --set --name:mystream \
	lang:other --set triage:mytriagestore
```

**Delete examples**

Delete the stream named old-stream (it can only be deleted if
defects have NOT yet been committed).

```
> cov-manage-im --mode streams --delete --name old-stream
```

**Update example**

Rename stream A to B and update description
at the same time.

```
> cov-manage-im --mode streams --update --name A \
	--set name:B --set "desc:This is now a B stream"
```
