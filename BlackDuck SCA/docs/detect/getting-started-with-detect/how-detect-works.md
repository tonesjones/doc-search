---
title: "How Detect Works"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/how-detect-works.html"
content_id: "b2JqybCgiQWZPVdXSahbKw"
version: "11.5.1"
section: "Getting started with Detect"
scraped_at: "2026-08-08T23:44:13.260001+00:00"
---

# How Detect Works

This page provides an overview of how Black Duck® Detect works.

Detect performs the following basic steps when scanning open source software, assuming you are connected to a Black Duck SCA instance.

1. Detect uses the project's package manager to derive the hierarchy of dependencies known to that package manager. For example, on a Maven project, Detect executes an mvn dependency:tree command, and derives dependency information from the output.
2. Runs the Black Duck Signature Scanner on the project. This might identify additional dependencies not known to the package manager such as a .jar file copied into the project directory.
3. Uploads both sets of results (dependency details) to Black Duck SCA creating the project/version if it does not already exist. Black Duck SCA uses the uploaded dependency information to build the Bill Of Materials (BOM) for the project/version.

In this case, the user has provided Black Duck SCA connection details through property settings to Detect, specifying that results (project dependency details) are to be uploaded to Black Duck SCA
By combining all these techniques, Detect is capable of scanning a wide range of software projects
utilizing a variety of package managers and programming languages for open source components.
