---
title: "Create and use a custom Docker image"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/create-and-use-a-custom-docker-image.html"
content_id: "KWKxORuBJ7h7U0KHzEzuXQ"
version: "latest"
section: "Bitbucket Integrations"
scraped_at: "2026-08-08T23:49:00.195293+00:00"
---

# Create and use a custom Docker image

A custom Docker image is required to run the Black Duck Security Scan Pipe when performing SAST scans for compiled languages and/or when there is a need to extend the default build environment for a scan, e.g. configuring SSL certificates, toolkit installation locations etc. This guide explains the use cases and provides accompanying examples for creating and using a custom image with the Black Duck Security Scan Pipe.

## When to use a custom image with Black Duck Security Scan Pipe?

A custom image is required for use with the Black Duck Security Scan Pipe when specific parameters are configured that require customized configuration of the build environment to run a scan. For example, if using a compiled language, Coverity must be configured using pipe parameters or a `coverity.yaml` file to specify the build and clean commands.

The table below summarises the Black Duck Security Scan Pipe parameters that require a custom image.

Table 1. Parameters that require a custom image

| Type | Parameters | Black Duck platforms |
| --- | --- | --- |
| Bridge | - `BRIDGECLI_INSTALL_DIRECTORY` - `BRIDGE_PROJECT_SOURCE_ARCHIVE` - `BRIDGE_PROJECT_DIRECTORY` | All platforms |
| Detect | - `BRIDGE_DETECT_INSTALL_DIRECTORY` - `BRIDGE_DETECT_CONFIG_PATH` | Blackduck SCA, Polaris SCA and Software Risk Manager SCA |
| Coverity | - `BRIDGE_COVERITY_BUILD_COMMAND` - `BRIDGE_COVERITY_CLEAN_COMMAND` - `BRIDGE_COVERITY_ARGS` - `BRIDGE_COVERITY_INSTALL_DIRECTORY` - `BRIDGE_COVERITY_CONFIG_PATH` - `BRIDGE_COVERITY_EXECUTION_PATH` (Applicable for SRM SCA and SAST only) | Coverity, Polaris SAST and Software Risk Manager SAST |
| Networking | - `BRIDGE_NETWORK_AIRGAP` - `BRIDGE_NETWORK_SSL_CERT_FILE` | All platforms |

## **Custom image configuration through Dockerfile**

Custom images can be used through the `CUSTOM_IMAGE` parameter *or* directly as a pipe in Bitbucket pipelines. Both methods of using custom images allow a custom Docker image to be specified for the Black Duck Security Scan Pipe execution. Subsequently, the scan will execute within a container using the specified custom image.

Note: The integration supports both **public and private docker images** from **Docker Hub** and **internal Docker registries**. Ensure proper authentication is configured for private images. For authentication, use `DOCKER_USERNAME`, `DOCKER_PASSWORD` and/or `DOCKER_REGISTRY` depending on your requirement.

Table 2. List of mandatory and optional parameters

| **Input parameter** | Description | **Mandatory / optional** |
| --- | --- | --- |
| `CUSTOM_IMAGE` | Specify the custom image to use for the pipe execution. | Optional |
| `DOCKER_USERNAME` | Specify the docker username, if the custom docker image is private. | Optional |
| `DOCKER_PASSWORD` | Specify the docker password or personal access token (PAT), if the custom docker image is private. | Optional |
| `DOCKER_REGISTRY` | Specify the internal Docker registry, if the custom image is privately hosted on an internal Docker registry. | Optional |

Custom images can be configured through using a `Dockerfile` in one of the following ways:

- Extend Black Duck Security Scan Pipe image
- Extend existing organization image

## Extend Black Duck Security Scan Pipe image

A custom image can be created using any valid image as the base image, and then configuring the required Black Duck Security Scan Pipe tools and dependencies within that custom image.

While configuring a custom image, ensure the image includes all the necessary build tools and other dependencies related to Black Duck Security Scan Pipe.

**Requirements for user-defined custom images for Black Duck Security Scan Pipe:**

