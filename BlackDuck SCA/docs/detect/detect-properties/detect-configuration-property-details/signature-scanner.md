---
title: "signature-scanner"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/signature-scanner.html"
content_id: "sjIE1jjGD~QxFTu4oeg64g"
version: "11.5.1"
section: "Detect Properties"
scraped_at: "2026-08-08T23:45:29.465712+00:00"
---

# signature-scanner

## Detect Excluded Directories Search Depth

```
--detect.excluded.directories.search.depth=4
```

Enables you to adjust the depth to which Detect will search when creating signature scanner exclusion patterns.

| Details |  |
| --- | --- |
| Added | 7.0.0 |
| Type | Integer |
| Default Value | 4 |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Individual File Matching

```
--detect.blackduck.signature.scanner.individual.file.matching=NONE,SOURCE,BINARY,ALL
```

Users may set this property to indicate what types of files they want to match. Corresponding Signature Scanner CLI Argument: --individualFileMatching.

| Details |  |
| --- | --- |
| Added | 6.2.0 |
| Type | IndividualFileMatching |
| Default Value | NONE |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | NONE, SOURCE, BINARY, ALL |
| Strict | Yes |

## Reduced Persistence

```
--detect.blackduck.signature.scanner.reduced.persistence=DEFAULT,RETAIN_UNMATCHED,DISCARD_UNMATCHED
```

Use this value to control how unmatched files from signature scans are stored. For a full explanation, refer to [about reduced persistence signature scanning.](https://documentation%2Eblackduck%2Ecom/bundle/bd%2Dhub/page/ComponentDiscovery/about%5Freduced%5Fpersistence%5Fsignature%5Fscanning%2Ehtml)

| Details |  |
| --- | --- |
| Added | 8.3.0 |
| Type | ReducedPersistence |
| Default Value | DEFAULT |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | DEFAULT, RETAIN_UNMATCHED, DISCARD_UNMATCHED |
| Strict | Yes |

## Signature Scanner Arguments

```
--detect.blackduck.signature.scanner.arguments
```

A space-separated list of additional arguments to use when running the Black Duck SCA signature scanner. Key-value pairs specified as arguments will replace the same entries specifed elswhere. Available signature scanner properties can be determined by specifying '--help' when executing the signature scanner jar file from the command line.

Example usage: Running in bash on Linux and you want signature scanner to read a list of directories to exclude from the scan (using the signature scanner '--exclude-from' option). Configure signature scanner to read excluded directories from a file named excludes.txt in the current working directory with: --detect.blackduck.signature.scanner.arguments='--exclude-from ./excludes.txt'

| Details |  |
| --- | --- |
| Added | 4.2.0 |
| Type | Optional String |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |
| Example | `--exclude-from ./excludes.txt` |

## Signature Scanner Copyright Search

```
--detect.blackduck.signature.scanner.copyright.search=false
```

When set to true, user will be able to scan and discover copyright names in Black Duck SCA. Corresponding Signature Scanner CLI Argument: --copyright-search.

| Details |  |
| --- | --- |
| Added | 6.4.0 |
| Type | Boolean |
| Default Value | false |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Signature Scanner CSV Archive Output

```
--detect.blackduck.signature.scanner.csv.archive=false
```

When set to true Signature Scanner output will be in CSV format. Corresponding Signature Scanner CLI Argument: --outputFormat csv for offline mode, --upload-csv for online mode.

| Details |  |
| --- | --- |
| Added | 10.2.0 |
| Type | Boolean |
| Default Value | false |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Signature Scanner Dry Run

```
--detect.blackduck.signature.scanner.dry.run=false
```

If set to true, the signature scanner results are not uploaded to Black Duck SCA, and the scanner results are written to disk via the Signature Scanner CLI argument: --dryRunWriteDir.

| Details |  |
| --- | --- |
| Added | 4.2.0 |
| Type | Boolean |
| Default Value | false |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Signature Scanner License Search

```
--detect.blackduck.signature.scanner.license.search=false
```

When set to true, user will be able to scan and discover license names in Black Duck SCA. Corresponding Signature Scanner CLI Argument: --license-search.

| Details |  |
| --- | --- |
| Added | 6.2.0 |
| Type | Boolean |
| Default Value | false |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Signature Scanner Local Path

```
--detect.blackduck.signature.scanner.local.path
```

To use a local signature scanner, specify the path where the signature scanner was unzipped. This will likely look similar to 'scan.cli-x.y.z' and includes the 'bin, icon, jre, and lib' directories of the expanded scan.cli.

| Details |  |
| --- | --- |
| Added | 4.2.0 |
| Type | Optional Path |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Signature Scanner Target Paths

```
--detect.blackduck.signature.scanner.paths
```

If this property is not set, the signature scanner target path is the source path (see property detect.source.path). If this property is set, the paths provided in this property's value will be signature scanned instead (the signature scanner will be executed once for each provided path).

| Details |  |
| --- | --- |
| Added | 4.2.0 |
| Type | Path List |
| Default Value |  |
| Comma Separated | Yes |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Snippet Matching

```
--detect.blackduck.signature.scanner.snippet.matching=NONE,SNIPPET_MATCHING,SNIPPET_MATCHING_ONLY
```

Use this value to enable the various snippet scanning modes. For a full explanation, refer to [Running a component scan using the Signature Scanner command line.](https://documentation%2Eblackduck%2Ecom/bundle/bd%2Dhub/page/ComponentDiscovery/CommandLine%2Ehtml) Corresponding Signature Scanner CLI Arguments: --snippet-matching, --snippet-matching-only.

| Details |  |
| --- | --- |
| Added | 5.5.0 |
| Type | SnippetMatching |
| Default Value | NONE |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | NONE, SNIPPET_MATCHING, SNIPPET_MATCHING_ONLY |
| Strict | Yes |

## Upload source mode

```
--detect.blackduck.signature.scanner.upload.source.mode=false
```

If set to true, the signature scanner will, if supported by your Black Duck SCA version, upload source code to Black Duck SCA. Corresponding Signature Scanner CLI Argument: --upload-source.

| Details |  |
| --- | --- |
| Added | 5.4.0 |
| Type | Boolean |
| Default Value | false |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Signature Scanner Memory (Advanced)

```
--detect.blackduck.signature.scanner.memory=4096
```

The memory for the scanner to use.

| Details |  |
| --- | --- |
| Added | 4.2.0 |
| Type | Integer |
| Default Value | 4096 |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |
