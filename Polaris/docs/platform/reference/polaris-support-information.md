---
title: "Polaris Support Information"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/polaris-support-information.html"
content_id: "9o4eV3hDO0h1ZTd7qZMDsA"
product_key: "polaris-platform-latest"
section: "Reference"
scraped_at: "2026-08-12T19:57:55.140099+00:00"
content_hash: "02a27c3e96b5423218de494422f8a7c25083c0f84c44261dfb0cfab47cce7519"
---

# Polaris Support Information

## Supported platforms

Polaris APIs are compatible with any operating system and hardware that can connect to the Polaris server or APIs via HTTPS.

## Browser support

The Polaris web UI can be accessed using:

Table 1. Browser support

| Browser | Versions | Provider | Notes |
| --- | --- | --- | --- |
| Firefox | Latest and latest - 1 | Versions supported by Mozilla |  |
| Google Chrome | Latest and latest - 1 | Versions supported by Google |  |
| Microsoft Edge | Latest and latest - 1 | Versions supported by Windows 10 |  |
| Safari | Latest and latest - 1 | Versions supported by Apple | "Prevent cross-site tracking" must be disabled. |

Note: Internet Explorer is not supported.

## Supported tools

Table 2. Supported tools

| Tool | Supported version(s) |
| --- | --- |
| Coverity (with Rapid Scan Static) | - 2026.6.0 (2026.6.1) **Latest, automatic update** - 2026.6.0 (2026.6.0) **Recommended** - 2026.3.0 (2026.3.0) - 2025.12.0 (2026.3.0) - 2025.9.1 (2026.1.0) **Deprecated** |
| Bridge CLI Bundle | 4.5.0 |
| Bridge CLI Thin Client | 3.0.18 |
| Black Duck® Detect | 11.4.2 |

Note: The version of Coverity used for SAST tests on Polaris can be customized. Each supported version of Coverity is paired with a specific version of Rapid Scan Static (Sigma). When you select a specific Coverity version — including the recommended version — both versions are locked. When you select the latest Coverity version, the latest version of Sigma is used automatically. For more information, see [Manage SAST tool versions](../how-to/manage-sast-tool-versions.md).

## Issue tracking integrations

You can configure issue tracking integrations between Polaris and the following platforms:

Table 3. Supported platforms

| Platform | Supported version |
| --- | --- |
| Azure DevOps | Azure DevOps Services Note: Azure DevOps server is not supported. |
| Jira | Classic Jira Cloud running the latest long term support release Note: Jira Next-Gen is not supported. |

## Supported file types and tests

Table 4. Scan Support

| Type | Description |
| --- | --- |
| Code Upload | Only scans using Coverity buildless mode, doesn't require access to the build to scan. |
| SCM | Only scans using Coverity buildless mode, doesn't require access to the build to scan. |
| CLI | Scans using Coverity buildless or CLI mode. |

Table 5. SAST Language Version and Scan Type Support

| Language | Language Versions | Code Upload (UI) | SCM Integration | CI via Bridge CLI (CLI) |
| --- | --- | --- | --- | --- |
| Salesforce® Apex™ |  | Supported | Supported | Supported |
| C/C++ | C++23  C++20  C++98  C++03  C++11  C++14  C++17  C89  C99  C11 | Not Supported | Not Supported | Supported |
| C# \* | Up to C# 14 | Supported | Supported | Supported |
| Dart \* | Version Agnostic | Supported | Supported | Supported |
| Go \* | Go 1.25-1.26 | Supported | Supported | Supported |
| Infrastructure as code \* |  | Supported | Supported | Supported |
| Java \* | Up to Java 26 | Supported | Supported | Supported |
| JavaScript \* | ECMAScript 2023 | Supported | Supported | Supported |
| Kotlin \* | Kotlin 2.0.0-2.0.21, 2.1.0-2.1.10, 2.2 | Supported | Supported | Supported |
| Objective-C/C++ |  | Not Supported | Not Supported | Supported |
| PHP \* | Version Agnostic | Supported | Supported | Supported |
| Python \* | Python 3.x–3.13 | Supported | Supported | Supported |
| Ruby | CRuby 2.0-3.4 and equivalents via Rapid Scan Static (Sigma). (Support for Brakeman Pro analyzer, which runs as part of the Coverity Analysis suite, will continue.) | Supported | Supported | Supported |
| Scala \* | Version Agnostic | Supported | Supported | Supported |
| Swift \* | Version Agnostic | Supported | Supported | Supported |
| TypeScript \* | TypeScript 1.0–5.2 | Supported | Supported | Supported |
| Visual Basic | Up to Visual Basic 16 | Not Supported | Not Supported | Supported |

