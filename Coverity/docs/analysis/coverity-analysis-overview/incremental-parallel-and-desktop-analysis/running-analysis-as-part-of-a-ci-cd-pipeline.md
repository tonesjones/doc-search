---
title: "Running analysis as part of a CI/CD pipeline"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/running-analysis-as-part-of-a-ci/cd-pipeline.html"
content_id: "LmdWPq_3z5YfX7KAZcilbA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:33:16.254639+00:00"
---

# Running analysis as part of a CI/CD pipeline

Deploying Coverity Analysis to a continuous integration / continuous delivery (CI/CD)
pipeline involves many trade-offs. These include balancing analysis speed versus thoroughness
of coverage, and which issues you do or do not want to stop your pipeline.

These are complex topics, and they are largely beyond the scope of this document.
However, as a starting point, consider a deployment that includes at least the first two
of the following types of jobs:

1. **An incremental build and analysis job** that runs continuously in the background, and
   that uploads scan summaries to Coverity Platform. This setup matches the Desktop use
   case.

   If this job finds any defects that the following job type (#2) misses,
   you can deal with those defects without blocking delivery.
2. **A continuous integration job** that runs a `cov-run-desktop` analysis
   on whatever changed since the last run. This job breaks the CI pipeline if any new
   defects are reported.

   This job will run quickly because it relies on summaries
   from the previous job.
3. **An incremental full build and analysis** that doesn’t block your pipeline but that runs
   a comprehensive set of checkers.

   As with the incremental job, #1, you can deal
   with the results from job #3 without blocking delivery.

The incremental job, #1, enables the continuous integration job, #2. As a rule, job #2
should run at an early stage of the CI/CD pipeline—for example, during the build phase
or the early test phase.

Both job #1 and job #2 should run *exactly* the same analysis configuration: that
is, the same set of checkers using the same options. The client might choose this
configuration so that analysis runs more quickly, or so that the logic of when a
pipeline might break is easy to follow.

For example, the following analysis hones in on code that is liable to be attacked:

```
cov-analyze --disable-default -en SQLI -en XSS
```

Job #3 is optional. A job of this kind does not have to run quickly. Instead, it can run
a comprehensive set of checkers in order to detect as many defects as possible. Unlike
job #2, the comprehensive job #3 is likely to run at a later point in the pipeline: for
example, as a last step before deployment to the staging location.

The following sample invocation, in contrast to the previous one, scans for a wide range
of security issues:

```
cov-analyze --webapp-security --distrust-database -en SQL_NOT_CONSTANT
```
