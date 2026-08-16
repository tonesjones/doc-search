---
title: "Configuring a yaml file"
source_url: "https://docs.blackduck.com/r/blackduck-tools/latest/black-duck-tools/configuring-a-yaml-file.html"
content_id: "TcX8XARTF1rjFFw0caD7wA"
version: "latest"
section: "Black Duck C/CPP Tool"
scraped_at: "2026-08-13T16:16:55.631336+00:00"
---

# Configuring a yaml file

The blackduck-c-cpp tool can be configured using a .yaml file instead of using command
line argument to run the scan. See the Arguments table in Executing the blackduck-c-cpp tool for a definition of the arguments used in
the sample below.

Here is a sample fully functional .yaml configuration:
`ardour-config.yaml`

```
build_cmd: ../waf build
build_dir: /Users/theUser/myProject/ardour/build/
coverity_root: /<Coverity location>
cov_output_dir: /user_home/.blackduck/blackduck-c-cpp/output/ardour
output_dir: /user_home/.blackduck/blackduck-c-cpp/output/ardour 
skip_build: False
verbose: True
project_name: ardour_mac
project_version: may-4-2021
codelocation_name: ardour-mac
bd_url: https://...
api_token: <token>
additional_sig_scan_args: <additional scan arguments>
insecure: False
force: False
disable_bdio_json_splitter: False
bdio_split_max_file_entries: 10000
bdio_split_max_chunk_nodes: 3000
scan_interval: 30
json_splitter_limit: 10485760
debug: True
skip_transitives: False
skip_includes: False
skip_dynamic: False
offline: True
modes: sig
use_offline_files: False
scan_cli_dir: /home/../../Black_Duck_Scan_Installation/
cov_configure_args: <Coverity configuration arguments>
additional_coverity_params: <Coverity build arguments>
expand_sig_files: True
port: 55432
bazel: True
```
