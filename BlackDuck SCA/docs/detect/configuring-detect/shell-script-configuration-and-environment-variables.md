---
title: "Shell script configuration and environment variables"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/shell-script-configuration-and-environment-variables.html"
content_id: "cRTX5LamgSL5Psah57EB4A"
version: "11.5.1"
section: "Configuring Detect"
scraped_at: "2026-08-08T23:44:23.846975+00:00"
---

# Shell script configuration and environment variables

The Black Duck® Detect Bash and PowerShell scripts are configured by setting the environment variables.

In Bash, an environment variable is set as follows:

```
export ENV_VAR_NAME=value
```

In Command or Batch, an environment variable is set as follows:

```
set ENV_VAR_NAME=value
```

In PowerShell, an environment variable is set as follows:

```
$Env:ENV_VAR_NAME = value
```

It is generally a good idea to quote the value as you assign it.
Be sure to check that the variable value has been set as expected by displaying its value after you have set it.

Refer to Running the Detect script for more information.

| Variable | Purpose | Value | Notes |
| --- | --- | --- | --- |
| DETECT_SOURCE | Download the Detect .jar from a given URL | The URL of the Detect .jar file to download and run |  |
| DETECT_LATEST_RELEASE_VERSION | Run a given Detect version | A Detect version (example: 11.0.0) | If you would like to run a Detect version other than the latest, set DETECT_LATEST_RELEASE_VERSION to the Detect version you would like to run (for example: 11.0.0). DETECT_SOURCE has precedence over DETECT_LATEST_RELEASE_VERSION. You can see the available Detect versions in the binary repository specified in download locations. |
| DETECT_VERSION_KEY | Continue running an earlier major version of Detect | DETECT_LATEST (default), DETECT_LATEST_10, DETECT_LATEST_9 | If neither DETECT_SOURCE nor DETECT_LATEST_RELEASE_VERSION is specified, the script will use the version key to query Artifactory for the correct version to download. By default it will look for DETECT_LATEST, however the Detect artifactory also includes keys for some of the major versions of Detect such as DETECT_LATEST_9. You can view the available values for DETECT_VERSION_KEY in Detect project in the binary repository specified in download locations. |
| DETECT_JAR_PATH | Change the Detect .jar download dir | The path to the .jar file download directory | If DETECT_JAR_PATH is provided, the script will use this location when downloading and running detect. The location of the jar will be DETECT_JAR_PATH/detect-{version}.jar. The Bash script will default to '{user home directory}/detect/download' if no option is specified. |
| TMP (PowerShell only) | Provides the user's temporary directory | The path to a directory for temporary files | If DETECT_JAR_PATH is not provided, the script will use the environment 'TMP' variable as the folder for the Detect .jar path. |
| HOME (PowerShell only) | Provides the user's home directory | The path to the user's home directory | If DETECT_JAR_PATH is not provided and no 'TMP' variable can be found, the '$HOME/tmp' folder will be used for the Detect jar path. |
| DETECT_JAVA_PATH | The path to the Java instance used to execute Docker Inspector | Path to the Java executable file. | To set the Java instance used by Detect, invoke Detect using a specific Java executible or set JAVA_HOME. |
| JAVA_HOME | The path to the Java installation directory. | The path to the Java home directory. | If DETECT_JAVA_PATH is not set, and JAVA_HOME is set, the script will execute $JAVA_HOME/bin/java. |
| PATH | The executable program path. | The list of directories in which the system looks for the executable file for each command executed (the syntax is operating system-specific). | If neither DETECT_JAVA_PATH nor JAVA_HOME are set, the script assumes the directory containing the Java executable file is on the path. |
| DETECT_EXIT_CODE_PASSTHRU (PowerShell only) | Prevent the shell from exiting on completion | 1 | Setting this variable to '1' will cause the script to simply return the exit code but not exit. By default, the Detect PowerShell script will exit with the exit code of Detect. This is desirable because many CI's such as Team Foundation Server(TFS), will look at the scripts exit code to decide build status. It may be undesirable to exit the script in some situations such as when debugging in a terminal. |
| DETECT_SKIP_JAVA_TEST (PowerShell only) | Skip the test for the presence of the Java command | 1 | Setting this variable to '1' causes the script not to ensure that Java is on the path. By default the script will attempt to execute "java -version" to ensure that Java is available and executable. |
| DETECT_CURL_OPTS (Bash only) | Add the given options to any curl commands executed | curl command options (a string) | Use this variable to add options to the curl command used to download files such as the Detect .jar file. For example, you can use this variable to set proxy settings for curl. The PowerShell script does not support this as it does not use curl. To supply proxy information to the PowerShell you can simply set the Detect proxy settings as environment variables. |
| DETECT_JAVA_OPTS (Bash only) | Add the given options to the Java command | Java command options (a string) | Use this variable to add options to the Java command used to execute Detect. The PowerShell script does not currently support this setting. |
| DETECT_DOWNLOAD_ONLY (Bash only) | Download the Detect .jar file, but do not run it | 1 | Set this variable to 1 to download, but not run, the Detect .jar file. The PowerShell script does not currently support this setting. |
| BLACKDUCK_PROXY_HOST (PowerShell only) | Proxy host to use to download detect |  | When set, the PowerShell script will use the configured proxy information to download detect. Supports both environment variable styles (see below). |
| BLACKDUCK_PROXY_PORT (PowerShell only) | Proxy port to use to download detect |  | When set, the PowerShell script will use the configured proxy information to download detect. Supports both environment variable styles (see below). |
| BLACKDUCK_PROXY_USERNAME (PowerShell only) | Proxy username to use to download detect |  | When set, the PowerShell script will use the configured proxy information to download detect. Supports both environment variable styles (see below). |
| BLACKDUCK_PROXY_PASSWORD (PowerShell only) | Proxy password to use to download detect |  | When set, the PowerShell script will use the configured proxy information to download detect. Supports both environment variable styles (see below). |
| BLACKDUCK_UPLOAD_CHUNK_SIZE | Sets the binary upload chunk size in bytes | Default 26,214,400 bytes (~26MB) | Maximum 2,145,386,496 bytes (2 GB) Minimum 5,242,880 bytes (5MB) |
| SCAN_CLI_OS | Sets OS value for downloading the correct Signature Scanner tool |  | This optional variable should be set only when running on ALPINE_LINUX. It assists Detect in accurately identifying the environment when standard detection methods (e.g., parsing os-release files) are unavailable. Manually setting this variable ensures correct behavior in restricted or minimal environments. |

Note: Proxy environment variables can be provided to the PowerShell script in both 'Bash' and 'PowerShell' formats. For example a given property name can be specified as "PROPERTY_NAME" or "property.name". The proxy can only be provided to the PowerShell script as an environment variable.
