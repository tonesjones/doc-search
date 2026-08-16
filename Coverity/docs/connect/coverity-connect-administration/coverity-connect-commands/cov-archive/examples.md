---
title: "Examples"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/examples.html"
content_id: "O33EFH66N8p66Yo8VS7qVg"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:51:18.575456+00:00"
---

# Examples

The following command displays the usage help for the command
export-streams:

```
cov-archive help export-streams
```

The following command exports a stream named s1 and all streams
linked to the projects named p1 and p2 to a file
../s1_p1_p2.covarch:

```
cov-archive export-streams --stream s1 --project p1 --project p2\
    --archive ../s1_p1_p2.covarch
```

The following command imports streams from the file
../s1_p1_p2.covarch and writes detailed logs:

```
cov-archive --debug import-streams --archive ../s1_p1_p2.covarch
```

The two commands that follow import streams from the file
../s1_p1_p2.covarch into a subscriber in a two-step process:

**Step one:** Execute on the coordinator:

```
cov-archive import-streams --archive ../s1_p1_p2.covarch --cluster-config ../s1_p1_p2.covclustcfg
```

**Step two:** Wait until the target subscriber catches up with the coordinator, then
execute on the subscriber:

```
cov-archive import-streams --archive ../s1_p1_p2.covarch --cluster-config ../s1_p1_p2.covclustcfg
```
