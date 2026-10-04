---
title: "Linux monitoring and diagnosis tools"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/linux-monitoring-and-diagnosis-tools.html"
content_id: "XL4h02fjRfghVurcSRo1jg"
version: "2026.9"
section: "Coverity Connect"
scraped_at: "2026-10-04T23:33:19.909066+00:00"
---

# Linux monitoring and diagnosis tools

You can use the following commands to monitor and diagnose the performance of your
Coverity Connect deployment on Linux:

CPU Core Count
:   The following command will help you monitor CPU usage. Note that this does not
    count hyperthreading (even if it is enabled):

    ```
    # cat /proc/cpuinfo | egrep "core id|physical id" | tr -d "\n" | sed s/physical/\\nphysical/g | grep -v ^$ | sort | uniq | wc -l
    ```

Total RAM
:   The following command will help you monitor the total RAM
    usage:

    ```
    # cat /proc/meminfo | grep MemTotal
    ```

Shared Memory
:   The following commands allow you to view the RAM that is shared between
    applications on your system.

    ```
    # sysctl -a | grep kernel.shmmax
    # sysctl -a | grep kernel.shmall
    ```
