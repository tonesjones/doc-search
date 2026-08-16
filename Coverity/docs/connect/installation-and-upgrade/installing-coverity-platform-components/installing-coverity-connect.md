---
title: "Installing Coverity Connect"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/installing-coverity-connect.html"
content_id: "7SHY3_TJla8stK126ULH5g"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:51:54.216373+00:00"
---

# Installing Coverity Connect

This section describes the procedure for installing Coverity Connect. You use the Coverity
Platform installer to perform this installation. Once Coverity Connect is
installed and running, IDE users can download and install Coverity Desktop plug-ins for
Eclipse, QNX Momentics, Wind River Workbench, IBM RTC, Visual Studio, IntelliJ, Android
Studio, and Gradle from the Downloads link in Coverity Connect. The link also provides access to the Coverity Reports
installer (report generators are installed separately from Coverity Connect itself: for more information, see Installing Coverity Reports).

Note:
If Coverity Connect is deployed in the cloud, refer to the
Coverity 2026.6.0 Cloud Deployment Administrator and User Guide for information on installing Coverity
Connect.

Before installing to a production environment:

- You must decide whether to use the embedded database or an external database. The Coverity
  Platform installer provides the option of using a Coverity Connect
  database that is embedded in the installation package or connecting to a
  pre-existing external PostgreSQL database.
- It is important to understand the deployment considerations and hardware recommendations
  described in Deployment planning and .
