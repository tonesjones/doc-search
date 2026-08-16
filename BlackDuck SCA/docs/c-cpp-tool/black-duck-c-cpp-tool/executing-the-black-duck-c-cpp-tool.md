---
title: "Executing the Black Duck C/CPP tool"
source_url: "https://docs.blackduck.com/r/blackduck-tools/latest/black-duck-tools/executing-the-black-duck-c/cpp-tool.html"
content_id: "Mkt31q4CrCHqlkWvzXQ0DA"
version: "latest"
section: "Black Duck C/CPP Tool"
scraped_at: "2026-08-13T16:16:55.004292+00:00"
---

# Executing the Black Duck C/CPP tool

## Running the tool

Once your Black Duck C/CPP tool is installed, simply run the command:

```
blackduck-c-cpp -d BUILD_DIR -proj PROJECT_NAME -vers PROJECT_VERSION -bd bd_url -a api_token
```

Or, if you have configured a yaml file:

```
blackduck-c-cpp --config /Users/theUser/myProject/<file name>.yaml
```

## Command line options

To run the Black Duck C/CPP tool, see the command below:

`blackduck-c-cpp [-h] [-c CONFIG] [-bc build_cmd] -d BUILD_DIR [-Cov
coverity_root] [-Cd cov_output_dir] [-od output_dir] [-s [SKIP_BUILD]] [-v
[verbose]] -proj PROJECT_NAME -vers PROJECT_VERSION [-Cl CODELOCATION_NAME] -bd
bd_url -a api_token [-as additional_sig_scan_args] [-i [insecure]] [-f [force]]
[-djs [DISABLE_JSON_SPLITTER]] [-si SCAN_INTERVAL] [-jsl json_splitter_limit]
[-dg [debug]] [-st [SKIP_TRANSITIVES]] [-sh [SKIP_INCLUDES]] [-sd
[SKIP_DYNAMIC]] [-off [OFFLINE]] [-md modes] [-uo [USE_OFFLINE_FILES]] [-sc
scan_cli_dir] [-Cc cov_configure_args] [-ac additional_coverity_params] [-es
[EXPAND_SIG_FILES]] [-po PORT]`

Table 1. Arguments

