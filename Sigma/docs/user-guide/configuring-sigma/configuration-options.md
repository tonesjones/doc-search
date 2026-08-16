---
title: "Configuration Options"
source_url: "https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/configuration-options.html"
content_id: "Xc624824UX6vjgtvQWII9A"
version: "2026.8.0"
section: "Sigma User Guide"
scraped_at: "2026-08-13T00:25:07.563409+00:00"
---

# Configuration Options

The following table shows the global options you can set and their corresponding
environment variables.

See the `sigma analyze` command for setting analysis options.

| Option | Description | Env Var |
| --- | --- | --- |
| `--config` file | The name of the configuration file.  **Default:** .sigma-config.yml at the root of the repository.  Note: Configuring Sigma with a .sigma-config.yml file is deprecated. Use the `coverity.yml` format with the `--coverity-config` option instead.  You can specify multiple configuration files; for example,  ``` --config <file1> --config <file2> ```   Note: This option cannot be used to pass a file in the `coverity.yml` format. | `SIGMA_CONFIG_FILE` |
| `--coverity-config` file | The name of the configuration file in the `coverity.yml` format. **Default:** `coverity.yml`, `coverity.yaml`, or `coverity.json` at the root of the repository. |  |
| `-j` threads, `--num-threads` threads | The number of threads to use in executing the command.  There is no limit to this number.  **Default:** the number of logical CPUs.  This field is optional and will not show up in the default configuration file. | `SIGMA_NUM_THREADS` |
| `--policy` file | The name of the file containing the policy.  **Default:** .sigma-policy.yml located at the root of the repository. If the path is relative, it is relative to the current working directory.  Note: This option is deprecated. | `SIGMA_POLICY_FILE` |
| `-w` dir, `--working-dir` dir | Location where to store temporary files.  **Default:** .sigma-dir | `SIGMA_TMPDIR` |
