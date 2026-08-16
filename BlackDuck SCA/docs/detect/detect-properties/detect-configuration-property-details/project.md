---
title: "project"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/project.html"
content_id: "EEtqCIB8vvhF~1uaB7ps3w"
version: "11.5.1"
section: "Detect Properties"
scraped_at: "2026-08-08T23:45:25.431001+00:00"
---

# project

## Deep License Analysis

```
--detect.project.deep.license=false
```

If set to true, enables Deep License Analysis for the project, including detailed license data and snippet analysis.

| Details |  |
| --- | --- |
| Added | 11.0.0 |
| Type | Boolean |
| Default Value | false |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Fail on Policy Names with Violations

```
--detect.policy.check.fail.on.names
```

A comma-separated list of policy names with a non-zero number of violations that will fail Detect.

If left unset, Detect will not fail due to violated policies of a certain name. This property does not change the behavior of detect.policy.check.fail.on.severities.

| Details |  |
| --- | --- |
| Added | 7.12.0 |
| Type | String List |
| Default Value |  |
| Comma Separated | Yes |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Fail on Policy Violation Severities

```
--detect.policy.check.fail.on.severities=ALL,NONE,BLOCKER,CRITICAL,MAJOR,MINOR,OK,TRIVIAL,UNSPECIFIED
```

A comma-separated list of policy violation severities that will fail Detect. If this is set to NONE, Detect will not fail due to policy violations. A value of ALL is equivalent to all of the other possible values except NONE.

| Details |  |
| --- | --- |
| Added | 3.0.0 |
| Type | PolicyRuleSeverityType List |
| Default Value | NONE |
| Comma Separated | Yes |
| Case Sensitive | No |
| Acceptable Values | ALL, NONE, BLOCKER, CRITICAL, MAJOR, MINOR, OK, TRIVIAL, UNSPECIFIED |
| Strict | Yes |

## Fail on Stateless Policy Violation Severities

```
--detect.stateless.policy.check.fail.on.severities=ALL,NONE,BLOCKER,CRITICAL,MAJOR,MINOR,OK,TRIVIAL,UNSPECIFIED
```

A comma-separated list of policy violation severities that will fail Detect. If this is set to NONE, Detect will not fail due to policy violations. A value of ALL is equivalent to all of the other possible values except NONE. This property works for both stateless and rapid scans.

| Details |  |
| --- | --- |
| Added | 10.6.0 |
| Type | PolicyRuleSeverityType List |
| Default Value | BLOCKER,CRITICAL |
| Comma Separated | Yes |
| Case Sensitive | No |
| Acceptable Values | ALL, NONE, BLOCKER, CRITICAL, MAJOR, MINOR, OK, TRIVIAL, UNSPECIFIED |
| Strict | Yes |

## Project Description

```
--detect.project.description
```

If project description is specified, your project will be created with this description. For updates, see detect.project.version.update.

| Details |  |
| --- | --- |
| Added | 4.0.0 |
| Type | Optional String |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Project Name

```
--detect.project.name
```

An override for the name to use for the Black Duck SCA project. If not supplied, Detect will attempt to use the tools to figure out a reasonable project name. If that fails, the final part of the directory path where the inspection is taking place will be used.

| Details |  |
| --- | --- |
| Added | 3.0.0 |
| Type | Optional String |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Project Tier

```
--detect.project.tier
```

If a Black Duck SCA project tier is specified, your project will be created with this tier. For updates, see detect.project.version.update.

| Details |  |
| --- | --- |
| Added | 3.1.0 |
| Type | Optional Integer |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Project Version License

```
--detect.project.version.license
```

If project version license is specified, your project version will be created with this license. For updates, see detect.project.version.update.

| Details |  |
| --- | --- |
| Added | 7.11.0 |
| Type | Optional String |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |
| Example | `Apache License 2.0` |

## Update Project Version

```
--detect.project.version.update=false
```

If set to true, Detect will update the Black Duck SCA project and project version according to configured project and project version properties. (By default, these properties are only set on created projects / project versions.)

When set to true, the following properties will be updated on the Project: description (detect.project.description), tier (detect.project.tier), and project level adjustments (detect.project.level.adjustments). The following properties will also be updated on the project version: notes (detect.project.version.notes), phase (detect.project.version.phase), distribution (detect.project.version.distribution), nickname (detect.project.version.nickname), license (detect.project.version.license).

| Details |  |
| --- | --- |
| Added | 4.0.0 |
| Type | Boolean |
| Default Value | false |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Version Name

