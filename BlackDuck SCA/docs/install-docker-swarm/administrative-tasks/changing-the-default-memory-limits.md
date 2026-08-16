---
title: "Changing the default memory limits"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/changing-the-default-memory-limits.html"
content_id: "~06CIixAbYKzxh5jsjWEwQ"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:33:48.994721+00:00"
---

# Changing the default memory limits

There are some containers that may require higher than default memory limits depending on
the load placed on Black Duck.

Note: The default memory limits should never be decreased as this will cause Black Duck to function incorrectly.

You can change the default memory limits for these containers:

- webapp
- jobrunner
- scan
- binaryscanner
- bomengine

## Changing the default webapp container memory limits

There are three memory settings for the webapp container:

- The HUB_MAX_MEMORY environment variable controls the maximum Java heap
  size.
- The `limits memory` and `reservations memory`
  settings control the limit that Docker uses to schedule and limit the
  overall memory of the webapp container.

  - The `limits memory` setting is the amount of memory a
    container can use.
  - Docker uses the `reservations memory` setting to
    determine if a container can be deployed (scheduled) to a machine.
    Using this value, Docker ensures that all containers deployed to a
    machine have enough memory instead of all containers competing for
    the same memory.

  Note that the value for each of these settings must be higher than the
  maximum Java heap size. If updating the Java heap size, Black Duck Software recommends setting the `limits
  memory` and `reservations memory` values to at
  least 1GB higher each than the maximum Java heap size.

