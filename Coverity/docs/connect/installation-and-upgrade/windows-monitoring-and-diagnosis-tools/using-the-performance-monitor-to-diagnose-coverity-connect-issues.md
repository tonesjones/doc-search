---
title: "Using the Performance Monitor to diagnose Coverity Connect issues"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/using-the-performance-monitor-to-diagnose-coverity-connect-issues.html"
content_id: "8_1Bw5x_Hc_k~JD6Q9wSaw"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:52:19.515339+00:00"
---

# Using the Performance Monitor to diagnose Coverity Connect issues

The Performance Monitor for Windows shows persistent values for various system statistics
including CPU, RAM and I/O Counters. The following example shows an overview of how to
use the Windows Performance Monitor. Note that this is just an example. For usage
information, see the Performance Monitor documentation at <http://technet.microsoft.com/en-us/library/dd744567(v=WS.10).aspx>.

1. Open the Performance Monitor.
2. Click Monitoring Tools / Performance Monitor in the Console
   Tree (the menu on the left).
3. Click the green plus sign on the top bar of the Performance Monitor screen.
4. Add the counters you want to measure from the list and then click OK.
5. On the right side, select More Actions > New > Data Collector Set. Follow the prompts to create the logs.
6. Click Data Collector Sets > User Defined > 
   name of the set you just created
    in the Console Tree.
7. Click the Play button on the top toolbar.
8. Attempt the task which is under-performing or failing to complete (commit, upgrade,
   viewing issues, triaging, and so forth).
9. Press the Stop button.
10. You can now view the data by clicking the view latest report
    button (a small green log book icon) on the top toolbar.

Use the following descriptions to diagnose the performance issue:

Table 1. Defect event processing

| Option | Description |
| --- | --- |
| **CPU Counters** | |
| Processor \ % Interrupt Time | Measures the time the processor spends receiving and servicing hardware interruptions during specific sample intervals. This counter indicates a possible hardware issue if the value is greater than 15%. |
| System \ Processor Queue Length | This indicates the number of threads in the processor queue. The server doesn't have enough processor power if the value is more than two times the number of CPUs for an extended period of time. |
| **I/O Counters** | |
| LogicalDisk \ % Free Space | Measures the percentage of free space on the selected logical disk drive. Take note if this falls below 15%, as you risk running out of free space for the OS to store critical files. One solution is to add more disk space. |
| PhysicalDisk \ Avg. Disk Queue Length | Indicates how many I/O operations are waiting for the hard drive to become available. If the value is larger than the two times the number of spindles, that means the disk itself may be the bottleneck. This is of particular interest when considering a RAID array as a single disk that may become overloaded as a result of the configuration. |
| PhysicalDisk \ % Idle Time | Measures the percentage of time the disk was idle during the sample interval. If this counter falls below 20 percent for an extended period of time, the disk system is saturated. Replacing the current disk system with a faster disk system may be warranted. Note that this alone is not a very strong indicator of an existing problem. |
| PhysicalDisk \ Avg. Disk Sec/Read | Measures the average time, in seconds, to read data from the disk. If the number is larger than 10 milliseconds (ms), that means the disk system is experiencing latency when reading from the disk. It is recommended to replace the current disk system with a faster disk system if possible. |
| PhysicalDisk \ Avg. Disk Sec/Write | Measures the average time, in seconds, it takes to write data to the disk. If the number is larger than 10 ms, the disk system is experiencing latency when writing to the disk. It is recommended to replace the current disk system with a faster disk system if possible. |
| **Memory Counters** | |
| Memory \ % Committed Bytes in Use | Measures the ratio of Committed Bytes to the Commit Limit—in other words, the amount of virtual memory in use. Ideally this should be zero or very small. This indicates insufficient memory if the number is greater than 80%. It probably indicates thrashing. Check the Pool Paged Bytes and Available Mbytes (see below). |
| Memory \ Available Mbytes | Measures the amount of physical memory, in megabytes, available for running processes. If this value is less than 5% of the total physical RAM, that means there is insufficient memory, which can increase paging activity. To resolve this problem, you should add more memory. |
| Memory \ Pool Paged Bytes | Measures the amount of physical memory, in megabytes, available for running processes. If this value is less than 5% of the total physical RAM, that means there is insufficient memory, and that can increase paging activity. To resolve this problem, you should add more memory. |
| Memory \ Pages per Second | Measures the rate at which pages are read from or written to disk to resolve hard page faults. If the value is greater than 1,000, as a result of excessive paging, tuning the JVM and PostgreSQL settings is likely required. |
| **Network Counters** | |
| Network Interface \ Bytes Total/Sec | Measures the rate at which bytes are sent and received over each network adapter, including framing characters. The network is saturated if you discover that more than 70 percent of the interface is consumed. For example, for a 100-Mbps NIC, the interface consumed is 8.7MB/Sec (100Mbps = (100Mb)*(1MB/8Mb)/Sec = 12.5MB/Sec => 12.5MB/Sec*(0.7) = 8.7MB/Sec). |
| Network Interface \ Output Queue Length | Measures the length of the output packet queue, in packets. There is network saturation if the value is more than 2 for an extended period of time. |
