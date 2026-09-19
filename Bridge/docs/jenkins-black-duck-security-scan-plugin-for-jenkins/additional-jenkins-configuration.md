---
title: "Additional Jenkins configuration"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/additional-jenkins-configuration.html"
content_id: "~Ulu5ax3LXOw3pSQsF3O_A"
version: "latest"
section: "Jenkins - Black Duck Security Scan Plugin for Jenkins"
scraped_at: "2026-08-08T23:48:48.775830+00:00"
---

# Additional Jenkins configuration

On this page you will find details about additional Jenkins configurations. Use the list below to navigate topics.

- Bridge CLI parameters
- Air-gapped usage
- Proxy support
- Using Docker containers

## Bridge CLI parameters

| Input parameter | description |
| --- | --- |
| `bridgecli_install_directory` | Provide a path, where you want to install or have already installed Bridge CLI.  If no path is provided, Bridge will use `$HOME/bridge-cli`. If Bridge CLI is already installed there but is not the latest version, the latest will be downloaded. |
| `bridgecli_download_url` | Provide a URL to the storage location of your Bridge ZIP file. Bridge CLI will be automatically downloaded from there to `bridgecli_install_directory` or the default path when a pipeline runs. The destination will be cleaned before every installation. |
| `bridgecli_download_version` | Specify the bridge version you want to download and configure. |
| `include_diagnostics` | When **true** the detailed Bridge logs appear in the console and Bridge diagnostics are uploaded in Jenkins Archive Artifact. |
| `network_airgap` | When network_airgap is `true`, the Black Duck Security Scan Plugin does not install Bridge. Bridge must already be present in one of the following locations:   - In the default Bridge installation path ($home/bridge-cli) - In the location specified by bridgecli_install_directory. - In the location specified by    ```   bridgecli_download_url.   ```   If Bridge isn't found, the plug-in errors out.  When the `bridgecli_download_url` is set:   - The ZIP is downloaded to the default directory or to bridgecli_install_directory, unless the same version is already installed there. Once downloaded, it is used and then cached. - If the same version already exists in the default directory, it is used without downloading from `bridgecli_download_url.` - The bridgecli_download_url should contain version information (Example: **https://subdomain.artifactory.com/bridge-cli/1.0.7/bridge.zip.** In this case, 1.0.7 is the version info.) If the URL doesn't contain version information, the plug-in looks for a versions.txt file in the same directory as the Bridge ZIP, and if none is found, Bridge is not cached after the pipeline runs. |
| `mark_build_status` | Specify the build status if issues are present. Default value: `FAILURE`.  Supported values: `FAILURE`,`UNSTABLE`,`SUCCESS` |

Note: If neither **bridgecli_download_version** nor **bridgecli_download_url** is provided, the plugin will download and configure the latest version of Bridge.

## Air-gapped usage

You can set up the Black Duck Security Scan Plugin for Jenkins to use a cached version of Bridge rather than downloading from our internet-accessible repository. This is useful for any of the following situations:

- Your scans run in an air-gapped environment.
- You don't want your build machine to make a connection through the firewall.
- Black Duck Support directed you to use a custom version of Bridge.

To use the plug-in without an internet connection, do the following:

1. Store an uncompressed version of Bridge locally. (Extract the ZIP file that you downloaded from Black Duck.) The latest version is available at: [repo.blackduck.com](https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/).
2. Set `bridgecli_download_url` with the location of your stored copy. This URL should be your internal instance of `repo.blackduck.com` or a similar repository service.
3. Set the value of `network_airgap` to `true`.

## Proxy support

Here are two common methods for declaring proxy settings in Jenkins:

1. Utilize the `environment` block in the Jenkinsfile.

   |  |
   | --- |
   | `environment { HTTP_PROXY = 'http://proxyIP:proxyPort' }` |
2. Employ the `export` keyword.

   |  |
   | --- |
   | `export HTTP_PROXY=http://proxyIP:proxyPort` |

Black Duck Security Scan Plugin supports the following environment variables.