1. **Use a base Image**: Use any valid docker image as the base image.
2. **Setup Black Duck Security Scan Pipe environment:**
   1. **Install** `python3` **and** `python3-pip`: Required to run the pipe script and to install the python dependencies.
   2. **Install** `openjdk-17-jdk`: Required to execute Detect.
   3. **Install** `curl`: Required to install additional tools if using any lightweight docker images as the base image (example: alpine)
   4. **Install** `git`: Required to clone the blackduck-security-scan pipe [repository](https://bitbucket.org/blackduck-inc/blackduck-security-scan.git/src). The `pipe.py`, `pipe.yml` and `requirements.txt` can also be downloaded directly from the repository, instead of using git clone. Installation of git can be ignored if you download directly.
   5. **Copy or move** `pipe.py`, `pipe.yml` and `requirements.txt`. Make sure to keep these files in the root folder of the custom docker image. These files are required for bridge-cli invocation, with the help of pipe script.
3. **Install additional tools**: Install any other additional tools that may be necessary during scan execution.
4. **Set entrypoint**: Set `["python3", "/pipe.py"]` as the entrypoint of the docker image.
5. **Public or private image support**: Docker images from Docker Hub and internal Docker registries may be publicly or privately accessible. For private images, ensure authentication is properly configured.

Example Dockerfile for creating the custom image:

```
# Use Node.js 20 as the base image
FROM node:20
                
# Set the working directory
WORKDIR /
                
# Install required dependencies: Python3, Pip, JDK 17, Curl, and Git
RUN apt-get update && apt-get install -y python3 python3-pip openjdk-17-jdk curl git
                
# Clone the Black Duck Security Scan Pipe repository
RUN git clone https://bitbucket.org/blackduck-inc/blackduck-security-scan.git /repo
# Move required files to the working directory
RUN mv /repo/requirements.txt / && mv /repo/pipe/pipe.py / && mv /repo/pipe.yml / && rm -rf /repo
                
# Install Python dependencies
RUN pip3 install --no-cache-dir --break-system-packages -r /requirements.txt
                
# Set the entrypoint to execute pipe.py
ENTRYPOINT ["python3", "/pipe.py"]
                
# Build and push your custom image to dockerhub
# docker build --platform linux/amd64 -t user/custom-blackduck-security-scan:node .
# docker push user/custom-blackduck-security-scan:node
```

Example Dockerfile for network **air-gap** configuration:

```
# Use Node.js 20 as the base image
FROM node:20
    
# Set the working directory
WORKDIR /
    
# Install required dependencies: Python3, Pip, JDK 17, Curl, and Git
RUN apt-get update && apt-get install -y python3 python3-pip openjdk-17-jdk curl git
    
# Clone the Black Duck Security Scan Pipe repository
RUN git clone https://bitbucket.org/blackduck-inc/blackduck-security-scan.git /repo
# Move required files to the working directory
RUN mv /repo/requirements.txt / && mv /repo/pipe/pipe.py / && mv /repo/pipe.yml / && rm -rf /repo
    
# Install Python dependencies
RUN pip3 install --no-cache-dir --break-system-packages -r /requirements.txt
    
# Copy the contents of the bridgecli directory to /usr/local/bridge-airgap or any other location in the container
COPY bridge-cli-bundle/ /usr/local/bridge-airgap/
    
# Set the entrypoint to execute pipe.py
ENTRYPOINT ["python3", "/pipe.py"]
    
# Build and push your custom image to dockerhub
# docker build --platform linux/amd64 -t user/custom-blackduck-security-scan:node .
# docker push user/custom-blackduck-security-scan:node
```

Example Dockerfile for `BRIDGE_PROJECT_SOURCE_ARCHIVE` and `BRIDGE_PROJECT_DIRECTORY`:

```
# Use Node.js 20 as the base image
FROM node:20
    
# Set the working directory
WORKDIR /
    
# Install required dependencies: Python3, Pip, JDK 17, Curl, and Git
RUN apt-get update && apt-get install -y python3 python3-pip openjdk-17-jdk curl git
    
# Clone the Black Duck Security Scan Pipe repository
RUN git clone https://bitbucket.org/blackduck-inc/blackduck-security-scan.git /repo
# Move required files to the working directory
RUN mv /repo/requirements.txt / && mv /repo/pipe/pipe.py / && mv /repo/pipe.yml / && rm -rf /repo
    
# Install Python dependencies
RUN pip3 install --no-cache-dir --break-system-packages -r /requirements.txt
    
# Copy the project zip to /usr/local/project-source-archive or any other location in the container
COPY /projects/my-project.zip /usr/local/project-source-archive/
    
# Copy the project directory to /usr/local/project-directory or any other location in the container
COPY /projects/my-project /usr/local/project-directory/
    
# Set the entrypoint to execute pipe.py
ENTRYPOINT ["python3", "/pipe.py"]
    
# Build and push your custom image to dockerhub
# docker build --platform linux/amd64 -t user/custom-blackduck-security-scan:node .
# docker push user/custom-blackduck-security-scan:node
```

Example Dockerfile for Arbitary Parameters Configuration:

```
# Use Node.js 20 as the base image
FROM node:20

# Set the working directory
WORKDIR /

# Install required dependencies: Python3, Pip, JDK 17, Curl, and Git
RUN apt-get update && apt-get install -y python3 python3-pip openjdk-17-jdk curl git

# Clone the Black Duck Security Scan Pipe repository
RUN git clone https://bitbucket.org/blackduck-inc/blackduck-security-scan.git /repo
# Move required files to the working directory
RUN mv /repo/requirements.txt / && mv /repo/pipe/pipe.py / && mv /repo/pipe.yml / && rm -rf /repo

# Install Python dependencies
RUN pip3 install --no-cache-dir --break-system-packages -r /requirements.txt

# Detect tools configuration
# Create Detect install directory to specify BRIDGE_DETECT_INSTALL_DIRECTORY
RUN mkdir -p /usr/local/detect
# Copy application.properties to specify BRIDGE_DETECT_CONFIG_PATH
COPY /config/application.properties /usr/local/config/application.properties

# Coverity tools configuration
# Create Coverity install directory to specify BRIDGE_COVERITY_INSTALL_DIRECTORY
RUN mkdir -p /usr/local/coverity
# Copy coverity.yml to specify BRIDGE_COVERITY_CONFIG_PATH
COPY /config/coverity.yml /usr/local/config/coverity.yml

# Set the entrypoint to execute pipe.py
ENTRYPOINT ["python3", "/pipe.py"]

# Build and push your custom image to dockerhub
# docker build --platform linux/amd64 -t user/custom-blackduck-security-scan:node .
# docker push user/custom-blackduck-security-scan:node
```

Example Dockerfile for Polaris SCA binary scan configuration:

```
# Use Node.js 20 as the base image
FROM node:20

# Set the working directory
WORKDIR /

# Install required dependencies: Python3, Pip, JDK 17, Curl, and Git
RUN apt-get update && apt-get install -y python3 python3-pip openjdk-17-jdk curl git

# Clone the Black Duck Security Scan Pipe repository
RUN git clone https://bitbucket.org/blackduck-inc/blackduck-security-scan.git /repo
# Move required files to the working directory
RUN mv /repo/requirements.txt / && mv /repo/pipe/pipe.py / && mv /repo/pipe.yml / && rm -rf /repo

# Install Python dependencies
RUN pip3 install --no-cache-dir --break-system-packages -r /requirements.txt

# Polaris SCA Binary scan configuration
COPY /path/to/artifact.zip /usr/local/artifact.zip

# Set the entrypoint to execute pipe.py
ENTRYPOINT ["python3", "/pipe.py"]

# Build and push your custom image to dockerhub
# docker build --platform linux/amd64 -t user/custom-blackduck-security-scan:node .
# docker push user/custom-blackduck-security-scan:node
```

## Extend existing organization Docker image

A custom image can be created using `blackducksoftware/blackduck-security-scan` as the base image. This allows installing additional tools required for the scan. While configuring the custom image, ensure that all necessary build tools are installed in addition to other dependencies related to Black Duck Security Scan Pipe.

**Requirements for user-defined custom images for Black Duck Security Scan Pipe:**

1. **Use the base Image**: The base image must be `blackducksoftware/blackduck-security-scan:<tag>`
2. **Install build tools**: Install the required build tools to execute the scan, with additional tools and path configuration.
3. **Public or private image support**: Docker images from Docker Hub and internal Docker registries may be publicly or privately accessible. For private images, ensure authentication is properly configured.

Example Dockerfile for creating the custom image:

```
# Use blackducksoftware/blackduck-security-scan:1.6.0 as the base image
FROM blackducksoftware/blackduck-security-scan:1.6.0
    
# Install Node.js and npm
RUN apt-get update && \
apt-get install -y nodejs npm file && \
apt-get clean
    
# Set the working directory
WORKDIR /
# Copy any additional files if needed (optional)
# COPY additional_files /path/to/destination
    
# Ensure the entrypoint is set to run the pipe
ENTRYPOINT ["python3", "/pipe.py"]
    
# Build and push your custom image to dockerhub
# docker build --platform linux/amd64 -t user/custom-blackduck-security-scan:node .
# docker push user/custom-blackduck-security-scan:node
```

Note: Make sure to install necessary tools/packages so that tool-specific commands will execute successfully during the scan. For example: Installation of `file` package is required along with `nodejs` and `npm` to execute `npm` commands.

## **Using a custom image**

After creating a custom image, it can be used in a Bitbucket pipeline. A custom image can be specified with the `CUSTOM_IMAGE` parameter, or directly as a pipe.

The following `bitbucket-pipelines.yml` examples represent the two ways in which a custom image can be used.

1. **Using the `CUSTOM_IMAGE` parameter**
   - A custom image can be specified through the `CUSTOM_IMAGE` parameter. Example: `CUSTOM_IMAGE: <user>/<image>:<tag>`.
   - Images from an internal docker registry must be specified as follows:

     ```
     CUSTOM_IMAGE:
                   '<registry>/<user>/<image>:<tag>'
     ```

     . Example:

     ```
     CUSTOM_IMAGE:
                   'internal.artifactory.net:5002/my-org/custom-private-image:1.0.0'
     ```
   - Use the `DOCKER_REGISTRY` variable only if the custom image is private and hosted in an internal Docker registry. Example: `DOCKER_REGISTRY: '<registry-url>'`
   - Detailed example:

     ```
     security-scan: &blackduck-security-scan
         step:
             name: Black Duck Security Scan
             script:
                 - pipe: blackduck-inc/blackduck-security-scan:1.6.0
                   variables:
                       BRIDGE_POLARIS_SERVERURL: $BRIDGE_POLARIS_SERVERURL
                       BRIDGE_POLARIS_ACCESSTOKEN: $BRIDGE_POLARIS_ACCESSTOKEN
                       BRIDGE_POLARIS_ASSESSMENT_TYPES: 'SCA,SAST'
                       BRIDGE_POLARIS_APPLICATION_NAME: $BRIDGE_POLARIS_APPLICATION_NAME
                       BRIDGE_POLARIS_PROJECT_NAME: $BRIDGE_POLARIS_PROJECT_NAME
                       BRIDGE_POLARIS_BRANCH_NAME: $BRIDGE_POLARIS_BRANCH_NAME

                       ### Enable Polaris PR scan
                       BRIDGE_POLARIS_PRCOMMENT_ENABLED: 'true'
                       BRIDGE_BITBUCKET_API_TOKEN: $BRIDGE_BITBUCKET_API_TOKEN
                       BRIDGE_POLARIS_PRCOMMENT_SEVERITIES: 'CRITICAL,HIGH'

                       ### Upload Polaris SARIF report as job artifact
                       BRIDGE_POLARIS_REPORTS_SARIF_CREATE: 'true'
                       BRIDGE_POLARIS_REPORTS_SARIF_FILE_PATH: '/usr/local/report/report.sarif.json'
                       BRIDGE_POLARIS_REPORTS_SARIF_ISSUE_TYPES: 'SCA,SAST'
                       BRIDGE_POLARIS_REPORTS_SARIF_SEVERITIES: 'CRITICAL,HIGH'
                       BRIDGE_POLARIS_REPORTS_SARIF_GROUPSCAISSUES: 'true'

                       # BRIDGE_POLARIS_WAITFORSCAN: 'false'   # Used to support the async mode

                       ### Signature scan
                       # BRIDGE_POLARIS_TEST_SCA_TYPE: 'SCA-SIGNATURE'

                       ### Uncomment this to use Source Upload method. Default value is CI (build based)
                       # BRIDGE_POLARIS_ASSESSMENT_MODE: "SOURCE_UPLOAD"
                       # BRIDGE_PROJECT_SOURCE_ARCHIVE: $PROJECT_ARCHIVE
                       # BRIDGE_PROJECT_SOURCE_EXCLUDES: $PROJECT_SOURCE_EXCLUDES

                       ### Enable Bridge CLI diagnostics
                       # INCLUDE_DIAGNOSTICS: 'true'

                       ### BRIDGE_BITBUCKET_API_TOKEN is required to upload SARIF report and diagnostics in the Bitbucket downloads section; otherwise, configure SARIF and diagnostics as artifacts in the bitbucket-pipelines.yml 
                       # BRIDGE_BITBUCKET_API_TOKEN: $BRIDGE_BITBUCKET_API_TOKEN

                       ### Mark build status if policy violating issues are found
                       # MARK_BUILD_STATUS: 'success'

                       ## Use custom image to configure paths and tools     
                       CUSTOM_IMAGE: 'user/custom-blackduck-security-scan:node'
                       ## Use below parameters to authenticate private custom docker image
                       # DOCKER_USERNAME: $DOCKER_USERNAME
                       # DOCKER_PASSWORD: $DOCKER_PASSWORD # Supports Password and Personal Access Token
                       ## Use this if the private docker image is hosted in an internal docker registry
                       # DOCKER_REGISTRY: $DOCKER_REGISTRY

                       ## Uncomment to specify the directory to scan. Default value is repository root
                       # BRIDGE_PROJECT_DIRECTORY: '/usr/local/my-project'

                       ## Network Airgap Configuration
                       # NETWORK_AIRGAP: true
                       # BRIDGECLI_INSTALL_DIRECTORY: '/usr/local/bridge-airgap'

                       ## Configure install directories
                       BRIDGE_DETECT_INSTALL_DIRECTORY: '/usr/local/detect'
                       BRIDGE_COVERITY_INSTALL_DIRECTORY: '/usr/local/coverity'

                       ## Coverity (SAST) Tools Settings
                       BRIDGE_COVERITY_CLEAN_COMMAND: 'npm cache clean'
                       BRIDGE_COVERITY_BUILD_COMMAND: 'npm install'
                       BRIDGE_COVERITY_CONFIG_PATH: '/usr/local/config/coverity.yml'
                       BRIDGE_COVERITY_ARGS: '-c /usr/local/config/coverity.yml -o capture.build.clean-command="npm cache clean" -- npm clean install'

                       ## Detect Tool Settings
                       BRIDGE_DETECT_SEARCH_DEPTH: 2
                       BRIDGE_DETECT_ARGS: ' --detect.diagnostic=true'
                       BRIDGE_DETECT_CONFIG_PATH: '/usr/local/config/application.properties'    

     pipelines:
         pull-requests:
             '**':  # Matches all pull requests
                 - <<: *blackduck-security-scan
         branches:
             '{main,master,develop,stage,release}':
                 - <<: *blackduck-security-scan
     ```
2. **Using a custom image directly as a pipe:**
   - For authentication, in the case of private images, use this command:

     ```
     - echo "${DOCKER_PASSWORD}" | docker login
                   "${DOCKER_REGISTRY}" --username "${DOCKER_USERNAME}" --password-stdin
     ```

     (before the pipe in pipeline script).
   - Detailed example:

     ```
     security-scan: &blackduck-security-scan
         step:
             name: Black Duck Security Scan
             script:
                 ### Use this to authenticate private custom docker image 
                 # - echo "${DOCKER_PASSWORD}" | docker login --username "${DOCKER_USERNAME}" --password-stdin
                 ### Use this if the private docker image is hosted in an internal docker registry
                 # - echo "${DOCKER_PASSWORD}" | docker login "${DOCKER_REGISTRY}" --username "${DOCKER_USERNAME}" --password-stdin
                 - pipe: docker://user/custom-blackduck-security-scan:node
                   variables:
                       BRIDGE_POLARIS_SERVERURL: $BRIDGE_POLARIS_SERVERURL
                       BRIDGE_POLARIS_ACCESSTOKEN: $BRIDGE_POLARIS_ACCESSTOKEN
                       BRIDGE_POLARIS_ASSESSMENT_TYPES: 'SCA,SAST'
                       BRIDGE_POLARIS_APPLICATION_NAME: $BRIDGE_POLARIS_APPLICATION_NAME
                       BRIDGE_POLARIS_PROJECT_NAME: $BRIDGE_POLARIS_PROJECT_NAME
                       BRIDGE_POLARIS_BRANCH_NAME: $BRIDGE_POLARIS_BRANCH_NAME

                       ### Enable Polaris PR scan
                       BRIDGE_POLARIS_PRCOMMENT_ENABLED: 'true'
                       BRIDGE_BITBUCKET_API_TOKEN: $BRIDGE_BITBUCKET_API_TOKEN
                       BRIDGE_POLARIS_PRCOMMENT_SEVERITIES: 'CRITICAL,HIGH'

                       ### Upload Polaris SARIF report as job artifact
                       BRIDGE_POLARIS_REPORTS_SARIF_CREATE: 'true'
                       BRIDGE_POLARIS_REPORTS_SARIF_FILE_PATH: '/usr/local/report/report.sarif.json'
                       BRIDGE_POLARIS_REPORTS_SARIF_ISSUE_TYPES: 'SCA,SAST'
                       BRIDGE_POLARIS_REPORTS_SARIF_SEVERITIES: 'CRITICAL,HIGH'
                       BRIDGE_POLARIS_REPORTS_SARIF_GROUPSCAISSUES: 'true'

                       # BRIDGE_POLARIS_WAITFORSCAN: 'false'   # Used to support the async mode

                       ### Signature scan
                       # BRIDGE_POLARIS_TEST_SCA_TYPE: 'SCA-SIGNATURE'

                       ### Uncomment this to use Source Upload method. Default value is CI (build based)
                       # BRIDGE_POLARIS_ASSESSMENT_MODE: "SOURCE_UPLOAD"
                       # BRIDGE_PROJECT_SOURCE_ARCHIVE: $PROJECT_ARCHIVE
                       # BRIDGE_PROJECT_SOURCE_EXCLUDES: $PROJECT_SOURCE_EXCLUDES

                       ### Enable Bridge CLI diagnostics
                       # INCLUDE_DIAGNOSTICS: 'true'

                       ### BRIDGE_BITBUCKET_API_TOKEN is required to upload SARIF report and diagnostics in the Bitbucket downloads section; otherwise, configure SARIF and diagnostics as artifacts in the bitbucket-pipelines.yml 
                       # BRIDGE_BITBUCKET_API_TOKEN: $BRIDGE_BITBUCKET_API_TOKEN

                       ### Mark build status if policy violating issues are found
                       # MARK_BUILD_STATUS: 'success'

                       ## Uncomment to specify the directory to scan. Default value is repository root
                       # BRIDGE_PROJECT_DIRECTORY: '/usr/local/my-project'

                       ## Network Airgap Configuration
                       # NETWORK_AIRGAP: true
                       # BRIDGECLI_INSTALL_DIRECTORY: '/usr/local/bridge-airgap'

                       ## Polaris SCA Binary Scan
                       BRIDGE_POLARIS_TEST_SCA_TYPE: 'SCA-SIGNATURE'
                       BRIDGE_POLARIS_ARTIFACTTOUPLOAD: '/path/to/artifact.zip'
                       ## Configure install directories

                       BRIDGE_DETECT_INSTALL_DIRECTORY: '/usr/local/detect'
                       BRIDGE_COVERITY_INSTALL_DIRECTORY: '/usr/local/coverity'

                       ## Coverity (SAST) Tools Settings
                       BRIDGE_COVERITY_CLEAN_COMMAND: 'npm cache clean'
                       BRIDGE_COVERITY_BUILD_COMMAND: 'npm install'
                       BRIDGE_COVERITY_CONFIG_PATH: '/usr/local/config/coverity.yml'
                       BRIDGE_COVERITY_ARGS: '-c /usr/local/config/coverity.yml -o capture.build.clean-command="npm cache clean" -- npm clean install'

                       ## Detect Tool Settings
                       BRIDGE_DETECT_SEARCH_DEPTH: 2
                       BRIDGE_DETECT_ARGS: ' --detect.diagnostic=true'
                       BRIDGE_DETECT_CONFIG_PATH: '/usr/local/config/application.properties'    

     pipelines:
         pull-requests:
             '**':  # Matches all pull requests
                 - <<: *blackduck-security-scan
         branches:
             '{main,master,develop,stage,release}':
                 - <<: *blackduck-security-scan
     ```
