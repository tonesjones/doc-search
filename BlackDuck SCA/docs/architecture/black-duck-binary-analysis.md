---
title: "Black Duck Binary Analysis"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/black-duck-binary-analysis.html"
content_id: "L5Ta9ELhc0GPdvlu3Uvqig"
version: "2026.7"
section: "Architecture and Network Communications"
scraped_at: "2026-08-08T15:32:48.293718+00:00"
---

# Black Duck Binary Analysis

Black Duck Binary Analysis(BDBA), an integrated add-on for Black Duck, identifies the
open-source security, compliance, and quality risks in the software libraries,
executables, and vendor-supplied binaries in use within your codebase. BDBA supports
expanded file type support including various firmware formats, filesystems/disk images,
installation formats, and various compression and archive formats. With Black Duck Binary Analysis, you can:

- Analyze virtually any compiled software, firmware, mobile applications, or
  multiple installer formats, without needing to access the source.
- Identify embedded open-source usage and risks within binary executables and libraries.
- Manage code decay and improve software quality within binary dependencies.
- Monitor new vulnerabilities in previously scanned binaries.

## Architecture overview

BDBA integrated with Black Duck consists of these components that work together to
provide Black Duck - Binary Analysis functionality.

  
 [image: BDBA Architecture]

## Black Duck Detect

Black Duck Detect uploads the binary file to the BDBA scanner located in the BDBA
container on the Black Duck server. Black Duck Detect does not scan the
binary file.

Tip: The maximum size of a binary that can be scanned is 100 GB.

The binary file, sent to the customer's Black Duck SCA server,
is treated as confidential information by Black Duck in accordance with our
customer agreements. By default, all communication with Black Duck servers is done via HTTPS. More specifically,
all session data is encrypted using TLS1.2. Customer sites always initiate
connections with Black Duck SCA services; the hosted Black Duck SCA services never call out to the Black Duck application. The customer's Black Duck servers
contain the HTTPS certificate, the Black Duck application
initiates all connection requests using the certificate’s public key.

Black Duck Detect always runs locally, on the customer's premises. Binaries stay
within the company's network environment and are uploaded to a Black Duck Binary Analysis container which is within the company's
premises.

## BDBA container

The BDBA scanner scans the binary file and generates a `.bdio` file. This file
contains signatures of the binary file and is passed to the Black Duck web
application. It then generates a Bill of Material, or “BOM”, which details the
open-source components/versions and presents the associated risk factors –
security risk, license risk, and operational risk. If also using Black Duck
scanning methods at the same time, the binary results are unified into a single
BOM with the Binary match type designating the BDBA identifications.

Once scanning is completed, the binaries are immediately deleted.

## How BDBA identifies components

Three of these methods can be applied to any type of component:

- **hashsum**: For Java and native components. Uses the checksum of a JAR file
  to find known components from Maven Central. Uses the checksum of a file to look
  up components originating from Linux distributions.
- **signature**: Matches file fingerprints to a database of known components.
  It works for native components (code compiled to a binary), .NET bytecode, Java
  bytecode, and Go binaries.
- **distro-package-manager**: Leverages information from a Linux distribution
  package manager database to extract component information. Also works with
  distribution package files such as `.deb` and
  `.rpm`. It works for components of any language.

One of these methods is only used for native components that are or contain macOS or
iOS executables:

- **cocoapod-package**: Extracts information from native Objective-C and Swift
  binaries and matches them against known CocoaPods projects downloaded via the
  CocoaPods package manager. CocoaPods components are matched from MacOS and iOS
  applications.

The next three matching methods are only used for Java bytecode:

- **pom**: Uses the Maven group and artifact names from the JAR file's
  `.pom` file to match components.
- **manifest**: Uses the Maven artifact names from the JAR file's manifest file
  to match components.
- **jar-filename**: Uses the Maven artifact name retrieved from the JAR
  filename to match components.

Then there are methods used for language-specific or platform-specific
components:

- **python-package-manager**: Uses metadata found inside Python Egg and
  Wheel packages to match components.
- **ruby-package-manager**: Uses found gemspec files to match
  components.

Some components which have been previously displayed as individual components are now
displayed as submodules and are listed under **Module files**. This applies
currently to the .NET component but can be expanded in future releases.

## Copyright information

Copyright ©2026 by Black Duck.

All rights reserved. All use of this documentation is subject to the license agreement
between Black Duck Software, Inc. and the licensee. No part of the contents of this
document may be reproduced or transmitted in any form or by any means without the prior
written permission of Black Duck Software, Inc.

Black Duck, Know Your Code, and the Black Duck logo are registered trademarks of Black
Duck Software, Inc. in the United States and other jurisdictions. Black Duck Code
Center, Black Duck Code Sight, Black Duck Hub, Black Duck Protex, and Black Duck Suite
are trademarks of Black Duck Software, Inc. All other trademarks or registered
trademarks are the sole property of their respective owners.