| Argument | Required | Details |
| --- | --- | --- |
| `-h`  `--help` | N | Show this help message and exit. |
| `-c CONFIG`  `--config CONFIG` | N | Configuration file path. |
| `-bc build_cmd`  `--build_cmd build_cmd` | N | Command used to execute the build. |
| `-d BUILD_DIR`  `--build_dir BUILD_DIR` | Y | Directory from which to run build. |
| `-Cov coverity_root`  `--coverity_root coverity_root` | N | Base directory for Coverity. If not specified, Black Duck C/CPP downloads latest mini-coverity package from GCP for authorized Black Duck customers for Black Duck versions >= 2021.10.  To download the Coverity package using GCP, you must open connection toward `*.googleapis.com:443`. If you don't have the Coverity package and your Black Duck version is older than 2021.10, please contact Black Duck Support to get latest version of Coverity package. |
| `-Cd cov_output_dir`  `--cov_output_dir cov_output_dir` | N | Target directory for coverity output files. If not specified, defaults to `user_home/.blackduck/blackduck-c-cpp/output/project_name`. |
| `-od output_dir`  `--output_dir output_dir` | N | Target directory for Black Duck C/CPP output files. If not specified, defaults to `user_home/.blackduck/blackduck-c-cpp/output/project_name`. |
| `-s [SKIP_BUILD]`  `--skip_build [SKIP_BUILD]` | N | Skip build and use previously generated build data. Make sure that your initial coverity wrapped build uses the `--emit-link-units` flag. |
| `-v [verbose]`  `--verbose [verbose]` | N | Verbose mode selection. |
| `-proj PROJECT_NAME`  `--project_name PROJECT_NAME` | Y | Black Duck project name. |
| `-vers PROJECT_VERSION`  `--project_version PROJECT_VERSION` | Y | Black Duck project version. |
| `-Cl CODELOCATION_NAME`  `--codelocation_name CODELOCATION_NAME` | N | This controls the Black Duck SCA's codelocation. The codelocation_name will overwrite any scans sent to the same codelocation_name, indicating that this is a new scan of a previous code location. Use with caution. |
| `-bd bd_url`  `--bd_url bd_url` | Y | Black Duck SCA URL. |
| `-a api_token`  `--api_token api_token` | Y | Black Duck SCA API token. Instead of specifying `api_token` value in command line or yaml file, use the `BD_HUB_TOKEN` environment variable to specify a Black Duck API token. |
| `-as additional_sig_scan_args`  `--additional_sig_scan_args additional_sig_scan_args` | N | Any additional args to pass to the signature scanner. |
| `-i [insecure]`  `--insecure [insecure]` | N | Disable SSL verification so self-signed Black Duck SCA certs will be trusted. |
| `-f [force]`  `--force [force]` | N | In case of GCP failure, force use of older version of Coverity (if present). |
| `-djs [disable_bdio_json_splitter]`  `--disable_bdio_json_splitter [DISABLE_BDIO_JSON_SPLITTER]` | N | Disable the JSON/BDIO splitter and always upload as a single scan. For using JSON/BDIO splitter, dryrun is needed, so please run in offline mode first. |
| `-bsfl [bdio_split_max_file_entries]`  `--bdio_split_max_file_entries [BDIO_SPLIT_MAX_FILE_ENTRIES]` | N | Set the limit for maximum scan node entries per generated BDIO file. |
| `-bscn [bdio_split_max_chunk_nodes]`  `--bdio_split_max_chunk_nodes [BDIO_SPLIT_MAX_CHUNK_NODES]` | N | Set the limit for maximum scan node entries per single BDIO-entry file. Default value is 5000. |
| `-si SCAN_INTERVAL`  `--scan_interval SCAN_INTERVAL` | N | Set the number of seconds to wait between scan uploads in case of multiple scans. |
| `-jsl json_splitter_limit`  `--json_splitter_limit json_splitter_limit` | N | Set the limit for a scan size in bytes.  For using JSON/BDIO splitter, dryrun is needed, so please run in offline mode first. |
| `-dg [debug]`  `--debug [debug]` | N | Debug mode selection. Setting debug: True sends all the files we found to all matching types. By default, it will only send files not detected by package manager to BDBA and Signature matching. |
| `-st [SKIP_TRANSITIVES]`  `--skip_transitives [SKIP_TRANSITIVES]` | N | Skipping all transitive dependencies. |
| `-sh [SKIP_INCLUDES]`  `--skip_includes [SKIP_INCLUDES]` | N | Skipping all .h and .hpp files from all types of scan. |
| `-sd [SKIP_DYNAMIC]`  `--skip_dynamic [SKIP_DYNAMIC]` | N | Skipping all dynamic (SO/DLL) files from all types of scan. |
| `-off [OFFLINE]`  `--offline [OFFLINE]` | N | Store BDBA and signature ZIP files, signature scan JSON, and raw_bdio.csv to disk if offline mode is true.  The `--scan_cli_dir` parameter must be specified when run in offline mode to generate dryrun files. |
| `-md modes`  `--modes modes` | N | Comma separated list of modes to run - `all` (default),`bdba`, `sig`, `pkg_mgr`. |
| `-uo [USE_OFFLINE_FILES]`  `--use_offline_files [USE_OFFLINE_FILES]` | N | Use offline generated files for upload in online mode. |
| `-sc scan_cli_dir`  `--scan_cli_dir scan_cli_dir` | N | Scan cli directory.  Ex: Providing `scan_cli_dir` as `/home/../../Black_Duck_Scan_Installation/` instead of `/home/../../Black_Duck_Scan_Installation/scan.cli-2022.4.0/` works. |
| `-Cc cov_configure_args`  `--cov_configure_args cov_configure_args` | N | Additional configuration commands to cov-configure for different compilers. Inputs taken are of format {"compiler":"compiler-type"}. There is a way to use Coverity template configuration to reduce number of template compiler configurations with wildcards: example: "`--compiler *g++ --comptype gcc`" for adding `x86_64-pc-linux-gnu-g++`. |
| `-ac additional_coverity_params`  `--additional_coverity_params additional_coverity_params` | N | Any additional args to pass to Coverity build command. example: `--record-with-source`. |
| `-es [EXPAND_SIG_FILES]`  `--expand_sig_files [EXPAND_SIG_FILES]` | N | Use `expand_sig_files` for creating exploded directory instead of ZIP in signature scanner mode. |
| `-po PORT`  `--port PORT` | N | Set a custom Black Duck SCA port. |
| `-ba`  `--bazel` | N | Use if this is a Bazel build - make sure you have followed the setup instructions for Coverity. |
| `-pgn PROJECT_GROUP_NAME`  `--project_group_name PROJECT_GROUP_NAME` | N | This is same as `--detect.project.group.name` in Detect. Sets the 'Project Group' to assign the project to. Must match exactly to an existing project group in Black Duck. |
| `-pgd PROJECT_DESCRIPTION`  `--project_description PROJECT_DESCRIPTION` | N | This is same as `--detect.project.description` in Detect. If project description is specified, your project will be created with this description. |
| `-scv set_coverity_mode`  `--set_coverity_mode set_coverity_mode` | N | Specify Coverity mode to `cov-build` to force run with cov-build. cov-cli runs by default for coverity versions >= 2023.9 and cov-build for < 2023.9. |
| `-fpc force_pull_coverity_vers`  `--force_pull_coverity_vers force_pull_coverity_vers` | N | For Linux platforms, force pull 2022.9 or latest version of Coverity if not auto downloaded by blackduck-c-cpp correctly by specifying `-old` or `latest` respectively. |

