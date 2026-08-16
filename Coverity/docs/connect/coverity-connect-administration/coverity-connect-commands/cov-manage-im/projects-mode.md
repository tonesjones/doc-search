---
title: "Projects mode"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/projects-mode.html"
content_id: "AN6EIBlxiCK08UvWZkwPdQ"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:51:33.414316+00:00"
---

# Projects mode

Query, add, delete, and update projects in Coverity Connect.

## Synopsis

```
--mode projects --show [<FILTER>] [<OUTPUT>] [<OTHER>]
				
--mode projects --add <SET> [<OTHER>]

--mode projects --delete <FILTER> [<OTHER>]

--mode projects --update <FILTER> <SET> [<OTHER>]

--mode projects --update <FILTER> <REMOVE> [<OTHER>]
```

## Projects mode options

In general, you can specify options in any order. The exception is when you add more
than one project within a single command. In this case, you must specify the options
for the properties of each new project at the same time.

The OTHER option listed in the synopsis refers to sets of command
line options that are common to all modes. The options are:

- Common OUTPUT options
- CONNECTION options
- Shared
  options

OPERATION options
:   Specify exactly one OPERATION option.

    --show
    :   Output a comma separated value (CSV) list of projects that match the filter criteria. Use the
        --fields option to control the display of the
        project fields and their order. FILTER options are not
        required with `--show`.

    --add
    :   Add one or more new projects. A project name is required for
        each project that is added. You can add multiple projects
        with a single command line by specifying groups of SET
        options for each new project.

    --delete
    :   Delete the project or projects that match the filter
        criteria. At least one FILTER option is required.

    --update
    :   Update the attributes of projects that match the filter
        criteria. At least one FILTER option and one SET/REMOVE
        option is required.

FILTER options
:   FILTER options focus the set of projects that are operated on. You can specify multiple instances
    of each filter, except for `--name` and
    `--description`.

    If you specify multiple instances of the same filter, the values are
    effectively ORed together. Different filter options are effectively
    ANDed together. For example, `--stream a --stream b --description
    c --description d` matches projects of the criteria
    `(stream = a OR b) AND (description = c OR d)`.

    The FILTER options are:

    --name glob
    :   Operate on a project, or projects, whose name matches the
        specified glob pattern.

    --description|--desc glob
    :   Operate on a project, or projects, whose description matches
        the specified glob pattern.

    --stream glob
    :   Operate on projects that are associated with a stream whose
        name matches the glob pattern.

OUTPUT options
:   OUTPUT options are not required and are only valid with the `--show`
    operation.

    The OUTPUT options are:

    --output fields
    :   Display the list of valid field names for the Projects mode.
        The field names can then be used with the --fields option.

    --output streams
    :   Display information about each stream associated with the
        project, rather than the information about the project
        itself.

    Output Options
    :   You can also specify Output options that are common to all modes.

