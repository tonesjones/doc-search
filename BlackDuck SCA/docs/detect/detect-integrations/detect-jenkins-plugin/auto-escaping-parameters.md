---
title: "Auto-escaping Parameters"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/auto-escaping-parameters.html"
content_id: "a5HYUdaxYY0cwIhiBJHefA"
version: "11.5.1"
section: "Detect Integrations"
scraped_at: "2026-08-08T23:46:02.644375+00:00"
---

# Auto-escaping Parameters

In Jenkins integrations for Black Duck® Detect, several special parameters are automatically escaped.
The workflows pertaining to quotation marks and spaces are as follows.

- Detect properties must be separated by spaces or carriage returns/line feeds.
- Values containing spaces must be surrounded by either single or double quotation marks ('single' or "double") for Linux and Mac agents while for Windows you must use single quotes ('single').
- Values containing single quotes must be surrounded with double quotation marks.
- Values containing double quotes must be surrounded with single quotation marks.

## Considerations for name escaping conventions for Black Duck® Detect for Jenkins

You can turn off auto escaping by setting the environment variable *DETECT_PLUGIN_ESCAPING* to false.
Jenkins enables you to set an environment variable at different levels, such as globally or on a per-job basis. If you set the environment variable globally to one value, you can set it at the job level to another value. It is recommended to set the environment variable globally to skip escaping (ensuring past jobs work as expected), and then if you want to make jobs with the auto escaping enabled, you modify the environment variable flag in that job's configuration to enable escaping the characters. The easiest way to accomplish this is to install the ["Environment Injector" Jenkins plugin](https://plugins.jenkins.io/envinject/).

**Note:** In Black Duck® Detect plugin version 10, the above recommendations remain the same for agents on Windows systems. For those agents running on 'NIX systems, *DETECT_PLUGIN_ESCAPING* should be set to false. Ensure that you adhere to the quoting conventions described above. Any input with spaces in the Jenkins configuration should be enclosed in quotes.

Black Duck® Detect for Jenkins allows some special characters when *DETECT_PLUGIN_ESCAPING* is set to false, and spaces can be included without escape sequences provided that they are enclosed in single or double quotes as described above for different agents. Therefore, instead of `My\ Test\ Project1`, you can pass it as `'My Test Project1'`, the project will be created and uploaded to Black Duck SCA as `My Test Project1*.*`

When *DETECT_PLUGIN_ESCAPING* is set to true, you can provide values that are enclosed in double quotes. For instance, values such as "Windows Project" may be included in the arguments.
