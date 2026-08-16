---
title: "Detect Exit Codes"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/detect-exit-codes.html"
content_id: "sj1yFly8UOQj9Uz5noKO_g"
version: "11.5.1"
section: "Troubleshooting"
scraped_at: "2026-08-08T23:45:52.665023+00:00"
---

# Detect Exit Codes

| Exit Code Key | Value | Description |
| --- | --- | --- |
| SUCCESS | 0 | Detect exited successfully. |
| FAILURE_BLACKDUCK_CONNECTIVITY | 1 | Detect was unable to connect to Black Duck SCA. Check your configuration and connection. |
| FAILURE_TIMEOUT | 2 | Detect was unable to wait for actions to be completed on Black Duck SCA. Check your Black Duck SCA server or increase your timeout. |
| FAILURE_POLICY_VIOLATION | 3 | Detect found policy violations. |
| FAILURE_PROXY_CONNECTIVITY | 4 | Detect was unable to use the configured proxy. Check your configuration and connection. |
| FAILURE_DETECTOR | 5 | Detect had one or more detector failures while extracting dependencies. Check that all projects build and your environment is configured correctly. |
| FAILURE_SCAN | 6 | Detect was unable to run the signature scanner against your source. Check your configuration. |
| FAILURE_CONFIGURATION | 7 | Detect was unable to start due to configuration issues. Check and fix your configuration. |
| FAILURE_DETECTOR_REQUIRED | 9 | Detect did not run all of the required detectors. Fix detector issues or disable required detectors. |
| FAILURE_BLACKDUCK_VERSION_NOT_SUPPORTED | 10 | Detect's configuration requires a Black Duck SCA capability that is not supported by your version of Black Duck SCA. Ensure that your Black Duck SCA version is compatible with this version of Detect. |
| FAILURE_BLACKDUCK_FEATURE_ERROR | 11 | Detect encountered an error while trying to perform an operation on Black Duck SCA. Ensure that your Black Duck SCA version is compatible with this version of Detect, your Black Duck SCA user account has the required roles, and the project version exists in Black Duck SCA when using BOM_COMPARE mode in a rapid scan. |
| FAILURE_MINIMUM_INTERVAL_NOT_MET | 13 | Detect did not wait the minimum required scan interval. |
| FAILURE_IAC | 14 | Detect was unable to perform IaC Scan against your source. Please check your configuration, and see logs and IaC Scanner documentation for more information. |
| FAILURE_ACCURACY_NOT_MET | 15 | Detect was unable to meet the required accuracy. |
| FAILURE_OUT_OF_MEMORY | 16 | Detect encountered an Out of Memory error. Please review memory settings and system resources. |
| FAILURE_IMAGE_NOT_AVAILABLE | 20 | Image scan attempted but no return data available. |
| FAILURE_BLACKDUCK_DUPLICATE_PROJECT_ERROR | 21 | Project name already exists, unable to create project. |
| FAILURE_COMPONENT_LOCATION_ANALYSIS | 25 | Component Location Analysis failed. |
| FAILURE_BOM_PREPARATION | 30 | Black Duck SCA failed to prepare BOM for the scan. |
| FAILURE_GENERAL_ERROR | 99 | Detect encountered a known error, details of the error are provided. |
| FAILURE_UNKNOWN_ERROR | 100 | Detect encountered an unknown error. |
