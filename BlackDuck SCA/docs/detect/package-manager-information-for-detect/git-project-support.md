---
title: "Git project support"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/git-project-support.html"
content_id: "sYngeGU3DjEpo_9Publ6WA"
version: "11.5.1"
section: "Package Manager information for Detect"
scraped_at: "2026-08-08T23:45:03.158835+00:00"
---

# Git project support

Unlike most detectors, the Git detectors do not discover dependencies;
they only discover project information.
Regardless of which Git detector runs, it
discovers as many of the following as it can find: project name, project version (branch), git repository URL, and commit hash.

Ideally a Git detector runs in combination with a package manager detector that discovers dependencies.
If the package manager detector is unable to derive project and project version names,
the Git detector may be able to provide them.

A Git detector will run if Detect finds a .git subdirectory in your source directory.

If Detect finds a git executable
(see the detect git executable
property)
the Git CLI detector will run git commands and derive project information from the output.

Otherwise the Git Parse detector will attempt to parse (and derive project information from)
*config*, *HEAD*, and *ORIGIN_HEAD* files within the .git subdirectory.
The Git Parse detector will only be able to discover (and supply to Black Duck SCA) the
git commit hash if it finds an *ORIGIN_HEAD* file in the .git directory.
