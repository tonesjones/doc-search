---
title: "Polaris prerequisites"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/polaris-prerequisites.html"
content_id: "~U27n0Nuq3p3rhWPibQicA"
version: "latest"
section: "Bridge CLI"
scraped_at: "2026-08-08T23:46:57.602384+00:00"
---

# Polaris prerequisites

To integrate Polaris with Bridge the following prerequisites are required:

1. Access to a Polaris server with permission granted to create access tokens and projects.
2. A [Polaris access token](hhttps://docs.blackduck.com/access?ft:originId=cba15d77e1e0a5989f94dbbae8f7dd44/0d97d272fb42796be0f9f52928a17d57.topic) or [service account token](https://docs.blackduck.com/access?ft:originId=4411d74355056751ace3917564d29bc0/ae0e60062f785563c1907b533597e5dd.topic) to allow integration with a Polaris server instance.
3. Bridge automates application onboarding based on license model:

   | License model | Description | Onboarding |
   | --- | --- | --- |
   | Concurrent(team member) | - Seat based license model | - Automated onboarding for SAST and SCA scans - Unlimited applications, projects and branches can be created. |
   | Subscriptions | - Customers purchase a specific number of applications. - An application contains one or more entitlements(SAST, DAST or SCA) that determine what type of tests can be run on Polaris. | - Application should be [created](https://docs.blackduck.com/access?ft:originId=4411d74355056751ace3917564d29bc0/fe4d8a4f06e42cc9d7c593e1f83ee5f2.topic) manually before SAST and/or SCA scan is run. |

   Note: For DAST assessments the application and project must be created manually. DAST projects require additional configurations when [Creating A DAST projects for Web Applications and APIs](https://docs.blackduck.com/access?ft:originId=4411d74355056751ace3917564d29bc0/0512dbec44b6eba533ecfced82de0f4c.topic).
4. Languages that are compiled with a build system (e.g. C++ Make, Java Maven, C# dotnet CLI and MSBuild) require configuration for Coverity to capture and analyze the build.
   1. Configuration details are provided in this guide.
   2. The pipeline environment should have the required build tools installed.
   3. Languages that do not require a build system are detected and configured automatically.
