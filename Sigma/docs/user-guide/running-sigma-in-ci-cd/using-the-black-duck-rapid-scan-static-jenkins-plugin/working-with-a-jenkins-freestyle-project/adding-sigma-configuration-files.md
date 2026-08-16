---
title: "Adding Sigma Configuration Files"
source_url: "https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/adding-sigma-configuration-files.html"
content_id: "TrjAAQB_Oko8dKxnJWHgqA"
version: "2026.8.0"
section: "Sigma User Guide"
scraped_at: "2026-08-13T00:25:20.703851+00:00"
---

# Adding Sigma Configuration Files

By default, Sigma searches for a .sigma-config.yml file in the
directory where Sigma is being executed, to define the configuration that controls
Sigma's execution.

If you want Sigma to use additional configuration files, add the
`--config` option to the Command Line field and specify the
correct path to the configuration file in the build workspace. The build workspace will
include files that are pulled from a source code repository such as Git.

The command syntax is as follows:

```
--config <PATH_TO_CONFIG_FILE_IN_WORKSPACE> analyze --format jenkins
```

In the following example, the `--config` parameter specifies that the file
sigma-config.yml is located in the config
directory in the workspace.

```
--config config/sigma-config.yml analyze --format jenkins
```

You can specify multiple configuration files by adding more `--config`
options to the command line:

```
--config config/sigma-config-1.yml --config config/sigma-config-2.yml analyze --format jenkins
```