| Name | Format | Example |
| --- | --- | --- |
| HTTP_PROXY / http_proxy | `http://user:password@proxyIP:proxyPort/` | `HTTP_PROXY="http://bob.example.com:1010"`  `http_proxy="http://username:password@alice.example.com:1030"` |
| HTTPS_PROXY / https_proxy | `https://user:password@proxyIP:proxyPort/` | `https_proxy="http://bob.example.com:1010"`  `HTTPS_PROXY="http://username:password@alice.example.com:1030"` |
| NO_PROXY / no_proxy | Comma separated list of URLs/addresses for which proxy is not used | `no_proxy="cern.ch,some.domain:8001,192.168.1.57"` |

- Proxy with auth: Users need to pass a username and password for authentication.

  Example: **http://user:password@proxyIP:proxyPort/**
- Proxy with no auth: Users do not need to pass credentials for authentication.

  Example: **http://proxyIP:proxyPort/**

If proxy configuration requires authentication and the agent needs to run behind the proxy, pass parameters with authentication data when connecting the agent to the controller.

## Using Docker containers

This guide explains how to configure the Black Duck Security Scan Plugin in Jenkins pipelines that use Docker agents. When using Docker agents, it is essential to mount specific directories into the container to ensure the the plugin functions correctly.

**Required environment variable:** `-e HOME=$HOME` must be provided. The Bridge CLI needs this variable so it can download and execute the necessary tools in the default `$HOME` path.

**Required mount paths:** To enable the plugin to invoke the Bridge CLI and access necessary configuration files, mount the following paths into your Docker container:

1. Bridge CLI installation directory

   - Default Path: `$HOME/bridge-cli-bundle`
   - Custom Path: If you installed the Bridge CLI elsewhere (e.g., `/opt/blackduck/bridge-cli-bundle`), mount that path instead.
2. Black Duck configuration directory
   - Path: `$HOME/.blackduck`
   - This is where the CLI downloads and stores product specific files and tools.
   - If you have pre-configured Detect or Coverity tools in a specific custom path on your host machine, make sure to mount that path into your pipeline to use those tools effectively.
3. `input.json` path
   - Path: `$JENKINS_HOME`
   - This is where the plugin writes the `input.json` file used by the Bridge CLI.

Refer to the [Docker documentation](https://docs.docker.com/engine/storage/bind-mounts/#choose-the--v-or---mount-flag) for more information.

**Jenkins pipeline configuration**

Use the `args` field in the `docker` block to mount the required volumes.

**Example 1: Using default Bridge CLI Path**

```
pipeline {
    agent {
        docker {
            ...
            args '-e HOME=$HOME -v $HOME/bridge-cli-bundle:$HOME/bridge-cli-bundle -v $HOME/.blackduck:$HOME/.blackduck -v $JENKINS_HOME:$JENKINS_HOME'
        }
    ...
...
```

**Example 2: Using custom Bridge CLI path**

If you installed the Bridge CLI in a custom directory (e.g., `/opt/blackduck/bridge-cli-bundle`), update the mount accordingly:

```
pipeline {
    agent {
        docker {
            ...
            args '-e HOME=$HOME -v /opt/blackduck/bridge-cli-bundle:/opt/blackduck/bridge-cli-bundle -v $HOME/.blackduck:$HOME/.blackduck -v $JENKINS_HOME:$JENKINS_HOME'
        }
    ...
...
```

**Notes**

- Ensure that the Bridge CLI is executable within the container by mounting the Bridge CLI path.
- The mounted `$JENKINS_HOME` and `$HOME/.blackduck` paths must be accessible and writable by the container user.
- If you are using a Jenkins agent running on a remote node, ensure the paths are valid on that node.
- For using any custom path in the pipeline, make your to mount those custom paths.

**Jenkins docker agent limitations**

- Docker agents are ephemeral and do not persist across builds.
- Jenkins does not treat Docker containers as separate nodes.
- Therefore, tools like the Bridge CLI must be installed and managed on the host, not inside the container.
- All required files and tools must be mounted into the container from the host system.

**Troubleshooting**

- Bridge CLI not found: Verify the mount path and ensure the CLI is installed and executable.
- `input.json` not found: Ensure `$JENKINS_HOME` is correctly mounted and writable.
- Permission denied errors (e.g., `mkdir /.blackduck`): Ensure `HOME` is set correctly and `$HOME/.blackduck` is mounted and writable.
