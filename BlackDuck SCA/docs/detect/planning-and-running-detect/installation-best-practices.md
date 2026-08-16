---
title: "Installation Best Practices"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/installation-best-practices.html"
content_id: "E96obnvwDl_TPzcspbSUKA"
version: "11.5.1"
section: "Planning and running Detect"
scraped_at: "2026-08-08T23:44:28.160899+00:00"
---

# Installation Best Practices

Manually installing Detect ensures that the running version is compatible with your environment. Invoking Detect with the bash and powershell scripts is easy but automatically downloaded updates may not be compatible with your environment.

The best practice for resilience is to add Detect on the path, allowing for an easier invocation than even the bash and powershell scripts. It still allows easy updating without modifying commands just as the bash and powershell scripts do. This is the recommended best practice approach when resiliency is required.

## Basic Manual Installation Steps

1. Download Java and make sure it is on your PATH
2. Download the version of Detect you want to use from https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/detect/

   - You should download the air gap zip if you do not want Detect to download Inspectors at runtime
3. Put the Detect jar/zip somewhere you can manage it

   - Examples:
   - Mac/Linux: $HOME/detect/download/detect-X.X.X.jar
   - Windows: C:\Program Files\detect\download\detect-X.X.X.jar
4. You can now run Detect

   - Example: java -jar $HOME/detect/download/detect-X.X.X.jar --help

## Mac/Linux Best Practice Installation Steps for Resilience

1. Download Java and make sure it is on your PATH
2. Download the version of Detect you want to use from https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/detect/

   - You should download the air gap zip if you do not want Detect to download Inspectors at runtime
3. Create a symlink for the Detect jar

   - ```
     ln -s $HOME/detect/download/detect-X.X.X.jar $HOME/detect/download/latest-detect.jar
     ```
4. Create a bash script named "detect" with the following content.

   - ```
     #!/bin/bash
     ```
   - ```
     java -jar $HOME/detect/download/latest-detect.jar "$@"
     ```
5. Add the script to your PATH variable

   - ```
     export PATH=${PATH}:${path_to_folder_containing_detect_script}
     ```
6. OR instead of altering your PATH you can place the script in a directory that is already on your PATH

   - Example: /usr/local/bin
7. You can now run Detect

   - Example: detect --help

## Windows Best Practice Installation Steps for Resilience

1. Download Java and make sure it is on your PATH
2. Download the version of Detect you want to use from https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/detect/

   - You should download the air gap zip if you do not want Detect to download Inspectors at runtime
3. Create a symbolic link for the Detect jar, called latest-detect.jar

   - Start a command prompt in the folder you downloaded detect.
   - Run the following: mklink latest-detect.jar detect-X.X.X.jar
4. Create a bat script named "detect.cmd" in the same folder with the following content

   - ```
     @java -jar "C:\Program Files\detect\download\latest-detect.jar" %*
     ```
5. Add the script to your PATH variable

   - In File Explorer right-click on the This PC (or Computer) icon, then click Properties -> Advanced System Settings -> Environment Variables
   - Under System Variables select Path, then click Edit
   - Add an entry with the path to the folder containing the script "C:\Program Files\detect\download"
6. You can now run Detect

   - Example: detect --help
