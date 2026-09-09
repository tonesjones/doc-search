---
title: "Software Risk Manager Support Information"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/software-risk-manager-support-information.html"
content_id: "NLurIe3o0cNqZbMbzBK5MQ"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:02:49.280380+00:00"
content_hash: "ae392a8194d6228c5b037433a504c7b6b37999b6be914f14b98a9e2e785c11ca"
---

# Software Risk Manager Support Information

Software Risk Manager supports the following browsers and configurations.

## Supported Platforms

Software Risk Manager APIs are compatible with any operating system and hardware that
can connect to the SRM server or APIs via HTTPS.

## Browser Support

The SRM web UI can be accessed using any of the supported browsers shown in the
following table:

Table 1.

| Browser | Versions | Provider |
| --- | --- | --- |
| Firefox | Latest | Versions supported by Mozilla |
| Google Chrome | Latest | Versions supported by Google |
| Microsoft Edge | Latest | Versions supported by Windows 10 |
| Safari | Latest | Versions supported by Apple |

## Scan Farm Supported File Types and Tests

Note: Supported file types and tests apply to integrated Coverity and Black Duck
only.

### SAST Language Support

SRM supports the following SAST languages:

Table 2.

| Language | Language Versions | Code Upload (UI) | Git Integration | CI via Black Duck Bridge CLI (CLI) |
| --- | --- | --- | --- | --- |
| Salesforce Apex |  | Supported | Supported | Supported |
| C/C++ | C++23 C++20  C++98  C++03  C++11  C++14  C++17  C89  C99  C11 | Not Supported | Not Supported | Supported |
| C# | Up to C# 12 | Supported | Supported | Supported |
| Dart | Version Agnostic | Supported | Supported | Supported |
| Go | Go 1.20–1.21 | Not Supported | Not Supported | Supported |
| Java | Up to Java 21 | Supported | Supported | Supported |
| JavaScript | ECMAScript 2023 | Supported | Supported | Supported |
| Kotlin | 1.8.0-1.8.22, 1.9.0 | Not Supported | Not Supported | Supported |
| Objective-C/C++ |  | Not Supported | Not Supported | Supported |
| PHP | Version Agnostic | Supported | Supported | Supported |
| Python | Python 3.x–3.11 | Supported | Supported | Supported |
| Ruby | Matz's Reference Impl. (MRI) 1.9.2–3.2 and equivalents (via Breakman pro bundles into analysis kit) | Supported | Supported | Supported |
| Swift | Version Agnostic | Supported | Supported | Supported |
| TypeScript | TypeScript 1.0–5.2 | Supported | Supported | Supported |
| Visual Basic | Up to Visual Basic 16 | Not Supported | Not Supported | Supported |

### Infrastructure as Code: Static Testing

SRM supports the following Infrastructure as Code Static Testing.

Table 3.

| Language | What is supported | Code Upload (UI) | Git Integration | CI via Black Duck Bridge CLI (CLI) |
| --- | --- | --- | --- | --- |
| IaC | **Platforms:** AWS CloudFormation, Kubernetes, Terraform. **Formats:** HCL (Terraform), JSON, XML, YAML | Supported | Supported | Supported |

## SCA Language and Package Manager Support

SRM supports the following SCA languages and package manager support:

Table 4.

