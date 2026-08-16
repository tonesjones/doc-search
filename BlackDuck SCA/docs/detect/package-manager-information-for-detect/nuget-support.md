---
title: "NuGet support"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/nuget-support.html"
content_id: "4y8oUw1fquHS1i5vPJgtrQ"
version: "11.5.1"
section: "Package Manager information for Detect"
scraped_at: "2026-08-08T23:45:08.228962+00:00"
---

# NuGet support

## Related properties

Detector properties

## Overview

The NuGet detectors are used to discover dependencies of NuGet projects.

There are three NuGet detectors:

- NuGet Solution Native Inspector
- NuGet Project Native Inspector
- NuGet Project Inspector

The detectors run a platform dependent self-contained executable that is currently supported on Windows, Linux, and Mac platforms.

Tip:

To retrieve project build information, NuGet Project Inspector relies on a Microsoft API which is dependant upon the installation of .NET 6.0 on the build machine.

- To ensure the most accurate results available, .NET 6.0 should be installed. The inspector will fall back to parsing the XML files if .NET 6.0 is not present.
- NuGet Project Inspector does not accept NuGet specific configuration properties.
- The NuGet Detectors do not work with mono.

## Excluding dependency types

Detect offers the ability to exclude package manager specific dependency types from the BOM.
Nuget dependency types can be filtered with the detect.nuget.dependency.types.excluded property.
This property supports exclusion of development-only dependencies in projects that use `PackageReference`, `packages.config`, `project.assests.json` or `project.lock.json`.

Note: Support for declaring dependencies in JSON files has been deprecated by NuGet. As such this property does not apply to scans that analyze `project.json`.

A project might be using a dependency purely as a development harness and you might not want to expose that to projects that will consume the package. You can use the PrivateAssets metadata to control this behavior. Detect looks for the PrivateAssets attribute used within PackageReference tags to identify a development dependency. Detect will ignore the contents of the tag and only observe the presence of these PrivateAssets to exclude those development related dependencies.
For packages.config file, Detect will look for developmentDependency tags to determine whether to include or exclude a dependency.

## NuGet Artifacts and Base Intermediate Output Paths

Detect supports the ArtifactsPath and BaseIntermediateOutputPath properties provided by NuGet to customize the path in which build artifacts are stored. The default location for storing artifacts is the \obj folder under each project directory, in which XML files for the project such as csproj are present.

To simplify the output paths and gather all the artifacts in a common location, support for the above properties was introduced. To support these properties, Detect uses the detect.nuget.artifacts.path property, which allows you to specify a custom project.assets.json location.

Detect will examine all directories in the provided path to find the project.assets.json file for the project being scanned.

To avoid using .NET 6 to retrieve the artifacts path from the Directory.Build.props file, it is required that the directory specified by the detect.nuget.artifacts.path property have permission set to allow Detect access.

### Detect NuGet Inspector downloads

Detect jar execution will automatically download any required binaries not located in the cache.

For direct access to the binaries or source code see download locations.

### Inspector Operation

An inspector is self-contained and requires no installation. Each executable is platform dependent and the correct inspector is downloaded by Detect at runtime.

NuGet Solution Native Inspector runs if one or more solution (.sln) files are found and derives packages (dependencies) via analysis of solution files. Central Package Management is supported to include any package versions and global package references mentioned under `Directory.Packages.props` files indicated the (.sln) file for each project under the solution. Any package references and versions in the solution's `Directory.Build.props` will be included for each project under the solution.

Tip: When running the NuGet Solution Native Inspector the `--detect.detector.search.depth=` value is ignored if a solution (.sln) file is found that contains project references that include subdirectories at levels lower than the specified search depth.

NuGet Project Native Inspector runs if no solution (.sln) files are found, and one or more project files are found. NuGet Project Native Inspector derives packages (dependencies) from project (.csproj, .fsproj, etc.) file content.

NuGet Native Project inspectors look for files to derive dependency information from in this order (only the first available in the list will be analyzed):

1. Directory.Packages.props
2. packages.config
3. project.lock.json
4. project.assets.json
5. project.json
6. XML of the project file

In addition to the packages and dependencies found from the above files, packages and dependencies will be included from other `project.assets.json` files if configured in the corresponding project's property file. (`<projectname>.<projectfiletype>.nuget.g.props`).

After discovering dependencies, NuGet client libraries are used to collect further information about the dependencies and write them to a JSON file (`<projectname>_inspection.json`). Detect then parses that file for the dependency information.

### NuGet Project Native Inspector supported project files

| Azure Stream Analytics | Cloud Computing | Common Project System Files | C# | Deployment | Docker Compose | F# |
| --- | --- | --- | --- | --- | --- | --- |
| *.asaproj | *.ccproj | *.msbuildproj | *.csproj | *.deployproj | *.dcproj | *.fsproj |

| Fabric Application | Hive | JavaScript | .NET Core | Node.js | Pig | Python |
| --- | --- | --- | --- | --- | --- | --- |
| *.sfproj | *.hiveproj | *.jsproj | *.xproj | *.njsproj | *.pigproj | *.pyproj |

| RStudio | Shared Projects | SQL | SQL Project Files | U-SQL | VB | VC++ |
| --- | --- | --- | --- | --- | --- | --- |
| *.rproj | *.shproj | *.sqlproj | *.dbproj | *.usqlproj | *.vbproj | *.vcxproj *.vcproj |

### NuGet Detector buildless mode

In buildless mode, Detect uses Project Inspector to find dependencies and only supports `.csproj` and `.sln` files.

As of Detect 9.5.0 the version of Project Inspector in use supports the `--build-system MSBUILD` argument in place of `--strategy MSBUILD`.
The `--force-nuget-repos "url"` argument will be removed from support in the next Detect major release and replaced with the `--conf "nuget.repo:url"` argument.

### Detect NuGet Inspector on Alpine

The Detect NuGet Inspectors depend on packages not installed by default on Alpine systems, such as the dynamic loader for DLLs.

When the dynamic loader is not present, an error message similar to the following appears in the log as a result of
Detect's attempt to execute the NuGet Inspector:

```
java.io.IOException: Cannot run program ".../tools/detect-nuget-inspector/detect-nuget-inspector-1.0.1-linux/detect-nuget-inspector" (in directory ...): error=2, No such file or directory
```

To add these packages to an Alpine system:

```
apk add libstdc++ gcompat icu
```
