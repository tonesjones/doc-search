---
title: "Configuring Coverity Thin Client for use with Black Duck Bridge CLI and SRM"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/configuring-coverity-thin-client-for-use-with-black-duck-bridge-cli-and-srm.html"
content_id: "G9CB~Xsr2nkoURH26SLzEg"
version: "latest"
section: "Software Risk Manager Plugins Guide"
scraped_at: "2026-09-08T20:06:10.919672+00:00"
content_hash: "ccf741fd1b29ecf56166f731994aea39a2cacfe94fa2c9900581abe1231421ff"
---

# Configuring Coverity Thin Client for use with Black Duck Bridge CLI and SRM

When you use Black Duck Bridge CLI to start a Coverity static scan, Black Duck Bridge CLI calls the Coverity Thin Client to manage code
capture. Black Duck Bridge CLI uploads the resulting data and artifacts
to SRM.

In some cases a configuration file, usually named `coverity.yaml`,
helps Coverity Thin Client by providing capture settings.

**When to use a Configuration file**

A scan is likely to succeed without any intervention for uncompiled languages like
Python, JavaScript, and PHP, because Coverity Thin Client can automatically detect
these languages and configure the scan.

Some scans require a configuration file to include project settings or optimize
Coverity for best results.

Use a configuration file in the following situations:

- When scanning a compiled language, such as C/C++, C#, Java, and Kotlin, use
  the configuration file to provide your build and clean commands.
- When scans for a project have failed or not returned useful results.

Note: Build environment components must be installed
and accessible when integrating with compiled languages, as illustrated in the
"Build commands and dependencies for various build systems" section further down in
this guide. If you plan to run build capture, make sure the build tools are
installed where the capture will run.

Things you can specify with the Coverity Thin Client configuration file:

- Your build and clean commands
- Whether source code in a specific language should be captured or
  excluded.
- A custom compiler configuration. This is helpful if you are compiling C++
  and Coverity does not automatically configure the compiler (for example,
  when using a GCC cross-compiler).

## How to start a configuration file

Save a `coverity.yaml` file in your project's root directory and use
the following examples to customize that file. When Coverity Thin Client is called
by Black Duck Bridge CLI, it automatically detects the file, reads the
contents, and executes custom configurations.

## Basic examples

For more build and clean commands see the reference section at the end of the
chapter.

**Java with Maven**

The following configuration specifies the clean and build commands needed by Maven.
The project will be cleaned by invoking mvn clean and built
using mvn install.

```
capture:
   build:
      clean-command: mvn clean
      build-command: mvn install
```

About this example:

- This example shows the complete contents of a
  coverity.yaml file that you can use to test a Maven
  project.
- Note that white space matters in YAML files. The three levels of indentation
  indicate that the build property is nested under the capture property and
  build-command and clean command are nested under build.

**Standard Java example**

```
capture:   
   build:
      build-command:  javac HelloWorld.java
```

**C# with msbuild**

```
capture:
   build:
      clean-command: dotnet msbuild /t:Restore;Clean OWASPTop10.SqlInjection.Web.csproj
       build-command: dotnet msbuild /t:Restore;Build OWASPTop10.SqlInjection.Web.csproj
```

**C# with dotnet**

```
capture:
   build:
      clean-command: dotnet clean Foo.sln
      build-command: dotnet build Foo.sln
```

**Executable script as a build command**

```
capture:
   build:
      clean-command: clean.sh
      build-command: build-it.sh
```

Coverity Thin Client will only accept one build command and one clean command in the
config file, but you can point to a script containing commands if you need more.

## Configuration properties

The tables in this section describe each of the keys that can be used in the
`coverity.yaml` file, starting at the top level with capture.

**Capture settings**

The following table describes the capture configuration; subsections describe the
fields that make up the Capture type. All the Keys in the first column of this table
can be nested directly under the capture key in the `coverity.yaml`
file. (For example, build can be seen in the first row of the table and is used in
the example immediately above.)

| Key | Type | Description |
| --- | --- | --- |
| build | Build Configuration | Specifies that build capture should be used to capture the project and provides the build configuration to use. If not specified and the project directory contains compiled source files, automatic build capture will be used to capture compiled source files in the project directory.  For compiled languages only: Java, Kotlin, C#, C, C++, Objective-C, Objective-C++.  See the Build configuration table below for keys that can be nested under this one. |
| encoding | string | Specifies the encoding to use when parsing and emitting the source files in C, C++, JavaScript.**Default**: US-ASCII |
| languages | Languages Configuration | Specifies which languages to include or exclude for capture.  See Language configuration for a list of supported languages.  **Default**: all languages are included  See the table in the Language configuration section for keys that can be nested under the languages key. |

**Build settings**

The following keys can be defined for compiled languages only. All the keys in this
table can be nested directly under the build key in the configuration file.

| Key | Type | Description |
| --- | --- | --- |
| aspnet-compiler | Boolean | Specifies whether to enable or disable the automatic invocation of `Aspnet_compiler.exe` for any ASP.NET 4 and earlier Web applications that are detected in the build. The output of `Aspnet_compiler.exe` is required by the C# security checker. |
| build-command | String | **Required**: The build command will be invoked to use build capture to capture the project. A build command specified on the command-line will override this setting. |
| clean-command | String | The clean command will be invoked prior to doing build capture to capture the project. |

