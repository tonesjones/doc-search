---
title: "How to run Container Analysis"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/how-to-run-container-analysis.html"
content_id: "f2O5v4f8zAorOgMSrmfytA"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-10-04T23:29:16.411760+00:00"
content_hash: "cc1acf05a8f62636843d78b3f505626c0d8cb15a8fdefb36be4ec79eac0c8136"
---

# How to run Container Analysis

How to run a Container Analysis test on a container image from the Polaris user interface.

Before you begin:

- You need a Container Analysis project. See [Container Analysis](../container-analysis.md).
- Export the container image you want to scan as a .tar file using `docker save`.

## Run a Container Analysis scan

Follow these steps to run a Container Analysis scan from the Polaris user interface:

1. There's more than one way to start this procedure:
   - Go to Portfolio, select an application, click the options icon at the end of the Container Analysis project's row, and select New Test.
   - Go to Tests and select New Test.
2. Use the Application, Project, and Container dropdown menus to select the container to scan.

   Note: Depending on how you started the test, some of these fields may already be filled in.
3. Upload the container image .tar file by dragging and dropping it into the upload zone, or by selecting Browse Files.

   Important: The file must be a .tar archive exported with `docker save`. Uploading an invalid archive will result in an error.
4. Select Begin Test.

   Note: The Begin Test button is locked until the file upload completes.

Monitor test progress on the Tests page (accessible from the left-hand navbar). Newer tests appear near the top of the page. Filter tests by date, type, mode, status, and the application, project, or container tested.

## View container layers for a component

View the container layers that introduced or modified a component identified in a Container Analysis test.

1. Go to Portfolio, select an application, and select a Container Analysis project.
2. Open the Components tab.
3. Select the name of a component to open its details.
4. Select the Component Details tab, then scroll to Container Layers to view the layers in which the component was introduced and, if applicable, modified.

   Each layer includes the command that touches the component (typically, `ADD`, `RUN`, or `COPY`).
