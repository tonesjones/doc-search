---
title: "Options"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/options.html"
content_id: "8E3GVC83xvKIC7fU8bjmkQ"
version: "2026.9"
section: "Coverity Connect"
scraped_at: "2026-10-04T23:33:16.025431+00:00"
---

# Options

--archive archive-file
:   The path of the file to which you are exporting or from which you are importing.
    The path is either absolute or relative to the shell's current working
    directory.

--cluster-config cluster-config-file
:   The path to the cluster config file. The path is either absolute or
    relative to the shell's current working directory. This file is created
    as a result of completing the first step of the two-step import into a
    subscriber Coverity Connect instance and is required to do the second
    step. This option must be specified for each of the two steps. If this
    option is not specified when the command is executed on the coordinator
    (step one), then the command imports an archive into the coordinator
    instead of producing a cluster config file.

    Importing into a standalone/coordinator Coverity Connect instance is a
    straightforward action. Importing into a subscriber Coverity Connect
    instance is a two-step process.

    Step one is executed on the coordinator instance in the Coverity Connect
    cluster that contains the target subscriber instance and produces a
    cluster config file required to do the second step.

    Step two is executed on the target subscriber instance only after this
    instance catches up with the changes introduced on the coordinator by
    the first step. These changes are specified by the cluster config file.
    Importing is refused if the data specified in the file is not present in
    the target subscriber. You may see whether the subscriber caught up with
    its coordinator by navigating to
    Help > System Diagnostics > Cluster
    and looking at the "Last synchronized" timestamp.

    Note:
    Having the same streams in different Coverity Connect instances in a cluster is allowed.

    This means that streams from the archive are
    allowed to exist in the coordinator when doing step one, and the streams
    existing in the coordinator are allowed to be imported to its subscriber
    when doing step two.

    Before deciding to import into a coordinator/subscriber instance you
    should make sure that the data replication between them is happening
    successfully. This can be done informally by checking that the
    aforementioned "Last synchronized" timestamp is not too old, e.g., that
    its value is within the last 24 hours. Do not import into a
    coordinator/subscriber if there appears to be an issue with the data
    replication process between them because doing so may only further
    complicate the issue.

command
:   One of the following: export-streams,
    import-streams, list or
    help.

    If nothing is specified, this option is interpreted as help.

--db-memory <number><unit> (e.g., 36GB, 512MB)
:   Allows users to specify memory of postgres DB instance and based on which
    postgres parameters (work_mem and maintenance_work_mem) will be set with
    optimal
    values.

    ```
    # Import with memory tuning
    cov-archive import-streams --archive android.arch --db-memory 36GB
    # Export with memory tuning
    cov-archive export-streams --project "my-project" --archive output.arch --db-memory 36GB
    ```

--project project-name
:   The name of the project from which you want to export streams. You must
    specify either a project or a stream; you may specify both project and
    stream names.

--remove
:   Remove the exported streams from the database, when exporting successfully
    completes.

    Note: The data belonging to the streams is deleted in the background
    while Coverity Connect is running. This does not
    prevent using the --remove option while Coverity Connect is in maintenance mode: The data will
    eventually be deleted once Coverity Connect starts.

    You can run vacuum full later if you need to
    return the freed-up storage space to the OS. We recommend setting
    cim.cleanup.stream.delay.min = 2 in
    cim.properties if you have a significantly higher
    value specified explicitly in cim.properties and you
    are going to delete large number of streams. See Coverity Platform User and Administrator Guide for more details about this
    property.

--silent
:   Suppress confirmation of the action. This option may be specified only when
    using the --remove option.

--stream stream-name
:   The name of the stream you want to export. You must specify either a project or
    a stream; you may specify both project and stream names.
