---
title: "Analysis configuration"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/analysis-configuration.html"
content_id: "clAHdJP6A05MjcU6a~gNVg"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:46:06.684236+00:00"
---

# Analysis configuration

The keys described next configure the analysis performed on the captured code.

| Key | Type | Description |
| --- | --- | --- |
| `aggressiveness-level` | string | Specifies the aggressiveness level for the analysis. Possible values are `low`, `medium`, or `high`. The aggressiveness level causes the analysis to make more or less aggressive assumptions during the analysis where the higher the aggressiveness level, the more defects are reported.  Default: `low` |
| `callgraph-metrics` | Boolean | Enables callgraph metrics output in the intermediate directory. Default: `false` |
| `c-cpp-virtual` | Boolean | For C, C++: Enables full virtual-call resolution for C++. Default: `false` |
| `c-cpp-fnptr` | Boolean | For C, C++: Enables analysis of calls to function pointers for defects. Default: `false` |
| `checkers` | Checker configuration | If no checker configuration is specified, the CLI will enable a set of checkers based on the files that were captured. |
| `coding-standards` | Coding standard configuration | If specified, the analysis will scan the code for compliance according to the given coding standard configuration. If this configuration is present, the `emit-complementary-info` setting is used during capture. |
| `connect` | Analyze Connect configuration | The Coverity Connect configuration to use when performing analysis in Coverity Connect. |
| `constraint-fpp` | Boolean | C, C++, C#, Java, Visual Basic: Enables additional filtering of defects by using an additional false-path pruner. If set to true, the constraint FPP is enabled.  Default: `false` |
| `cov-analyze-args` | array of strings | Specify additional arguments to pass to the `cov-analyze` command when performing an analysis. The following example illustrates how to use `cov-analyze-args`:  In the following example, `cov-analyze-args` specifies the arguments:  - `disable-sigma` - `enable: DC.CUSTOM_MY_CHECKER` - `dc-config: my_dc_config.json`   ``` analyze:   parse-warnings:     enabled: true     file: my_parse_warnings.conf   checkers:     default: false   cov-analyze-args:     - --disable-sigma     - --enable     - DC.CUSTOM_MY_CHECKER     - --dc-config     - my_dc_config.json ```   Note: Options previously used with the `cov-analyze` command can still be used as-is with `coverity analyze`, by specifying them with the `cov-analyze-args` key, even if they are not explicitly defined in the configuration file (schema). |
| `cov-collect-models-args` | array of strings | Additional arguments to pass to the `cov-collect-models` command following analysis when “`output-model-file`" is specified. |
| `directives` | array of Directives configuration entries | Specifies directives to use for the analysis, including for Web application security analysis. |
| `enable-check-set` | array of strings | List of check sets to enable. Valid values are "cwe-top-25-2023", "cwe-top-25-2024", "owasp-mobile-top-10-2016", "owasp-mobile-top-10-2024", "owasp-web-top-10-2021", "owasp-web-top-10-2025". |
| `files` | Analyze files configuration | Lists the files to analyze when the `mode` key is set to `"hfi"`. |
| `jobs` | Jobs configuration | Specifies analysis worker parallelism. |
| `location` | string | Specifies whether the analysis is done locally or in the Cloud:  - `connect` Runs the analysis in the Cloud. The   analysis is performed by the Coverity Scan   Service located in a Kubernetes cluster in the Cloud. - `local` Runs the analysis locally.   Default: `local`  Note: For options and information about performing an analysis in the Cloud, refer to "Performing an analysis in a Coverity cloud deployment" in the Coverity Analysis 2026.6.0 User and Administrator Guide and to the Coverity 2026.6.0 Cloud Deployment Administrator and User Guide. |
| `mode` | string | Allowable values are `"hfi"` or `"pfi"`. Default: `"pfi"`. `"hfi"`  Stands for *high fidelity incremental*. When `mode` is set to `"hfi"`, Coverity Analysis analyzes only those files listed in the `files` key.  `"pfi"`  Stands for *perfect fidelity incremental*. When `mode` is set to `"pfi"`, Coverity Analysis analyzes the complete set of files.  CAUTION:  An `"hfi"` analysis can be faster than a `"pfi"` analysis, but it might produce results that are incomplete or inconsistent, due to the lack of context. Use it only when speed is more important than accuracy.  Important: `hfi` mode is only applicable to Coverity Connect deployments, and `"hfi"` mode is only supported for local results. `"hfi"` results cannot be committed to Coverity Connect. When using `"hfi"` mode, ensure your configuration uses the `--local` option or `commit.local` configuration.  See also Analyze files configuration. |
| `model-file` | string | The name of a file containing function models. This value overrides models specified in the default location of config/user_models.xmldb. |
| `one-tu-per-psf` | Boolean | If set to `true`, only one TU (translation unit) will be analyzed per source file. If set to `false`, all translation units will be analyzed. Default: `true` |
| `output-model-file` | string | Output file to which function models for the project should be written following analysis, |
| `parse-warnings` | Parse warnings configuration | Specifies how parse warnings are handled. |
| `pool-size` | string | Pool size to use for analysis in Connect. Valid values are `"small"`, `"medium"`, `"large"`, `"extralarge"`, and custom pool labels. |
| `replay-processes` | integer | Controls the number of processes used to do a replay prior to analysis if a project has been captured using `record-with-source`. |
| `scan-transparency` | Boolean | Specifies whether to enable the collection of scan transparency data for analysis. This setting must be enabled if the Coverity Connect instance has `scan.transparency.enabled=true` in its configuration. For more information, see "Enabling collection of scan transparency data" in the Coverity Platform 2026.6.0 User and Administrator Guide.  Default: `true` |
| `sigma` | Sigma configuration | Specifies options for Sigma analysis. |
| `trust` | map from string to Boolean | This is a map from a trust-option name to a Boolean value that indicates whether the particular trust property should be trusted. Use the special trust-option name `"all"` to specify whether *all* trust options should be trusted or distrusted.  Default: empty  The value option names are as follows:   - `"all"` - `"command-line"` - `"console"` - `"cookie"` - `"database"` - `"environment"` - `"filesystem"` - `"http"` - `"http-header"` - `"js-client-cookie"` - `"js-client-external"` - `"js-client-html-element"` - `"js-client-http-header"` - `"js-client-http-referer"` - `"js-client-other-origin"` - `"js-client-url-query-or-fragment"` - `"llm"` - `"mobile-other-app"` - `"mobile-other-privileged-app"` - `"mobile-same-app"` - `"mobile-user-input"` - `"network"` - `"rpc"` - `"servlet` - `"system-properties"` |

## Subsections for "Analysis configuration":

- Checker configuration
- Coding standard configuration
- Resolved coding standard configuration
- Directives configuration
- Analyze files configuration
- Jobs configuration
- Parse warnings configuration
- Web app security configuration
