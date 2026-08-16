---
title: "Changing the number of concurrent commits"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/changing-the-number-of-concurrent-commits.html"
content_id: "QgY7mnqfr9UW4FePjrwOrQ"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:52:00.733417+00:00"
---

# Changing the number of concurrent commits

These properties can be set in the cim.properties file.

commitPoolThreads
:   Specifies the number of concurrent threads to process commits off of the queue.
    Minimum 1. Maximum 50. Default 5. To change this number, insert the following
    property:

    ```
    commitPoolThreads=N (where N is the number of commits)
    ```

    As commit performance and scale are affected by a number of factors (lines of
    code, number of defects/issues, complexity of events, etc.) it is difficult to
    predict the concurrency load on the application. While
    commitPoolThreads allows for greater levels of
    concurrency, it is possible to subject the application to too much load.

    When
    this occurs, there are errors in the
    $CIM_HOME/logs/cim.log that are indicative of this
    issue. In some cases, these errors can be mitigated by increasing the heap
    memory allocation via the `-Xmx java_opts_post` setting in
    the $CIM_HOME/config/system.properties file with the
    provision that there is sufficient available system RAM. If not, the
    application load must be reduced and/or limited by reducing
    commitPoolThreads value.

    The errors are as follows:

    1. `java.lang.OutOfMemoryError: Java heap space` -
       suggests that the maximum heap size is insufficient for the JVM
       load.
    2. `java.lang.OutOfMemoryError: GC overhead limit exceeded`
       - suggests that the application is spending a significant amount of time
       performing garbage collection instead of processing the application
       requests. This error can be disabled by appending the
       `-XX:-UseGCOverheadLimit` to the
       java_opts_post in the
       $CIM_HOME/config/system.properties file. This
       not recommended however as messages of this nature suggest extreme
       memory pressure on the application.

commitWorkQueueCapacity
:   Specifies the number of commits that can wait in the queue. Minimum 15. Maximum
    255. Default 80.
