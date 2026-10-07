---
title: "Black Duck C/CPP tool quickstart guide"
source_url: "https://docs.blackduck.com/r/blackduck-tools/latest/black-duck-tools/black-duck-c/cpp-tool-quickstart-guide.html"
content_id: "0srW4O_agivlsh6QavfU6w"
version: "latest"
section: "Black Duck C/CPP Tool"
scraped_at: "2026-10-04T23:32:44.027633+00:00"
content_hash: "10d1910e519d5347ebe268429f7dd00f5c37c4a0243db2319f6abb55c1051746"
---

# Black Duck C/CPP tool quickstart guide

## Prerequisites

In order to run the Black Duck C/CPP tool, you must first:

- have a registered Black Duck SCA account.
- have Black Duck SCA 2020.10.0 or greater installed.
- have a Black Duck SCA API authentication
  token.

## Running the Black Duck C/CPP tool

Follow the steps below to run the Black Duck C/CPP tool:

1. Install the Black Duck C/CPP tool.
2. Run the Black Duck C/CPP tool command.

   ```
   blackduck-c-cpp -d BUILD_DIR -proj PROJECT_NAME -vers PROJECT_VERSION -bd bd_url -a api_token
   ```

   Note: Optionally, you can configure the
   Black Duck C/CPP tool using a yaml file.
3. View the [results](https://documentation.blackduck.com/bundle/bd-hub/page/InternalProjectVersions/Understanding_project_version_BOM_information.html) in Black Duck SCA.
