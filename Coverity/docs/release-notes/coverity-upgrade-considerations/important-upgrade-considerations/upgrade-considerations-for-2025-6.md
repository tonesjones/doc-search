---
title: "Upgrade considerations for 2025.6"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/upgrade-considerations-for-2025.6.html"
content_id: "9hNAPncVMbarOAloPQiACA"
version: "2026.6"
section: "Coverity release notes and upgrade considerations"
scraped_at: "2026-08-12T19:56:48.266849+00:00"
---

# Upgrade considerations for 2025.6

For information about deprecated and dropped support, other updates, known issues, and
fixed bugs, see "Coverity 2025.6.0 Release Notes" (and the sections for associated hot
fixes) in the Coverity 2026.6.0 Release Notes Archive.

For the list of Sigma checkers disabled by default when running Coverity Analysis 2025.3,
see ["Checkers disabled in Sigma when running Coverity
Analysis"](https://documentation.blackduck.com/bundle/coverity-docs-2025.6/page/checker-ref/checkers/S/sigma._checkers.html#d100634e144) in the [*Coverity 2025.6.0 Checker
Reference*](https://documentation.blackduck.com/bundle/coverity-docs-2025.6/page/webhelp-files/checkerref_start.html).

CAUTION:

When you upgrade Coverity Analysis, all previous settings are
overwritten. All checkers listed in the [" Sigma checks disabled by default in Coverity
2025.6"](https://documentation.blackduck.com/bundle/coverity-docs-2025.6/page/checker-ref/checkers/S/sigma._checkers.html#SIGMA_checkers__section_disabled_sigma_checkers) table in the [*Coverity 2025.6.0 Checker Reference*](https://documentation.blackduck.com/bundle/coverity-docs-2025.6/page/webhelp-files/checkerref_start.html)
will be disabled by default in Coverity Analysis 2025.6, regardless of their enablement
status in previous installations.

## Changes to Bazel integration method

`cov-build` has been changed so that, by default, when it is run with
the `--bazel` argument, an agent is injected into the java process
running Bazel so that the changes that you previously had to make to either your
`WORKSPACE` file or your `MODULE.bazel` file are
made automatically as the file is read, if they’re not already present. If this
agent detects the string `rules_coverity` in a file, it will not
attempt to modify the file. Going forward, there are two options if you’ve already
modified your `WORKSPACE` or `MODULE.bazel` files:

1. Leave the files as they currently are—a warning will be emitted when you run
   `cov-build` with the `--bazel` argument,
   letting you know that the modifications are no longer necessary, but there
   won’t be any other major consequences for your build at this point; however,
   future releases may require that you move to option 2.
2. Remove all mentions of `rules_coverity` from whichever file
   you use—doing this is recommended and will allow `cov-build`
   to automatically use the version of `rules_coverity` packaged
   in the same Coverity installation as `cov-build`.

If you wish not to use the agent at this time and keep your modified
`WORKSPACE` or `MODULE.bazel` files in place, add
the argument `--bazel-disable-module-workspace-agent` to the
`cov-build` command. If you had previously modified those files
to cause an empty C++ toolchain to be registered for compatibility with builds that
don’t use C or C++, but do target platforms where Bazel doesn’t have a built in C++
toolchain, add the argument `--bazel-provide-empty-cpp-toolchain` to
the `cov-build` command.

## Analysis

- Sigma taint-flow checkers will be enabled for C#, JS and Python. Most Sigma
  taint-flow defects are expected to also be reported by Coverity taint-flow
  checkers. They will have the same defect ids, and so will not be displayed
  separately in the issue manager. However some new defects may be reported.
  In addition, a small number of duplicate defects may not properly merge with
  the corresponding Coverity defects, and will need to be retriaged in the
  issue manager.
