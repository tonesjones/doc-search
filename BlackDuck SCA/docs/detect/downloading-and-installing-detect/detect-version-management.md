---
title: "Detect Version Management"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/detect-version-management.html"
content_id: "6D23NaLqMtQC1EE1g6d52A"
version: "11.5.1"
section: "Downloading and Installing Detect"
scraped_at: "2026-08-08T23:44:02.774412+00:00"
---

# Detect Version Management

Detect self-updating feature will allow customers who choose to enable Centralized Detect Version Management in Black Duck SCA to automate the update of Detect across their pipelines.

## Self updating Detect scenarios

The Self Update feature will call the `/api/tools/detect` API end point to check for the existence of a specified Detect version in Black Duck SCA under the **Admin > System Settings > Detect > Detect Version** drop-down. If a version that is eligible for upgrade or downgrade has been specified, the request to download that version of the Detect .jar will execute and the current run of Detect will invoke it for the requested scan.

Detect will download the required version from the repository when the service is hosted, or from a custom URL as configured in Black Duck SCA, when internally hosted. To support self-update via internal hosting, the Detect binary must be in a location accessible via https to all executing Detect instances.Centralized Detect Version Management feature support in Black Duck SCA is available from Black Duck SCA version 2023.4.0 onwards.

Note:

- If the Black Duck **Internally Hosted** option has been configured, Detect will be downloaded via https on the client side from the fully formatted URL specified under the "Hosting Location for Detect" setting. This setting over-rides version and integrity checks that would otherwise be performed by Detect.
- If the Black Duck **Hosted** option has been configued, Detect will be downloaded on the client side from the repository.

## Scenarios where Detect self update will not execute

If there exists no mapping in Black Duck SCA, or if the current version of Detect matches the mapped version in Black Duck SCA, or any issue occurs during the execution of the Self Update feature, then Detect will continue with the current version to execute the scan.

If the Detect URL of the Detect .jar file to download and run has been hardcoded via Detect property `DETECT_SOURCE` environment variable or the Detect version set by the `DETECT_LATEST_RELEASE_VERSION` or `DETECT_VERSION_KEY` variables, self update will not occur. These are optional System environment properties used by Detect upgrade scripts.

If the Black Duck SCA “Internally Hosted” option has been selected and a Detect download location has not been provided, the feature will not be enabled.

For further Black Duck SCA configuration information, refer to the documentation provided under the topic:
 Hosting location for Detect.

### Detect log examples for self update

Downgrade to prior version blocked:

```
2024-10-31 12:20:57 EDT INFO  \[main] - Detect-Self-Updater:  Checking https://test1.blackduck‎.com/api/tools/detect API for centrally managed Detect version to download to /Users/testuser/tmp.   

2024-10-31 12:21:03 EDT WARN  \[main] - Detect-Self-Updater:  The Detect version 8.7.0 mapped at Black Duck SCA server is not eligible for downgrade as it lacks the self-update feature. The self-update feature is available from 8.9.0 onwards.
```

Update to version allowed (8.9.0+):

```
2024-10-31 12:33:52 EDT INFO  \[main] - Detect-Self-Updater:  Checking https://test1.blackduck‎.com/api/tools/detect API for centrally managed Detect version to download to /Users/testuser/tmp.  

2024-10-31 12:33:53 EDT WARN  \[main] - Detect-Self-Updater:  The Detect version 10.0.0 mapped at Black Duck SCA server is eligible for downgrade from the current version of 10.0.1. The self-update feature is available from 8.9.0 onwards.

2024-10-31 12:33:53 EDT INFO  \[main] - Detect-Self-Updater:  Centrally managed version of Detect was downloaded successfully and is ready to be run: /Users/testuser/tmp/detect-10.0.0.jar.
```

Current version of Detect matches the mapped version or there is no mapped version in Black Duck SCA:

```
2024-10-31 12:33:52 EDT INFO  \[main] - Detect-Self-Updater:  Checking https://test1.blackduck‎.com/api/tools/detect API for centrally managed Detect version to download to /Users/testuser/tmp.  

2024-10-31 12:33:53 EDT INFO  \[main] - Detect-Self-Updater:  Present Detect installation is up to date - skipping download.
```

Important:

- Downgrading to versions earlier than 8.9.0 is not supported.
- This feature is not available in offline 'blackduck.offline.mode=true' or air gap configurations or if the [bd_product_short] URL has not been provided via the `blackduck.url` variable.
- When running an "Internally Hosted" instance of [detect_product_short] and using custom scripts, checks should be made to prevent [detect_product_short] from querying [bd_product_short] for version management and re-downloading itself.
- Self update makes it easy to switch to a new major [detect_product_short] version, so care should be taken to validate that automated scanning is not impacted.
