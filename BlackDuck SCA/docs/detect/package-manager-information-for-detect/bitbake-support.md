---
title: "BitBake support"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/bitbake-support.html"
content_id: "y6N4zLCl3UxSpDT4JahPjA"
version: "11.5.1"
section: "Package Manager information for Detect"
scraped_at: "2026-08-08T23:44:48.906781+00:00"
---

# BitBake support

## Related properties

Detector properties

## Requirements

The BitBake detector will run if it finds a BitBake build environment setup script (which defaults to *oe-init-build-env*, but can be configured
using property *detect.bitbake.build.env.name*)
and at least one package (target image) name is provided using property *detect.bitbake.package.names*.

If you are excluding build dependencies using the *detect.bitbake.dependency.types.excluded* property, the {builddir}/tmp directory must be left intact since a file (license.manifest)
that Detect uses in that scenario resides in that tmp directory.

## Processing

The BitBake detector builds a dependency graph (codelocation) for each given package (target image). It sources your project's build environment setup
script (by default: oe-init-build-env), and executes BitBake commands to collect project and dependency details.

The BitBake detector generates one codelocation for each given package (target image) name by performing the following steps:

1. Determines the build directory path by sourcing the given build environment setup script and determining the resulting working directory.
2. Runs 'bitbake --environment' to determine the currently-configured target machine architecture and licenses directory path.
3. Runs 'bitbake-layers show-recipes' to derive the list of layers and collect recipe layer information.
4. For each given package (target image) name:

- If the user requested that build dependencies be excluded, Detect locates and reads the license.manifest file for the given package (target image) and the currently-configured target machine architecture. This provides a list of recipes that are included in the target image (the non-build dependencies).
- Runs 'bitbake -g {package}' to generate task-depends.dot, and reads recipes and dependency relationships from it.
- If the user requested that build dependencies be excluded: Detect excludes recipes not declared in license.manifest, as well as native recipes. Detect always excludes virtual recipes (recipes with names prefixed with "virtual/").
- Detect adds at the root level of the graph for the package (target image) each recipe found in task-depends.dot that is not excluded as described above.
- Child (transitive) relationships are created from those root dependencies to their children (as specified in task-depends.dot).

Before running each BitBake command, Detect sources the build environment init script,
passing any arguments the user has provided via the *detect.bitbake.source.arguments* property.

## Configuration

Detect properties provide a number of different ways to customize the BitBake detector's behavior for your project. A few of the most important are:

1. You can configure the build environment setup script name using the *detect.bitbake.build.env.name property*.
2. You can add arguments (such as the path to your build directory) to the 'source {build env setup script}' command that Detect executes using the *detect.bitbake.source.arguments* property.
3. You can exclude build dependencies from results using the *detect.bitbake.dependency.types.excluded* property.

See the BitBake properties page for a complete list of BitBake detector-related properties and details on how to use them.

## Troubleshooting Tips

### Missing components for projects using the Yocto Package Revision Service

Symptom: Components are missing from the Black Duck SCA BOM.

Problem: The Yocto Package Revision Service can increment a package revision to a value not present in the Black Duck SCA Knowledge Base, causing
a package to fail to match.
