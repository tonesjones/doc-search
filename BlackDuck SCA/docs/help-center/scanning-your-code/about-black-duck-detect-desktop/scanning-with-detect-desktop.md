---
title: "Scanning with Detect Desktop"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/scanning-with-detect-desktop.html"
content_id: "xnRc590TmZDKZKAmRTYcFg"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T14:53:29.339025+00:00"
---

# Scanning with Detect Desktop

Black Duck Detect Desktop makes it easier to scan:

- Source directories
- Binaries or executables
- Containers
- Docker images or distributions

By default, all scans are uploaded to the Black Duck server and
mapped to a project version. However, you can create a scan file as described here, to output the scan to a file which you can later
upload to Black Duck.

To specify project and/or version names:

1. Click [image: Pencil icon] located next to **Project Settings**.
2. Select **Project Name** and/or **Version Name**. The fields appear in
   the UI.
3. Specify the values for the field(s).

## Scanning your code with Detect Desktop

Detect Desktop supports multiple scanning methods to help you analyze different types
of code artifacts from your local environment. Whether you're working with source
code, binaries, or container images, Detect Desktop simplifies the process by
automatically detect and applying the the appropriate technique based on your
input.

To perform a scan:

1. Click [image: Scan icon] .
2. From the **What type of scan?** dropdown menu, select the desired scan
   type:

   - **Source Directory**. Scans source and build data for a
     project.
   - **Binary/Executable**. Scans a single binary or executable
     file.
   - **Container Scan**. Scan each layer of your container.
   - **Docker Inspector**. Scans an image name or distribution file
     (.tar) with Docker Inspector.
3. When selecting **Source Directory**, **Container Scan**, or **Docker
   Inspector** as the scan type, you must also specify a Scan Mode:

   - **Intelligent**: Performs a full analysis using multiple scanning
     techniques. Recommended for most use cases where accuracy is
     important.
   - **Rapid**. Prioritizes speed over depth by focusing on faster
     scanning methods. Ideal for quick assessments or when immediate
     feedback is needed.
   - **Stateless**. Runs the scan without storing results on the
     scanning machine and avoids using local scan state. Useful in
     automated or ephemeral environments where persistence is not
     required.
4. The way you provide input to Detect Desktop varies depending on the selected
   Scan Type. After choosing a scan type from the What type of scan downdown
   menu, you'll be prompted to select the appropriate file, direct, container
   image for analysis:

   - For **Source Directory**, **Binary/Executable**, and
     **Container Scan**: Click [image: Folder icon] and select the directory/file/container scan target you
     would like to scan.
   - For **Docker Inspector**, select either:

     - **Docker image name**: Provide a container image name
       (e.g., alpine:latest).
     - **Docker archive (.tar)**: Click [image: Folder icon] and select a Docker archive file (.tar) .
5. Click **Scan**.

   The status of the scan appears along with an option to cancel the scan.

You can optionally configure **Project Settings** or **Scan Settings** by clicking
[image: Pencil icon] next to each section. If your organization has a Snippet Scanning license
and you wish to enable it, go to **Scan Settings**, select **Snippet
Matching**, and toggle it on.

When the scan is complete, select the **History** tab to view information on the
completed scan. From this tab, you can manage your scan. You can also view the uploaded scan using the **Black
Duck** tab.

Note: An error message appears if you exceed the scan size
limit, which is 5 GB (6 GB for Black Duck Binary Analysis). Contact Customer
Support if you receive this message.

## Creating a scan file (offline mode)

Detect Desktop allows you to generate a scan file that can be uploaded to Black Duck later. This is especially useful for offline or
air-gapped environments, or when your organization prefers to review scans before
upload.

Note: Snippet scanning is not supported in offline mode, as it requires communication with the
Black Duck server.

To create a scan file, toggle **Offline Mode** to the on position and perform a
scan as described above.

Once the scan is complete, go to the **History** tab to view and manage the
generated scan file. You can later upload this scan file using the command line, or
by using the Black Duck UI.