```
--detect.project.version.name
```

An override for the version to use for the Black Duck SCA project. If not supplied, Detect will attempt to use the tools to figure out a reasonable version name. If that fails, the current date will be used.

| Details |  |
| --- | --- |
| Added | 3.0.0 |
| Type | Optional String |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Version Nickname

```
--detect.project.version.nickname
```

If a project version nickname is specified, your project version will be created with this nickname. For updates, see detect.project.version.update.

| Details |  |
| --- | --- |
| Added | 5.2.0 |
| Type | Optional String |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Version Notes

```
--detect.project.version.notes
```

If project version notes are specified, your project version will be created with these notes. For updates, see detect.project.version.update.

| Details |  |
| --- | --- |
| Added | 3.1.0 |
| Type | Optional String |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Version Phase

```
--detect.project.version.phase=ARCHIVED,DEPRECATED,DEVELOPMENT,PLANNING,PRERELEASE,RELEASED
```

If project version phase is specified, your project version will be created with this phase. For updates, see detect.project.version.update.

| Details |  |
| --- | --- |
| Added | 3.0.0 |
| Type | ProjectVersionPhaseType |
| Default Value | DEVELOPMENT |
| Comma Separated | No |
| Case Sensitive | Yes |
| Acceptable Values | ARCHIVED, DEPRECATED, DEVELOPMENT, PLANNING, PRERELEASE, RELEASED |
| Strict | Yes |
| Deprecated Values | ARCHIVED: With the Black Duck SCA 2026.1.0 release, the ARCHIVED option was deprecated and is no longer supported. To ensure compatibility with both current and upcoming releases, please update your configuration to use a supported project version phase.  ARCHIVED: This phase has been deprecated. |

## Allow Project Level Adjustments (Advanced)

```
--detect.project.level.adjustments=true
```

If set, created projects will be created with the value of this property. For updates, see detect.project.version.update.

Corresponds to the 'Always maintain component adjustments to all versions of this project' checkbox under 'Component Adjustments' on the Black Duck SCA Project settings page.

| Details |  |
| --- | --- |
| Added | 3.0.0 |
| Type | Boolean |
| Default Value | true |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Application ID (Advanced)

```
--detect.project.application.id
```

Sets the 'Application ID' project setting.

| Details |  |
| --- | --- |
| Added | 5.2.0 |
| Type | Optional String |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Clone Latest Project Version (Advanced)

```
--detect.clone.project.version.latest=false
```

If set to true, detect will attempt to use the latest project version as the clone for this project. The project must exist and have at least one version.

| Details |  |
| --- | --- |
| Added | 5.6.0 |
| Type | Boolean |
| Default Value | false |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Clone Project Categories (Advanced)

```
--detect.project.clone.categories=ALL,NONE,COMPONENT_DATA,CUSTOM_FIELD_DATA,DEEP_LICENSE,LICENSE_TERM_FULFILLMENT,VERSION_SETTINGS,VULN_DATA
```

The value of this property is used to set the 'Cloning' settings on created Black Duck SCA projects. If property detect.project.version.update is set to true, the value of this property is used to set the 'Cloning' settings on updated Black Duck SCA projects.

| Details |  |
| --- | --- |
| Added | 4.2.0 |
| Type | ProjectCloneCategoriesType List |
| Default Value | ALL |
| Comma Separated | Yes |
| Case Sensitive | No |
| Acceptable Values | ALL, NONE, COMPONENT_DATA, CUSTOM_FIELD_DATA, DEEP_LICENSE, LICENSE_TERM_FULFILLMENT, VERSION_SETTINGS, VULN_DATA |
| Strict | Yes |

## Clone Project Version Name (Advanced)

```
--detect.clone.project.version.name
```

The name of the project version to clone this project version from. Respects the given Clone Categories in detect.project.clone.categories or as set on the Black Duck SCA.

| Details |  |
| --- | --- |
| Added | 4.2.0 |
| Type | Optional String |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Custom Fields (Advanced)

```
--detect.custom.fields.project
```

A list of custom fields with a label and comma-separated value starting from index 0. For each index, provide one label and one value. For example, to set a custom field with label 'example' to 'one,two': `detect.custom.fields.project[0].label='example'` and `detect.custom.fields.project[0].value='one,two'`. To set another field, use index 1. Note that these will not show up in the detect configuration log.

When assigning a value that contains a comma to a single-value field such as a text field, append '[0]' to the end of the value property name. For example, to set the value of the first field you are setting ('detect.custom.fields.version[0]') to 'text1,text2', use 'detect.custom.fields.version[0].value[0]=text1,text2'.

