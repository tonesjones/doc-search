---
title: "Run a database tuning job"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/run-a-database-tuning-job.html"
content_id: "H0xHiBCpF4bezUyYeK~5Tg"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:42:25.833064+00:00"
---

# Run a database tuning job

You can run a database tuning job using the method that fits your process. For example,
you might use the `kubectl apply` command as follows.

To run a tuning write job:

```
kubectl apply -f static-tuning-write.yaml
```

To run a tuning suggest job:

```
kubectl apply -f static-tuning-suggest.yaml
```

Note: If you will run any script that will perform a write operation
in the `cim-tools` pod storage, you must create a persistent
`/data` volume and mounted it to the `cim-tools` pod.
See also Create and mount a /data persistent volume.

Note: If you encounter a Read Only File System error while executing
any of our scripts or binaries within a Connect pod, refer to Read-only file system error.