## Snippet scanning

Black Duck recommends using `--snippet-matching` when using the Black
Duck C/CPP tool. To use snippet scanning, pass the snippet scanning parameters to
the signature scanner using:

```
--additional_sig_scan_args <snippet scanning parameter(s)>
```

See [Running a component scan using the Signature
Scanner command line](https://documentation.blackduck.com/bundle/bd-hub/page/ComponentDiscovery/CommandLine.html) in the Black Duck Help Guide for more details.

## Accessing Black Duck SCA via a proxy

To access the Black Duck SCA server via a proxy, you must set a
`SCAN_CLI_OPTS` environment variable prior to running the scan.
See [Accessing the Black Duck server via a
proxy](https://documentation.blackduck.com/bundle/bd-hub/page/ComponentDiscovery/Proxy_Information.html) in the Black Duck Help Guide for details.

## Scans exceeding 5GB

Black Duck SCA scans typically have an upper limit of 5GB. You can get around this
limitation by following the steps below:

1. Run the Black Duck C/C++ tool in offline
   mode to generate the scan files and Coverity linkage files by
   adding the offline parameter to your command:

   ```
   blackduck-c-cpp -d BUILD_DIR -proj PROJECT_NAME -vers PROJECT_VERSION -bd bd_url -a api_token -off
   ```
2. Rerun the scan in online mode, add the use offline files parameter to point to your
   first run generated files, and adding in the splitter parameters on the props page. The values used below
   are for example purposes:

   ```
   blackduck-c-cpp -d BUILD_DIR -proj PROJECT_NAME -vers PROJECT_VERSION -bd bd_url -a api_token -uo -bsfl 3000
   ```

   or

   ```
   blackduck-c-cpp -d BUILD_DIR -proj PROJECT_NAME -vers PROJECT_VERSION -bd bd_url -a api_token -uo -bscn 10000
   ```

The second run will take your offline files, run the BDIO splitter on them, and
upload them to Black Duck SCA in chunks, avoiding the 5GB scan limit.

Alternatively, you can configure these
parameters in a yaml file for ease of use.
