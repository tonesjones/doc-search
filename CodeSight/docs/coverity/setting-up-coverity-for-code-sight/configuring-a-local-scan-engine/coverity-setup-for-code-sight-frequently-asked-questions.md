---
title: "Coverity setup for Code Sight: Frequently asked questions"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/coverity-setup-for-code-sight-frequently-asked-questions.html"
content_id: "hfeMfer1FNtxw__g_sKIbg"
version: "2026.9.0"
section: "Coverity with Code Sight"
scraped_at: "2026-10-06T23:39:53.287145+00:00"
---

# Coverity setup for Code Sight: Frequently asked questions

Here are some questions that can arise.

## What happens if both a Coverity configuration file and a polaris.yml file specify a server URL?

- If you entered a URL when you used the Notifications panel to authenticate yourself,
  then that is the URL that Code Sight uses.
- Otherwise, Code Sight uses the URL in polaris.yml.
  This is simply because Code Sight reads polaris.yml before it reads the project-specific coverity.conf,
  if one is in use (and Code Sight does not read the CLI-based configuration files, at all).

CAUTION:

If different projects in your IDE specify different servers, then Code Sight uses the correct server,
but the server name shown in the Code Sight interface might not be the correct one.

## If multiple versions of Coverity Analysis are installed, which version will Code Sight run?

- If polaris.yml is present and specifies a valid version of Coverity Analysis,
  then Code Sight uses that version.
- Otherwise, Code Sight uses the installation that matches the current project and stream.
  If these are not known, it uses the most recent version specified in the local, user-specific coverity.conf file, if one is present.

## What if I get a report of a central analysis issue, but Code Sight does not locate the issue in my local source code?

Typically the central analysis server saves path names in a relative format; for example:

```
../project/source/testme.java
```

Instead of relative paths, a local instance of Coverity Analysis typically saves file names
as absolute paths. The format of an absolute path depends on the operating system.
For example:

```
C:\Users\your-name-here\project\source\testme.java
```

To resolve this issue, in the configuration file that you use, add an `"ide"` object,
and then within it create a `"path_mapping"` object to specify (1) the paths to strip off of the
path names from central analysis, and (2) the local paths to search for.

The object has this format:

```
"ide": {
    "path_mapping": {
        "strip_paths":  [ "path1", "path2" ],
        "search_paths": [ "path3", "path4" ]
    }
}, ...
```

So using the previous example, testing only a single project, the `"ide"` object might look like
the following JSON code:

```
"ide": {
    "path_mapping": {
        "strip_paths":  [ "../" ],
        "search_paths": [ "C:\Users\your-name-here\" ]
    }
}, ...
```

For additional information, see the “IDESettings” and “PathMapping” sections in the
*Coverity Desktop Analysis User Guide*.
