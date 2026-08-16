---
title: "Installing Coverity Analysis"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/installing-coverity-analysis.html"
content_id: "q32~U90EHnUS3evaWyJ2qA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:44:51.541255+00:00"
---

# Installing Coverity Analysis

Prior to starting this procedure, you should have your license ready. For details, see
Coverity Analysis license options. Prior to installing to a
production environment, you should also make sure that you understand the deployment
considerations and hardware recommendations in Deployment planning.

In general, you should use the installation procedure described in this chapter. For rare
cases where it is not possible to do so, an alternative is described in Using an archive file to install Coverity Analysis.

**To install Coverity Analysis:**

1. Verify that your operating system and compiler versions are supported by checking the
   following sections of this guide:
   - Supported platforms for Coverity Analysis
   - Supported languages, compilers, and frameworks for Coverity Analysis
2. On the machine on which you want to install Coverity Analysis, download the installer file,
   as described here.
3. Run the installer script or program for your operating system.

   The installer file name is
   similar to
   cov-analysis-platform-version.sh
   *or*
   .exe. For example, the Linux 64-bit installer file is named
   cov-analysis-linux64-2026.6.0.sh, and you might run it as
   follows:

   ```
   > cov-analysis-linux64-2026.6.0.sh
   ```

   For
   Windows systems, double-click the .exe
   program.

   Depending on whether you are using Linux or Windows, the
   installer uses a text-based console mode or a graphical mode. The installation
   choices for graphical and console modes are identical.

   For guidance with
   changing the installer mode, see Coverity Platform installer modes.

   CAUTION:

   In accordance with proper security practices, we do not advise installing Coverity Analysis as a root user.
4. Select and accept the End User Software License and Maintenance Agreement for your
   region of the world.
5. Choose a destination directory for the Coverity Analysis components.

   In this
   document, the Coverity Analysis installation directory is referred to as
   <install_dir>.
6. Choose the Coverity Analysis components that you want to install.

   Select from the
   following options:
   - Coverity Static Analysis

     Note that this option cannot be deselected.
   - Extend SDK
   - .NET Core SDKs
   - Documentation
     - English Documentation
     - Japanese Documentation
     - Korean Documentation
     - Chinese Documentation
7. Choose your license file type:
   - Coverity - Choose this option if you are using a license file with a
     .dat extension, for example
     license.dat. To obtain or inquire about your
     license file from Coverity, open a Support case
     by logging in to the [Black Duck Community site](https://community.blackduck.com/s/contactsupport).
   - FlexNet - Choose this option if you are using a
     FlexNet license file.
   - Obtain from server - If you want the desktop analysis
     tool to automatically obtain a license file from the Coverity Connect
     server. In order to use this option the administrator must first install the
     analysis license file on the server. This is only valid when performing
     strictly Desktop Analysis, and should not be used for Central Analysis
     servers.

   Note: The Coverity Analysis installation process will not
   continue if you do not specify a license file or license server location.
8. For Coverity licensing: Specify the location of your Coverity License file.

   If you chose
   the Coverity option for the license type, the installer
   prompts you to specify the location of your license
   (.dat).
9. For FlexNet licensing: Set up your FlexNet license.config file.

   If
   you chose the FlexNet option for the license type, this
   step sets up the configuration file that tells Coverity Analysis where the
   FlexNet license server is. Choose from the following options:
   1. Basic - Choose this option if you use a single
      license server. You will be prompted to enter the license server
      hostname and license server port for your FlexNet server.
   2. Advanced - Choose this option if your license servers are a
      redundant triad. This option prompts you to enter a comma-seperated list
      of three port
      `@`
      hostname values. For
      example:

      `28000@flex1,28001@flex2,28002@flex3`

      For more information about setting up FlexNet licensing, see
      "Installing FlexNet licenses" in the Coverity 2026.6.0 Installation and Upgrade Guide (located in the
      <install_dir>/doc
      directory).
   3. Use an existing license.config file - Choose this
      option if you have an existing FlexNet configuration file. This option
      prompts you to specify the location of the configuration file.
10. On Windows, choose whether you want to create Start Menu folders and shortcuts.
11. Indicate whether to open the Coverity documentation after the installation is complete.

    For
    Coverity Analysis documentation, see "Analyzing
    source code from the command line" in the Coverity Analysis 2026.6.0 User and Administrator Guide.
12. After the installation finishes, add <install_dir>/bin
    to your PATH environment variable.
13. [Optional] Check your installation directory.

    Access to Coverity Analysis
    components in the following directories depends on the scope of your license and
    the platform on which you are running Coverity Analysis (see Supported platforms for Coverity Analysis).

    - **Coverity Analysis**

      Coverity Analysis tools and binaries are located at the top level
      installation directory. For example, the Coverity Analysis commands are
      located in:

      <install_dir>/bin

      All of the Coverity Analysis product documentation is accessible from the following locations:
      - <install_dir>/doc/en/index.html
        (English)
      - <install_dir>/doc/ja/index.html
        (Japanese). Please see the notice regarding the availability of
        Japanese-language documentation in this file.
      - <install_dir>/doc/ko/index.html
        (Korean)
      - <install_dir>/doc/zh-cn/index.html
        (Simplified Chinese)
    - For Coverity Analysis
      commands:

      <install_dir>/bin

**To uninstall Coverity Analysis:**

1. Go to <install_dir>.
2. On Linux, run the uninstall script.

   On Windows, run the
   uninstall.exe program, and follow the
   prompts.

   The uninstall script does not remove files
   that contain user-supplied data. To remove user-supplied data, manually delete
   the installation directory after running the uninstall or
   uninstall.exe script.
