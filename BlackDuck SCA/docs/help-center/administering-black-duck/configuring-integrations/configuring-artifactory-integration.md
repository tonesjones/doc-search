---
title: "Configuring Artifactory Integration"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/configuring-artifactory-integration.html"
content_id: "aHOMTFWSce2ymoKn3Bx97g"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:31:57.403597+00:00"
---

# Configuring Artifactory Integration

The Artifactory Integration is a new mechanism to protect the Software Supply Chain.
Since Artifactory is typically one of the last links of that chain, scanning each and
every artifact within a configured set of Artifactory Repositories allows customers to
have control of their individual supply chain.

Note: In order to take advantage of this feature, you must have **Artifactory Integration** enabled on your
product registration key.

## Enabling Artifactory Integration

Add the following in your `values.yaml` file:

```
enableIntegration: true
```

For more information on how to configure Artifactory Integration in your environment,
please refer to [Artifactory Integration](https://documentation.blackduck.com/bundle/bd-iarth/page/topics/artifactoryIntegration.html).

To access the Integrations page:

1. Log in to Black Duck with the Integration Manager role.
2. Click [image: image] .
3. Click **Integrations**.

## Adding an Artifactory server

From the Integrations page, you can add an Artifactory server by following the steps
below:

1. Click **Artifactory Repositories** from the left-hand menu.
2. Click the **+ Add Server** button.
3. Add the following information:

   - Enter the **Name** of your Artifactory server. This field is
     mandatory.
   - Check the **Enable Server** checkbox if this server is ready for
     use.
   - Use the **Search Interval** slider to select a desired polling
     time for your server.

     CAUTION:

     Avoid setting the **Search Interval** lower than
     1 minute in the **Artifact Repositories** configuration, as doing
     so can interfere with other jobs running properly.
   - Use the **Storage Limit** slider to select the maximum space that can
     be used by artifacts while being scanned.
   - Enter a **Search Cutoff Date** in the date selector to set a date
     where artifacts having a `lastUpdated` time prior to this
     value will not be subject to the blocking strategy set for the
     repository regardless of the blocking strategy value.
4. Click the **+ Add Repository** button to add a repository.

   [image: Add Repository dialog box]

   - Enter the **Repository Name**.
   - Check any of the **Lightweight BOM** or **Docker** checkboxes if
     they apply to your repository. A lightweight BOM is a data store with
     minimum set of functionalities which can scale to store large number of
     persistent project versions within Black Duck.
     Enabling this option will build a json file when the artifacts in the
     repository are scanned. Vulnerabilities are asynchroneously updated from
     the KnowledgeBase. The JSON file will be replaced by a Black Duck User interface in the upcoming
     releases.

     Note: Starting with Artifactory plugin 2.1.0, the Docker flag is no
     longer honored as the repository type is now identified
     automatically. This flag will be removed in a future Black Duck release.
   - Select the **Blocking Strategy** for your repository.

   You can also add additional **Filtering Options** by clicking the link.
   Available options are:

   - **Folder Names**: Enter a folder name to add to the list of folders
     in this repository which should be searched for artifacts to scan.
   - **Exclude Patterns**: Wildcard filter of file patterns which will
     exclude an artifact from being subject to the blocking strategy
     provided. An empty value indicates no files are excluded.
   - **Include Patterns**: Wildcard filter of file patterns which are
     subject to the blocking strategy provided. An empty value indicates all
     files are to be included.

## Modifying an Artifactory server

From the Integrations page, you can edit an Artifactory server by following the steps
below:

1. Click your server from the displayed list or click the [image: Options button] button at the end of your server and select **Edit**. The
   Artifactory server's page appears.

   [image: image]
2. Edit the desired field(s).
3. Click the **Save** button.

## Deleting an Artifactory server

From the Integrations page, you can delete an Artifactory server by clicking the
[image: Options button] button at the end of your server and selecting **Delete** or by clicking
your server from the displayed list and then clicking the **Delete Server**
button from the Artifactory Server page.
