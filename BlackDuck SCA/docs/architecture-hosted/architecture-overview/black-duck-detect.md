---
title: "Black Duck Detect"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/black-duck-detect.html"
content_id: "KtWDPgeEITGR8xSgVHGUOw"
version: "2026.7"
section: "Hosted Architecture and Network Communications"
scraped_at: "2026-08-08T15:32:51.088112+00:00"
---

# Black Duck Detect

Black Duck Detect consolidates the functionality of Black Duck and Black Duck
Binary Analysis into a single solution. Black Duck Detect is designed to
integrate natively into the build/CI environment and for Black Duck and Black Duck
Binary Analysis, it makes it easier to set up and scan code bases using a variety of
languages and package managers. Black Duck Detect performs the task of
determining all the direct and transitive dependencies, collecting that data, and
sending it to the Black Duck server (as JSON data in BDIO format) for open source
software (OSS) matching. After determining the dependencies, it can also launch the
Black Duck Scan Client to perform a variety of file scanning methods. Those methods
and network communication requirements are described in the next section, *The
Scan Client*. Black Duck Detect can also run a Black Duck Binary
Analysis (BDBA) scan in conjunction with other scan methods. This method and its
network communication requirements are covered in Chapter 2.

A few key points about Black Duck Detect:

1. Black Duck Detect typically runs in a network-enabled environment and typically
   downloaded via a curl command from <https://detect.blackduck.com>. However, this is not required and
   Black Duck Detect can run in an air gap environment. If running Black Duck Detect in an air gap environment is desired, click this [link](https://docs.blackduck.com/access?ft:originId=9c0814dc6c47bd8e1b015657cf47a869/2767292a573dc549b9b4297b701af3ab.topic) in the Black Duck Detect
   documentation about how to configure this mode of operation.
2. Black Duck Detect can be run offline and the contents examined. The
   content is JSON data in BDIO format.

   For information on the BDIO spec, click this [link](https://github.com/blackducksoftware/bdio).

   For additional information on how to run Black Duck Detect in an
   offline mode, click this [link](https://docs.blackduck.com/access?ft:originId=9c0814dc6c47bd8e1b015657cf47a869/3868efca6fcac61e306669473765639d.topic).
3. Black Duck Detect can run independently of a scan on the Black Duck
   server, or it can be configured to wait for the Black Duck scans to complete
   so it can retrieve additional information. Typically this is done if a user
   wants to fail a build due to a policy violation or collect a post scan
   report and store it as a build artifact.
4. Black Duck Detect does use Google Analytics to collect anonymized usage metrics
   which helps to set engineering priorities. In a network where access to outside
   servers is limited, this mechanism may fail, and those failures may be visible
   in the log. This is a harmless failure; Black Duck Detect will continue
   to function normally. If you wish to disable this mechanism, click this [link](https://docs.blackduck.com/access?ft:originId=9c0814dc6c47bd8e1b015657cf47a869/6e2def2a138a87be68398b685d50ca6e.topic) for instructions.
