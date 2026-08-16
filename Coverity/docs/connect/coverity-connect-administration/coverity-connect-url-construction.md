---
title: "Coverity Connect URL construction"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-connect-url-construction.html"
content_id: "BVbqD4tY9Vscib8xBULdRA"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:50:51.274108+00:00"
---

# Coverity Connect URL construction

To reconstruct Coverity Connect URLs so that you can query for issues programmatically,
you can use the following query prefix followed by the parameters that you need:

`/query/defects.htm`

Supported parameters:

- `cid`
- `mergeKey`
- `outstanding`
- `preview`
- `project` or `projectId`
- `snapshotId`
- `stream`

All parameters are optional, but you must specify at least one of
`project`, `projectId`, or
`stream`. If you do not specify a project, by name or
ID, Coverity Connect will use the default project for the first named stream. Both
`project` and `stream` expect
names, while `projectId` accepts the numeric project ID. The
`stream` and `cid` parameters
can both appear multiple times. The `outstanding` parameter is
boolean (`true`/`false`); an absent value means
`false`. Only a single `mergeKey` parameter
can be specified at one time. The `preview` parameter filters out preview
issues when set to `false` (the default value) or returns them when set
to `true` (preview issues are issues whose First
Detected value is Preview, meaning that they were
first committed using the `--preview-report` option).

If a project is not specified, and the first named stream does not belong to any
projects, the URL will redirect to the Projects list. If an
unrecognized project or stream name is given, Coverity Connect will return an error
page.

**Examples:**

Show CIDs 1, 2 and 3 in project ProjectA
:   http://machine1.eng.company.com:8080/query/defects.htm?project=ProjectA&cid=1&cid=2&cid=3

Show all outstanding CIDs from streams StreamA and StreamB inside project ID 10001
:   http://machine1.eng.company.com:8080/query/defects.htm?projectId=10001&stream=StreamA&stream=StreamB&outstanding=true

Show CIDs 1, 2 and 3 from stream StreamA
:   http://machine1.eng.company.com:8080/query/defects.htm?stream=StreamA&cid=1&cid=2&cid=3

Show a single issue in project ID 10001 using the issue's mergeKey
:   http://machine1.eng.company.com:8080/query/defects.htm?projectId=10001&mergeKey=f7e9b5e82a9046ca51c136e8786c20b2

Show all outstanding issues in stream StreamA
:   http://machine1.eng.company.com:8080/query/defects.htm?stream=StreamA&outstanding=true

Show issues for the specified snapshotId
:   `/query/defects.htm?project=ProjectA&snapshotId=10040&snapshotId=10041`

    `/query/defects.htm?project=ProjectA&cid=10020&snapshotId=10040`

    You can pass multiple snapshot IDs to the URL, and you can combine the snapshot ID with
    other parameters.

Show issues (including preview issues) for the specified snapshotId
:   `/query/defects.htm?project=ProjectA&snapshotId=10040&preview=true`
