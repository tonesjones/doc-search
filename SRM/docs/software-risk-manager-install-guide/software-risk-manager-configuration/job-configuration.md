---
title: "Job Configuration"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/job-configuration.html"
content_id: "Z0erfUb9h0NtomfmlSIvBg"
version: "latest"
section: "Software Risk Manager Install Guide"
scraped_at: "2026-09-08T20:05:28.638948+00:00"
content_hash: "cfe2131ada5b9f9eb11ca44b77e4a3812fc0857ce59a7514a3ecde7a9d25a225"
---

# Job Configuration

Software Risk Manager performs most long-running tasks, including background cleanup
tasks, on a job system. Controls are in place to limit the number of such tasks running
concurrently to ensure the system isn't overloaded. The resource limits listed below may
be adjusted. Higher numbers translate to more available resources of that type. The
minimum value allowed is 1000, and the default is 2000. Values for this setting are
unitless; they are relative measures of the power of your Software Risk Manager server.
Certain jobs are more CPU-intensive, while others are more database-intensive. Each
running job uses a certain amount of the "limit," and this is the mechanism for limiting
job concurrency.

These values should be adjusted in relation to the default value. For example, if you
believe your server is twice as powerful as an average server, set these settings to
4000 (double the default) to increase the number of concurrent jobs that may be run.

- `swa.jobs.cpu-limit` determines the maximum available CPU
- `swa.jobs.memory-limit` determines the maximum available
  memory
- `swa.jobs.database-limit` determines the maximum available
  database I/O
- `swa.jobs.disk-limit` determines the maximum available disk
  I/O

In addition, certain jobs (e.g., generating reports for a project) may produce outputs.
The `swa.jobs.expiration` (default: `60`) setting
specifies how long the job results will be available (in minutes).
