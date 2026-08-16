---
title: "Using Docker Containers - Best Practice"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/using-docker-containers-best-practice.html"
content_id: "W8YmSCcas9p4hMBUJ~zGpQ"
version: "11.5.1"
section: "Detect Integrations"
scraped_at: "2026-08-08T23:46:04.148655+00:00"
---

# Using Docker Containers - Best Practice

When running Detect for Jenkins using the *DETECT_JAR* environment variable in a pipeline that has a Docker agent, remember to mount the Detect JAR as a volume.

For example, if you've installed the jar on a node, the JAR won't be accessible from your docker agent unless you either put it somewhere you regularly
include, or if you mount the path to the jar. Refer to [Docker documentation](https://docs.docker.com/storage/bind-mounts/#choose-the--v-or---mount-flag) for more information.

This is accomplished by adding:
`-v $DETECT_JAR:$DETECT_JAR` to your Docker arguments, which is shown in the following example.

```
pipeline {
    agent {
        docker {
            ...
            args '-v $DETECT_JAR:$DETECT_JAR'
        }
    ...
...
```

Applies when running Detect for Jenkins with a local JAR (which requires setting the *DETECT_JAR* environment variable).
