---
title: "The analysis"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-analysis.html"
content_id: "nkZn2DQlkaXSXGIwqSAOgA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:32:47.863813+00:00"
---

# The analysis

After capturing your source (see The capture), you can invoke `cov-analyze`
to run Coverity Analysis on your source code and find software issues.

For example, here is a command line to start an analysis:

```
> cov-analyze --dir <intermediate_directory> --strip-path <path/to/source/code>
```

Note:
As shown here, we highly recommend that you use the --strip-path option with
`cov-analyze` to specify the root directory of the source
code tree. This shortens the paths that Coverity Connect will display.
It also allows your deployment to be more portable if you need to move it to a new machine in
the future.

Using --strip-path with `cov-analyze` can also enhance overall performance when you commit
the analysis results to Coverity Connect.

By default, the `cov-analyze` command analyzes all code in
the specified intermediate directory through a single invocation of the
`cov-analyze` command. The command runs a series of default
checkers. You can add or remove checkers from the analysis. For information
about which checkers are enabled by default and how to enable additional
checkers, see "Enabling and disabling checkers" in
Customizing Coverity.

## Licensing

If you get a fatal `No license
found` error when you attempt to run this command, you need to make sure
that license.dat was copied correctly to <install_dir>/bin.

To correct this issue, see "Setting up a license.dat
file" in the Coverity 2026.6.0 Installation and Upgrade Guide.

## See also:

- The analysis: Special cases
- The analysis: Analysis Summary Report
