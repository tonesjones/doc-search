---
title: "Viewing snapshot data"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/viewing-snapshot-data.html"
content_id: "WCAZuB1XdoxKrOmqiXvyfQ"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:50:08.345080+00:00"
---

# Viewing snapshot data

Each stream that is listed in the Projects & Streams menu
contains a Snapshots tab, which displays the values of attributes
that are associated with each snapshot of the stream.

**To view snapshot data for a stream:**

1. Select a stream in the Projects & Streams
   menu.
2. On the Snapshots tab, select the ID
   to examine.
3. Click Details to view information about the snapshot.

   The following table provides information about properties of the snapshot.

   Table 1. Snapshot attributes

   | Snapshot Attributes | Value |
   | --- | --- |
   | ID | A number that uniquely identifies the snapshot |
   | Version | The version of the product being analyzed. This attribute is optionally set in Coverity Connect in the Snapshots view type, or on the `cov-commit-defects` command line. |
   | Target | Intended to represent a milestone of a given product or code base, such as a release version number. This field is optionally defined in Coverity Connect in the Snapshots view type, or on the `cov-commit-defects` command line. |
   | Description | The description of the snapshot. This field is optionally defined on the `cov-commit-defects` command line. |
   | Date Committed | The date when the snapshot was committed. |
   | Committer | The username of the person who committed the issue data to Coverity Connect. |

   The following table provides build information on the snapshot.

   Table 2. Build details

   | Build Details | Description |
   | --- | --- |
   | Working Directory | The directory in which the source code is built. |
   | Command Line | The command, options, and values used for the build. |
   | Intermediate Directory | The location of the intermediate directory specified for the build command. |
   | Configuration File | The name of the configuration file used during analysis. By default, it is coverity_config.xml |
   | Build Host | Name of the host machine used to compile the source code associated with the snapshot. |
   | Build Time | The duration of the build. |
   | Source Files Captured | The percentage of source files captured for the snapshot. |

   The following table provides code analysis information on the snapshot.

   Table 3. Analysis details

   | Analysis Details | Description |
   | --- | --- |
   | Working Directory | The directory in which the analysis takes place. |
   | Command Line | The command, options, and values used for the analysis. |
   | Intermediate Directory | The location of the intermediate directory specified for the analysis command. |
   | Configuration File | The name of the configuration file used during analysis. By default, it is coverity_config.xml |
   | Analysis Host | Name of the host machine used to run the analysis of the source code associated with the snapshot. |
   | Functions Analyzed (with Models) | The number of functions in the snapshot, whether or not they were analyzed and whether or not custom or built-in models were used. |
   | Analysis Time | The duration of the analysis. |
   | Number of Annotations | The number of annotations in the snapshot. |
   | Number of Custom Models | The number of custom models in the snapshot. |
   | Enabled Checkers | The list of checkers that were enabled for the analysis. |
