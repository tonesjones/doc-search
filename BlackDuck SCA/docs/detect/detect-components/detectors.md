---
title: "Detectors"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/detectors.html"
content_id: "QCxasHgk6nxXRhe7O3QfpQ"
version: "11.5.1"
section: "Detect Components"
scraped_at: "2026-08-08T23:44:46.317560+00:00"
---

# Detectors

The Detect Detector tool runs one or more detectors to find and
extract dependencies from all supported package managers.

Each package manager ecosystem is assigned a detector type. Each detector type may have
multiple methods (detectors) used to extract dependencies.

Which detector(s) will run against your project is determined by the detector search
process.

## Detector Types, and Detectors

The following table contains information for each Detector type, and detector. Details on
these terms is available on the detector search page.

| Detector Type | Detector | Language | Forge | Requirements | Accuracy |
| --- | --- | --- | --- | --- | --- |
| **BITBAKE** |  |  |  |  |  |
|  | Bitbake CLI | various | YOCTO | Properties: Package names  File: build env script  Executable: bash | HIGH |
| **CARGO** |  |  |  |  |  |
|  | Cargo CLI | Rust | crates | Files: Cargo.toml  Executable: Cargo version 1.44.0+ | HIGH |
|  | Cargo Lock | Rust | crates | Files: Cargo.lock, Cargo.toml | HIGH |
| **CARTHAGE** |  |  |  |  |  |
|  | Carthage Lock | various | GitHub | Files: Cartfile, Cartfile.resolved | HIGH |
| **CLANG** |  |  |  |  |  |
|  | Clang CLI | C or C++ | Derived from the Linux distribution. | File: compile_commands.json  Executable: Linux package manager | HIGH |
| **COCOAPODS** |  |  |  |  |  |
|  | Pod Lock | Objective C | COCOAPODS and NPMJS | File: Podfile.lock | HIGH |
| **CONAN** |  |  |  |  |  |
|  | Conan 2 CLI | C/C++ | conan | Files: conanfile.txt or conanfile.py  Executable: conan (version 2.x) | HIGH |
|  | Conan Lock | C/C++ | conan | File: conan.lock | HIGH |
|  | Conan 1 CLI | C/C++ | conan | Files: conanfile.txt or conanfile.py  Executable: conan (version 1.x) | HIGH |
| **CONDA** |  |  |  |  |  |
|  | Conda Tree | Python | Anaconda | File: environment.yml or environment.yaml  Executables: conda, conda-tree | HIGH |
|  | Conda CLI | Python | Anaconda | File: environment.yml or environment.yaml  Executable: conda | HIGH |
| **CPAN** |  |  |  |  |  |
|  | Cpan CLI | Perl | CPAN | File: Makefile.PL  Executables: cpan, and cpanm | HIGH |
| **CRAN** |  |  |  |  |  |
|  | Packrat Lock | R | CRAN | File: packrat.lock | HIGH |
| **DART** |  |  |  |  |  |
|  | Dart CLI | Dart | Dart | Files: pubspec.yaml, pubspec.lock  Executable: dart, flutter | HIGH |
|  | Dart PubSpec Lock | Dart | Dart | Files: pubspec.yaml, pubspec.lock | HIGH |
| **GIT** |  |  |  |  |  |
|  | Git | various | N/A | Directory: .git  Executable: git | HIGH |
|  | Git Parse | various | N/A | Files: .git/config, .git/HEAD, .git/ORIG_HEAD | HIGH |
| **GO_DEP** |  |  |  |  |  |
|  | GoDep Lock | Golang | GitHub | File: Gopkg.lock | HIGH |
| **GO_GRADLE** |  |  |  |  |  |
|  | GoGradle Lock | Golang | GitHub | File: gogradle.lock | HIGH |
| **GO_MOD** |  |  |  |  |  |
|  | GoMod CLI | Golang | Go Modules | File: go.mod  Executable: go | HIGH |
|  | Go Mod File | Golang | Go Modules | File: go.mod | HIGH |
| **GO_VENDOR** |  |  |  |  |  |
|  | Go Vendor | Golang | GitHub | File: vendor/vendor.json | HIGH |
| **GO_VNDR** |  |  |  |  |  |
|  | GoVndr CLI | Golang | GitHub | File: vendor.conf | HIGH |
| **GRADLE** |  |  |  |  |  |
|  | Gradle Native Inspector | various | Maven Central | File: build.gradle or build.gradle.kts  Executable: gradlew or gradle | HIGH |
|  | Gradle Project Inspector | various | Maven Central | Files: build.gradle, *.gradle | LOW |
| **HEX** |  |  |  |  |  |
|  | Rebar CLI | Erlang | Hex | File: rebar.config  Executable: rebar3 | HIGH |
| **IVY** |  |  |  |  |  |
|  | Ivy CLI | various | Maven Central | Files: ivy.xml, build.xml  Executables: Ant 1.6.0+ and Ivy 2.4.0+ | HIGH |
|  | Ivy Build Parse | various | Maven Central | Files: ivy.xml, build.xml | LOW |
| **LERNA** |  |  |  |  |  |
|  | Lerna CLI | Node JS | npmjs | Files: lerna.json, package.json  Executable: Lerna  One of: package-lock.json, npm-shrinkwrap.json, or yarn.lock | HIGH |
| **MAVEN** |  |  |  |  |  |
|  | Maven CLI | various | Maven Central | File: *pom.xml  Executable: mvnw or mvn | HIGH |
|  | Maven Wrapper CLI | various | Maven Central | File: pom.groovy  Executable: mvnw or mvn | HIGH |
|  | Maven Project Inspector | various | Maven Central | File: pom.xml | LOW |
| **NPM** |  |  |  |  |  |
|  | NPM Shrinkwrap | Node JS | npmjs | File: npm-shrinkwrap.json  Optionally, for better results: package.json | HIGH |
|  | NPM Package Lock | Node JS | npmjs | File: package-lock.json  Optionally, for better results: package.json | HIGH |
|  | NPM CLI | Node JS | npmjs | Files: node_modules, package.json  Executable: npm | HIGH |
|  | NPM Package Json Parse | Node JS | npmjs | File: package.json | LOW |
| **NUGET** |  |  |  |  |  |
|  | NuGet Solution Native Inspector | C# | NuGet.org | File: a solution file with .sln extension | HIGH |
|  | NuGet Project Native Inspector | C# | NuGet.org | File: project file with one of the following extensions: .csproj, .fsproj, .vbproj, .asaproj, .dcproj, .shproj, .ccproj, .sfproj, .njsproj, .vcxproj, .vcproj, .xproj, .pyproj, .hiveproj, .pigproj, .jsproj, .usqlproj, .deployproj, .msbuildproj, .sqlproj, .dbproj, .rproj | HIGH |
|  | NuGet Project Inspector | C# | NuGet.org | File: project file with one of the following extensions: .csproj, .sln | LOW |
| **OPAM** |  |  |  |  |  |
|  | Opam CLI | OCaml | opam | File: opam file (with .opam extension)  Executable: opam | HIGH |
|  | Opam Lock | OCaml | opam | Files: opam files (with .opam and .opam.locked extensions) | LOW |
| **PACKAGIST** |  |  |  |  |  |
|  | Composer Lock | PHP | Packagist.org | Files: composer.lock, composer.json | HIGH |
| **PEAR** |  |  |  |  |  |
|  | Pear CLI | PHP | Pear | File: package.xml  Executable: pear | HIGH |
| **PIP** |  |  |  |  |  |
|  | Pipenv CLI | Python | PyPI | Files: Pipfile or Pipfile.lock  Executables: python or python3 specified via --detect.python.path property, and pipenv | HIGH |
|  | PIP Native Inspector | Python | PyPI | Files: setup.py file, pyproject.toml file, or one or more requirements.txt files  Executables: python and pip, or python3 and pip3 specified via --detect.python.path and --detect.pip.path properties | HIGH |
|  | Pipfile Lock | Python | PyPI | Files: Pipfile, Pipfile.lock | HIGH |
|  | PIP Requirements File Parse | Python | PyPI | File: requirements.txt | LOW |
| **PNPM** |  |  |  |  |  |
|  | Pnpm Lock | Node JS | npmjs | Files: pnpm-lock.yaml and package.json | HIGH |
| **POETRY** |  |  |  |  |  |
|  | Poetry Lock | Python | PyPI | Files: Poetry.lock, pyproject.toml | HIGH |
| **RUBYGEMS** |  |  |  |  |  |
|  | Gemfile Lock | Ruby | RubyGems | File: Gemfile.lock | HIGH |
|  | Gemspec Parse | Ruby | RubyGems | File: gemspec file (with .gemspec extension) | LOW |
| **Rush** |  |  |  |  |  |
|  | Rush Lock | Node JS | npmjs | Files: rush.json file, pnpm-lock.yaml, npm-shrinkwrap.json, or yarn.lock | HIGH |
| **SBT** |  |  |  |  |  |
|  | Sbt Native Inspector | Scala | Maven Central | File: build.sbt  Plugin: Dependency Graph | HIGH |
| **Setuptools** |  |  |  |  |  |
|  | Setuptools CLI | Python | PyPI | Files: pyproject.toml and optionally setup.cfg, or setup.py  Executables: pip or pip3 specified via --detect.pip.path properties. | HIGH |
|  | Setuptools Parse | Python | PyPI | File: pyproject.toml and optionally setup.cfg, or setup.py | LOW |
| **SWIFT** |  |  |  |  |  |
|  | Swift Lock | Swift | Swift.org | Files: Package.swift, Package.resolved | HIGH |
|  | Swift CLI | Swift | Swift.org | File: Package.swift  Executables: swift | HIGH |
| **UV** |  |  |  |  |  |
|  | UV CLI | Python | PyPI | Files: pyproject.toml  Executable: uv | HIGH |
|  | UV Lock | Python | PyPI | Files: pyproject.toml and uv.lock or requirements.txt file | HIGH |
| **XCODE** |  |  |  |  |  |
|  | Xcode Workspace Lock | Swift | GITHUB | Directory: *.xcworkspace | HIGH |
|  | Xcode Project Lock | Swift | GITHUB | Directory: *.xcodeproj  File: Package.resolved | HIGH |
| **YARN** |  |  |  |  |  |
|  | Yarn Lock | Node JS | npmjs | Files: yarn.lock and package.json | HIGH |
