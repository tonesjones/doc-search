---
title: "Diagnosing performance problems"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/diagnosing-performance-problems.html"
content_id: "hzRqw_RUTFThFSpfpx0pSg"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:52:17.614090+00:00"
---

# Diagnosing performance problems

You can use the Linux/Unix `top` command as a preliminary diagnosis tool
for performance-related problems. The following table lists the tools that you can use
to diagnose performance problems with `top`.

Table 1. top command options

| Option | Description |
| --- | --- |
| `iowait` | `iowait` (or just `wa`) displays the percentage of time that the CPU (or CPUs) were idle during which the system had an outstanding disk I/O request. Sustained values higher than 5-10% can indicate that an IO bottleneck exists. This command might display misleading values and should be used with other fields to support/deny a particular diagnosis path. |
| `SWAP` | SWAP contains statistics about swap space. The SWAP field can be turned on to show swap size for each process. High values coupled with high `iowait` give a strong indication of thrashing. Processes with high SWAP values need to be tuned in order to decrease the swap space. |
| `Mem` | Contains statistics on memory usage. Usage values nearing the physical memory in the machine, coupled with a large swap space, indicate the need for additional RAM. It is recommended that the amount of RAM be at least 25% of the database size. The database size can be found in Coverity Connect by navigating to Help > About... > Database Size. |

For usage information, see the <http://linux.die.net/man/1/top>.
