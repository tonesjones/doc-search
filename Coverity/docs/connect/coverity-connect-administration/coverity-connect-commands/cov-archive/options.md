---
title: "Options"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/options.html"
content_id: "8E3GVC83xvKIC7fU8bjmkQ"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:51:17.313964+00:00"
---

# Options

--archive archive-file
:   The path of the file to which you are exporting or from which you are importing.
    The path is either absolute or relative to the shell's current working
    directory.

--cluster-config cluster-config-file
:   The path to the cluster config file. The path is either absolute or relative to
    the shell's current working directory. This file is created as a result of
    completing the first step of the two-step import into a subscriber Coverity
    Connect instance and is required to do the second step. This option must be
    specified for each of the two steps. If this option is not specified when the
    command is executed on the coordinator (step one), then the command imports an
    archive into the coordinator instead of producing a cluster config file.

    Importing into a standalone/coordinator Coverity Connect instance is a
    straightforward action. Importing into a subscriber Coverity Connect
    instance is a two-step process.

    Step one is executed on the coordinator instance in the Coverity Connect
    cluster that contains the target subscriber instance and produces a cluster
    config file required to do the second step.

    Step two is executed on the target subscriber instance only after this
    instance catches up with the changes introduced on the coordinator by the
    first step. These changes are specified by the cluster config file.
    Importing is refused if the data specified in the file is not present in the
    target subscriber. You may see whether the subscriber caught up with its
    coordinator by navigating to Help > System Diagnostics > Cluster and looking at the "Last synchronized" timestamp.

    Note: Having the same streams in different Coverity Connect instances in a cluster is allowed. This means that streams from the
    archive are allowed to exist in the coordinator when doing step one, and the
    streams existing in the coordinator are allowed to be imported to its
    subscriber when doing step two.

    Before deciding to import into a coordinator/subscriber instance you should
    make sure that the data replication between them is happening successfully.
    This can be done informally by checking that the aforementioned "Last
    synchronized" timestamp is not too old, e.g., that its value is within the
    last 24 hours. Do not import into a coordinator/subscriber if there appears
    to be an issue with the data replication process between them because doing
    so may only further complicate the issue.

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

export-streams
:   cov-archive export-streams produces archives in BIS
    (binary) format.
:   The 2026.6.0 release introduces the BIS data format. The following table
    identifies the data format behavior supported by cov-archive
    export-streams before and after the 2026.6.0 release.

    | Behavior | Legacy pre-2026.6.0 | 2026.6.0 and newer |
    | --- | --- | --- |
    | Archive format produced | V1 ZIP/CSV | BIS is the new default archive format. |
    | Staging schema | Huge temp export schema created then dropped | Eliminated — streams directly from the source database |
    | OID columns (architecture_data, snapshot, etc.) | Raw OID numbers copied — orphaned references in target | Zeroed/nulled at export — no orphaned `pg_largeobject` entries |

    The cov-archive export-streams command-line flags have not
    changed. BIS format is produced automatically.

help
:   The cov-archive help command returns command option help.
    This is the default value if no subcommand option is specified..

import-streams
:   The cov-archive import-streams command automatically
    detects the archive format and handles both BIS and legacy V1 ZIP/CSV
    archives transparently.

    - cov-archive help returns command option help.
      This is the default value if no subcommand option is specified.
:   The 2026.6.0 release introduces the BIS data format. The following table
    identifies the data format behavior supported by cov-archive
    import-streams before and after the 2026.6.0 release.

    | Behavior | Legacy pre-2026.6.0 | 2026.6.0 and newer |
    | --- | --- | --- |
    | Supported archive format | - V1 ZIP/CSV only | - BIS (default) - V1 ZIP/CSV supported |

    The cov-archive import-streams command-line flags
    have not changed. BIS format is used by default, however, V1 ZIP/CSV is
    still supported for backward compatibility.

