---
title: "Parallel analysis"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/parallel-analysis.html"
content_id: "cqMGVmGcvsBTnhpAemT2JA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:33:14.972191+00:00"
---

# Parallel analysis

By default, `cov-analyze` takes advantage of extra CPU cores to speed up
analysis. It spawns a number of analysis worker processes according to the number of CPU
cores and the amount of physical memory on the machine. Because each worker requires a
certain amount of RAM, `cov-analyze` only spawns workers when there is
enough RAM to support them.

Important: Prior to running a parallel analysis, make sure that you have the
appropriate hardware and enough free memory for each worker that you start. For details,
see the Coverity Analysis memory requirements listed in "Minimum requirements" and "Memory requirements
for parallel analysis" in the Coverity 2026.6.0 Installation and Upgrade Guide.

There might be times when you need to adjust the number of workers: for example, because
`cov-analyze` runs on a shared machine that also runs other jobs.
You can use the `cov-analyze` command with the `--jobs`
option set to the number of workers that you want to run.

For example, the following command starts six workers:

```
> cov-analyze --dir my_intermediate_dir --jobs 6
```

The following guidelines provide scalability recommendations for different languages and
platforms:

- Scalability of a combined C and C++ analysis on Linux (64-bit) and Windows (64-bit) operating systems:
  - Typically, running eight workers yields about a 4x increase in speed over
    running one worker.
  - Typically, running three workers yields a 2.5x increase in the overall speed
    of the analysis.
  - Running more than eight workers might not decrease the overall analysis time
    significantly.
- Scalability of C# analysis on Windows (64-bit) operating systems:
  - Typically, running four workers on C# code yields about a 2.5x increase in
    speed over running one worker.
  - Typically, running two workers on C# code yields a 1.75x increase in the
    overall speed of the analysis.
  - Running more than four workers on C# code might not decrease the overall
    analysis time significantly.
- Scalability of combined C, C++, and C# analysis

  The time for a combined analysis of C, C++,
  and C# code is close to the time to analyze one after the other with the same
  settings, but combined analysis usually shows a small advantage when four or
  more workers are used.
