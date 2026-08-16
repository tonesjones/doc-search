---
title: "gradle"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/gradle.html"
content_id: "Zh66buQNZAzFcMrxTAP4mg"
version: "11.5.1"
section: "Detect Properties"
scraped_at: "2026-08-08T23:45:36.822066+00:00"
---

# gradle

## Gradle Build Command

```
--detect.gradle.build.command
```

Gradle command line arguments to add to the gradle/gradlew command line.

By default, Detect runs the gradle (or gradlew) command with one task: dependencies. You can use this property to insert one or more additional gradle command line arguments (options or tasks) before the dependencies argument.

| Details |  |
| --- | --- |
| Added | 3.0.0 |
| Type | Optional String |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Gradle Configuration Types Excluded

```
--detect.gradle.configuration.types.excluded=NONE,UNRESOLVED
```

Set this value to indicate which Gradle configuration types Detect should exclude from the BOM.

Including dependencies from unresolved Gradle configurations could lead to false positives. Dependency versions from an unresolved configuration may differ from a resolved one. See Gradle docs [for more information.](https://docs%2Egradle%2Eorg/8%2E2/userguide/declaring%5Fdependencies%2Ehtml)

| Details |  |
| --- | --- |
| Added | 7.10.0 |
| Type | GradleConfigurationType List |
| Default Value | NONE |
| Comma Separated | Yes |
| Case Sensitive | No |
| Acceptable Values | NONE, UNRESOLVED |
| Strict | Yes |
| Example | `UNRESOLVED` |

## Gradle Executable

```
--detect.gradle.path
```

The path to the Gradle executable (gradle or gradlew).

If set, Detect will use the given Gradle executable instead of searching for one.

| Details |  |
| --- | --- |
| Added | 3.0.0 |
| Type | Optional Path |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Gradle Exclude Configurations (Advanced)

```
--detect.gradle.excluded.configurations
```

A comma-separated list of Gradle configurations to exclude.

As Detect examines the Gradle project for dependencies, Detect will skip any Gradle configurations specified via this property. This property accepts filename globbing-style wildcards. For more information, refer to the [Property wildcard support page.](https://documentation%2Eblackduck%2Ecom/bundle/detect/page/configuring/propertywildcards%2Ehtml)

| Details |  |
| --- | --- |
| Added | 3.0.0 |
| Type | String List |
| Default Value |  |
| Comma Separated | Yes |
| Case Sensitive | Yes |
| Acceptable Values | Any |
| Strict | No |

## Gradle Exclude Projects (Advanced)

```
--detect.gradle.excluded.projects
```

A comma-separated list of Gradle subprojects to exclude.

As Detect examines the Gradle project for dependencies, Detect will skip any Gradle subprojects specified via this property. This property accepts filename globbing-style wildcards. For more information, refer to the [Property wildcard support page.](https://documentation%2Eblackduck%2Ecom/bundle/detect/page/configuring/propertywildcards%2Ehtml)

| Details |  |
| --- | --- |
| Added | 3.0.0 |
| Type | String List |
| Default Value |  |
| Comma Separated | Yes |
| Case Sensitive | Yes |
| Acceptable Values | Any |
| Strict | No |

## Gradle Exclude Subproject Paths (Advanced)

```
--detect.gradle.excluded.project.paths
```

A comma-separated list of Gradle subproject paths to exclude.

As Detect examines the Gradle project for dependencies, Detect will skip any Gradle subproject whose path matches one of the values passed via this property. Run 'gradle projects' to see the paths to your subprojects. Subproject paths have the form ':subproject:subsubproject' and are unique. This property accepts filename globbing-style wildcards. For more information, refer to the [Property wildcard support page.](https://documentation%2Eblackduck%2Ecom/bundle/detect/page/configuring/propertywildcards%2Ehtml)

| Details |  |
| --- | --- |
| Added | 7.12.0 |
| Type | String List |
| Default Value |  |
| Comma Separated | Yes |
| Case Sensitive | Yes |
| Acceptable Values | Any |
| Strict | No |

## Gradle Include Configurations (Advanced)

```
--detect.gradle.included.configurations
```

A comma-separated list of Gradle configurations to include.

As Detect examines the Gradle project for dependencies, if this property is set, Detect will include only those Gradle configurations specified via this property that are not excluded. Leaving this unset implies 'include all'. Exclusion rules always win. This property accepts filename globbing-style wildcards. For more information, refer to the [Property wildcard support page.](https://documentation%2Eblackduck%2Ecom/bundle/detect/page/configuring/propertywildcards%2Ehtml)

| Details |  |
| --- | --- |
| Added | 3.0.0 |
| Type | String List |
| Default Value |  |
| Comma Separated | Yes |
| Case Sensitive | Yes |
| Acceptable Values | Any |
| Strict | No |

## Gradle Include Project Paths (Advanced)

```
--detect.gradle.included.project.paths
```

A comma-separated list of Gradle subproject paths to include.

As Detect examines the Gradle project for dependencies, if this property is set, Detect will include only those subprojects whose path matches this property. Gradle project paths usually take the form ':parent:child' and are unique. Leaving this unset implies 'include all'. Exclusion rules always win. This property accepts filename globbing-style wildcards. For more information, refer to the [Property wildcard support page.](https://documentation%2Eblackduck%2Ecom/bundle/detect/page/configuring/propertywildcards%2Ehtml)

| Details |  |
| --- | --- |
| Added | 7.12.0 |
| Type | String List |
| Default Value |  |
| Comma Separated | Yes |
| Case Sensitive | Yes |
| Acceptable Values | Any |
| Strict | No |

## Gradle Include Projects (Advanced)

```
--detect.gradle.included.projects
```

A comma-separated list of Gradle subprojects to include.

As Detect examines the Gradle project for dependencies, if this property is set, Detect will include only those subprojects specified via this property that are not excluded. Leaving this unset implies 'include all'. Exclusion rules always win. This property accepts filename globbing-style wildcards. For more information, refer to the [Property wildcard support page.](https://documentation%2Eblackduck%2Ecom/bundle/detect/page/configuring/propertywildcards%2Ehtml)

| Details |  |
| --- | --- |
| Added | 3.0.0 |
| Type | String List |
| Default Value |  |
| Comma Separated | Yes |
| Case Sensitive | Yes |
| Acceptable Values | Any |
| Strict | No |

## Gradle Root Only Enabled (Advanced)

```
--detect.gradle.root.only=false
```

If set to true, Gradle Native Inspector will only evaluate root project dependencies.

This property overrides other inclusion/exclusion rules and therefore should not be combined with detect.gradle.excluded.projects, detect.gradle.excluded.project.paths, detect.gradle.included.projects, or detect.gradle.included.project.paths.

| Details |  |
| --- | --- |
| Added | 10.1.0 |
| Type | Boolean |
| Default Value | false |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |
