---
title: "Building a full analysis kit and automatically uploading the kit to Connect during deployment"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/building-a-full-analysis-kit-and-automatically-uploading-the-kit-to-connect-during-deployment.html"
content_id: "Q3qlfncmpoOUYc49ItW_xA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:44:23.319404+00:00"
---

# Building a full analysis kit and automatically uploading the kit to Connect during deployment

Perform this procedure if any user (programmer) needs to perform a local analysis using
the full analysis client. This procedure creates a kit which contains the analysis
client image and the license file. You perform this procedure when you need to provide a
new analysis image version or new license file.

Users (programmers) who need to run a local analysis must download Coverity Analysis
product packages and `license.dat` file from the Connect UI
Downloads page to their local system. For these files to be
available to the programmer (end user), the Coverity administrator must upload these
files into Connect. This procedure describes how to build an analysis kit and configure
the Helm chart to automatically upload the kit to Connect. With Coverity deployed in a
Kubernetes cluster, if Coverity is restarted for any reason such as an upgrade, these
files will be available in the Connect UI.

Important:

The license file is not automatically provided through the Connect UI, Do not use
analysis client images directly from the [repo.blackduck.com](https://repo.blackduck.com/) repository unless you
also have a way to provide the `license.dat` file to your analysis
users. The analysis images will not work without a license.

In this procedure, you will:

1. Pull the full-analysis client files from the Black Duck registry, tag them, then
   push them to your private registry.
2. Obtain the Coverity `license.dat` file and save it to your private
   registry.
3. Create a Dockerfile.
4. Build a Docker image from the files and save the image in your private
   registry.
5. In the Helm chart, create an init container that automatically copies the Docker
   image to Coverity Connect storage.

Important: We recommend that you create your own private
Docker registry. This procedure assumes that you have created one. Refer to Create your own private Docker registry.

Note: This procedure uses BusyBox tools. Refer to <https://busybox.net/>.

To generate Coverity analysis package files and upload them to Connect:

1. Create a `/cov_analysis` directory on your local system.
2. Change directory cd into the /cov_analysis
   directory.

   ```
   cd /cov_analysis
   ```
3. Download each needed Coverity Analysis package from the Black Duck registry using `curl`.

   For a list of files, see Coverity client installer and documentation files. These files are
   available for several operating systems and several Coverity releases, including
   the current release. You can download files for any supported version as listed
   in the following section for this release: Supported Coverity Tools (Thin Client) and full analysis client versions.

   Download the desired files from the Black Duck registry using the following
   `curl` command syntax: Each `curl` command
   downloads one file.

   ```
   curl https://repo.blackduck.com/coverity-releases/<COVERITY_VERSION>/cov-analysis-linux64-<ANALYSIS_VERSIION>.sh
      -o cov-analysis-linux64-<ANALYSIS_VERSION>.sh -u <user:password>
   ```

   where:

   - `<COVERITY_VERSION>` is the Coverity release version.
   - `<ANALYSIS_VERSION>` is the full analysis client
     version.
   - `<user:password>` are your Black Duck registry credentials
     that you can obtain from Black Duck community. See Access the Black Duck private Docker registry credentials.

   For example, to download the Linux64 .sh file for the 2026.6.0
   release:

   ```
   curl https://repo.blackduck.com/coverity-releases/2026.6.0/cov-analysis-linux64-2026.6.0.sh
      -o cov-analysis-linux64-2026.6.0.sh -u <user:password>
   ```
4. Download the analysis SAVE `license.dat` file into
   `/cov_analysis/`.
5. Create a Dockerfile that copies the downloaded installer packages from the
   `/cov_analysis/` directory to a new downloads directory. This
   step copies the downloaded analysis files for all versions, and the license
   file, to a Dockerfile.

   ```
   FROM busybox
   COPY cov_analysis /downloads/
   ```
6. Build a Docker image file:

   ```
   docker build --platform <platform> -t /<path>/<filename>:<tag> .
   ```

   where:

   - `<platform>` is the target Connect OS platform: linux,
     linux64, linux/amd64, macosx, macosarm, win32, or win64.
   - `-t` tags the image. Provide the `<path>`,
     `<filename>`, and `<tag>`,
     where:
   - `<path>` includes the registry URL and the path to the
     target folder.
   - `<filename>` is the name of the file being built.
   - `<tag>` is the version Coverity deployed in Kubernetes.
     For example, 2026.6.0.

   For additional information on building a Docker image, see <https://docs.docker.com/reference/cli/docker/image/build/>.

   For example, to build a Docker image for analysis software to be run on a Linux
   AMD64 client connected to Coverity 2026.6.0 depoyed in
   Kubernetes:

   ```
   docker build --platform linux/amd64 -t <registry_url>/coverity-cloud/analysis-downloads:2026.6.0 .
   ```

   and for `<registry_url>` = gcr.io:

   ```
   docker build --platform linux/amd64 -t gcr.io/coverity-cloud/analysis-downloads:2026.6.0 .
   ```
7. Push the Dockerfile image to your private company registry:

   ```
   docker push <registry_service_url>/<company-folder>/coverity-cloud/analysis-downloads/<imageName>:2026.6.0
   ```

   where <registry_url> consists of the
   `<registry_service_url>` which is the URL of the private
   registry service, and `<company-folder>` which is the
   top-level directory for your company's private registry

   For example, to push images to a folder
   `/coverity-cloud/analysis-downloads` within the private
   registry for a company named `mycompany`  within the
   `gcr.io` registry service:

   ```
   docker push gcr.io/mycompany/coverity-cloud/analysis-downloads/<filename>:<COVERITY_VERSION>
   ```
8. In the `cnc` chart, create a
   `cim-analysis-downloads` init container that copies the image
   and license files to `cimweb/downloads`.

   ```
   cim:
     cimweb:
       initContainers:       
         - name: cim-analysis-downloads
           image: <registry_service_url>/<company_folder>/coverity-cloud/analysis-downloads:<COVERITY_VERSION>
           command:
             - sh
             - '-c'
             - |
               cp /downloads/* /cimweb/downloads
           resources:
             limits:
               cpu: 100m
               memory: 128Mi
             requests:
               cpu: 100m
               memory: 128Mi
           volumeMounts:
             - name: cim-downloads
               mountPath: /cimweb/downloads
           imagePullPolicy: Always
   ```

   where:

   - <registry_service_url> consists of the
     `<registry_service_url>` which is the registry
     host URL (for example, gcs.io), and `<company-folder>`
     is the top-level directory for the company's private registry
   - <COVERITY_VERSION> is the Coverity version.
   - `volumeMounts:` mounts the Connect
     `/cimweb/downloads` storage for the image and license
     files copied from `/downloads/`.

   For example, to upload the analysis-downloads file for Coverity 2026.6.0 from a `gcr.io` repository to
   Connect:

   ```
   cim:
     cimweb:
       initContainers:       
         - name: cim-analysis-downloads
           image: gcr.io/<mycompany>/coverity-cloud/analysis-downloads:2026.6.0
           command:
             - sh
             - '-c'
             - |
               cp /downloads/* /cimweb/downloads
           resources:
             limits:
               cpu: 100m
               memory: 128Mi
             requests:
               cpu: 100m
               memory: 128Mi
           volumeMounts:
             - name: cim-downloads
               mountPath: /cimweb/downloads
           imagePullPolicy: Always
   ```

   When you run a Helm install or upgrade, the init container will automatically
   upload the files from your private repository to Connect storage.
9. Perform a Helm upgrade using the following command:

   ```
   helm upgrade "${CNC_APP_NAME}" "${CHART_LOCATION}" -n "${NS}" -f values.yaml
   ```

   where:

   - `"${CNC_APP_NAME}"` is Helm chart name.
   - `"${CHART_LOCATION}"` is the Helm chart ocation.
   - `"${NS}"` is the Coverity Connect Kubernetes namespace.
   - `values.yaml` is the values file in which you have added the
     new init container.
10. Now you can make the image available to users in the Connect UI as described in the
    section, Adding Coverity Analysis to the Downloads page in Coverity Platform 2026.6.0 User and Administrator Guide.

Once the image is added to the Connect UI Downloads page, users (programmers, etc) can
download Coverity Analysis client installer file(s) as described in the section,
Installing Coverity Analysis for local analysis in the Coverity 2026.6.0 Installation and Upgrade Guide.
