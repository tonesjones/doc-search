---
title: "Defects mode"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/defects-mode.html"
content_id: "kuA9s6~C1Q0_MzDR~S3KKw"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:51:32.700243+00:00"
---

# Defects mode

Query and update defects in Coverity Connect.

## Synopsis

```
--mode defects --show SCOPE [FILTER] [OUTPUT] [OTHER]

--mode defects --update SCOPE [FILTER] SET [OTHER]
```

## Defects mode options

In general, you can specify options in any order. The exception is when you add more
than one project or stream within a single command. In this case, you must specify
the options for the properties of each new stream or project at the same time.

The OTHER option listed in the synopsis refers to sets of command
line options that are common to all modes. The options are:

- Common OUTPUT options
- CONNECTION options
- Shared
  options

OPERATION options
:   Exactly one OPERATION option is required:

    --show
    :   Output a comma separated value (CSV) list of defects from the
        specified scope that matches the filter criteria. Use the
        --fields option to control the display of the
        defect fields and their order.

    --update
    :   Update attributes of defects from the specified scope that
        match the filter criteria. At least one SET option is
        required. FILTER options are not required.

SCOPE
:   Define the project or the set of streams to show or update. All defect
    operations require a scope definition.

    When the same defect occurs in multiple streams, and a project scope is
    specified, the defects are represented as a merged
    defect for display and filtering purposes. For example,
    if the same defect occurs in two separate streams, and the action
    attribute values are different, Coverity Connect calculates a merged
    action. The merged action is then displayed for the merged defect.
    FILTER options match against the merged defect.

    The SCOPE options are:

    --project name
    :   Specify the name of a project that contains the defects that
        you want to show or update. You can only scope for one
        project.

    --stream name
    :   Specify the name of a stream, or streams.

FILTER
:   FILTER options focus the set of defects in the given scope that will be operated on. You can
    specify multiple instances of each filter, with the exception of the
    `--file` and `--function` filters,
    which you can only specify once.

    If you specify multiple instances of the same filter, the values are
    effectively ORed together. Different filter options are effectively
    ANDed together. For example, `--action a --action b --severity c
    --severity d` matches defects of the criteria
    `(action = a OR b) AND (severity = c OR d)`.

    The FILTER options are:

    --cid cid-set
    :   Operate on a single CID or set of CIDs.
        cid-set can be:

        - A single CID. For example, `--cid
          10118`.
        - A range of CIDs. Denote range with a hyphen
          (`-`). For example, -`-cid
          10203-10209`.
        - A comma-separated list of single CIDs and ranges of
          CIDs. For example, `--cid
          10118,10119,10203-20109,10388`.

    --action action
    :   Operate on defects whose action attribute value exactly
        matches the action string. Valid strings
        match the list of Action values on the Coverity Connect
        Attribute Details screen. The
        standard (unedited) values in Coverity Connect are:

        - Undecided
        - Fix Required
        - Fix Submitted
        - Modeling Required
        - Ignore

        Use Various for action to select merged
        defects that have different action attribute values.

    --classification|--class class
    :   Operate on defects whose classification attribute value
        exactly matches the class string.

        class must be one of the following:

        - Unclassified
        - Pending
        - False Positive
        - Intentional
        - Bug
        - Various

        Use Various for classification to select
        merged defects that have different classification attribute
        values.

    --severity severity
    :   Operate on defects whose severity attribute value exactly
        matches the severity string. Valid
        strings match the list of severity levels on the Coverity
        Connect Attribute Details screen. The
        standard (unedited) values in Coverity Connect are:

        - Unspecified
        - Major
        - Moderate
        - Minor

        Use Various for severity to select merged
        defects that have different severity attribute values.

    --status status
    :   Operate on defects whose status attribute value exactly
        matches the status string.

        status must be one of the following:

        - New
        - Triaged
        - Dismissed
        - Fixed

    --component comp_map_name.comp_name
    :   Operate on defects found by a specified component name. The
        name of the component map and component must match the
        comp_map_name.comp_name
        string.

    --component-not comp_map_name.comp_name
    :   Causes defects found by a specified component name to be
        excluded from the result. The name of the component map and
        component must match the
        comp_map_name.comp_name
        string. You can specify multiple component names.

    --checker checker
    :   Operate on defects found by a specific checker. The name of
        the checker must match the checker
        string. For example:

        `--checker FORWARD_NULL`

    --external-reference|--ext-ref ext-reference
    :   Operate on defects whose external reference exactly matches
        the ext-reference string.

    --language|--lang lang
    :   Operate on a stream, or streams, based on language. lang can
        be one of:

        - `C/C++, cpp`
        - `Java, java`
        - `C#, cs`
        - `dynamic_java`
        - `Mixed, mixed`
        - Other, other

    --mergekey mergekey
    :   Operate on defects whose mergekey exactly matches the
        mergekey string. You may specify
        multiple mergekeys in a comma-separated list.

    --owner owner
    :   Operate on defects whose owner exactly matches the
        owner string.

        Use `Unassigned` for owner
        to update defects that are not yet assigned.

    --file file
    :   Operate on defects whose file matches the
        file glob pattern.
        file refers to the terminal part of a
        filename, not a full path. You can specify this option only
        once.

        The glob file
        pattern refers to the entire pathname.
        Pathnames are separated by a slash on all platforms. For
        example, --file *.java will match all
        Java files, and --file Win.java will
        match only Win.java at the root of the
        source tree. But --file */Win.java will
        match all files named Win.java in all
        directories.

    --function function
    :   Operate on defects whose function matches the
        function glob pattern. You can
        specify this option only once.

    --legacy status
    :   Operate on defects whose legacy status matches the
        status string. Legacy status can be
        any of the following values:

        - `True`
        - `False`
        - `Various`

    --newest [snapshotId]
    :   Operate on defects which occur only in the project's most
        recent snapshot.

        An optional parameter, [snapshotId], will compare the newest
        snapshot with the older specified snapshot. The snapshot ID
        number must match the number in [snapshotId] exactly.

