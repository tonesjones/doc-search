---
title: "Integrating Coverity Analysis into the build environment—'cov-build'"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/integrating-coverity-analysis-into-the-build-environment-cov-build-.html"
content_id: "nzi88gISU_MffJ9wtAbhGQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:33:58.989772+00:00"
---

# Integrating Coverity Analysis into the build environment—'cov-build'

The `cov-build` command integrates Coverity Analysis with a
build system, usually without any modifications to the build system itself. Using
`cov-build` is the preferred method of build integration. Figure 2 shows
the basic process that `cov-build` uses to piggyback on a build system to
produce the intermediate data. This intermediate data can then be analyzed to produce
defect reports. For information about alternative build integration commands, see Alternative build command: 'cov-translate'.

After the cov-config.xml file is created, you can run the
`cov-build` command by placing it in front of your usual build
command. The required `--dir` option specifies the intermediate
directory.

If the build command depends on features of the command shell that usually invoke it,
such as certain shell variables or non-alphanumeric arguments, invoke the build command
with a wrapper script. This method preserves the original behavior, since the build
command is directly invoked by the type of shell on which it depends.

For example, if the normal invocation of a Windows build is:

```
> build.bat Release"C:\Release Build Path\"
```

use:

```
> cov-build --dir <intermediate_directory> wrapper.bat
```

where wrapper.bat is an executable command script that contains the
original and unmodified build command.

On Windows systems, specify both the file name and extension for the build command when
using `cov-build`.

For example:

```
> cov-build --dir <intermediate_directory> custombuild.cmd
```

Because `cov-build` uses the native Windows API to launch the build
command, the appropriate interpreter must be specified with any script that is not
directly executable by the operating system. For example, if the normal invocation of a
build within Msys or Cygwin is:

```
> build.sh
```

prefix it with the name of the shell:

```
> cov-build --dir <intermediate_directory> sh build.sh
```

Similarly, if a Windows command file does not have Read and Execute permissions, invoke
it as:

```
> cov-build --dir <intermediate_directory> cmd /c build.bat
```

The time that it takes to complete a build increases when you use
`cov-build` because after the normal build runs, the Coverity
compiler parses the same files again to produce the intermediate data. Consider the
following factors that can increase build times with `cov-build`:

- The intermediate data directory is on a network mounted drive. Coverity Analysis creates many files and subdirectories in the
  intermediate directory, and these operations can be slow on network file systems.
  Using an intermediate directory on a local disk can eliminate this bottleneck. On
  Windows, you must use a local drive for the intermediate directory (Windows shared
  network drives are not supported for the intermediate directory).
- `cov-emit` does not take advantage of pre-compiled headers.

If the speed of `cov-build` is prohibitively slow when compared with
your normal build time, one possible solution is to use more processes to parallelize
the build. To see how to do so without altering your build scripts, see the section
describing record/replay.

In this section:

- The output of 'cov-build': The 'build-log.txt' log file
- Building non-ASCII source code
- Detecting parse warnings, parse errors, and build failures
- Getting linkage information
- Record/Replay: Deferred builds and parallelizing single-process builds
- Error handling with commands
- Troubleshooting build problems
- Platform-specific 'cov-build' issues