| Details |  |
| --- | --- |
| Added | 5.6.0 |
| Type | Optional String |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Custom Fields (Advanced)

```
--detect.custom.fields.version
```

A list of custom fields with a label and comma-separated value starting from index 0. For each index, provide one label and one value. For example , to set a custom field with label 'example' to 'one,two': `detect.custom.fields.version[0].label='example'` and `detect.custom.fields.version[0].value='one,two'`. To set another field, use index 1. Note that these will not show up in the detect configuration log.

When assigning a value that contains a comma to a single-value field such as a text field, append '[0]' to the end of the value property name. For example, to set the value of the first field you are setting ('detect.custom.fields.version[0]') to 'text1,text2', use 'detect.custom.fields.version[0].value[0]=text1,text2'.

| Details |  |
| --- | --- |
| Added | 5.6.0 |
| Type | Optional String |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Parent Project Name (Advanced)

```
--detect.parent.project.name
```

When a parent project and version name are specified, the created detect project will be added as a component to the specified parent project version. The specified parent project and parent project version must exist on Black Duck SCA.

| Details |  |
| --- | --- |
| Added | 3.0.0 |
| Type | Optional String |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Parent Project Version Name (Advanced)

```
--detect.parent.project.version.name
```

When a parent project and version name are specified, the created detect project will be added as a component to the specified parent project version. The specified parent project and parent project version must exist on Black Duck SCA.

| Details |  |
| --- | --- |
| Added | 3.0.0 |
| Type | Optional String |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Project Group Name (Advanced)

```
--detect.project.group.name
```

Sets the 'Project Group' to assign the project to. Must match exactly to an existing project group on Black Duck SCA.

| Details |  |
| --- | --- |
| Added | 7.8.0 |
| Type | Optional String |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Project Settings JSON File (Advanced)

```
--detect.project.settings
```

Path to a JSON file containing project settings. The file should contain a JSON object with detect.project properties specified as key-value pairs.

detect.project properties provided on the command line take precedence over values specified in the JSON file.

| Details |  |
| --- | --- |
| Added | 11.0.0 |
| Type | Optional Path |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |
| Example | `/path/to/project-settings.json` |

## Project Tags (Advanced)

```
--detect.project.tags
```

A comma-separated list of tags to add to the project. This property is not supported when using Detect in offline mode.

| Details |  |
| --- | --- |
| Added | 5.6.0 |
| Type | String List |
| Default Value |  |
| Comma Separated | Yes |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |
| Example | `Critical` |

## Project User Groups (Advanced)

```
--detect.project.user.groups
```

A comma-separated list of names of user groups to add to the project.

| Details |  |
| --- | --- |
| Added | 5.4.0 |
| Type | String List |
| Default Value |  |
| Comma Separated | Yes |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |
| Example | `ProjectManagers,TechLeads` |

## Scan Name (Advanced)

```
--detect.code.location.name
```

An override for the base name Detect will use for the scan (codelocation) it creates. Detect appends a suffix to the base name that indicates the source ("scan" for the signature scanner, "gradle/bom" for the Gradle detector, etc.). If this property is set and multiple code locations are generated from the same source, Detect will also append an index to avoid name collisions. When this property is set, detect.project.codelocation.prefix and detect.project.codelocation.suffix are ignored.

| Details |  |
| --- | --- |
| Added | 4.0.0 |
| Type | Optional String |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Scan Name Prefix (Advanced)

```
--detect.project.codelocation.prefix
```

A prefix to the name of the scans created by Detect. Useful for running against the same projects on multiple machines.

| Details |  |
| --- | --- |
| Added | 3.0.0 |
| Type | Optional String |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Scan Name Suffix (Advanced)

```
--detect.project.codelocation.suffix
```

A suffix to the name of the scans created by Detect.

| Details |  |
| --- | --- |
| Added | 3.0.0 |
| Type | Optional String |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Version Distribution (Advanced)

```
--detect.project.version.distribution=EXTERNAL,INTERNAL,OPENSOURCE,SAAS
```

If project version distribution is specified, your project version will be created with this distribution. For updates, see detect.project.version.update.

| Details |  |
| --- | --- |
| Added | 3.0.0 |
| Type | ProjectVersionDistributionType |
| Default Value | EXTERNAL |
| Comma Separated | No |
| Case Sensitive | Yes |
| Acceptable Values | EXTERNAL, INTERNAL, OPENSOURCE, SAAS |
| Strict | Yes |