| Package Manager | Language | Test Mode | Supported | Entry Point | Supported Detectors, Requirements | Accuracy |
| --- | --- | --- | --- | --- | --- | --- |
| Apache Ivy | Various | Code upload or SCM integration | Not Supported |  |  |  |
| Black Duck Bridge CLI (CI/CLI) | Supported | Ivy Build Parse | Ivy Build Parse  - Files: ivy.zml, build.zml | Low |
| BitBake | Various | Code upload or SCM integration | Not Supported |  |  |  |
| Black Duck Bridge CLI (CI/CLI) | Supported | Bitbake CLI |  |  |
| Cargo | Rust | Code upload or SCM integration | Not Supported |  |  |  |
| Black Duck Bridge CLI (CI/CLI) | Supported | Cargo Lock | Cargo Lock  - Files: Cartfile, Cartfile.resolved | High |
| Carthage | Various | Code upload or SCM integration | Not Supported |  |  |  |
| Black Duck Bridge CLI (CI/CLI) | Supported | Carthage Lock | Carthage Lock  - Files: Cartfile, Cartfile.resolved | High |
| CocoaPods | Objective-C | Code upload or SCM integration | Not Supported |  |  |  |
| Black Duck Bridge CLI (CI/CLI) | Supported | Pod Lock | Pod Lock  - Files: Podfile.lock | High |
| Conan | C/C++ | Code upload or SCM integration | Not Supported |  |  |  |
| Black Duck Bridge CLI (CI/CLI) | Supported | Conan Lock | Conan Lock  - Files: conan.lock | High |
| Conan CLI  - Files: conanfile.txt or conanfile.py - Executables: conan | High |
| Conan CLI | Conan CLI  - Files: conanfile.txt or conanfile.py - Executables: conan | High |
| Conda | Python | Code upload or SCM integration | Not Supported |  |  |  |
| Black Duck Bridge CLI (CI/CLI) | Supported | Conda CLI | Conda CLI  - Files: environment.yml - Executables: conda | High |
| CPAN | Perl | Code upload or SCM integration | Not Supported |  |  |  |
| Black Duck Bridge CLI (CI/CLI) | Supported | Cpan CLI | Cpan CLI  - File: Makefile.PL - Executables: cpan | High |
| CRAN | R | Code upload or SCM integration | Not Supported |  |  |  |
| Black Duck Bridge CLI (CI/CLI) | Supported | Packrat Lock | Packrat Lock  - File: packrat.lock | High |
| Dart | Dart | Code upload or SCM integration | Not Supported |  |  |  |
| Black Duck Bridge CLI (CI/CLI) | Supported | Dart CLI | Dart CLI  - Files: pubspec.yaml, pubspec.lock - Executables: dart, flutter | High |
| Dart PubSpec Lock  - Files: pubspec.yaml,pubspec.lock | High |
| Dart PubSpec Lock | Dart PubSpec Lock  - Files: pubspec.yaml,pubspec.lock | High |
| Go Dep | Golang (Go) | Code upload or SCM integration | Not Supported |  |  |  |
| Black Duck Bridge CLI (CI/CLI) | Supported | GoDep Lock | GoDep Lock  - File: Gopkg.lock | High |
| Go Gradle | Golang (Go) | Code upload or SCM integration | Not Supported |  |  |  |
| Black Duck Bridge CLI (CI/CLI) | Supported | GoGradle Lock | GoGradle Lock  - File: gogradle.lock | High |
| Go Modules | Golang (Go) | Code upload or SCM integration | Not Supported |  |  |  |
| Black Duck Bridge CLI (CI/CLI) | Supported | GoMod CLI | GoMod CLI  - Files: go.mod - Executables: go | High |
| Go Vendor | Golang (Go) | Code upload or SCM integration | Not Supported |  |  |  |
| Black Duck Bridge CLI (CI/CLI) | Supported | Go Vendor | Go Vendor  - Files: vendor/vendor.json | High |
| GoVndr CLI | GoVndr CLI  - Files: vendor.conf | High |
| Gradle | Various | Code upload or SCM integration | Supported | Gradle Project Inspector | Gradle Project Inspector  - Files: build.gradle | Low |
| Black Duck Bridge CLI (CI/CLI) | Supported | Gradle Native Inspector | Gradle Native Inspector  - Files: build.gradle or build.gradle.kts - Executables: gradlew or gradle | High |
| Gradle Project Inspector  - Files: build.gradle | Low |
| Hex | Erlang | Code upload or SCM integration | Not Supported |  |  |  |
| Black Duck Bridge CLI (CI/CLI) | Supported | Rebar CLI | Rebar CLI  - Files: rebar.config - Executables: rebar3 | High |
| Lerna | Node.js | Code upload or SCM integration | Not Supported |  |  |  |
| Black Duck Bridge CLI (CI/CLI) | Supported | Lerna CLI | Lerna CLI  - Files: lema.json, package.json - Executables: Lerna, and one of the following:   - packagelock.json   - npmshrinkwrap.json   - yarn.lock | High |
| Maven | Various | Code upload or SCM integration | Supported | Maven Project Inspector | Maven Project Inspector  - Files: pom.xml | Low |
| Black Duck Bridge CLI (CI/CLI) | Supported | Maven CLI | Maven CLI  - Files: pom.xml - Executables: mvnw or mvn | High |
| Maven Project Inspector  - Files: pom.xml | Low |
| Maven Wrapper CLI | Maven Wrapper CLI  - Files: pom.groovy - Executables: mvnw or mvn | High |
| Maven Project Inspector  - Files: pom.xml | Low |
| npm | Node.js | Code upload or SCM integration | Supported | NPM Package Lock | NPM Package Lock  - Files: packagelock.json. For better results, include a   package.json also. | High |
| NPM Package Json Parse | NPM Package Json Parse  - Files: package.json | Low |
| Black Duck Bridge CLI (CI/CLI) | Supported | NPM Shrinkwrap | NPM Shrinkwrap  - Files: npm-shrinkwrap.json. For better results, include   a package.json also. | High |
| NPM Package Lock  - Files: packagelock.json. For better results, include   package.json also. | High |
| NPM CLI  - Files node_modules, package.json - Executables: npm | High |
| NPM Package Json Parse  - Files: packagelock.json | High |
| NPM Package Lock | NPM Package Lock  - Files: packagelock.json. For better results, include a   package.json also. | High |
| NPM CLI  - Files: node_modules, package.json - Executables: npm | High |
| NPM Package Json Parse  - Files: package.json | Low |
| NPM CLI | NPM CLI  - Files: node_modules, package.json - Executables: npm | High |
| NPM Package Json Parse  - Files: package.json | Low |
| NPM Package Json Parse | NPM Package Json Parse  - Files: package.json | Low |
| NuGet | C# | All | Supported | NuGet Solution Native Inspector | NuGet Solution Native Inspector  - Files: A solution file with a .sln extension | High |
| NuGet Project Inspector  - Files: A project file with the .csproj or .sln   extension | Low |
| NuGet Project Native Inspector | NuGet Project Native Inspector  - Files: A project file with the csproj, .fsproj, .vbproj,   .asaproj, .dcproj, .shproj, .ccproj, .sfproj, .njsproj,   .vcxproj, .vcproj, .xproj, .pyproj, .hiveproj, .pigproj,   .jsproj, .usqlproj, .deployproj, .msbuildproj, .sqlproj,   .dbproj, or .rproj extension | High |
| NuGet Project Inspector  - Files: A project file with the .csproj or .sln   extension | Low |
| Packagist | PHP | Code upload or SCM integration | Not Supported |  |  |  |
| Black Duck Bridge CLI (CI/CLI) | Supported | Composer Lock | Composer Lock  - Files: composer.lock, composer.json | High |
| PEAR | PHP | Code upload or SCM integration | Not Supported |  |  |  |
| Black Duck Bridge CLI (CI/CLI) | Supported | Pear CLI | Pear CLI  - Files: package.xml - Executables: pear | High |
| pip | Python | Code upload or SCM integration | Supported | Pipfile Lock | Pipfile Lock  - Files: Pipfile or Pipfile.lock | High |
| Black Duck Bridge CLI (CI/CLI) | Supported | Pipenv Lock | Pipfile Lock  - Files: Pipfile or Pipfile.lock - Executables: python or python3, and pipenv | High |
| PIP Native Inspector  - Files: setup.py, or one or more requirements.txt - Executables: python and pip, or python3 and pip3 | High |
| Pipfile Lock  - Files: Pipfile, Pipfile.lock | High |
| Pip Native Inspector | PIP Native Inspector  - Files: setup.py, or one or more requirements.txt - Executables: python and pip, or python3 and pip3 | High |
| Pipfile Lock  - Files Pipfile, Pipfile.lock | High |
| Pipfile Lock | Pipfile Lock  - Files: Pipfile, Pipfile.lock | High |
| pnpm | Node.js | All | Supported | Pnpm Lock | Pnpm Lock  - Files pnpmlock.yaml, package.json | High |
| Poetry | Python | All | Supported | Poetry Lock | Poetry Lock  - Files Poetrylock, pyproject.toml | High |
| RubyGems | Ruby | Code upload or SCM integration | Not Supported |  |  |  |
| Black Duck Bridge CLI (CI/CLI) | Supported | Gemfile Lock | Gemfile Lock  - Files: Gemfile.lock | High |
| Gemspec Parse  - Files: A gemspec file with the .gemspec extension | Low |
| Gemspec Parse | Gemspec Parse  - Files: A gemspec file with a .gemspec extension | Low |
| SBT | Scala | Code upload or SCM integration | Not Supported |  |  |  |
| Black Duck Bridge CLI (CI/CLI) | Supported | Sbt Native Inspector | Sbt Native Inspector  - Files: build.sbt - Plugins: Dependency Graph | High |
| Swift | Swift | Code upload or SCM integration | Supported | Swift Lock | Swift Lock  - Files: Package.swift, Package.resolved | High |
| Black Duck Bridge CLI (CI/CLI) | Supported | Swift Lock | Swift Lock  - Files: Package.swift, Package.resolved | High |
| Swift CLI  - Files: Package.swift - Executables: swift | High |
| Swift CLI | Swift CLI  - Files: Package.swift - Executables: swift | High |
| Xcode | Swift | Code upload or SCM integration | Not Supported |  |  |  |
| Black Duck Bridge CLI (CI/CLI) | Supported | Xcode Workspace Lock | Xcode Workspace Lock  - Directories: *.xcworkspace | High |
| Xcode Project Lock  - Directories: *.xcodeproj - Files: Package.resolved |  |
| Xcode Project Lock | Xcode Project Lock  - Directories: *.xcodeproj - Files: Package.resolved |  |
| Yarn | Node.js | All | Supported | Yarn Lock | Yarn Lock  - Files: yarn.lock, package.json | High |

