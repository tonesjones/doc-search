---
title: "Code Sight version 2019.11"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/code-sight-version-2019.11.html"
content_id: "iEdotpt98C0oWyb_0oPG~Q"
version: "2026.9.0"
section: "Code Sight Release Notes and Known Issues"
scraped_at: "2026-10-06T23:40:01.107108+00:00"
---

# Code Sight version 2019.11

The 2019.11 release of the Black Duck® Code Sight™ plug-in introduces new features
and fixes various bugs.

## New features

- Eclipse™ version 2019-09 (4.13) is now supported.
- Android™ Studio version 3.5 is now supported (support for both version
  3.4 and 3.5 of Android Studio is in beta for this release).
- Icons in a new Status column in the Scans panel show whether the scan
  of an individual file is pending or in progress.
- The Location column in the Scans panel now shows the end, rather than
  the beginning, of a file’s path name.
- For Polaris users, depending on your configuration Code Sight now attempts to use the tools specified either
  in your local polaris.yml file, or on your Polaris server.
  In other words, you can now explicitly specify the tool version you want Code Sight to run, and are no longer
  restricted to using the most recent release of a tool.
- During build capture, Code Sight uses the build command specified in the `"cov_run_desktop"`
  record of the coverity.conf file, provided that `"build_cmd"` is specified and
  `"build_strategy"` is set to `"CUSTOM"` in the `"ide"` record.

  If `"clean_cmd"` is also specified `"build_strategy": "CUSTOM"` enables that as well.

  The following code example shows these settings:

```
...
"cov_run_desktop": {
    "build_cmd": ["make", "-j", "$(num_cores)"], // build command
    "clean_cmd": ["make", "clean"]               // clean command
},
"ide": {
    "build_strategy": "CUSTOM"
    ...
}
```

## Bug fixes

- Code Sight now respects the Eclipse JavaScript® exclude path when performing a full scan locally.
  UD-1216
- This release fixes an issue with “The elevated helper does not have full admin rights” that occurred on
  Windows® during the installation of Coverity® Analysis when it was downloaded from Polaris.
  This bug is resolved as long as updated Coverity Analysis Tools are configured to be downloaded from Polaris version 2019.11.
  UD-3351
- Fixed an issue where Code Sight was incorrectly reporting that a full scan had been started
  (“Black Duck: Improving accuracy ...” in the progress notification bar)
  whenever *any* new scan was started, including an individual file scan.
  UD-3371
- This release fixes an issue where Code Sight for Visual Studio® caused delays in the IDE when opening large solutions
  containing many projects.
  UD-3477
- This release fixes an issue where Code Sight for IntelliJ® caused high resource usage when working with large projects.
  UD-3494
- This release fixes an issue where Visual Studio 2019 was incorrectly displaying the “Tool Compatibility Warning”
  for analysis tools when running Code Sight with newer Coverity Analysis Tools.
  UD-3673
- This release fixes an issue in Code Sight for Visual Studio where an error message for the issue location was
  incorrectly displayed for a file that was found locally.
  UD-3696
- This release fixes an issue with Code Sight for Visual Studio where the Code Sight tool window continued to report
  “No solutions have been opened” after opening a solution.
  UD-3779
- Fixed an issue where Code Sight crashed and failed to scan when a `polaris.yml` file specified an invalid tool version.
  UD-3823
