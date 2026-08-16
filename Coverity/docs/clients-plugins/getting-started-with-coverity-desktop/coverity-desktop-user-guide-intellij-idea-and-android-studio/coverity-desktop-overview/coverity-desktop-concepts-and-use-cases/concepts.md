---
title: "Concepts"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/concepts.html"
content_id: "Jz0E9YzDN2BqmqJ28E0gwA"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:48:24.746901+00:00"
---

# Concepts

## Central Analysis

A central analysis occurs when the central source code repository is analyzed by Coverity Analysis outside of the IDE. Central analyses are
typically run on a build server and are triggered by an automated process. In most
installations, a central analysis will be run as part of a nightly build.
Alternatively, a central analysis might be initiated whenever code is checked in to
the source code repository.

The issues discovered by the central analysis are committed to a Coverity Connect database that Coverity Desktop uses to retrieve and update
issue information that you view and triage within the IDE.

Central analysis options, including server and stream
information, are set using one or more Analysis Configurations. You
must set up at least one analysis configuration to retrieve central analysis results
in the plug-in.

## Local Analysis

With local analysis, you analyze your source code for issues within your IDE. By
running a local analysis, you can examine issues, fix issues, and verify that the
issues are fixed before checking your code back into the central code repository.
You have the option of analyzing a single source file, a set of source files of your
choosing, or your entire project.

Local analysis options are set using one or more Analysis Configurations.
Upon initial set up Coverity Desktop, you will have a default
analysis configuration with your choice of analysis options. You may create
additional analysis configurations, with different sets of options, and choose the
correct configuration for each individual analysis run. This allows you to easily
change the type of analysis you want to run, depending on the project or file(s) you
are currently working on.

Before you begin using Coverity Desktop, there are a few important points to
keep in mind. Local analyses will run on the files within your workspace. Whether
you have run a local analysis or you are viewing remote issues from a central
analysis, the plug-in will present a list of issues in the Issues view, and will
also show issue markers alongside the defect occurrences in the source code editor.
To help the analysis run smoothly and report accurate information:

- Check the console view for output while running an analysis. Some
  non-critical warnings (such as number of missing classes) appear only in
  the console.
- There may be files added to your workspace since your last build that are
  not available for analysis. In these cases, when you select an analysis
  option to run, Coverity Desktop will prompt you with
  several options in the Uncaptured Source Files
  dialog. Select Capture Build and Analyze to
  complete the analysis.

## Analysis Configurations

Analysis Configurations are entities that define the analysis scope and set the
options for local and central analyses. You must have at least one analysis
configuration in order to use the plug-in, and you may also set up additional
configurations for using different options and analysis scopes.

Each Analysis Configuration can be associated with a reference stream and snapshot from a
central analysis on the Coverity Connect server. It is possible, and
recommended, to use the analysis settings that are associated with the reference
stream. However, you may also choose to pass additional analysis options, or exclude
certain files from analysis through your analysis configuration.
