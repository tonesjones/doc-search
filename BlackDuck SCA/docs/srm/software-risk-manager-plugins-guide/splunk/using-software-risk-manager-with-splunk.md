---
title: "Using Software Risk Manager with Splunk"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/using-software-risk-manager-with-splunk.html"
content_id: "46HrzEpfkm4IQ99MN~68Jw"
version: "latest"
section: "Software Risk Manager Plugins Guide"
scraped_at: "2026-09-08T20:06:09.014555+00:00"
content_hash: "80f856814befd7437749dfb7ed05d326ba7afbed56bfa618f0777524b7d6f89d"
---

# Using Software Risk Manager with Splunk

## Getting Software Risk Manager data into Splunk

Go to *Inputs* and click *Create New Input*. Then fill out the fields to
create your first Software Risk Manager data input.

  
 [image: image]   

Notes:

- `Interval` determines how often your data input will run
  (every `x` seconds)

  - If a run's start-to-finish duration exceeds the time specified by the
    `Interval` field (for example, if the
    `Interval` is set to `60` and a
    particular run takes more than 60 seconds to finish), the next run
    will wait for that previous run and start as soon as it
    finishes
- `Project Specifier` can be a project ID or a special string
  representation of a set of projects:

  - To represent a single project, use that project's ID number, e.g.
    `12`
  - To represent all projects, use `all`
  - To represent an arbitrary set of projects, join the IDs of each
    project with an underscore, e.g.
    `12_42_123_124`
  - To include 'descendant' projects, add a `d` before the
    IDs of the main projects, e.g. `d12` or
    `d12_42_123_124` (note that there is only one
    `d` needed; it applies to each of the specified
    projects)
- `Detection Method` and `Severity` will filter
  the data by detection method and severity respectively

  - These are both multi-value fields, so if you like you can specify
    multiple detection methods and/or severities to filter by

To manage a specific input, click on its *Action* button, in the rightmost,
*Actions*, column.

  
 [image: image]   

From there you are given 4 options:

  
 [image: image]   

- *Edit*: view and potentially edit the input
- *Delete*: remove the input
- *Enable/Disable*: toggle whether the input is enabled or not

  - Inputs are automatically enabled when first created
  - An input will not run if it is disabled
- *Clone*: create a new input with the same default settings as this
  input

## View your Software Risk Manager data in Splunk

Go to *Search* and search for whatever Software Risk Manager data you want to
find.

  
 [image: image]   

`source="csv_report"` - A simple search to start off with that gets
results from all inputs (all inputs retrieve data from Software Risk Manager through
CSV reports)

  
 [image: image]   

By default, the `host`, `source`, and
`sourcetype` fields are included in *Selected Fields* (on
the left sidebar after running a search). You can change which fields are selected
by clicking on *All Fields* (also at top of left sidebar) and
selecting/deselecting fields.

  
 [image: image]