Use the `webapp` section in the
`docker-compose.local-overrides.yml` file and if necessary,
remove the comment characters (#) and enter new values.

The following example changes the maximum Java heap size for the Web App container to
8GB and the value for the `limit memory` and `reservations
memory` settings to 9GB each.

**Original values**:

```
#webapp:
#environment: {HUB_MAX_MEMORY: REPLACE_WITH_NEW_MAX_MEMORYm}
#deploy:
  #limits: {MEMORY: REPLACE_WITH_NEW_MEM_LIMITm}
  #reservations: {MEMORY: REPLACE_WITH_NEW_VALUEm}
```

**Updated values**:

```
webapp:
environment: {HUB_MAX_MEMORY: 8192m}
deploy:
  limits: {MEMORY: 9216m}
  reservations: {MEMORY: 9216m}
```

## Changing the default jobrunner container memory limits

There are three memory settings for the jobrunner container:

- The HUB_MAX_MEMORY environment variable controls the maximum Java heap
  size.
- The `limits memory` and `reservations memory`
  settings control the limit that Docker uses to schedule and limit the
  overall memory of the jobrunner container.

  - The `limits memory` setting is the amount of memory a
    container can use.
  - Docker uses the `reservations memory` setting to
    determine if a container can be deployed (scheduled) to a machine.
    Using this value, Docker ensures that all containers deployed to a
    machine have enough memory instead of all containers competing for
    the same memory.

  Note that the value for each of these settings must be higher than the
  maximum Java heap size. If updating the Java heap size, Black Duck Software recommends setting the `limits
  memory` and `reservations memory` values to at
  least 1GB higher each than the maximum Java heap size.

Note: These settings apply to all Job Runner containers, including scaled Job Runner
containers.

Use the `jobrunner` section in the
`docker-compose.local-overrides.yml` file and if necessary,
remove the comment characters (#) and enter new values.

The following example changes the maximum Java heap size for the jobrunner container
to 8GB and the value for the `limit memory` and `reservations
memory` settings to 9GB each.

**Original values**:

```
#jobrunner:
#environment: {HUB_MAX_MEMORY: REPLACE_WITH_NEW_MAX_MEMORYm}
#deploy:
  #limits: {MEMORY: REPLACE_WITH_NEW_MEM_LIMITm}
  #reservations: {MEMORY: REPLACE_WITH_NEW_VALUEm}
```

**Updated values**:

```
jobrunner:
environment: {HUB_MAX_MEMORY: 8192m}
deploy:
  limits: {MEMORY: 9216m}
  reservations: {MEMORY: 9216m}
```

### Changing the default memory limits

The following values may be changed if more memory is given to the container when
you modify the HUB_MAX_MEMORY value.

- org.quartz.scheduler.periodic.maxthreads: 4
- org.quartz.scheduler.periodic.prefetch: 2
- org.quartz.scheduler.ondemand.maxthreads: 8
- org.quartz.scheduler.ondemand.prefetch: 4

**Examples for guidance**

```
SMALL
HUB_MAX_MEMORY: 4096m
org.quartz.scheduler.periodic.maxthreads: 4
org.quartz.scheduler.periodic.prefetch: 2
org.quartz.scheduler.ondemand.maxthreads: 8
org.quartz.scheduler.ondemand.prefetch: 4
```

```
Medium
HUB_MAX_MEMORY: 6144m
org.quartz.scheduler.periodic.maxthreads: 4
org.quartz.scheduler.periodic.prefetch: 2
org.quartz.scheduler.ondemand.maxthreads: 12
org.quartz.scheduler.ondemand.prefetch: 8
```

```
Large/X-Large
HUB_MAX_MEMORY: 12288m
org.quartz.scheduler.periodic.maxthreads: 8
org.quartz.scheduler.periodic.prefetch: 4
org.quartz.scheduler.ondemand.maxthreads: 24
org.quartz.scheduler.ondemand.prefetch: 16
```

Note: Large and X-Large differ only in the number of jobrunner instances. The memory and thread
counts are the same.

Note: The number of max threads for both pools should not exceed 32

## Changing the default scan container memory limits

There are three memory settings for the scan container:

- The HUB_MAX_MEMORY environment variable controls the maximum Java heap
  size.
- The `limits memory` and `reservations memory`
  settings control the limit that Docker uses to schedule and limit the
  overall memory of the Scan container.

  - The `limits memory` setting is the amount of memory a
    container can use.
  - Docker uses the `reservations memory` setting to
    determine if a container can be deployed (scheduled) to a machine.
    Using this value, Docker ensures that all containers deployed to a
    machine have enough memory instead of all containers competing for
    the same memory.

  Note that the value for each of these settings must be higher than the
  maximum Java heap size. If updating the Java heap size, Black Duck Software recommends setting the `limits
  memory` and `reservations memory` values to at
  least 1GB higher each than the maximum Java heap size.

Note: These settings apply to all Scan containers, including scaled Scan containers.

Use the `scan` section in the
`docker-compose.local-overrides.yml` file and if necessary,
remove the comment characters (#) and enter new values.

The following example increases the maximum Java heap size for the scan container to
4GB and the value for the `limits memory` and `reservations
memory` settings to 5GB each.

**Original values**:

```
#scan:
#environment: {HUB_MAX_MEMORY: REPLACE_WITH_NEW_MAX_MEMORYm}
#deploy:
  #limits: {MEMORY: REPLACE_WITH_NEW_MEM_LIMITm}
  #reservations: {MEMORY: REPLACE_WITH_NEW_VALUEm}
```

**Updated values**:

```
scan:
environment: {HUB_MAX_MEMORY: 4096m}
deploy:
  limits: {MEMORY: 5210m}
  reservations: {MEMORY: 5210m}
```

## Changing the default binaryscanner container memory limits

The only default memory size for the binaryscanner container is the actual memory
limit for the container.

Note: These settings apply to all binaryscanner containers, including scaled binaryscanner
containers.

Add the `binaryscanner` section to the
`docker-compose.local-overrides.yml` file.

The following example changes the container memory limits to 4GB.

**Updated values**:

```
binaryscanner:
  limits: {MEMORY: 4096M}
```

## Changing the default bomengine container memory limits

There are three memory settings for the bomengine container:

- The HUB_MAX_MEMORY environment variable controls the maximum Java heap
  size.
- The `limits memory` and `reservations memory`
  settings control the limit that Docker uses to schedule and limit the
  overall memory of the bomengine container.

  - The `limits memory` setting is the amount of memory a
    container can use.
  - Docker uses the `reservations memory` setting to
    determine if a container can be deployed (scheduled) to a machine.
    Using this value, Docker ensures that all containers deployed to a
    machine have enough memory instead of all containers competing for
    the same memory.

Note: These settings apply to all bomengine containers, including scaled bomengine
containers.

Use the `bomengine` section in the
`docker-compose.local-overrides.yml` file and if necessary,
remove the comment characters (#) and then enter new values.

The following example changes the maximum Java heap size for the bomengine container
to 8GB and the value for the `limits memory` and `reservations
memory` settings to 9GB each.

**Original values**:

```
#bomengine:
#environment: {HUB_MAX_MEMORY: REPLACE_WITH_NEW_MAX_MEMORYm}
#deploy:
  #limits: {MEMORY: REPLACE_WITH_NEW_MEM_LIMITm}
  #reservations: {MEMORY: REPLACE_WITH_NEW_VALUEm}
```

**Updated values**:

```
bomengine:
environment: {HUB_MAX_MEMORY: 8192m}
deploy:
  limits: {MEMORY: 9216m}
  reservations: {MEMORY: 9216m}
```

Important: Black Duck recommends allocating HUB_MAX_MEMORY and limits memory for the
bomengine container using the same values as the jobrunner container.