SET options
:   The SET options apply changes to project attributes. Use `--add` to set the
    attributes of new projects, or `--update` to update the
    attributes of existing projects. At least one SET option is required
    with `--update`.

    --set name:name
    :   Specify a name for a new project with the `--add OPERATION` option. This option is
        required for each project being added with
        `--add`. For example:

        `--add --set name:Project1`

        Update the name of an existing project using the `--update OPERATION`
        option. For example:

        `--update --name A --set name:B`

        Important: Project names are
        case-sensitive and must be 1 - 256 characters. Project names
        can NOT contain the following special characters:

        - `:` (colon)
        - `*` (asterisk)
        - `/` (forward slash)
        - `\` (back slash)
        - `` ` `` (backtick)
        - `'` (single quote)
        - `"` (double quote)

    --set {description|desc}:description
    :   Specify a description for a new project using the `--add OPERATION` option, or
        update the description of an existing project using the
        `--update OPERATION` option.

    --insert stream:name
    :   Associate an existing stream with a new project using the `--add OPERATION`
        option, or with an existing project using the
        `--update OPERATION` option.

        This option does not create the specified stream, or streams. The streams must already
        exist in Coverity Connect. You can specify multiple
        `--insert stream` options to associate
        multiple streams with a project with a single command.

        A stream has two types of associations with a project:

        - Primary, in which a given stream is associated
          with a designated primary project.
        - Linked, in which a non-primary project is
          associated with the given project through a stream
          link.

        See "Working with projects and streams"
        in Coverity Platform 2026.6.0 User and Administrator Guide for
        more information about primary projects and stream
        links.

        When a stream is associated with a primary project
        (ProjectA) and then inserted into
        another project (ProjectB), its
        association with ProjectA is changed
        from a primary association to a stream link.
        ProjectB becomes the stream's
        primary project. Although `cov-manage-im`
        cannot explicitly create stream links, this mechanism can be
        used to create a stream link.

        To help you locate primary and linked associations, stream listings in Streams mode have
        a column called Primary Project. This
        column contains the name of the primary project that is
        associated with the stream (if any). Additionally, in
        Projects mode, you can specify
        `is-stream-linked` in the --fields option. This produces a column that
        displays yes if the stream has a linked
        association, or no if it has a primary
        association.

REMOVE options
:   The REMOVE options remove stream associations from projects. Remove
    options work for both primary and linked streams.

    These options are only valid with the `--update OPERATION` option.

    At least one FILTER option must be specified to prevent accidental bulk
    removals.

    The REMOVE options are:

    --remove stream:name
    :   Remove a stream association from the specified projects.
        Streams are not removed from the Coverity Connect. Only the
        project's association with the stream is removed.

        The name argument must exactly match a
        stream name.

        You can specify multiple `--remove stream` options.

    --clear streams
    :   Remove all stream associations from the selected
        project(s).

## Projects mode examples

The first example shows the four connection options that must contain values either
on the command line, or in the XML configuration file (host, port, user, password).
These connection options are intentionally dropped from most of the subsequent
examples to reduce the length of the command lines. When the connection options are
not specified, assume that the values are retrieved from the default XML
configuration file.

**Show examples**

Show all projects.

```
> cov-manage-im --host cim.company.com --port 8080 --user test \
					--password secret --mode projects --show
```

Show all projects that contain a stream named x or
y.

```
> cov-manage-im --mode projects --show --stream x --stream y
```

List the fields that can be passed to `--fields` in projects mode.

```
> cov-manage-im --mode projects --show --output fields
```

Next, control what fields are shown by specifying some of these fields with the
`--fields` option.

```
> cov-manage-im --mode projects --show --fields project
```

Show stream associations for all projects.

```
> cov-manage-im --mode projects --show --output streams
```

Show stream associations for projects where the project name starts with 'a'.

```
> cov-manage-im --mode projects --show --output streams --name "a*"
```

**Add examples**

Add a new project with minimal attributes specified.

```
> cov-manage-im --mode projects --add --set name:"HelloWorld"
```

Add a new project with all attributes specified

```
> cov-manage-im --mode projects --add \
--set name:"hello world" \
--set desc:"A full project" \
--insert stream:mystream
```

Add two new projects at the same time.

```
> cov-manage-im --mode projects --add \
--set name:proj1 \
--set desc:"First project" \
--insert stream:mystream   \
--set name:proj2 \
--set desc:"Second project"
```

**Delete examples**

Delete a project named old-project.

```
> cov-manage-im --mode projects --delete --name old-project
```

**Update examples**

Rename project A to B and update
description at the same time.

```
> cov-manage-im --mode projects --update --name A \
	--set name:B --set "desc:This is now a B project"
```

Add stream associations to project P's existing stream
associations.

```
> cov-manage-im --mode projects --update --name P \
	--insert stream:x
```

Remove all stream associations named x from project
P.

```
> cov-manage-im --mode projects --update --name P --remove stream:x
```

Remove all stream associations from project P

```
> cov-manage-im --mode projects --update --name P \
	--clear streams
```