For example:

```
capture:
   build:
      clean-command: dotnet msbuild /t:Restore;Clean OWASPTop10.SqlInjection.Web.csproj
      build-command: dotnet msbuild /t:Restore;Build
      aspnet-compiler: true
```

**Language configuration**

Use the following keys to specify which languages to include or exclude from capture.
You may not specify both fields.

**Language strings may be the following:**

- apex
- c-family *(This family includes C, C++, Objective C, and Objective
  C++)*
- csharp
- go
- java *(Includes JSP and android config files)*
- javascript *(Includes JavaScript and TypeScript)*
- kotlin
- php
- python
- ruby
- swift
- vb *(Visual Basic)*

**The following languages are not supported by the Coverity CLI**:

- CUDA
- Fortran
- Scala

Keys in this table can be nested under the `languages` key, which
appears in the first table above and is nested under the `capture`
key.

| Key | Type | Description |
| --- | --- | --- |
| include | Array of String | Specifies the languages for which the source code should be included in the capture. This key is mutually exclusive with the exclude key.  **Default**: all languages are included. |
| exclude | Array of String | Specifies the languages for which the source code should be excluded in the capture. This key is mutually exclusive with the include key.  **Default**: No languages are excluded. |

For example:

```
capture: 
   languages: 
      exclude:
         - python
```

## **Build commands and dependencies for various build systems**

You may need to install the machine dependencies in order to run the corresponding
build. If build and clean commands don't work—check for the dependencies.

| Build System | How to Detect | Minimal Set of Machine Dependencies | Build and Clean commands |
| --- | --- | --- | --- |
| Maven | Look for the presence of "pom.xml" files in the project directory | [Maven build tool](https://maven.apache.org/download.cgi)  [Java compiler](https://www.oracle.com/java/technologies/downloads/) | `build-command:` mvn -DskipTests -DskipITs install  `clean-command:` mvn clean |
| Gradle | Look for the presence of "build.gradle" files in the project directory |  |  |
| With a "gradlew" file (Linux/Mac) | [Java compiler](https://www.oracle.com/java/technologies/downloads/)  (Gradle will be downloaded automatically) | `build-command:` gradlew --no-daemon -x test build testClasses  `clean-command:` gradlew clean |
| With a "gradlew.bat file (Windows) | [Java compiler](https://www.oracle.com/java/technologies/downloads/)  (Gradle will be downloaded automatically) | `build-command:` gradlew.bat --no-daemon -x test build testClasses  `clean-command:` gradlew.bat clean |
| Without a "gradlew" or "gradlew.bat" file | [Gradle build tool](https://gradle.org/install/)  [Java compiler](https://www.oracle.com/java/technologies/downloads/) | `build-command:` gradle --no-daemon -x test build testClasses  `clean-command:` gradle clean |
| Make | Look for the presence of a file called "Makefile" | [Make build tool](https://www.gnu.org/software/make/)  Compiler for the appropriate language | `build-command:` make  `clean-command:` make clean |
| Ant | Look for the presence of a "build.xml" | [Ant build tool](https://ant.apache.org/bindownload.cgi)  [Java compiler](https://www.oracle.com/java/technologies/downloads/) | `build-command:` ant  `clean-command:` ant clean |
| MSBuild | Look for the presence of files with ".sln" or ".csproj" extensions. | [.NET SDK](https://dotnet.microsoft.com/en-us/download/visual-studio-sdks) | `build-command:` dotnet msbuild /t:Build  `clean-command:` dotnet msbuild /t:Restore;Clean |
| XCode | Look for the presence of directories ending with ".xcodeproj" | [XCode](https://developer.apple.com/xcode/) | `build-command:` xcodebuild -workspace <xcodeproj dir> -scheme <scheme> build -UseModernBuildSystem=No CODE_SIGN_IDENTITY= CODE_SIGNING_REQUIRED=NO  `clean-command:` xcodebuild -workspace <xcodeproj dir> -scheme <scheme> clean |

## GCC configuration

The GNU Compiler Collection (GCC) requires its own `coverity.yaml`
configuration settings. To use GCC, add lines to:

- Specify the GCC compiler using `cov-configure`.
- Designate the language and CPU
  target:

  ```
  cov-configure:
      - [ --template, --compiler, arm-linux-gnueabi-gcc, --comptype, gcc ]
      - [ --template, --compiler, arm-linux-gnueabi-g+, --comptype, g+ ]
  ```

Below is an example `coverity.yaml` settings block for GCC, telling
it to run a `make clean` then run the `make` command
in parallel with at least 10 job slots (`make -j 10`).

```
C/C++ Cross Compiler coverity.yaml example:
-------------------------------------------
# Coverity configuration file.
# The schema is available here: <install-dir>/doc/configuration-schema.json
capture:
  build:
    clean-command: "make clean"
    build-command: "make -j 10"
  compiler-configuration:
    cov-configure:
    - [ --template, --compiler, arm-linux-gnueabi-gcc, --comptype, gcc ]
    - [ --template, --compiler, arm-linux-gnueabi-g+, --comptype, g+ ]
```

Note: Pay special attention to GCC binary naming conventions if using more than one
language and/or CPU target.
