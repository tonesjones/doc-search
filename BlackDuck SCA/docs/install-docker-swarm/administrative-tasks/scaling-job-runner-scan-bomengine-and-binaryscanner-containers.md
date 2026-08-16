---
title: "Scaling job runner, scan, bomengine, and binaryscanner containers"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/scaling-job-runner-scan-bomengine-and-binaryscanner-containers.html"
content_id: "uVrSPgv8JWeuqi9Uyg0WHQ"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:33:55.315164+00:00"
---

# Scaling job runner, scan, bomengine, and binaryscanner containers

The job runner, scan, bomengine, and binaryscanner containers can be scaled.

You may need to be a user in the docker group, a root user, or have `sudo`
access to run the following command.

## Scaling bomengine containers

This example adds a second bomengine container:

```
docker service scale hub_bomengine=2
```

You can remove a bomengine container by specifying a lower number than the current
number of bomengine containers. The following example scales back the bomengine
containers to a single container:

```
docker service scale hub_bomengine=1
```

Note: Black Duck recommends that you scale bomengine containers to the same level as the jobrunner
containers.

## Scaling job runner containers

This example adds a second Job Runner container:

```
docker service scale hub_jobrunner=2
```

You can remove a job runner container by specifying a lower number than the current
number of job runner containers. The following example scales back the job runner
containers to a single container:

```
docker service scale hub_jobrunner=1
```

## Scaling scan containers

This example adds a second Scan container:

```
docker service scale hub_scan=2
```

You can remove a scan container by specifying a lower number than the current number
of scan containers. The following example scales back the scan containers to a
single container:

```
docker service scale hub_scan=1
```

## Scaling binaryscanner containers

Binaryscanner containers are used with Black Duck Binary Analysis.

This example adds a second binaryscanner container:

```
docker service scale bdba-worker=2
```

Note: An additional CPU, 2 GB RAM, and 100 GB of free disk space is needed for every additional
binaryscanner container.

You can remove a binaryscanner container by specifying a lower number than the
current number of binaryscanner containers. The following example scales back the
binaryscanner containers to a single container:

```
docker service scale bdba-worker=1
```