Note: \*Languages that are scanned with Rapid Scan Static and are included in your full and rapid results. See table below for more information and other technologies included in Rapid Scan Static scans.

Note: Rapid Scan Static supports and will support all existing versions for supported languages.

Note: Find the CWEs Coverity can identify in different languages here: [Coverity Coverage for Common Weakness Enumeration (CWE)](https://www.blackduck.com/static-analysis-tools-sast/cwe.html).

Table 6. SAST Capture File Types and Supported Frameworks (Rapid Scan Static)

| Language or Technology | Captured File Types | Supported Frameworks |
| --- | --- | --- |
| C# | Config  CS | .NET Framework  Bouncy Castle  Akka.NET  Amazon AWSSDK  Apache log4net  ASP.NET Boilerplate  ASP.NET Core  ASP.NET Core MVC  ASP.NET MVC  ASP.NET Web API  Castle Project  Consul.NET  Google Cloud  HtmlAgilityPack  IdentityModel  IdentityServer4  MongoDB  MySQL  Newtonsoft Json.NET  NLog  SendGrid |
| Dart | Dart  XML | Flutter  Realm |
| Go | Go | Gorilla |
| Docker and Containers | Containerfile  Dockerfile  YAML |  |
| Infrastructure as Code (IaC) technologies | HCL  JSON  YAML | Ansible  AWS CloudFormation  Azure Resource Manager (ARM)  Docker  Google Cloud Platform (GCP) Deployment Manager  Helm  Kubernetes  Terraform (for AWS, Azure, GCP, Kubernetes) |
| Java | Java  Java Properties  XML  YAML | ActiveMQ  Android  AndroidX  Apache Cordova  Apache Kafka  Apache Struts  Apache Zookeeper  Cassandra  EJB  Grails® framework  GraphQL  gRPC  Hazelcast  Jackson  Jakarta Server Faces  Java Servlet  Java/Jakarta EE  JWT  MyBatis  MySQL  Netty  Spring  Spring Boot  Spring Roo  Spring Security  Spring WebFlux  Struts  Struts2  Tomcat  Vertx |
| JavaScript / TypeScript | HTML  JavaScript  JSX  TypeScript  TSX  Vue | Angular  Apollo GraphQL  Electron  Express  Fastify  Hapi.js  JWT  Koa  MariaDB  Moleculer  MongoDB  MSSQL  MySQL  Nest.js  NodeJS  Postgres  React  React Native  Realm  Redis  Restify  Socket.IO  Vue.js  Winston |
| Kotlin | Kotlin | Android  AndroidX |
| Microservices | JSON  YAML  XML  CONF | Consul  Istio  Mulesoft  OpenAPI  Postman  RabbitMQ |
| PHP | ENV  INI  PHP | Drupal  Laminas  Laravel  Symfony  WordPress  Zend |
| Python | Python | Django  Django REST  FastAPI  Flask |
| Scala | Scala | Akka HTTP  Http4s  Play |
| Swift | plist  Swift | Alamofire  Auth0  Couchbase  CryptoSwift  Moya  OAuth  Realm  Starscream  Tealium |

Note: Rapid Scan Static supports and will support all existing versions for the listed formats.

Note: Only SCM Integration Test Automation and CI via Bridge CLI are supported for Rapid Scan Static only.

Table 7. SAST Build Tool

| Build Tool | Test mode | Support |
| --- | --- | --- |
| Bazel | Code upload or SCM integration | Not Supported |
| Bridge CLI (CI/CLI) | Supported |

Table 8. SCA Language and Package Manager Support

| Package manager | Language | Test mode | Supported | Entry point | Supported detectors, requirements | Accuracy |
| --- | --- | --- | --- | --- | --- | --- |
| Apache Ivy | *Various* | Code upload or SCM integration | Supported | Ivy Build Parse | Ivy Build Parse  - Files: ivy.xml, build.xml | Low |
| Bridge CLI (CI/CLI) | Supported | Ivy CLI | Ivy CLI  - Files: ivy.xml, build.xml - Executables: Ant 1.6.0+ and Ivy 2.4.0+ | High |
| Ivy Build Parse | Ivy Build Parse  - Files: ivy.xml, build.xml | Low |
| BitBake | *Various* | Code upload or SCM integration | Not Supported |  |  |  |
| Bridge CLI (CI/CLI) | Supported | Bitbake CLI | Bitbake CLI  - Properties: Package names - Files: build env script - Executables: bash | High |
| Cargo | Rust | Code upload or SCM integration | Supported | Cargo Lock | Cargo Lock  - Files: Cargo.lock, Cargo.toml | High |
| Bridge CLI (CI/CLI) | Supported | Cargo CLI | Cargo CLI  - Files: Cargo.lock, Cargo.toml - Executable: Cargo (version 1.44.0+) | High |
| Cargo Lock | Cargo Lock  - Files: Cargo.lock, Cargo.toml | High |
| Carthage | *Various* | All | Supported | Carthage Lock | Carthage Lock  - Files: Cartfile, Cartfile.resolved | High |
| CocoaPods | Objective-C | All | Supported | Pod Lock | Pod Lock  - Files: Podfile.lock | High |
| Conan | C/C++ | Code upload or SCM integration | Supported | Conan Lock | Conan Lock  - Files: conan.lock | High |
| Bridge CLI (CI/CLI) | Supported | Conan Lock | Conan Lock  - Files: conan.lock | High |
| Conan CLI  - Files: conanfile.txt or conanfile.py - Executables: conan | High |
| Conan CLI | Conan CLI  - Files: conanfile.txt or conanfile.py - Executables: conan | High |
| Conda | Python | Code upload or SCM integration | Not Supported |  |  |  |
| Bridge CLI (CI/CLI) | Supported | Conda CLI | Conda CLI  - Files: environment.yml. - Executable: conda | High |
| CPAN | Perl | Code upload or SCM integration | Not Supported |  |  |  |
| Bridge CLI (CI/CLI) | Supported | Cpan CLI | Cpan CLI  - File: Makefile.PL - Executables: cpan | High |
| CRAN | R | All | Supported | Packrat Lock | Packrat Lock  - File: packrat.lock | High |
| Dart | Dart | Code upload or SCM integration | Supported | Dart PubSpec Lock | Dart PubSpec Lock  - Files: pubspec.yaml, pubspec.lock | High |
| Bridge CLI (CI/CLI) | Supported | Dart CLI | Dart CLI  - Files: pubspec.yaml, pubspec.lock - Executables: dart, flutter | High |
| Dart PubSpec Lock  - Files: pubspec.yaml, pubspec.lock | High |
| Dart PubSpec Lock | Dart PubSpec Lock  - Files: pubspec.yaml, pubspec.lock | High |
| Go Dep | Golang (Go) | All | Supported | GoDep Lock | GoDep Lock  - Files: Gopkg.lock | High |
| Gogradle | Golang (Go) | All | Supported | GoGradle Lock | GoGradle Lock  - Files: gogradle.lock | High |
| Go Modules | Golang (Go) | Code upload or SCM integration | Supported | Go Mod File | Go Mod File  - File: go.mod | High |
| Bridge CLI (CI/CLI) | Supported | GoMod CLI | GoMod CLI  - Files: go.mod - Executables: go | High |
| Go Mod File | Go Mod File  - File: go.mod | High |
| Go Vendor | Golang (Go) | All | Supported | Go Vendor | Go Vendor  - Files: vendor/vendor.json | High |
| GoVndr CLI | GoVndr CLI  - Files: vendor.conf | High |
| Gradle | *Various* | Code upload or SCM integration | Supported | Gradle Project Inspector | Gradle Project Inspector  - Files: build.gradle | Low |
| Bridge CLI (CI/CLI) | Supported | Gradle Native Inspector | Gradle Native Inspector  - Files: build.gradle or build.gradle.kts - Executables: gradlew or gradle | High |
| Gradle Project Inspector  - Files: build.gradle | Low |
| Hex | Erlang | Code upload or SCM integration | Not Supported |  |  |  |
| Bridge CLI (CI/CLI) | Supported | Rebar CLI | Rebar CLI  - Files: rebar.config - Executables: rebar3 | High |
| Lerna | Node.js | Code upload or SCM integration | Not Supported |  |  |  |
| Bridge CLI (CI/CLI) | Supported | Lerna CLI | Lerna CLI  - Files: lerna.json, package.json - Executables: Lerna, and one of the following:   - package-lock.json   - npm-shrinkwrap.json   - yarn.lock. | High |
| Maven | *Various* | Code upload or SCM integration | Supported | Maven Project Inspector | Maven Project Inspector  - Files: pom.xml | Low |
| Bridge CLI (CI/CLI) | Supported | Maven CLI | Maven CLI  - Files: pom.xml - Executables: mvnw or mvn | High |
| Maven Project Inspector  - Files: pom.xml | Low |
| Maven Wrapper CLI | Maven Wrapper CLI  - Files: pom.groovy - Executables: mvnw or mvn | High |
| Maven Project Inspector  - Files: pom.xml | Low |
| npm | Node.js | Code upload or SCM integration | Supported | NPM Package Lock | NPM Package Lock  - Files: package-lock.json. For better results, include a package.json also. | High |
| NPM Package Json Parse | NPM Package Json Parse  - Files: package.json | Low |
| Bridge CLI (CI/CLI) | Supported | NPM Shrinkwrap | NPM Shrinkwrap  - Files: npm-shrinkwrap.json. For better results, include a package.json also. | High |
| NPM Package Lock  - Files: package-lock.json. For better results, include a package.json also. | High |
| NPM CLI  - Files: node\_modules, package.json - Executables: npm | High |
| NPM Package Json Parse  - Files: package-lock.json | Low |
| NPM Package Lock | NPM Package Lock  - Files: package-lock.json. For better results, include a package.json also. | High |
| NPM CLI  - Files: node\_modules, package.json - Executables: npm | High |
| NPM Package Json Parse  - Files: package.json | Low |
| NPM CLI | NPM CLI  - Files: node\_modules, package.json - Executables: npm | High |
| NPM Package Json Parse  - Files: package.json | Low |
| NPM Package Json Parse | NPM Package Json Parse  - Files: package.json | Low |
| NuGet | C# | All | Supported | NuGet Solution Native Inspector | NuGet Solution Native Inspector  - Files: A solution file with a .sln extension | High |
| NuGet Project Inspector  - Files: A project file with the .csproj or .sln extension | Low |
| NuGet Project Native Inspector | NuGet Project Native Inspector  - Files: A project file with the csproj, .fsproj, .vbproj, .asaproj, .dcproj, .shproj, .ccproj, .sfproj, .njsproj, .vcxproj, .vcproj, .xproj, .pyproj, .hiveproj, .pigproj, .jsproj, .usqlproj, .deployproj, .msbuildproj, .sqlproj, .dbproj, or .rproj extension | High |
| NuGet Project Inspector  - Files: A project file with the .csproj or .sln extension | Low |
| OPAM | OCaml | Code upload or SCM integration | Supported | Opam Lock | Opam Lock  - Files: opam files (with .opam and .opam.locked extensions) | Low |
| Bridge CLI (CI/CLI) | Supported | Opam CLI | Opam CLI  - File: opam file (with .opam extension) - Executable: opam | High |
| Opam Lock | Opam Lock  - Files: opam files (with .opam and .opam.locked extensions) | Low |
| Packagist | PHP | All | Supported | Composer Lock | Composer Lock  - Files: composer.lock, composer.json | High |
| PEAR | PHP | Code upload or SCM integration | Not Supported |  |  |  |
| Bridge CLI (CI/CLI) | Supported | Pear CLI | Pear CLI  - Files: package.xml - Executables: pear | High |
| pip | Python | Code upload or SCM integration | Supported | Pipfile Lock | Pipfile Lock  - Files: Pipfile, Pipfile.lock | High |
| PIP Requirements File Parse | PIP Requirements File Parse  - Files: requirements.txt | Low |
| Bridge CLI (CI/CLI) | Supported | Pipenv Lock | Pipenv Lock  - Files: Pipfile or Pipfile.lock - Executables: python or python3, and pipenv | High |
| PIP Native Inspector  - Files: setup.py, or one or more requirements.txt - Executables: python and pip, or python3 and pip3 | High |
| Pipfile Lock  - Files: Pipfile, Pipfile.lock | High |
| PIP Native Inspector | PIP Native Inspector  - Files: setup.py, or one or more requirements.txt - Executables: python and pip, or python3 and pip3 | High |
| Pipfile Lock  - Files: Pipfile, Pipfile.lock | High |
| Pipfile Lock | Pipfile Lock  - Files: Pipfile, Pipfile.lock | High |
| PIP Requirements File Parse | PIP Requirements File Parse  - Files: requirements.txt | Low |
| pnpm | Node.js | All | Supported | Pnpm Lock | Pnpm Lock  - Files: pnpm-lock.yaml, package.json. | High |
| Poetry | Python | All | Supported | Poetry Lock | Poetry Lock  - Files: Poetry.lock, pyproject.toml | High |
| RubyGems | Ruby | All | Supported | Gemfile Lock | Gemfile Lock  - Files: Gemfile.lock | High |
| Gemspec Parse  - Files: A gemspec file with the .gemspec extension | Low |
| Gemspec Parse | Gemspec Parse  - Files: A gemspec file with the .gemspec extension | Low |
| Rush | Node.js | All | Supported | Rush Lock | Rush Lock  - Files: rush.json file, pnpm-lock.yaml, npm-shrinkwrap.json, or yarn.lock | High |
| SBT | Scala | Code upload or SCM integration | Not Supported |  |  |  |
| Bridge CLI (CI/CLI) | Supported | Sbt Native Inspector | Sbt Native Inspector  - Files: build.sbt - Plugins: Dependency Graph | High |
| Setuptools | Python | Code upload or SCM integration | Supported | Setuptools Parse | Setuptools Parse  - File: pyproject.toml and optionally setup.cfg, or setup.py | Low |
| Bridge CLI (CI/CLI) | Supported | Setuptools CLI | Setuptools CLI  - Files: pyproject.toml and optionally setup.cfg, or setup.py - Executables: pip or pip3 specified via --detect.pip.path properties. | High |
| Setuptools Parse | Setuptools Parse  - File: pyproject.toml and optionally setup.cfg, or setup.py | Low |
| Swift | Swift | Code upload or SCM integration | Supported | Swift Lock | Swift Lock  - Files: Package.swift, Package.resolved | High |
| Bridge CLI (CI/CLI) | Supported | Swift Lock | Swift Lock  - Files: Package.swift, Package.resolved | High |
| Swift CLI  - Files: Package.swift - Executables: swift | High |
| Swift CLI | Swift CLI  - Files: Package.swift - Executables: swift | High |
| UV | Python | Code upload or SCM integration | Supported | UV Lock | UV Lock  - Files: pyproject.toml and uv.lock or requirements.txt file | High |
| Bridge CLI (CI/CLI) | Supported | UV CLI | UV CLI  - Files: pyproject.toml - Executable: uv | High |
| UV Lock | UV Lock  - Files: pyproject.toml and uv.lock or requirements.txt file | High |
| Xcode | Swift | All | Supported | Xcode Workspace Lock | Xcode Workspace Lock  - Directories: \*.xcworkspace | High |
| Xcode Project Lock  - Directories: \*.xcodeproj - Files: Package.resolved | High |
| Xcode Project Lock | Xcode Project Lock  - Directories: \*.xcodeproj - Files: Package.resolved | High |
| Yarn | Node.js | All | Supported | Yarn Lock | Yarn Lock  - Files: yarn.lock, package.json | High |

Note: Package manager version requirements are only applicable to tests created with Bridge CLI (when testing relies on/requires access to executables). N/A in the table below indicates buildless capture is used to test projects that depend on the package manager.

Table 9. SCA Package Manager Versions (latest)

| Package manager | Latest supported version |
| --- | --- |
| Apache Ivy | Apache Ant 1.6.0 Apache Ivy 2.4.0 |
| BitBake | 2.8.0 (Yocto 5.0.3) |
| Cargo | 1.85.1 |
| Carthage | N/A |
| CocoaPods | N/A |
| Conan | 2.20.1 |
| Conda | 25.1.1 |
| CPAN | Cpan Script 1.678 CPAN.pm 2.36  Cpanm 1.7047 |
| CRAN | N/A |
| Dart | Dart 3.5.0 Flutter 3.22.2 |
| Go Dep | N/A |
| Gogradle | N/A |
| Go Modules | 1.25.0 |
| Go Vendor | N/A |
| Gradle | 9.0.0 |
| Hex | Rebar 3.20.0 |
| Lerna | 8.1.8 |
| Maven | 3.9.11 |
| npm | Node v24.7.0 npm 11.5.2 |
| NuGet | NuGet 6.8.1 .NET runtime is not required with 7.13.0 |
| OPAM | 2.3.0 |
| Packagist | N/A |
| PEAR | 1.10.12 |
| pip | 25.2.0 (with pipenv 2024.0.1) |
| pnpm | 10.32.1 |
| Poetry | N/A |
| RubyGems | 3.7.1 |
| Rush | N/A |
| SBT | 1.11.3 |
| Setuptools | N/A |
| Swift | 5.6.1 |
| UV | N/A |
| Xcode | N/A |
| Yarn | 4.9.4 |

Table 10. SCA Reachability Analysis Supported Languages

| Language |
| --- |
| C |
| C# |
| C++ |
| Go |
| Java |
| JavaScript |
| Kotlin |
| PHP |
| Python |
| Ruby |
| Rust |
| Scala |
| Swift |
| TypeScript |

## Source code upload limitations

Limits in the table below apply when you upload source code to start SAST and SCA tests.

Table 11. Source code upload limitations

| Type | Size limits |
| --- | --- |
| Single file | 1 GB |
| ZIP file | 2 GB |
| Maximum file count | 200,000 files |

Note: For code uploads (when you start a test by uploading source code manually), filenames can include letters, digits, and the characters “.”, “-” and “\_”. No other characters or spaces are allowed.

## Binary upload limitations

Limits in the table below apply when you upload a binary file or a ZIP/tar of multiple binary files to start an **SCA - Binary Analysis** test.

Table 12. Binary upload limitations

| Type | Size limits |
| --- | --- |
| Default | Up to 10 GB per upload |
| Maximum file count | One binary file or a ZIP or tar file of multiple binary files |

Note: For binary file uploads, filenames can include letters, digits, and the characters “.”, “-” and “\_”. No other characters or spaces are allowed.

## Supported Source Code Management (SCM) systems

Support matrix for SCM repositories that can integrate a single repository integrated into Polaris. Bulk onboarding is only supported for Azure Repos, Bitbucket Cloud (Premium), GitHub, GitHub Enterprise, and GitLab SaaS (Premium and Ultimate). See [Connect Polaris to Multiple SCM Repositories](../how-to/connect-polaris-to-multiple-scm-repositories.md) for more information.

Table 13. Supported SCM systems

| SCM | Offering | Supported versions | Deployment type |
| --- | --- | --- | --- |
| **Azure DevOps\*** | Azure DevOps Services |  | Cloud |
| **Bitbucket** | Bitbucket Cloud |  | Cloud |
| Bitbucket Data Center | 8.19-10.0 | Self-hosted |
| **GitHub** | GitHub Standard (including Free, Pro, free for Organizations, Team) |  | Cloud |
| GitHub Enterprise Cloud |  | Cloud |
| GitHub Enterprise Server | 3.15-3.17 | Self-hosted |
| **GitLab** | GitLab SaaS (Free, Premium, Ultimate) |  | Cloud |
| GitLab Self-Managed (Free, Premium, Ultimate) | 16.11-18.4 | Self-hosted |

Note: \*For Azure DevOps

- Example: https://{org\_name}@dev.azure.com/{org\_name}/{project\_name}/\_git/{repo\_name}
- You do not need to convert your existing Azure DevOps URL repo format, for example “visualstudio.com" is accepted.

## Supported third-party tools

You can import SAST and SCA issue data from any of the following third-party tools.

Note: You can upload one file (up to 2GB) for each external analysis test. Each file you upload can only include one type of issue data (SAST or SCA).

Table 14. Supported third-party tools

| Tool | Results | File format |
| --- | --- | --- |
| Android Lint | SAST | XML or Zip |
| Brakeman | SAST | JSON |
| Black Duck® Binary Analysis | SCA | CSV or JSON Note: In Black Duck Binary Analysis, follow these steps to export vulnerabilities to CSV: [Export Vulnerabilities as CSV](https://docs.blackduck.com/access?ft:originId=0524c1a5d742cf5fa85adeada864c660/7d132d65b28cc430ff113a7833c8022e.topic&Version=latest). Or, use the `GET api/product/{productId}` endpoint to export vulnerabilities to JSON. |
| Checkmarx | SAST | XML |
| Checkstyle | SAST | XML |
| Clang | SAST | ZIP Note: Clang outputs one HTML file per checked source file. The ZIP you upload can include one or more HTML files. |
| Clippy | SAST | JSON |
| CodePeer | SAST | CSV |
| Coverity | SAST | JSON Note: Use the `cov-format-errors` command line tool to export issues captured with Coverity to JSON. For example:  ``` cov-format-errors --dir /tmp/idir --json-output-v10 file.json ``` |
| CppCheck | SAST | XML |
| DefenseCode ThunderScan | SAST | JSON |
| Dependency-Check | SCA | XML |
| ErrCheck | SAST | TXT |
| error-prone | SAST | TXT |
| ESLint | SAST | JSON |
| Fortify | SAST | FPR |
| FxCop | SAST | XML |
| Gendarme | SAST | XML |
| GitLab Security | SAST | JSON |
| GoCyclo | SAST | TXT |
| GoLint | SAST | TXT |
| GoSec | SAST | TXT |
| HCL AppScan Source | SAST | OZASMT |
| HCL AppScan on Cloud (ASoC) | SAST | XML |
| SCA | XML |
| Helix QAC | SAST | CVS |
| IneffAssign | SAST | TXT |
| JFrog Xray | SCA | JSON |
| JLint | SAST | TXT |
| Microsoft Code Analysis | SAST | TXT or TSV |
| MobSF | SAST | JSON |
| MobSF Scan | SAST | JSON |
| NDepend | SAST | XML |
| OCLint | SAST | XML |
| Parasoft JTest/C++Test/dotTest | SAST | XML |
| PHP\_CodeSniffer | SAST | XML |
| PHPMD | SAST | XML |
| PMD | SAST | XML |
| Pylint | SAST | JSON |
| Rapid Scan SAST (Sigma) | SAST | JSON |
| Retire.js | SCA | JSON |
| SafeSQL | SAST | TXT |
| SARIF | SAST | JSON |
| SATE | SAST | XML |
| Scalastyle | SAST | XML |
| SCARF | SAST | XML |
| SciTools Understand | SAST | CSV |
| Semgrep | SAST | JSON |
| Snyk Open Source | SCA | JSON |
| SonarQube Generic Issue Import Format | SAST | JSON |
| SpotBugs/FindBugs | SAST | XML |
| Black Duck® Software Risk Manager™ | SAST | XML |
| SCA | XML |
| Staticcheck | SAST | JSON |
| TFLint | SAST | SARIF JSON |
| TruffleHog | SAST | JSON |
| Veracode | SAST | ZIP or XML |
| SCA | ZIP or XML |
| Vet | SAST | JSON |
| WPScan | SCA | JSON |
| ZPA | SAST | JSON |
