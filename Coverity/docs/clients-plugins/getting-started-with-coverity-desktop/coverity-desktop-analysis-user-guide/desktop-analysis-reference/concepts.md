---
title: "Concepts"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/concepts.html"
content_id: "uKmCJ2mQx9XuACDH_6nzGA"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:46:55.530493+00:00"
---

# Concepts

This section provides conceptual definitions for Coverity Desktop Analysis. These
concepts are integral to more advanced usage of the Desktop Analysis tools.

Build Capture
:   Build capture is the process of running a build under monitoring software that records
    information about the build. To parse code accurately and consistently with
    your build settings, build capture is required to analyze compiled code with
    `cov-run-desktop`. Build capture is typically done in a
    separate step before analysis but can be done automatically, on demand, if
    configured for that.

Code Version Date
:   In contrast to the snapshot date, which is when a snapshot was committed (copied) into
    Coverity Connect, the code version date is the date when the code was
    checked in to the Source Code Management (SCM) system.

Desktop Analysis
:   Desktop Analysis is used by developers to locally analyze a small subset of the code base
    for which they are responsible. The developer can run Desktop Analysis on a
    specific file (or set of files) after making changes. By specifying a
    smaller number of files (or translation units) to analyze, the Desktop
    Analysis user gets analysis results back in a significantly shorter time.

    In order to accurately locate the more complex static analysis
    issues, Desktop Analysis uses previously reported analysis summary
    information for any code that isn't included in the analysis run.
    Desktop Analysis connects to the Coverity Connect server to download
    analysis summary data.

    Because the Coverity Connect server may
    contain several streams for organizing different versions of the code
    base, Desktop Analysis users must also specify a reference stream from
    which to retrieve summary information. This ensures that the analysis
    summaries are the most relevant to the code being analyzed. See Coverity Platform 2026.6.0 User and Administrator Guide for more information on stream
    configuration.

Primary Source File
:   For C and C++, the primary source file (PSF) of a translation unit is the file that is
    directly named on the compilation command line when compiling that
    translation unit. Header files, and other files that are read in the context
    of a PSF, are called "non-PSF" files. For Java, Kotlin, C#, and filesystem
    capture languages, every source file is considered a PSF of its own
    translation unit, even if it is not explicitly listed on a compiler command
    line.

Reference Snapshot
:   A snapshot is a set of source files and the defects that were detected in those source
    files. A reference snapshot additionally contains analysis summaries that
    are used during desktop analysis to supplement the information derived from
    locally compiled code, and analysis options that are used as the default
    starting point for local analysis options.

Static analysis
:   Static analysis is the process by which Coverity Analysis tools scan your source code for
    bugs without having to run the code. Static analysis makes use of various
    "checkers" to scan for hard-to-find software issues. Some of these checkers
    are relatively simple, finding issues based on patterns in local files.
    Other checkers combine information gleaned from across the code base to find
    more complex issues.

    This process is generally executed on a periodic
    basis, analyzing the full code base. The results of the analysis are
    then committed to the central Coverity Connect server, where they can be
    viewed by the developer responsible.

Stream
:   Snapshots are organized into streams. All snapshots in a stream should be from the same
    code base and branch, be compiled for the same target platform, and analyzed
    with the same options.

Translation Unit
:   A translation unit is smallest unit of re-compilation for a compiler. In Java, for example,
    it is possible to recompile any single source file in a project, so a
    translation unit corresponds to a source file. In C/C++, a translation unit
    is a primary source file and all the other files it includes. Coverity tools
    capture artifacts for analysis as a collection of translation units,
    including those input files used to generate object code, as well as other
    files and information that form the context of the compilation. For example,
    in Java, this context includes bytecode files in the classpath. In C/C++,
    this context includes platform information about the compiler and defined
    preprocessor directives. Coverity Desktop build capture typically only
    records the primary source file and its corresponding command line, although
    there is an option (--record-with-source) to additionally record the
    supporting files.

Triage
:   Triage is user-specified metadata associated with a defect, or more precisely, an
    equivalence class of defects that all share certain essential
    characteristics. The equivalence class is named by the numeric CID, the
    "Coverity ID". The most important triage attribute is
    Classification, which includes the settings of
    "False Positive" and "Intentional", both of which effectively mean the user
    wants to suppress the defect from that point forward.

    All defects
    detected by desktop analysis have a triage record on the Coverity
    Connect server (unless using disconnected mode), even if they have not
    been committed as part of a snapshot.
