---
title: "Detect Quickstart guide"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/detect-quickstart-guide.html"
content_id: "vvW90cEGhPZfykg08tbpqQ"
version: "11.5.1"
section: "Detect Quickstart guide"
scraped_at: "2026-08-08T23:44:04.633534+00:00"
---

# Detect Quickstart guide

The following is a simple example to help you get started using Detect.

Note: For another quick path to scanning with Detect, see Autonomous Scanning.

## Step 1: Locate or acquire a source code project on which you will run Detect.

To run Detect on junit4, which is an open source project written in Java and built with Maven, you can acquire junit4 by running the following commands:

```
git clone https://github.com/junit-team/junit4.git
cd junit4
```

To understand what Detect does, it can be helpful to think about what you would do if you wanted to discover a project's dependencies without using Detect. You might do the following:

1. Look in the project directory (junit4) for hints about how dependencies are managed. In this case, the *mvnw* and *pom.xml* files are hints that dependencies are managed using Maven.
2. Since it's a Maven project, you would likely run `./mvnw dependency:tree` to reveal the project's dependencies; both direct and transitive.
3. Examine files in the project directory, which might identify additional dependencies not known to the package manager such as a .jar file copied in.

This is essentially the process that Detect expands upon and automates when it executes project manager tools and runs the Black Duck Signature Scanner on the directory. Using detectors, inspectors, and other tools, Detect may discover not only dependencies managed at the package level, but additional dependencies added to the project by means other than the package manager.

## Step 2: Run Detect connected to Black Duck.

Note: Downloading and running the latest unversioned `detect.sh/ps1` script will use the latest version of the Detect .jar file, whereas running a versioned script such as `detect11.sh/ps1` will use the latest version of the Detect .jar file within that specific major version.

To run Detect, you will need to provide login credentials for your Black Duck SCA
server. One way to do that is to add the following arguments to the command line:

- `--blackduck.url={your [bd_product_short] server URL}`
- `--blackduck.api.token={your [bd_product_short] access token}`

The command you run looks like this:

On Linux or Mac:

```
bash <(curl -s -L https://detect.blackduck.com/detect.sh) --blackduck.url={your Black Duck SCA server URL} --blackduck.api.token={your Black Duck SCA access token}
```

On Windows:

```
powershell "[Net.ServicePointManager]::SecurityProtocol = 'tls12'; irm https://detect.blackduck.com/detect.ps1?$(Get-Random) | iex; detect" --blackduck.url={your Black Duck SCA server URL} --blackduck.api.token={your Black Duck SCA access token}
```

The operations performed by Detect depends on what it finds in your source directory.
By default, Detect considers the current working directory to be your source directory.

In the junit4 case, Detect will:

1. Run the Maven detector, which uses Maven to discover dependencies.
2. Run the Black Duck Signature Scanner which scans the files in the source directory to discover dependencies.
3. Upload the discovered dependencies to Black Duck SCA.
4. Add a log entry for the Black Duck® SCA Project BOM URL that you can use to view the results in Black Duck SCA.

Once the scan is complete, navigate with your browser to the Black Duck SCA Project BOM URL to see the Bill Of Materials for junit4.

For guidance on getting started using, and viewing results in Black Duck SCA, check out [Getting Started with Black Duck SCA](https://docs.blackduck.com/r/blackduck/latest/black-duck-documentation/getting-started-with-black-duck-sca.html)

## Next steps

Detect can be used on a variety of project types, and in a variety of ways, due to it's behavior being highly configurable.
For more detailed information on how to configure Detect for your needs, see Configuring Detect.
