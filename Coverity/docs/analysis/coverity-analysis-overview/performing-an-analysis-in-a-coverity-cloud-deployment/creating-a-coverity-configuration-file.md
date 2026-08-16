---
title: "Creating a Coverity configuration file"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/creating-a-coverity-configuration-file.html"
content_id: "9Yk3fgNu9VqDy_0bgo1zVg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:32:31.767287+00:00"
---

# Creating a Coverity configuration file

To create a Coverity configuration file, `coverity.yaml`, use the
`coverity setup` command. If you are using the Thin Client, the
resulting configuration will automatically configure the Coverity CLI to
do the analysis in the Coverity Connect Scan Service. The following
example uses the `coverity setup` command to generate a configuration
file. You need to provide the following information when prompted:

- Coverity Connect URL.
- Name of the upload stream to upload the scan results.
- Coverity Connect username.
- Coverity Connect password.

To create a Coverity configuration file:

1. Run the `coverity setup` command:

   ```
   $ coverity setup
   [INFO] coverity version covcli-version
   [INFO] Using Coverity Capture kit at: "/Users/jbloggs/Downloads/cov-analysis-OS-version/bin".
   ```

   Attention: The Coverity CLI has a known issue when
   reading the Coverity Connect password in the Cygwin shell using the `coverity
   setup` or `coverity scan` commands. To work around this
   issue, run `coverity setup` using the Windows command shell
   `cmd.exe`. You can then switch back to the Cygwin shell.
2. As prompted, provide the Coverity Connect URL. For example,
   https://connect.example.com:8443:

   ```
   Which Coverity Connect instance? Enter in the format https://<hostname>:<port>
   Coverity Connect URL: https://connect.example.com:8443
   ```
3. As prompted, provide the upload stream:

   ```
   Which stream would you like to upload the analysis results to?
   Stream name (Enter to accept default or enter a new name) [mystream]:
   ```
4. As prompted, provide the Coverity Connect username and password:

   ```
   What is your Coverity Connect username?
   Username (Enter to accept default or enter a new name) [myname]:
    
   What is your Coverity Connect password (will not be echoed)?
   ```

`coverity setup` creates the `coverity.yaml` configuration file
in the project directory and indicates the file location and name. For example:

```
[INFO] Authentication key file written to '/Users/jbloggs/.coverity/authkeys/ak-connect.example.com-8443'.
[INFO]
[INFO] Coverity configuration file written to '/Users/jbloggs/Projects/open-source/my-project/coverity.yaml'.
[INFO] To scan your project, type 'coverity scan'.
```

In this section:

- Setting up TLS and certificates for analysis in the cloud
- Configuring client authentication with the cluster
- Analysis location
