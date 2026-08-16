---
title: "detector"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/detector.html"
content_id: "L~TiKC4qX_r~kGCabHRS7Q"
version: "11.5.1"
section: "Detect Properties"
scraped_at: "2026-08-08T23:45:20.323598+00:00"
---

# detector

## Required Detect Types

```
--detect.required.detector.types=BITBAKE,CARGO,CARTHAGE,COCOAPODS,CONAN,CONDA,CPAN,CRAN,DART,GIT,GO_MOD,GO_DEP,GO_VNDR,GO_VENDOR,GO_GRADLE,GRADLE,HEX,IVY,LERNA,MAVEN,NPM,NUGET,PACKAGIST,PEAR,PIP,PNPM,POETRY,RUBYGEMS,SBT,SETUPTOOLS,SWIFT,YARN,CLANG,XCODE,OPAM,UV,RUSH
```

The set of required detectors.

If you want one or more detectors to be required (must be found to apply), use this property to specify the set of required detectors. If this property is set, and one (or more) of the given detectors is not found to apply, Detect will fail.

| Details |  |
| --- | --- |
| Added | 4.3.0 |
| Type | DetectorType List |
| Default Value |  |
| Comma Separated | Yes |
| Case Sensitive | Yes |
| Acceptable Values | BITBAKE, CARGO, CARTHAGE, COCOAPODS, CONAN, CONDA, CPAN, CRAN, DART, GIT, GO_MOD, GO_DEP, GO_VNDR, GO_VENDOR, GO_GRADLE, GRADLE, HEX, IVY, LERNA, MAVEN, NPM, NUGET, PACKAGIST, PEAR, PIP, PNPM, POETRY, RUBYGEMS, SBT, SETUPTOOLS, SWIFT, YARN, CLANG, XCODE, OPAM, UV, RUSH |
| Strict | Yes |
| Example | `NPM` |

## Detector Accuracy Requirements (Advanced)

```
--detect.accuracy.required=ALL,NONE,BITBAKE,CARGO,CARTHAGE,COCOAPODS,CONAN,CONDA,CPAN,CRAN,DART,GIT,GO_MOD,GO_DEP,GO_VNDR,GO_VENDOR,GO_GRADLE,GRADLE,HEX,IVY,LERNA,MAVEN,NPM,NUGET,PACKAGIST,PEAR,PIP,PNPM,POETRY,RUBYGEMS,SBT,SETUPTOOLS,SWIFT,YARN,CLANG,XCODE,OPAM,UV,RUSH
```

Detector types from which HIGH accuracy results are required when a detector of that type applies.

The value of this property only affects detector types which apply to the source project. If a detector type applies, and is one of the accuracy-required detector types indicated by the value of this property, low accuracy results for that detector type are treated as a failure. For further information refer to [Detector search and accuracy.](https://documentation%2Eblackduck%2Ecom/bundle/detect/page/runningdetect/detectorcascade%2Ehtml)

| Details |  |
| --- | --- |
| Added | 7.13.0 |
| Type | DetectorType List |
| Default Value | ALL |
| Comma Separated | Yes |
| Case Sensitive | No |
| Acceptable Values | ALL, NONE, BITBAKE, CARGO, CARTHAGE, COCOAPODS, CONAN, CONDA, CPAN, CRAN, DART, GIT, GO_MOD, GO_DEP, GO_VNDR, GO_VENDOR, GO_GRADLE, GRADLE, HEX, IVY, LERNA, MAVEN, NPM, NUGET, PACKAGIST, PEAR, PIP, PNPM, POETRY, RUBYGEMS, SBT, SETUPTOOLS, SWIFT, YARN, CLANG, XCODE, OPAM, UV, RUSH |
| Strict | Yes |
| Example | `ALL,NONE` |

## Detectors Excluded (Advanced)

```
--detect.excluded.detectors
```

By default, all Detectors will be included. If you want to exclude specific Detectors, specify the ones to exclude here. Exclusion rules take precedence.

This property is similar to --detect.excluded.detector.types; but, allows for more granular control. Values are case-insensitive and spaces can be omitted.

| Details |  |
| --- | --- |
| Added | 11.0.0 |
| Type | String List |
| Default Value |  |
| Comma Separated | Yes |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |
| Example | `PIPNativeInspector,PIPRequirementsFileParse` |

## Detector Types Excluded (Advanced)

```
--detect.excluded.detector.types=NONE,BITBAKE,CARGO,CARTHAGE,COCOAPODS,CONAN,CONDA,CPAN,CRAN,DART,GIT,GO_MOD,GO_DEP,GO_VNDR,GO_VENDOR,GO_GRADLE,GRADLE,HEX,IVY,LERNA,MAVEN,NPM,NUGET,PACKAGIST,PEAR,PIP,PNPM,POETRY,RUBYGEMS,SBT,SETUPTOOLS,SWIFT,YARN,CLANG,XCODE,OPAM,UV,RUSH
```

By default, all Detector types will be included. To exclude specific Detector types, specify them via this parameter. Exclusion rules take precedence.

To prevent Detect from executing one or more Detector types on your project, specify the Detector types using this property. For more granular control, please see --detect.excluded.detectors.

| Details |  |
| --- | --- |
| Added | 3.0.0 |
| Type | DetectorType List |
| Default Value | NONE |
| Comma Separated | Yes |
| Case Sensitive | No |
| Acceptable Values | NONE, BITBAKE, CARGO, CARTHAGE, COCOAPODS, CONAN, CONDA, CPAN, CRAN, DART, GIT, GO_MOD, GO_DEP, GO_VNDR, GO_VENDOR, GO_GRADLE, GRADLE, HEX, IVY, LERNA, MAVEN, NPM, NUGET, PACKAGIST, PEAR, PIP, PNPM, POETRY, RUBYGEMS, SBT, SETUPTOOLS, SWIFT, YARN, CLANG, XCODE, OPAM, UV, RUSH |
| Strict | Yes |
| Example | `NPM,LERNA` |

## Detector Types Included (Advanced)

```
--detect.included.detector.types=ALL,BITBAKE,CARGO,CARTHAGE,COCOAPODS,CONAN,CONDA,CPAN,CRAN,DART,GIT,GO_MOD,GO_DEP,GO_VNDR,GO_VENDOR,GO_GRADLE,GRADLE,HEX,IVY,LERNA,MAVEN,NPM,NUGET,PACKAGIST,PEAR,PIP,PNPM,POETRY,RUBYGEMS,SBT,SETUPTOOLS,SWIFT,YARN,CLANG,XCODE,OPAM,UV,RUSH
```

By default, all tools will be included. If you want to include only specific tools, specify the ones to include here. Exclusion rules always win.

If you want to limit Detect to a subset of its detectors, use this property to specify that subset.

| Details |  |
| --- | --- |
| Added | 3.0.0 |
| Type | DetectorType List |
| Default Value | ALL |
| Comma Separated | Yes |
| Case Sensitive | No |
| Acceptable Values | ALL, BITBAKE, CARGO, CARTHAGE, COCOAPODS, CONAN, CONDA, CPAN, CRAN, DART, GIT, GO_MOD, GO_DEP, GO_VNDR, GO_VENDOR, GO_GRADLE, GRADLE, HEX, IVY, LERNA, MAVEN, NPM, NUGET, PACKAGIST, PEAR, PIP, PNPM, POETRY, RUBYGEMS, SBT, SETUPTOOLS, SWIFT, YARN, CLANG, XCODE, OPAM, UV, RUSH |
| Strict | Yes |
| Example | `NPM` |