OUTPUT options
:   OUTPUT options are not required and are only valid with the `--show` option.

    --newest [snapshotId]
    :   Outputs those defects which occur only in the project's most
        recent snapshot.

        An optional parameter, [snapshotId], will compare the newest
        snapshot with the older specified snapshot. The snapshot ID
        number must match the number in [snapshotId] exactly.

    --output fields
    :   Display the list of valid field names for this mode. These
        field names can then be used with the --fields option.

    --page
    :   Sets the number of defects that are pulled per batch. The
        default number of defects is 100. If you set the
        `--page` option to 1000 then there will
        be fewer queries and performance can improve. For example,
        by setting the `--page` option to 1000 you
        will get 20 queries rather than 200, so you will get 10
        times fewer.

        Example:

        ```
        cov-manage-im --host localhost --port 8080 --user admin --password coverity --mode defects --show --project foo --page 1000
        ```

    Output options
    :   You can also specify Output options that are common to all modes.

SET options
:   SET options update defect attributes of the selected defects defined with the FILTER options. You
    can use only one `--set` option for each defect
    attribute, such as action, severity, classification, and so forth.
    However, you can specify `--set` options for different
    defect attributes on the same command line.

    --set action:action
    :   Set the action defect attribute for defects that match the
        filter criteria to action. The action
        attribute used for action must already
        exist in the Coverity Connect database.

    --set {classification|class}:class
    :   Set the classification attribute of defects that match the
        filter criteria to class.

        The class string must be one of the
        following:

        - Unclassified
        - Pending
        - False Positive
        - Intentional
        - Bug

    --set severity:severity
    :   Set the severity defect attribute of defects that match the
        filter criteria to severity. The severity
        attribute used for severity must already
        exist in the Coverity Connect database.

    --set owner:owner
    :   Set the owner of defects that match the filter criteria to
        owner. The owner attribute used for
        owner must already exist in the
        Coverity Connect database.

    --set comment:comment
    :   Add a comment to the defects that match the filter
        criteria.

    --set {ext-ref|external-reference}:reference
    :   Add an external reference to the defects that match the
        filter criteria.

    --set legacy:status
    :   Set the legacy status for the defect. The acceptable values
        are:

        - `True`
        - `False`

## Defects mode examples

The first example shows the four connection options that must contain values either
on the command line, or in the XML configuration file (host, port, user, password).
These connection options are intentionally dropped from most of the subsequent
examples to reduce the length of the command lines. When the connection options are
not specified, assume that the values are retrieved from the default XML
configuration file.

**Show examples**

Show all (merged) defects in project X.

```
> cov-manage-im --host cim.company.com --port 8080 --user test \
				--password secret --mode defects --show --project X
```

Show all open defects in project X

```
> cov-manage-im ---mode defects --show --project X \
				--status New --status Triaged
```

Show all defects with the specified mergekey in the stream named
Y.

```
> cov-manage-im --mode defects --show --stream Y --mergekey 46941efa13559f40754b0d90dd99f2d2
```

List the defect fields that can be passed to --fields in defects
mode.

```
> cov-manage-im --mode defects --show --project P --output fields
```

Control what defect fields are shown by specifying some of these fields with the
--fields option.

```
> cov-manage-im --mode defects --show --project P \
				--fields cid,action,severity
```

Show particular (merged) defects in project X, filtering with
different CID specifiers.

```
> cov-manage-im --mode defects --show --project X --cid 123
				> cov-manage-im --mode defects --show --project X --cid 123,456
				> cov-manage-im --mode defects --show --project X --cid 1-4
				> cov-manage-im --mode defects --show --project X --cid 1-4,18,25-30
```

Show all Triaged defects in stream Y that are classified as
Bugs.

```
> cov-manage-im --mode defects --show --stream Y \
				--status Triaged --class Bug
```

Show all open defects in stream Y with no owner.

```
> cov-manage-im --mode defects --show --stream Y \
				--status New --status Triaged --owner Unassigned
```

Show all open defects in "client" source files.

```
> cov-manage-im --mode defects --show --stream Y \
				--status New --status Triaged --file "client-*.c"
```

Show all open defects listed by CID in all components.

```
cov-manage-im --mode defects --show --project project1 \ 
				--fields cid,component
```

**Update examples**

Assign all unassigned defects in streams X and
Y to jdoe

```
> cov-manage-im --mode defects --update --stream X \
				--stream Y --owner Unassigned --set owner:jdoe
```

Set the classification of CID 10002 in project P to False
Positive.

```
> cov-manage-im --mode defects --update --project P \
				--cid 10002 --set "class:False Positive"
```

Set all the attributes of CID 10002 in project P.

```
> cov-manage-im --mode defects --update --project P \
				--cid 10002 --set "action:Fix Required" --set class:Bug \
				--set severity:Major --set owner:jdoe \
				--set "comment:This appears to be real." \
				--set ext-ref:yyy
```

Set the classification of defects with the specified mergekey in stream
Y to False Positive.

```
> cov-manage-im --mode defects --update --stream Y \
				--mergekey 46941efa13559f40754b0d90dd99f2d2 --set "class:False Positive"
```

Mark all defects in MyStream which were introduced in the most
recent snapshot as Legacy=true.

```
> cov-manage-im --mode defects --stream MyStream --update --newest --set legacy:True
```

Mark all defects in MyStream which were introduced after
snapshot 10006 as Legacy=true.

```
> cov-manage-im --mode defects --stream MyStream --update --newest 10006 --set legacy:True
			
```
