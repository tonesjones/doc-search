---
title: "pip"
source_url: "https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/pip.html"
content_id: "_lSpJ2uWh9s~VOF_9B_05w"
version: "12.0.0"
section: "Detect Properties"
scraped_at: "2026-09-07T21:16:56.253747+00:00"
---

# pip

## Pipenv Executable

```
--detect.pipenv.path
```

The path to the Pipenv executable.

| Details |  |
| --- | --- |
| Added | 4.1.0 |
| Type | Optional Path |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Pip Executable

```
--detect.pip.path
```

The path to the Pip executable.

| Details |  |
| --- | --- |
| Added | 6.8.0 |
| Type | Optional Path |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Pipfile Dependency Types Excluded

```
--detect.pipfile.dependency.types.excluded=NONE,DEV
```

A comma-separated list of dependency types that will be excluded.

If DEV is excluded, the Pipfile Lock Detector will exclude 'develop' dependencies when parsing the Pipfile.lock file.

| Details |  |
| --- | --- |
| Added | 7.13.0 |
| Type | PipenvDependencyType List |
| Default Value | NONE |
| Comma Separated | Yes |
| Case Sensitive | No |
| Acceptable Values | NONE, DEV |
| Strict | Yes |
| Example | `DEV` |

## PIP Include Only Project Tree

```
--detect.pip.only.project.tree=false
```

By default, pipenv includes all dependencies found in the graph. Set to true to only include dependencies found underneath the dependency that matches the provided pip project and version name.

| Details |  |
| --- | --- |
| Added | 6.1.0 |
| Type | Boolean |
| Default Value | false |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## PIP Project Name

```
--detect.pip.project.name
```

The name of your PIP project, to be used if your project's name cannot be correctly inferred from its setup.py file.

| Details |  |
| --- | --- |
| Added | 3.0.0 |
| Type | Optional String |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## PIP Project Version Name

```
--detect.pip.project.version.name
```

The version of your PIP project, to be used if your project's version name cannot be correctly inferred from its setup.py file.

| Details |  |
| --- | --- |
| Added | 4.1.0 |
| Type | Optional String |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## PIP Requirements Path

```
--detect.pip.requirements.path
```

A comma-separated list of paths to requirements files, to be used to analyze requirements files with a filename other than requirements.txt or to specify which requirements files should be analyzed.

This property should only be set if you want the PIP Inspector Detector to run. For example: If your project uses Pipenv, do not set this property.

| Details |  |
| --- | --- |
| Added | 3.0.0 |
| Type | Path List |
| Default Value |  |
| Comma Separated | Yes |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |
