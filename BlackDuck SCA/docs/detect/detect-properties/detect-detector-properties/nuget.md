---
title: "nuget"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/nuget.html"
content_id: "ELNbmNjUPKoS~EwcY6KXsQ"
version: "11.5.1"
section: "Detect Properties"
scraped_at: "2026-08-08T23:45:40.117329+00:00"
---

# nuget

## Nuget Artifacts Path

```
--detect.nuget.artifacts.path
```

The path to the obj directory build artifacts of the NuGet project, if not the default path.

| Details |  |
| --- | --- |
| Added | 10.3.0 |
| Type | Optional Path |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Nuget Config File

```
--detect.nuget.config.path
```

The path to the Nuget.Config file to supply to the nuget exe.

| Details |  |
| --- | --- |
| Added | 4.0.0 |
| Type | Optional Path |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Nuget Dependency Types Excluded

```
--detect.nuget.dependency.types.excluded=NONE,DEV
```

Set this value to indicate which Nuget dependency types Detect should exclude from the BOM.

This property supports exclusion of dependencies in projects that use PackageReference, packages.config, project.lock.json or project.assets.json. This property does not apply to scans that analyze project.json. For more information, refer to [excluding NuGet dependency types.](https://documentation%2Eblackduck%2Ecom/bundle/detect/page/packagemgrs/nuget%2Ehtml/#ariaid%2Dtitle4)

| Details |  |
| --- | --- |
| Added | 9.4.0 |
| Type | NugetDependencyType List |
| Default Value | NONE |
| Comma Separated | Yes |
| Case Sensitive | No |
| Acceptable Values | NONE, DEV |
| Strict | Yes |
| Example | `DEV` |

## Nuget Packages Repository URL

```
--detect.nuget.packages.repo.url=https://api.nuget.org/v3/index.json
```

The source for nuget packages

Set this to "https://www.nuget.org/api/v2/" if your are still using a nuget client expecting the v2 api.

| Details |  |
| --- | --- |
| Added | 3.0.0 |
| Type | String List |
| Default Value | https://api.nuget.org/v3/index.json |
| Comma Separated | Yes |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Ignore Nuget Failures (Advanced)

```
--detect.nuget.ignore.failure=false
```

If true errors will be logged and then ignored.

| Details |  |
| --- | --- |
| Added | 3.0.0 |
| Type | Boolean |
| Default Value | false |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## NuGet Inspector Path (Advanced)

```
--detect.nuget.inspector.path
```

Use this property to point Detect to a local NuGet Inspector executable, instead of the default that Detect downloads from the binary repository.

| Details |  |
| --- | --- |
| Added | 11.2.0 |
| Type | Optional Path |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |
| Example | `/path/to/unzipped/detect-nuget-inspector` |

## Nuget Projects Excluded (Advanced)

```
--detect.nuget.excluded.modules
```

The projects within the solution to exclude. Detect will exclude all projects with names that include any of the given regex patterns. To match a full project name (for example: 'BaGet.Core'), use a regular expression that matches only the full name ('^BaGet.Core$'). Note that the term 'modules' in the parameter name is synonymous with Nuget 'project'.

| Details |  |
| --- | --- |
| Added | 3.0.0 |
| Type | String List |
| Default Value |  |
| Comma Separated | Yes |
| Case Sensitive | Yes |
| Acceptable Values | Any |
| Strict | No |
| Example | `^BaGet.Core$,^BaGet.Core.Tests$` |

## Nuget Projects Included (Advanced)

```
--detect.nuget.included.modules
```

The names of the projects in a solution to include (overrides exclude). Detect will include all projects with names that include any of the given regex patterns. To match a full project name (for example: 'BaGet.Core'), use a regular expression that matches only the full name ('^BaGet.Core$'). Note that the term 'modules' in the parameter name is synonymous with Nuget 'project'.

| Details |  |
| --- | --- |
| Added | 3.0.0 |
| Type | String List |
| Default Value |  |
| Comma Separated | Yes |
| Case Sensitive | Yes |
| Acceptable Values | Any |
| Strict | No |
| Example | `^BaGet.Core$,^BaGet.Core.Tests$` |