## SCA Package Manager Versions

SRM supports the following SCA package manager versions:

Note: Package manager version
requirements are only applicable to tests created with Black Duck Bridge CLI (when testing relies on/requires access to
executables). "N/A" in the table below indicates buildless capture is used to
test projects that depend on the package manager.

Table 5.

| Package Manager | Latest Supported Version |
| --- | --- |
| Apache Ivy | N/A |
| Bazel | 4.2.0 |
| BitBake | 2.6.0 (Yocto 4.3.2) |
| Cargo | N/A |
| Carthage | N/A |
| CocoaPods | N/A |
| Conan | 2.0.14 |
| Conda | 4.10.3 |
| CPAN | Cpan Script 1.678 CPAN.pm 2.36  Cpanm 1.7047 |
| CRAN | N/A |
| Dart | Dart 3.1.2 Flutter 3.13.4 |
| Go | 1.20.4 |
| Go Dep | N/A |
| Gogradle | N/A |
| Go Modules | 1.20.4 |
| Go Vendor | N/A |
| Gradle | 8.2.1 |
| Hex | Rebar 3.20.0 |
| Lerna | 6.6.2 |
| Maven | 3.8.1 |
| npm | Node 20.5.1 npm 9.8.1 |
| NuGet | nuget 6.2 .NET runtime is not required with 7.13.0 |
| Packagist | N/A |
| PEAR | 1.10.12 |
| pip | 23.1.2 |
| pnpm | N/A |
| Poetry | N/A |
| RubyGems | 2.0.0 |
| SBT | 1.5.0 |
| Swift | 5.6.1 |
| Xcode | N/A |
| Yarn | 4.1.0 |
