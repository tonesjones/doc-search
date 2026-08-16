---
title: "Project settings via JSON"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/project-settings-via-json.html"
content_id: "B1bJzejZZPtJweRVLCffuw"
version: "11.5.1"
section: "Configuring Detect"
scraped_at: "2026-08-08T23:44:19.432957+00:00"
---

# Project settings via JSON

The `detect.project.settings` property allows for submission of several project related properties to Detect in one JSON file.

The JSON file can include a subset of fields supported by Black Duck SCA SCA for the projects and versions API endpoints.

Note: For more information about Black Duck SCA SCA API endpoints, please refer to the REST API Developers Guide available via the Black Duck SCA SCA UI.

Adding the following parameter to a run of Detect allows you to use a JSON file for specifying multiple project-related property settings:

```
--detect.project.settings=<Path to .json file containing project property settings>
```

The `.json` file should contain a JSON object with any of the following `detect.project` properties, linked to their respective documentation content, specified as key-value pairs:

- detect.project.name
- detect.project.description
- detect.project.tier
- detect.project.level.adjustments
- detect.project.clone.categories
- detect.project.deep.license
- detect.project.version.name
- detect.project.version.nickname
- detect.project.version.notes
- detect.project.version.phase
- detect.project.version.distribution
- detect.project.version.update

Important: `detect.project` properties specified on the command line take precedence over values specified in the JSON file.

## JSON file example

```
{
  "name": "project-name",                 // detect.project.name
  "description": "project description",   // detect.project.description
  "projectTier": 3,                       // detect.project.tier
  "projectLevelAdjustments": true,        // detect.project.level.adjustments
  "cloneCategories": "ALL",               // detect.project.clone.categories
  "deepLicenseDataEnabled": true,         // detect.project.deep.license
  "versionRequest": {
    "versionName": "1.0.0",               // detect.project.version.name
    "nickname": "nickname",               // detect.project.version.nickname
    "releaseComments": "releaseComments", // detect.project.version.notes
    "phase": "DEVELOPMENT",               // detect.project.version.phase
    "distribution": "EXTERNAL",           // detect.project.version.distribution
    "update": false                       // detect.project.version.update
  }
}
```
