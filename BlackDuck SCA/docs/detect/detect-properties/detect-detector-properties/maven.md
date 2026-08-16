---
title: "maven"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/maven.html"
content_id: "dhW7fWxJwgRvSjQSnb2XJw"
version: "11.5.1"
section: "Detect Properties"
scraped_at: "2026-08-08T23:45:38.770767+00:00"
---

# maven

## Dependency Scope Excluded

```
--detect.maven.excluded.scopes
```

A comma separated list of Maven scopes. Output will be limited to dependencies outside these scopes (overrides include).

If set, Detect will include only dependencies outside of the given Maven scope. This property accepts filename globbing-style wildcards. For more information, refer to the [Property wildcard support page.](https://documentation%2Eblackduck%2Ecom/bundle/detect/page/configuring/propertywildcards%2Ehtml)

| Details |  |
| --- | --- |
| Added | 6.0.0 |
| Type | String List |
| Default Value |  |
| Comma Separated | Yes |
| Case Sensitive | Yes |
| Acceptable Values | Any |
| Strict | No |

## Dependency Scope Included

```
--detect.maven.included.scopes
```

A comma separated list of Maven scopes. Output will be limited to dependencies within these scopes (overridden by exclude).

If set, Detect will include only dependencies of the given Maven scope. This property accepts filename globbing-style wildcards. This property accepts filename globbing-style wildcards. For more information, refer to the [Property wildcard support page.](https://documentation%2Eblackduck%2Ecom/bundle/detect/page/configuring/propertywildcards%2Ehtml)

| Details |  |
| --- | --- |
| Added | 6.0.0 |
| Type | String List |
| Default Value |  |
| Comma Separated | Yes |
| Case Sensitive | Yes |
| Acceptable Values | Any |
| Strict | No |

## Include Shaded Dependencies

```
--detect.maven.include.shaded.dependencies=false
```

If set to true, Detect will include shaded dependencies as part of BOM.

A shaded dependency is packaged inside the uber jar of the direct or transitive dependency referenced in the project. Detect will find the use of maven-shade-plugin from original POM file and based on that will derive information for these dependencies. This property will only be supported in build mode just like all other MAVEN properties.

| Details |  |
| --- | --- |
| Added | 9.5.0 |
| Type | Boolean |
| Default Value | false |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Maven Build Command

```
--detect.maven.build.command
```

Maven command line arguments to add to the mvn/mvnw command line.

By default, Detect runs the mvn (or mvnw) command with two arguments: dependency:tree and -T1. You can use this property to insert one or more additional mvn command line arguments (goals, etc.) before the dependency:tree argument. For example: suppose you are running in bash on Linux, and want to point maven to your settings file (maven_dev_settings.xml in your home directory) and assign the value 'other' to property 'reason'. You could do this with: --detect.maven.build.command='--settings \${HOME}/maven_dev_settings.xml --define reason=other'. Please note that Detect will omit any thread-specifying arguments in order to ensure the accuracy of the dependency tree.

| Details |  |
| --- | --- |
| Added | 3.0.0 |
| Type | Optional String |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Maven Executable

```
--detect.maven.path
```

The path to the Maven executable (mvn or mvnw).

If set, Detect will use the given Maven executable instead of searching for one.

| Details |  |
| --- | --- |
| Added | 3.0.0 |
| Type | Optional Path |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Maven Modules Excluded (Advanced)

```
--detect.maven.excluded.modules
```

A comma-separated list of Maven modules (subprojects) to exclude.

As Detect parses the mvn dependency:tree output for dependencies, Detect will skip any Maven modules specified via this property. This property accepts filename globbing-style wildcards. For more information, refer to the [Property wildcard support page.](https://documentation%2Eblackduck%2Ecom/bundle/detect/page/configuring/propertywildcards%2Ehtml)

| Details |  |
| --- | --- |
| Added | 3.0.0 |
| Type | String List |
| Default Value |  |
| Comma Separated | Yes |
| Case Sensitive | Yes |
| Acceptable Values | Any |
| Strict | No |

## Maven Modules Included (Advanced)

```
--detect.maven.included.modules
```

A comma-separated list of Maven modules (subprojects) to include.

As Detect parses the mvn dependency:tree output for dependencies, if this property is set, Detect will include only those Maven modules specified via this property that are not excluded. Leaving this unset implies 'include all'. Exclusion rules always win. This property accepts filename globbing-style wildcards. For more information, refer to the [Property wildcard support page.](https://documentation%2Eblackduck%2Ecom/bundle/detect/page/configuring/propertywildcards%2Ehtml)

| Details |  |
| --- | --- |
| Added | 3.0.0 |
| Type | String List |
| Default Value |  |
| Comma Separated | Yes |
| Case Sensitive | Yes |
| Acceptable Values | Any |
| Strict | No |