- It is recommended that you or your database administrator choose and tune your file system
  settings. Database-dependent application behavior relies on I/O (input/output), and
  the system I/O can be further tuned for better performance. A good source for such
  information can be found in [PostgreSQL 9.0 High Performance](https://www.postgresql.org/about/news/postgresql-90-high-performance-book-now-available-1249/) authored
  by Gregory Smith and published by Packt Publishing.

Note that if you are simply performing a preliminary installation for trial purposes, you
might opt to use the embedded database and proceed with the installation without
reference to the deployment considerations described above. However, if you want to
fully evaluate your installation, you should heed all preliminary requirements and
recommendations.

Also be sure that you have the following information prior to launching the installer:

- Desired installation directory.
- Location of your Coverity Connect license file.
- Desired ports for Coverity Connect communications.
- External PostgreSQL credentials (if not using the embedded database).
- Amount of available RAM (for embedded database performance).

**To install Coverity Connect:**

1. Verify that your installation environment meets Coverity software and platform
   requirements.

   For details, see Supported platforms for Coverity Connect and Coverity Reports.
2. On the machine where you want to install Coverity Connect, download the
   Coverity Platform installer file for your operating system.

   **On Linux
   systems:** If the `/tmp` directory on this machine is set
   to `noexec`, you must set the Java property
   `java.io.tmpdir` to a location that is not set to
   `noexec`.
3. If you do not plan to run Coverity Connect as a service, choose or create an
   operating system user under which the Coverity Connect server software will
   run.

   On Windows and Linux systems, this is the user who can start or stop
   Coverity Connect.

   **On Linux systems:** If this user's home directory
   is set to `noexec`, you must set the Java property
   `jna.tmpdir` to a location that is not set to
   `noexec`.

   On Windows systems that run Coverity Connect
   as a service, the Administrator can start and stop Coverity Connect.
4. Run the installer script or program for your operating system:

   Linux, 64-bit
   :   cov-platform-linux64-2026.6.0.sh

   Windows, 64-bit
   :   cov-platform-win64-2026.6.0.exe

   Note: On Linux systems, ensure that you are not logged in as root.

   For
   Windows, double-click the .exe program. It is recommended
   that you install Coverity Connect with Windows Administrator
   privileges (installing Coverity Connect as a service requires it).
   To do so, right click the installer and choose Run as
   Administrator.

   For Linux, run the installer script in a
   Bourne shell, for example:

   ```
   > ./cov-platform-linux64-2026.6.0.sh
   ```

   The installer uses a text-based console mode or a graphical mode. The
   installation options for graphical and console modes are equivalent.

   - To change the installer mode, see Coverity Platform installer modes.
5. Complete the installation process:
   1. Select and accept the license agreement for your region of the world.
   2. Select the Fresh Installation option.

      Note that if you intend to
      upgrade an existing Coverity Connect instance, you should follow one of
      the upgrade procedures in the Coverity 2026.6.0 Installation and Upgrade Guide
      instead of using the steps in this guide.
   3. Enter the destination directory for the installation.

      The destination directory should
      be on a local file system. In this documentation, the Coverity Connect
      installation directory is referred to as
      <install_dir>.

      Note:
      - For a fresh installation, you must use an empty directory. If an
        earlier version of Coverity Connect is installed
        in the specified destination directory, the Coverity Platform
        installer will treat the installation as an upgrade and attempt
        to install over the existing instance.
      - Coverity Connect must be installed in a location where the user
        has full permissions. Specifically, it is recommended that
        Coverity Connect not be installed into a location that is only
        accessible by root.
   4. Enter the location of the Coverity license file
      (license.dat).

      Note: If your license is invalid, you
      will not be able to log into Coverity Connect. The installer will not
      alert you if there is a problem with your license.
   5. Choose the database type for Coverity Connect.

      You can choose the embedded
      PostgreSQL database that is bundled within the installer (which is
      recommended) or opt to connect to an external database that is hosted on
      a PostgreSQL server. For supported PostgreSQL versions, see Coverity Connect software requirements.

      Note that the external database option is only intended for
      experienced PostgreSQL DBAs. For the installer settings for an external
      database, see Using an external PostgreSQL database with Coverity Connect.
   6. If you chose the Embedded database option, enter the Coverity Connect
      database port and the database location.

      The TCP port that the embedded
      database server uses to listen for connections is only used for
      localhost connections, so you should not need to configure your
      firewall. The default is 5432.

      Choose the
      location for the embedded Coverity Connect database files. This location
      should be on a local volume that has at least 2GB of free space. The
      default is <install_dir>/database.
   7. If you chose the External database option, enter the following PostgreSQL configuration
      parameters for the database you will use:
      - PostgreSQL server name
      - Database port
      - Database name
      - Database user
      - Database password
      - SSL mode
      - Root certificate
      - Perform client authentication
      - Client certificate
      - Client certificate key
      - Key password

      If you have not already done so, you must ask your database
      administrator (DBA) to create a database and user role for Coverity
      Connect. This user role must have privileges to create and alter tables
      in the database. For more information, see Advanced installation options.
   8. Select your Coverity Connect database
      performance tuning option.

      The Coverity Platform installer will warn you
      if your system does not meet the RAM requirements on your system and you
      will not be able to select that tuning option.

      To help with
      performance, you can choose from the following options:
      - **Production** – Allows Coverity Connect to use all of the installed RAM on your
        system.
      - **Demo** – Will run on a small computer and does not require the full 8GB of
        recommended RAM. *You should not use this option for any
        production system. This option should be used for
        proof-of-concept or testing environments only.*

      Depending on your selection, the installer will suitably
      configure the JVM settings and PostgreSQL configuration. For more
      information, see PostgreSQL database tuning: embedded database and JVM settings.

      Note: These deployment tunings do not
      affect database memory allocation when installed with an external
      database; The PostgreSQL settings will not be modified. However, the JVM
      settings are set whether an embedded or external database is used.
   9. (Windows only) Choose whether or not to create Start Menu entries.

      If you
      choose to have Start Menu entries created, you have the option to change
      the default Start Menu folder, and you can choose whether or not to
      create shortcut entries for all users.
   10. Choose and confirm the Coverity Connect administrator password.

       This is the password for
       the Coverity Connect administrator (`admin`) account.
       Administrators can use this account to log in with a web browser and
       configure users, create projects, and manage other administrative
       settings.

       Note: The administrative account for Coverity Connect must adhere to a strong password policy.
       The password needs to be at least 8 characters long and contain at least one digit, as
       well as lowercase, uppercase, and special characters. We recommend a strong password
       policy for all Connect users.
   11. (Windows only) Choose to run Coverity Connect as a service.

       You must have Windows
       Administrator privileges to install and run Coverity Connect as a service. The service runs as the built-in Windows account
       `LocalService`. You cannot change this setting during
       the installation process.
   12. Choose the host name configuration.

       Choose from the host name of your
       machine, or the IP address.
   13. Enter the HTTP port number.

       This is the general purpose port for the Coverity Connect
       server and is the preferred port for transferring analysis data to the
       server. Users connect to the HTTP port to access Coverity Connect with a
       web browser or web-service client. If you are using a firewall, make
       sure it is configured to allow incoming connections on this port. This
       is referred to as the `<http_port>`. The default is
       `8080`

       If you want to configure Coverity Connect with a secure server (and
       thereby enable the "commit over HTTPS" feature), select
       Provide HTTPS service.

       The HTTPS
       protocol requires an installed server certificate from a certificate
       authority. If you choose this option, you must specify the
       HTTPS Port number. The default is
       `8443`.

       For more information about the "commit
       over HTTPS" feature, refer to the 
       `cov-commit-defects` command documentation
       in the Coverity 2026.6.0 Command Reference.
   14. Configure the following ports:
       - Commit port - (Optional) Although the HTTP(S) port is the preferred
         port for receiving data from the build and analysis processes, you
         *can* use the Commit port instead. Note, however, that the
         Commit port will be deprecated for this purpose in a future release.
         If you plan to use the Commit port and have a firewall in place,
         make sure the firewall is configured to allow incoming connections
         on this port. The default is 9090.

         Note: The
         Commit port will be deprecated for committing analysis data but
         will continue to be used in clustered environments for
         Coordinator-to-Subscriber communication.
       - Control port - The Port used by the embedded application server for
         internal server communication. The default is
         8005.
6. If you changed any of the default ports, make a note of the port number(s) for later use,
   such as for the `cov-commit-defects --dataport` command.

   After
   the installation completes, a record of some of this information is also
   available in the following files:
   - <install_dir>/config/cim.properties
   - <install_dir>/config/web.properties
   - <install_dir>/config/system.properties
   - The Tomcat configuration files located
     at:

     <install_dir>/server/base/conf/server.xmlFor example, see `commitPort` in
   cim.properties.
7. Check your installation:
   1. Launch Coverity Connect by entering one of the following URLs into your web browser:
      - `http://hostname:http_port`
      - `https://hostname:https_port`
   2. Sign into Coverity Connect with user name admin, and the administrator password that you
      previously created.

      If you are using HTTPS and you open Coverity Connect
      in a web browser before you have enabled the server for SSL, you will
      receive an error message that you do not have the correct certificate
      installed. After you have configured Coverity Connect to use the
      appropriate certificates, you will be able to log into the system. For
      more information, see the "Configuring Coverity Connect for TLS/SSL" section in the
      Coverity Platform 2026.6.0 User and Administrator Guide.
   3. Review Post-installation notes.

**To uninstall Coverity Connect:**

1. Go to <install_dir>.
2. On Linux, run the uninstall script.

   On Windows, run the
   uninstall.exe program, and follow the prompts. Note
   that you should uninstall as an administrative user, particularly if you were
   running Coverity Connect as a service.

   The uninstall
   script provides an option for removing user-supplied data. If you want to retain
   these files for your own purposes, you should back them up before uninstalling
   Coverity Connect.
