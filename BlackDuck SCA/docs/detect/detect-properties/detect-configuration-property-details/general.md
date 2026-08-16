---
title: "general"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/general.html"
content_id: "RSz4mVge0PjEygxM2F_LPA"
version: "11.5.1"
section: "Detect Properties"
scraped_at: "2026-08-08T23:45:21.056563+00:00"
---

# general

## Component Location Analysis Enabled

```
--detect.component.location.analysis.enabled=false
```

If set to true, Detect will save an output file named 'components-with-locations.json' in the Scan subdirectory detailing where in the project's source code OSS components are declared.

All components will be included when using Detect in offline mode. Only policy violating components will be included for Rapid and Stateless Scan modes.

| Details |  |
| --- | --- |
| Added | 8.11.0 |
| Type | Boolean |
| Default Value | false |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Component Location Analysis Status

```
--detect.component.location.analysis.status=false
```

If set to true, Detect status and exit code will be affected by the status of the Component Location Analysis run.

| Details |  |
| --- | --- |
| Added | 9.7.0 |
| Type | Boolean |
| Default Value | false |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Correlated Scanning Enabled

```
--detect.blackduck.correlated.scanning.enabled=false
```

When enabled, Detect activates the Black Duck SCA correlated scanning capability to enhance match accuracy.

The correlated scanning capability must be present and enabled in your Black Duck SCA server before you enable the correlated scanning feature in Detect.

| Details |  |
| --- | --- |
| Added | 10.0.0 |
| Type | Boolean |
| Default Value | false |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Detect Scan Mode

```
--detect.target.type=SOURCE,IMAGE
```

Informs detect of what is being scanned which allows improved user experience when scanning different types of targets.

Changes the behaviour of detect to better suite what is being scanned. For example, when IMAGE is selected and the DOCKER tool applies and has not been excluded, detect will not pick a source directory, will automatically disable the DETECTOR tool and run BINARY/SIGNATURE SCAN on the provided image.

| Details |  |
| --- | --- |
| Added | 7.0.0 |
| Type | DetectTargetType |
| Default Value | SOURCE |
| Comma Separated | No |
| Case Sensitive | Yes |
| Acceptable Values | SOURCE, IMAGE |
| Strict | Yes |

## Follow Symbolic Links

```
--detect.follow.symbolic.links=true
```

If set to true, Detect will follow symbolic links when searching for detectors, when searching for files that select detectors (such as Bitbake and Sbt) need, when searching for directories to exclude from signature scan, and when searching for binary scan targets. Symbolic links are not supported for Impact Analysis.

| Details |  |
| --- | --- |
| Added | 7.0.0 |
| Type | Boolean |
| Default Value | true |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Wait For Results

```
--detect.wait.for.results=false
```

If set to true, Detect will wait for Black Duck SCA products until results are available or the detect.timeout is exceeded.

Note that scan failures will exit with FAILURE_SCAN (6) and time out will exit with FAILURE_TIMEOUT (2) code.

| Details |  |
| --- | --- |
| Added | 5.5.0 |
| Type | Boolean |
| Default Value | false |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Detect Ignore Connection Failures (Advanced)

```
--detect.ignore.connection.failures=false
```

If true, Detect will ignore any products (eg. Black Duck SCA) that it cannot connect to.

If true, when Detect attempts to boot a product (eg. Black Duck SCA) it will also check if it can communicate with it - if it cannot, it will not run the product.

| Details |  |
| --- | --- |
| Added | 5.3.0 |
| Type | Boolean |
| Default Value | false |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Detect Parallel Processors (Advanced)

```
--detect.parallel.processors=1
```

The number of threads to run processes in parallel, defaults to 1, but if you specify less than or equal to 0, the number of processors on the machine will be used.

| Details |  |
| --- | --- |
| Added | 6.0.0 |
| Type | Integer |
| Default Value | 1 |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Force Success (Advanced)

```
--detect.force.success=false
```

If true, Detect will always exit with code 0.

| Details |  |
| --- | --- |
| Added | 3.0.0 |
| Type | Boolean |
| Default Value | false |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Force Success On Skip (Advanced)

```
--detect.force.success.on.skip=false
```

If true, Detect will always exit with code 0 when a scan of any type is skipped. Typically this happens when the Black Duck SCA minimum scan interval timer has not been met.

| Details |  |
| --- | --- |
| Added | 7.12.1 |
| Type | Boolean |
| Default Value | false |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |
