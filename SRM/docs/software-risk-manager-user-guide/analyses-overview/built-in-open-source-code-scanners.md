---
title: "Built-In Open Source Code Scanners"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/built-in-open-source-code-scanners.html"
content_id: "KTIpwea3AucY2lOQ74QJew"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:03:35.633440+00:00"
content_hash: "0cb8bda178e06f685ed4e55e63ed54320182694011d253bc57864b9500833e49"
---

# Built-In Open Source Code Scanners

Software Risk Manager bundled open source code analyzers can analyze C/C++, Objective-C,
Java, JavaScript, JSP, .NET (C#, VB), PHP, Terraform, Docker, Swift, Scala, Python, Ruby
on Rails, and Rust applications. For all [supported languages](https://www.blackduck.com/integrations.html#logoWall6), Software Risk Manager
will analyze the source using [open source bundled tools](https://www.blackduck.com/integrations.html#logoWall6) built specifically
for a target language. For applications built with any combination of the supported
languages, Software Risk Manager will run the appropriate checkers on the provided
source.

Note: The Software Risk Manager built-in open-source
code scanners are turned off by default and can be turned on from the Integrations
page. For more information, see the Integrations Overview
section.

For Java applications, Software Risk Manager bundled open source code analyzers supports
scanning compiled bytecode. In fact, the preferred approach for Java projects is to
upload **both** source and bytecode to Software Risk Manager in the supported file
format described in the bullets below. This yields the best coverage for issue
detection.

For .NET applications, Software Risk Manager supports scanning compiled DLLs. It is also
recommended that the source be uploaded. This will provide better source location
information and will allow for viewing the source while looking at finding details.

Note: If you choose to upload an entire Visual Studio solution
folder, there may be duplicates of the build DLLs and third-party DLLs. This will
cause a longer analysis time and possibly incorrect results if some DLLs are stale.
To achieve the best results, upload a zip that contains only the DLLs and PDB files
for the binaries you wish to analyze. Upload the source as a separate
zip.

## Accepted zip Archive Formats

Software Risk Manager accepts application inputs in the following zip archive
formats for running bundled open source tools:

- **C/C++.**
  `.zip` containing C/C++ source files that will be analyzed by
  Software Risk Manager bundled tools. Software Risk Manager will scan the
  `.zip` file for `.h`, `.c`,
  `.hpp`, and `.cpp` files. *(Note: If
  your project contains Objective-C source files then `.h`
  files will be treated as Objective-C rather than C/C++).*
- **Java source.**
  `.zip` containing Java source files – with a .java extension
  – to be analyzed by the Software Risk Manager bundled tools.
- **Java bytecode.**
  `.zip` containing `.class` or
  `.jar` bytecode files intended for the JVM.
- **.NET.**
  `.zip` containing C# or VB.NET source files – with a .cs or .vb
  extension.
- **.NET DLLs.**
  `.zip` containing compiled `.dll`s. You must
  also include the PDB files for `.dll`s you wish to scan.
  Software Risk Manager will only scan `.dll`s with
  corresponding PDB files – unless there are no PDB files, in which case
  Software Risk Manager will scan all `.dll`s but source
  location information may be sub-optimal.
- **iOS.**
  `.zip` containing `.ipa` files. *(Note: This
  detection is only for associating add-in tools with these files).*
- **Windows UWP.**
  `.zip` containing `.appx` files. *(Note:
  This detection is only for associating add-in tools with these
  files).*
- **Ruby on Rails.**
  `.zip` containing Ruby source files that are inside an
  `app/` directory.
- **PHP.**
  `.zip` containing PHP source files.
- **PL/SQL.**
  `.zip` containing PL/SQL source files.
- **Python.**
  `.zip` containing Python source files.
- **JavaScript.**
  `.zip` containing .js files; minified JavaScript will be
  ignored.
- **Scala.**
  `.zip` containing .scala files.
- **Swift.**
  `.zip` containing `.swift` files.
- **Objective-C.**
  `.zip` containing `.m`, `.mm`,
  `.M`, `.h` files. *(Note: '.h' will only
  be detected as Objective-C if there are other Objective-C file types in
  the '.zip').*
- **Terraform.**
  `.zip` containing `.tf` files.
- **Docker.**
  `.zip` containing `Dockerfile` files. Note
  that this has no extension.
- **Rust.**`.zip` containing Rust project files. Software Risk
  Manager will scan the `.zip` archive for the
  `Cargo.toml` file (which is the manifest for Rust
  projects) and `.rs` source files.

Note: **Software Risk Manager enforces a single source .zip archive per
analysis**. Although Software Risk Manager supports multiple languages, the
expectation is that they will all be packaged in a single `.zip`archive
to enable consistent path correlation across all the checkers. And while source and
bytecode inputs can be uploaded in separate files, they do not have to be split up. A
single `.zip` file containing C/C++ source, Java source, Java bytecode,
.NET DLLs, .NET source, PHP source, Scala source, Ruby on Rails source, Python source,
JavaScript source and Rust source is perfectly acceptable.
