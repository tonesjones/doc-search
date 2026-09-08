---
title: "Analysis Behavior"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/analysis-behavior.html"
content_id: "YkdE_neR8CU2mSGmN8vPcQ"
version: "latest"
section: "Software Risk Manager Install Guide"
scraped_at: "2026-09-08T20:05:29.257641+00:00"
content_hash: "bf1c4e37533630f345bc4a191b98c051f03d9fab3d8de0be553444d1ea2cad4a"
---

# Analysis Behavior

Various settings allow you to affect Software Risk Manager behavior regarding the
analyses it conducts. Changing any of the analysis behavior properties can be done at
any time after the initial installation; however, you will still need to restart the
Tomcat server to reload the properties.

- `analysis.concurrent-analysis-limit` (default: `2`)
  - the maximum number of analyses to run concurrently. Note that this does not
  override the *Job
  Configuration* settings, but merely sets another
  limit.
- `storage.keep-raw-inputs` (default: `true`) - when
  this setting is true, Software Risk Manager will keep copies of all files
  uploaded for analysis. While these inputs are not required by Software Risk
  Manager after the analysis is complete, keeping them for archival purposes will
  allow them to be downloaded from the *Show Inputs* list. If storage space
  is an issue, setting this to `false` will prevent Software Risk
  Manager from storing the raw inputs.
- `storage.keep-archived-inputs` (default: `false`) -
  when this setting is true, Software Risk Manager will keep all uploaded files,
  whether they are archived or not. Leaving this setting `false`
  will cause Software Risk Manager to delete stored copies of data upon archival.
  Note that this setting is dependent on the value of
  `storage.keep-raw-inputs`, which must also be
  `true` in order to keep the archived data.
- `swa.tools.keep-all-logs` (default: `false`) - this
  setting determines whether to keep all the log files for the tools that Software
  Risk Manager runs. If false, only the logs from failures are kept.
- `swa.upload.maxfilesize` (default: `2048`) - this
  setting controls the maximum file upload size allowed (in megabytes) for a
  single file.
- `swa.upload.maxuploadsize` (default: `2048`) - this
  setting controls the maximum size of all uploaded files (in megabytes) for a
  single analysis.
- `codedx.analysis.hybrid-enabled-by-default` (default:
  `false`) - this setting determines the default value for the
  "Enable hybrid analysis" setting in *Analysis Config*. Since hybrid
  analysis requires some relatively time-consuming steps, this setting is
  `false` by default.
- `codedx.analysis.auto-archive-enabled-by-default` (default:
  `true`) - this setting determines the default value for the
  "Archive findings" setting in *Analysis Config*. Most projects will only upload
  a scan from a tool if it represents a new state of the project, but an organization
  may want to be able to upload many tool result files in sequence without having them
  interfere with each other. Such organizations should set this setting to
  `false`.
- `codedx.analysis.auto-archive.excluded-tools` (default: none) -
  this setting allows excluding outputs from certain tools from the auto archival
  process. This setting is a comma-separated list of the names of the tools to
  exempt from auto archival.
- `ingestion.skip-code-metrics` (default: false) - if set to true,
  code metrics will not be gathered during analysis.
- `finding.reopen-gone` (default: true) - this setting determines
  the default value for the "Allow gone findings to be reopened" setting in
  *Analysis Config*.
- `finding.reopen-resolved` (default: false) - this setting
  determines the default value for the "Reopen resolved findings when updated"
  setting in *Analysis Config*.
- `storage.keep-failed-analysis-inputs` (default: false) - this
  setting determines whether to keep files associated with failed
  analyses.
- `analysis-prep.idle-lifetime` (default: 30 minutes) - this setting
  controls how long an analysis prep must be inactive before it expires and its
  prep id becomes invalid. Note that if uploading to an analysis prep **via the
  Software Risk Manager API**, the analysis prep is still considered
  inactive until the upload finishes. It is possible for the analysis prep to
  expire before the upload finishes. If you're encountering an error from the API
  stating the prep doesn't exist, it is recommended to increase the default of
  this prop. A value for this property should follow the form of
  `{number}{unit}`, for example, `50m` for 50
  minutes or `1h` for 1 hour.
- `srm.correlation.default-component-correlation-mode` (default:
  `vulnerability,identifier,type`) - this setting configures what
  the default component correlation mode will be for newly created projects in SRM.
  Valid values are
  - `vulnerability,name&version,type`
  - `vulnerability,identifier,type`
  - `identifier,type`
  - `name&version,type`
  - `vulnerability,type`
- `code-metrics.keep-all-logs` (default: false) - this setting
  determines whether to keep all the log files for the code metrics tools that
  Software Risk Manager runs. If false, only the logs from failures are kept.

## Bundled Tools

Software Risk Manager bundles various tools that run independently during the
analysis process. Each of these tools requires a memory budget during its own
analysis. The memory requirements vary based on the sizes of the codebases the
analyzers are checking. The memory budget for each of these tools is configurable in
the properties file; each of the following settings specify the number of megabytes
allotted to their respective tools. In general, the static analyzers will require
more memory in order to analyze larger projects.

- `java.tools.maxmemory` (default: `1024` (1GB))
  determines the maximum heap size for java-based tools.
- `java.tools.maxmemorypercentage` (default:
  `<none>`) determines maximum heap size for
  java-based tools as a percentage of total system memory.
- `ruby.tools.maxmemory` (default: `1024` (1GB))
  determines the maximum heap size for Ruby-based tools, which are run with
  Java via JRuby.
- `ruby.tools.maxmemorypercentage` (default:
  `<none>`) determines the maximum heap size for
  Ruby-based tools as a percentage of total system memory, which are run with
  Java via JRuby.
- `php.tools.maxmemory` (default: `1024` (1GB))
  determines the maximum heap size for PHP tools.

Additionally, these bundled tools may be disabled entirely, if necessary, by setting
`bundled-tools.disable` to `true` (default:
`false`). When this flag is set, no bundled tools will be
available on the new analysis page nor will they be run.
