---
title: "Coverity Analysis Ant tasks"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-analysis-ant-tasks.html"
content_id: "mjC3dA_0R~2UOnnredHhzw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:42:53.866875+00:00"
---

# Coverity Analysis Ant tasks

The following Ant tasks are installed with Coverity Analysis for Java:

- `covanalyzeandcommit`
- `covbuild`

Coverity Analysis includes two Ant tasks, `covbuild` and
`covanalyzeandcommit`, to facilitate integration into existing Ant
build processes. If you use these tasks, you do not need to directly call
`cov-build`, `cov-analyze`, and
`cov-commit-defects`.

To access these tasks, include the resource `com/coverity/anttask.xml`,
located in <install_dir>
/library/coverity-anttask.jar, in a target. Define a property
`${anttask.jar}` that points to
coverity-anttask.jar. An example of how to do this follows:

```
<property name="anttask.jar" value="${sa_install_dir}/library/coverity-anttask.jar"/> 
  <target name="loadtask" description="Load the Java tasks">no the 
    <taskdef resource="com/coverity/anttask.xml" classpath="${anttask.jar}"/>
  </target>
```

Coverity Ant tasks require Java 1.5, 1.6, or 1.7. Ant
versions 1.6.0, 1.6.5, 1.7.1, and 1.8.1 are supported. Other versions of Ant that are
higher than 1.6.0 are compatible. Coverity supports compatible versions
only if an issue can be reproduced on a supported version.

Note: For assistance with Ant build files, see the Ant user
documentation at <http://ant.apache.org/manual/using.html#references>.
