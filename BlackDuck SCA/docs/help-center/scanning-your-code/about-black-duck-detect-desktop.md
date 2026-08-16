---
title: "About Black Duck Detect Desktop"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/about-black-duck-detect-desktop.html"
content_id: "26bJksLhAF1UbhvjiWv0kA"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T14:53:27.939056+00:00"
---

# About Black Duck Detect Desktop

Detect Desktop provides an interface to make it easier to scan code.

With Detect Desktop, you can:

- Scan source directories, binaries and
  executables, and docker images and distributions.
- Create a scan
  file to be uploaded at a later time.
- Manage scan files.
- View uploaded scans.

To get started with Detect Desktop:

1. Download
   Detect Desktop
2. Install
   Detect Desktop.
3. Configure
   Detect Desktop with your Black Duck SCA server settings and complete the installation process.

## System Requirements

- **Operating Systems**

  - Windows 11
  - macOS 14
  - Linux (Ubuntu 20.04 or newer)
- **System Memory**

  - 8 GB RAM
- **Available hard disk space**

  - 150 MB+ free space
- **Other**

  - Java: OpenJDK 64-bit version 8, 11, 13, 14, 15, 16, 17, or 21. If using Java 11: 11.0.5 or higher is required.

Ensure that your system complies with the requirements for Black Duck Detect.

- For the latest system requirements, please refer to the [Black Duck Detect system requirements page](https://docs.blackduck.com/access?ft:originId=9c0814dc6c47bd8e1b015657cf47a869/4b8e79c1f741f56e79b9cdfb3f80843c.topic).

## Downloading Detect Desktop

1. Log in to Black Duck SCA.
2. Navigate to the drop-down menu under your username and select
   **Tools**.
3. Select the operating system you wish to use in the **Downloads**
   **Black Duck Detect (Desktop)** section to download the
   executable from Google Cloud Storage.

## Installing Detect Desktop

1. **Run the Executable**

   Run the executable downloaded above to install Black Duck Detect Desktop.
2. **Data Migration (if applicable)**

   If you are upgrading from a previous version of Black Duck Detect Desktop, an option
   will appear to migrate data from the earlier version.

## Important Notes

- **Uninstallation of Previous Versions**: The installer will not automatically uninstall
  previous versions of Black Duck Detect Desktop or versions installed
  in non-default directories. You must manually uninstall all previous
  versions and fix or delete any shortcuts as necessary.
- **Sandbox Configuration Error**: If you encounter the following error
  after installation:

  **"The SUID sandbox helper binary was found, but is not configured
  correctly. Rather than run without sandboxing I'm aborting now. You need
  to make sure that /opt/Black Duck Detect/chrome-sandbox is owned by root
  and has mode 4755."** This indicates that your operating system does
  not support the Sandbox at the kernel layer. To run Black Duck Detect
  (Desktop) with the Sandbox disabled, enter the following command in the
  terminal:

  ```
  blackduck-detect --no-sandbox
  ```

## Command line options for Windows

- **Unattended (Silent) Install**

  To perform a silent installation of Black Duck Detect, use the following
  command:

  ```
  ./blackduck-detect-latest.exe /S
  ```
- **Install to a Specific Directory**

  To install Black Duck Detect to a custom directory, use:

  ```
  ./blackduck-detect-latest.exe /D=C:\directory
  ```

## Installing the Linux version of Black Duck Detect Desktop

1. **Download the Executable**

   Download the executable from your Black Duck SCA server, as described above.
2. **Install Black Duck Detect Desktop**:

   Open a terminal and navigate to your Downloads directory:

   ```
   cd Downloads
   ```

   - **For CentOS/RedHat**:

     ```
     sudo yum localinstall blackduck-detect-latest.rpm
     ```
   - **For Ubuntu/Debian**:

     ```
     sudo apt install ./blackduck-detect-latest.deb
     ```
3. **Change Permissions**:

   Change the permissions of the `chrome-sandbox` file:

   ```
   cd "/opt/Black Duck Detect"
   sudo chmod 4755 chrome-sandbox
   ```
4. **Run Black Duck Detect Desktop**:

   Finally, launch Black Duck Detect Desktop with the following command:

   ```
   ./blackduck-detect --no-sandbox
   ```
