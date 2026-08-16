---
title: "covbuild"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/covbuild.html"
content_id: "k4kMRnOyM2xfI44tNKyvMg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:42:55.268776+00:00"
---

# covbuild

Intercept all calls to the compiler invoked by the build system using an
Ant task.

## Synopsis

```
<covbuild 
  dir="int_dir"
  [OPTIONAL_ATTRIBUTES]>
</covbuild>
```

## Description

The `covbuild` task calls Ant with a specified build file and
target, and it captures any compilations under this call.

Attributes

antargs
:   Passes command-line arguments to Ant.

antfile="build.xml"
:   Specifies the location of the build file that is called by Ant. The
    default is the current Ant build file.

binpath="<install_dir>/bin"
:   Specifies the directory containing `cov-build`. Use this
    attribute if the Ant task fails to find this command. Without this
    attribute, the Ant task searches for `cov-build` based
    on the PATH environment variable and/or the location of
    coverity-anttask.jar.

covbuildargs="options"
:   Passes space-delimited options to `cov-build`.

dir="dir"
:   Specifies the intermediate directory into which the build is
    captured.

inheritAll="false"
:   When this attribute is set to `true`, the properties
    passed to the Ant invocation that runs the `covbuild`
    task will be passed on to the Ant invocation made by the
    `covbuild` task (similar to the
    `inheritAll` attribute of the built-in Ant task,
    which ships as part of Ant). Unlike the attribute of the built-in Ant
    task, the `covbuild` attribute defaults to
    `false`.

target="target"
:   Specifies a target in the build file (see antfile). Defaults to the
    default target of the specified Ant build file.

## Examples

Note that the following are equivalent.

- Ant:

  ```
  <covbuild dir="idir" 
    antfile="build0.xml" 
    target="build"
  />
  ```
- Command line:

  ```
  > "cov-build --dir idir ant -f build0.xml build"
  ```

Additional examples:

```
<target name="build.default" depends="loadtask">
  <property environment="env4"/>
  <echo message="Current PATH = ${env4.PATH}"/>
  <covbuild
    dir="${env.SA_INT_DIR}"
    target="build1"/>
</target>

<target name="build.alternative" depends="loadtask">
  <property environment="env4"/>
  <echo message="Current PATH = ${env4.PATH}"/>
  <covbuild
    dir="${env.SA_INT_DIR}"
    antfile="alternative.xml"
    target="build-alternative"/>
</target>

<target name="build.executable" depends="loadtask">
  <echo message="binpath = ${build.binpath}"/>
  <covbuild
    binpath="${build.binpath}"
    dir="${env.PREVENTINTDIR}"
    target="build1"/>
</target>
```

## See Also

cov-build

covanalyzeandcommit