inspect-bis --archive <path-to-bis-archive>
:   **What it does:** Displays a human-readable summary of a BIS archive file
    without requiring a database connection or server running. Useful for
    verifying archive contents before importing, checking which streams are
    included, and confirming the archive's source schema version.

    **Does not require:**
    `--host`, `--port`, `--db`, or
    any database credentials.

    **When to use:**

    - Before importing an archive, to verify it contains the expected
      streams.
    - When receiving an archive from another team or customer to inspect
      its provenance (source version, stream names, row counts).
    - To troubleshoot a failed import by confirming the archive is
      well-formed.

    **Example output**

    ```
    BIS Archive: /Users/ssajith/BDREPO/My MarkDown/cov0archive/V2/archives/halon.arch.new4
      Version:    3
      Timestamp:  2026-04-15T10:17:02.339Z
      Tables:     49
      File size:  8.4 GB
    #     Table Name                                      Rows          ID Min          ID Max  Type      Compressed
    ----  ----------------------------------------  ----------  --------------  --------------  --------  ----------
    1     analysis_summaries_instance                  5556399        10012002       384631639  NORMAL      134.5 MB
    2     architecture_data                                  0               0               0  NORMAL          23 B
    3     attribute_definition                               0               0               0  SHARED          23 B
    4     checker                                          177           10001           11187  SHARED        2.8 KB
    5     checker_category                                  27               1           10007  SHARED         488 B
    6     checker_descriptions                             188               7           19246  SHARED       19.5 KB
    7     checker_properties                               185               2           12921  SHARED        7.2 KB
    8     checker_type                                     180               2           13284  SHARED        3.1 KB
    .....
    METADATA
    {
      "id" : "d97314b2-1d65-4ca2-a753-1cef0fd33f3e",
      "version" : {
        "external" : "main",
        "internal" : "ad20572b36e im-main-push-2686-6-gad20572b36e-dirty",
        "schema" : 2025120101
      },
      "timestamp" : "2026-04-15T10:17:02.339183Z",
      "comment" : null,
      "latestSnapshotTimestamp" : "2021-03-29T22:58:20.156Z",
      "numberOfStreams" : 11,
      "streams" : [
        {
          "name" : "halon-bristol-master",
          "uuid" : "910006da-88ba-41d0-96b2-b0656f2a0594",
          "description" : "",
          "latestSnapshotTimestamp" : "2021-03-29T21:55:44.204Z",
          "numberOfSnapshots" : 54
        },
    }
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
    are going to delete large number of streams. See Coverity Platform 2026.6.0 User and Administrator Guide for more details about this
    property.

repair-connect-schema
:   *(Uses the same database connection config as other subcommands:*`--host`, `--port`,
    `--db`, etc.)

    **What it does:** Repairs a Coverity Connect database left partially
    degraded by an interrupted BIS import or as a standalone repair. This occurs
    if `import-streams` is forcibly terminated (killed, power
    loss, OOM) during the post-copy index rebuild, constraint cleanup, or any
    other unknown phases.

    **Symptoms that indicate repair is needed:**

    - `cov-archive import-streams` was killed or crashed,
      and the server now shows unexpected errors after restart.
    - Database contains indexes that are not yet valid (`indisvalid
      = false` in `pg_index`).
    - Foreign key constraints were left in a `DEFERRABLE`
      state (normally they are non-deferrable after import completes).

    **What it repairs:**

    1. Foreign key constraints left `DEFERRABLE` — resets to
       non-deferrable.
    2. Missing foreign key constraints — compared against the expected
       schema baseline and recreated.
    3. Invalid (`indisvalid = false`) indexes — dropped and
       rebuilt.
    4. Missing indexes — compared against the expected schema baseline and
       recreated.
    5. Mark ‘autovacuum on’ for tables where it is off.
    6. Data integrity test - Report any orphaned/corrupted data among entity
       relationship, note that corrpution could have preexisted before
       import as well.

    **Safe to run on a healthy database:** Each repair check is idempotent.
    Running `repair-connect-schema` on a healthy database reports
    no issues and makes no changes.

    **When to run:** Only needed after an unclean termination of
    `import-streams`. Normal `import-streams`
    completions (including those interrupted mid-stream by a recoverable error
    that produces a proper error message) do not leave the database in a state
    that requires repair.Running anytime helps validate the schema and generate
    a report.

--silent
:   Suppress confirmation of the action. This option may be specified only when
    using the --remove option.

--stream stream-name
:   The name of the stream you want to export. You must specify either a project or
    a stream; you may specify both project and stream names.
