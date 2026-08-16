---
title: "Release Notes for Jenkins Plugin"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/release-notes-for-jenkins-plugin.html"
content_id: "cw98W6bXF8O9JmLkHqHJ~Q"
version: "11.5.1"
section: "Detect Integrations"
scraped_at: "2026-08-08T23:45:56.609828+00:00"
---

# Release Notes for Jenkins Plugin

## Version 11.0.0

**New features**

- This release is compatible with Black Duck® Detect 11.x.x. (Downloading and using detect11.(sh/ps1)).

**Changed features**

- Updated to use Black Duck® Detect 11.x.x for execution.
- Jenkins version 2.462.3 or later is required.

Note: Configuration and usage of the plugin is unchanged.

## Version 10.0.0

**Notice**

The Synopsys Software Integrity Group is now Black Duck Software, Inc.

- As part of this activity, sig-repo.synopsys.com and detect.synopsys.com are being deprecated and will be decommissioned on March 31st, 2025. Please make use of repo.blackduck.com and detect.blackduck.com respectively.
- Refer to the [Black Duck Domain Change FAQ](https://community.blackduck.com/s/article/Detect-Overview-of-Domain-Changes-for-Black-Duck).

  Note: It is recommended that customers add both `repo.blackduck.com`, and `detect.blackduck.com`, to their allow list, while also maintaining `sig-repo.synopsys.com`, and `detect.synopsys.com`, until March 31st, 2025 when `sig-repo.synopsys.com`, and `detect.synopsys.com`, will be fully replaced by `repo.blackduck.com` and `detect.blackduck.com` respectively.

  Synopsys Detect Jenkins plugin is now the Black Duck® Detect Jenkins plugin.

For existing users, the Black Duck® Detect Jenkins plugin should be considered a fresh installation as the domain has changed.

- Prior to moving from the Detect Jenkins plugin to the Black Duck® Detect Jenkins plugin, you should record your existing system configuration for use reconfiguring your pipelines after installation.
- **Before** installing the Black Duck® Detect Jenkins plugin, read the additional information about the upgrade process.

  Note: For continued functionality and to receive future updates to the Jenkins plugin, you must upgrade to Black Duck® Detect Jenkins plugin version 10.0.0 prior to March 31st, 2025.

If you are a new user, you may proceed with installing the Black Duck® Detect Jenkins plugin as per Downloading and Installing.

**Changed features**

- (IDTCTJNKNS-277) Updated to use the new 'blackduck' namespace.
- Updated to use Black Duck® Detect 10.x.x for execution.

  - Black Duck® Detect Release Notes
- Jenkins version 2.426.3 or later is required.

**Resolved issues**

- The plugin has been built against upgraded Jenkins/Jenkins plugin versions to mitigate known security risks.

## Version 9.0.0

**New features**

- This release is compatible with Synopsys Detect 9.x.x. (Downloading and using detect9.(sh/ps1)).

**Changed features**

- Updated to use Synopsys Detect 9.x.x for execution.
- The plugin has been built against upgraded Jenkins/Jenkins plugin versions in order to mitigate known security risks.
- Jenkins version 2.401.3 or later is required.

Note: Configuration and usage of the plugin is unchanged.

**Resolved issues**

- (IDTCTJNKNS-263) Updated Synopsys Detect Jenkins Plugin to provide consistent behavior for Linux, and Mac Agent when project names have leading or trailing spaces.
- (IDTCTJNKNS-272) Updated Synopsys Detect Jenkins Plugin to support passing '&' in the DETECT_SOURCE_PATH property.

## Version 8.0.1

**Resolved issues**

- (IDTCTJNKNS-266) Resolved the following issues:

  - Jenkins 2.410 fails to start/exits during startup if using the 8.0.0 plugin. [JENKINS-71480](https://issues.jenkins.io/browse/JENKINS-71480)
  - Inclusion of too many dependencies in version 8.0.0 [JENKINS-70671](https://issues.jenkins.io/browse/JENKINS-70671)
  - 8.0.0 bundles pull-parser.jar by mistake. [JENKINS-71023](https://issues.jenkins.io/browse/JENKINS-71023)

Important: Customers running Jenkins version 2.410 and above should upgrade to Synopsys Detect Jenkins plugin 8.0.1

## Version 8.0.0

**New features**

- Updated to be compatible with Synopsys Detect 8.x.x. (Downloading and using detect8.(sh/ps1)).

**Changed features**

- The Jenkins plugin has been upgraded to use Synopsys Detect 8.x.x for execution.
- The plugin has been built against upgraded Jenkins/Jenkins plugin versions in order to mitigate known security risks.
- The minimal Jenkins version required is 2.377.
- Configuration and usage of the plugin is unchanged.

**Resolved issues**

- (IDTCTJNKNS-258) CVE-2022-42889 for Synopsys Detect Jenkins plugin 7.0.0
- (IDTCTJNKNS-261) Synopsys Detect v8 for Jenkins plugin
- (IDTCTJNKNS-255) Update dependency for Jenkins version, including optional plugin dependencies
- (IDTCTJNKNS-254) Only escape Synopsys Detect parameter values
- (IDTCTJNKNS-253) Improve clarity of messages logged when running plugin
- (IDTCTJNKNS-252) Update internal dependencies to latest
- (IDTCTJNKNS-247) Detect shell scripts are executed first and then downloaded in Pipeline execution in Linux and Windows slave nodes
- (IDTCTJNKNS-239) Avoid leaking API token string in the console output
- (IDTCTJNKNS-228) Unable to use java version specified in pipeline when running Synopsys Detect in air gap mode
- (IDTCTJNKNS-224) Improve clarity in the transition between the different stages of Synopsys Detect for Jenkins
- (IDTCTJNKNS-220) Jenkins Build is changed to Unstable for Invalid values in Synopsys Detect Installers
- (IDTCTJNKNS-192) Size must be between 1 and 50 when --detect.project.tag is more than 50 characters

## Version 7.0.0

**New features**

- Update major version to match major version of Synopsys Detect that it runs.
- Update plugin to be compatible with Synopsys Detect 7.x.x. (Downloading and using detect7.(sh/ps1)).

  - Use property detect.timeout instead of blackduck.timeout
  - Remove support for using blackduck.password and blackduck.username and exclusively use blackduck.api.token
- Update UI when configuring plugin so that it will only list 'Secret Text' saved entries (Manage Jenkins -> Configure System -> Synopsys Detect -> Black Duck credentials)

**Changed features**

- When using script (sh/ps1), no longer cache the script. Plugin will download the script on each execution.

## Version 3.1.0

**New features**

- Added the capability to run Synopsys Detect in air gap mode using the Synopsys Detect plugin.

## Version 3.0.0

**New features**

- Added capability to turn off automatic escaping by setting the environment variable DETECT_PLUGIN_ESCAPING to false.

**Resolved issues**

- (IDTCTJNKNS-181) Resolved an issue wherein proxy details could not be determined from Jenkins when running a Black Duck job on a Jenkins agent because it only worked on the Jenkins main node.

**Changed features**

- The Polaris fields in the plugin are removed.

  - This functionality has moved to Synopsys Polaris for Jenkins.
- Updated the minimum version for Jenkins to 2.150.3.
- Connection validation is improved when testing through a proxy.

## Version 2.1.1

**Resolved issues**

- Resolved an issue wherein Synopsys Detect for Jenkins didn't escape commas correctly in PowerShell arguments.
- Resolved an issue wherein Synopsys Detect for Jenkins didn't function when there were spaces in the workspace path resulting in failure to find the shell/PowerShell script.
- Version 2.0.2 of the SSynopsys Detect for Jenkins plugin violated semantic versioning by introducing a non-backward compatible change. Updating to any 2.X version from version 2.0.1 or earlier must be done with caution as that update might break existing functionality.

## Version 2.1.0

**New features**

- Synopsys Detect for Jenkins now returns an exit code of 0 for a successful pipeline run.

**Changed features**

- On build failures, Synopsys Detect for Jenkins no longer modifies the build status when run in a Jenkins pipeline. Now, it throws an exception error if Detect fails.
- Synopsys Detect for Jenkins is improved to support the pipeline step context. Using *withEnv* and running Docker now works as expected.
- Added improvements for working with containers.
- Verified support for Synopsys Detect Jenkins plugin in the Cloudbees Core environment built with Kubernetes.

## Version 2.0.2

**New features**

- Added auto-escaping parameters.

**Changed features**

- Now uses Synopsys Detect site to resolve the shell scripts.

**Resolved issues**

- Resolved an issue wherein a null pointer exception may be thrown when the proxy user name is blank.
- Resolved in issue wherein the plugin was not properly escaping the path to the PowerShell script.  This also improves handling of elements like random pipes in the path.

## Version 2.0.1

**Resolved issues**

- Resolved an issue wherein configuration/connection settings for the plugin are deleted when restarting Jenkins.

## Version 2.0.0

**New features**

- You can now run Synopsys Detect for Jenkins by uploading a Detect JAR file.
- Synopsys Detect for Jenkins now uses the Polaris credentials stored in the credentials plugin in Jenkins.

## Version 1.5.0

**Resolved issues**

- Resolved an issue wherein the proxy settings may be ignored when downloading the jar file.
- Resolved an issue that may have caused an error when connecting to the test repository.

**Changed features**

- Synopsys Detect for Jenkins now displays in parenthesis the version of Detect packaged with the plugin.

## Version 1.4.1

- Maintenance release with overall improvements in stability and security.

## Version 1.4.0

- Added support for converting from a Maven project to a Gradle project.
- Improved error handling for Synopsys Detect exit codes.
- Addressed an issue wherein cancelling a Synopsys Detect job was not terminating correctly.

## Version 1.3.0

- Added support for Java 8.
- Synopsys Detect for Jenkins now supports Jenkins version 2.60.1 and higher.
- Added API key support.
- Added support for Microsoft NT Lan Manager (NTLM) protocol.

## Version 1.2.0

- Added support for Java 7.
- Now includes support for an Artifactory URL override option.

## Version 1.1.0

- Added DSL support.

## Version 1.0.2

**Resolved Issues**

- Subordinate nodes do not use the proxy to download the Synopsys Detect *.jar* file (potential fix)

## Version 1.0.1

**Resolved Issues**

- Resolved an issue wherein *JenkinsProxyHelper.shouldUseProxy* (final URL, final String noProxyHosts) was incorrectly returning *false* if the Hub URL was set, and incorrectly returning *true* when the Hub host name should be ignored.
- Resolved an issue with the Java executable path.

## Version 1.0.0

- First release of product
