---
title: "Diagnosing I/O problems"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/diagnosing-i/o-problems.html"
content_id: "DnRVqCO1hCUh6L26KaVZYw"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:52:18.253627+00:00"
---

# Diagnosing I/O problems

If an I/O bottleneck is presumed to exist in the system, `iostat` can
assist in finding it. The following table lists the recommended options that you can use
to diagnose performance problems with `iostat`. Run
`iostat` with `-x` to see all fields.

Table 1. top command options

| Option | Description |
| --- | --- |
| `svctm` and `await` | Displays the number of milliseconds spent servicing requests. High values indicate that the device might be overloaded. Spikes in `svctm` and `await` are usually normal and only drives that show persistently slow service times should raise alarm. You can try running `iostat -d 1 -x > iostatout.txt` to look at persistent data. This will measure I/O every second for as long as it is left to run. |
| `%util` | A value of 100% means the device is saturated with requests. |
| `avgqu-sz` | Indicates the average queue size. High values along with high svctm, await and %util values near 100% likely means the device is overloaded with read/write requests. |

For usage information, see <http://linux.die.net/man/1/iostat>.
