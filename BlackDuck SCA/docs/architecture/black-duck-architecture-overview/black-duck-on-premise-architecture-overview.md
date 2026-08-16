---
title: "Black Duck on-premise architecture overview"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/black-duck-on-premise-architecture-overview.html"
content_id: "1dmuNgr8p6A3bxA~xn2cKw"
version: "2026.7"
section: "Architecture and Network Communications"
scraped_at: "2026-08-08T15:32:43.141201+00:00"
---

# Black Duck on-premise architecture overview

[image: Black Duck Architecture]   

Black Duck's architecture consists of different components
that work together to provide Black Duck functionality.

## Black Duck Detect

Black Duck Detect consolidates the functionality of Black Duck and Black Duck Binary
Analysis into a single solution. Black Duck Detect is designed to integrate
natively into the build/CI environment and for Black Duck and Black Duck Binary
Analysis, it makes it easier to set up and scan code bases using a variety of
languages and package managers. Black Duck Detect performs the task of
determining all the direct and transitive dependencies, collecting that data, and
sending it to the customer's Black Duck server (as JSON data in BDIO format) for
open-source software (OSS) matching. After determining the dependencies, it can also
launch the Black Duck Scan Client to perform a variety of file scanning methods.
Those methods and network communication requirements are described in the next
section, *The Scan Client*. Black Duck Detect can also run a Black Duck
Binary Analysis (BDBA) scan in conjunction with other scan methods. This method and
its network communication requirements are covered in Chapter 2.

A few key points about Black Duck Detect:

1. Black Duck Detect typically runs in a network-enabled environment and
   typically downloaded via a curl command from <https://detect.blackduck.com>.
   However, this is not required and Black Duck Detect can run in an
   air gap environment. If running Black Duck Detect in an air gap
   environment is desired, click this [link](https://docs.blackduck.com/access?ft:originId=9c0814dc6c47bd8e1b015657cf47a869/922ab7c0cde7d0b0a2f9245babfbbf23.topic) in the Black Duck Detect
   documentation about how to configure this mode of operation.
2. Black Duck Detect can be run offline and the contents examined. The
   content is JSON data in BDIO format.

   For information on the BDIO spec, click this [link](https://github.com/blackducksoftware/bdio).

   For additional information on how to run Black Duck Detect in an
   offline mode, click this [link](https://docs.blackduck.com/access?ft:originId=9c0814dc6c47bd8e1b015657cf47a869/3868efca6fcac61e306669473765639d.topic).
3. Black Duck Detect can run independently of a scan on the customer's
   Black Duck server, or it can be configured to wait for the Black Duck scans
   to complete so it can retrieve additional information. Typically, this is
   done if a user wants to fail a build due to a policy violation or collect a
   post scan report and store it as a build artifact.
4. Black Duck Detect does use Google Analytics to collect anonymized
   usage metrics which helps to set engineering priorities. In a network where
   access to outside servers is limited, this mechanism may fail, and those
   failures may be visible in the log. This is a harmless failure; Black Duck Detect will continue to function normally. If you wish to
   disable this mechanism, click this [link](https://docs.blackduck.com/access?ft:originId=9c0814dc6c47bd8e1b015657cf47a869/6e2def2a138a87be68398b685d50ca6e.topic) for instructions.

## The Scan Client

The Scan Client performs the task of scanning a file system, collecting data, and sending it
to the customer's Black Duck server for open-source software (OSS) matching. This
software always runs locally, on the customer's premises or wherever the files to be
scanned are located. As the Scan Client examines the files, it generates
“signatures” of the files and directories it is scanning and collects other metadata
like file path and file/directory sizes in order to accurately identify open-source
code; refer to the diagram on page 1 to see what is additionally sent. This
information is used to match against information in the Black Duck KnowledgeBase to
determine the open-source components/versions that are contained in the software
being analyzed. As part of its operation, if the Scan Client can connect to the
specified customer's Black Duck server, it will check its current version against
that server and update itself if necessary.

There are various options for running the Scan Client – it can be used via Black Duck Detect and integrated into CI Tools (for example, Jenkins),
standalone (either with a CLI or GUI), or as a Docker container for scanning other
containers. The typical best practice is to run the scan client as part of Black Duck Detect.

In addition to running a component-level signature scan, the client can also
optionally perform other scan functions. If desired by the end user, it can
also:

1. Run a type of string search analysis on textual-based files looking for license
   text and copyright statements.
   - The string search matches only return the match category, file name,
     and byte offset (location inside the file) where the match was
     found.
   - For copyright matches, it also uploads textual content (the copyright
     statement).
2. Wait for component analysis to complete and scan unmatched files for OSS snippets.
   - Snippet scanning creates codeprints (one-way cryptographic hashes)
     over fragments of the files via a sliding window method which are
     then used to match for OSS.
   - It does not capture, store, or send any textual file content to the
     Black Duck KB for analysis. All code stays behind the company
     firewall. Only hashes are transferred.
3. Encrypt and upload scanned source to the customer's Black Duck server for
   snippet side-by-side comparison, or license and copyright display in the Black
   Duck UI.
   - Uploading code is an optional feature that must be enabled at the
     server and scan levels.
   - If the server is enabled for source upload (which includes defining a
     company-specific encryption key) and the user indicates they wish to
     upload source files, the client will encrypt and upload the OSS
     files scanned for snippets and strings to the customer's Black Duck
     Server. See the *Black Duck upload service* section for more
     information.

Most of these activities can be controlled either at the customer's Black Duck Server
level if the behavior is not desired. For example, if required by company policy,
one can set the customer's Black Duck server to:

1. Not accept upload of encrypted source files.
2. Not send file/path name information.

Not sending up the source files can impact a user’s ability to triage matches, however it does
not affect the quality of the Bill of Material, or “BOM”. It is up to individual
customers policies to enable this feature and by default it is off.

However, not sending the file and path names to the customer's Black Duck server can lead to
inexact component matching and a poorer quality BOM. Therefore, this feature is on
by default and Black Duck recommends that customers do not disable it as using this
information leads to stronger, more accurate matching. If file/path information is
not desired to be uploaded, this can be controlled with the KBMATCH_SENDPATH system
parameter. Instructions on how a system administrator can configure system
parameters is included in the appropriate installation guides for your container
orchestration platform.

Note: The KBMATCH_SENDPATH parameter has been deprecated as of 2023.4.0 and will be removed in a
future update. Black Duck users with Match as a Service (MaaS) enabled will not be
able to use this parameter. Customers wanting to continue using this option will
need to contact Black Duck support to have MaaS disabled for their Black Duck
registration keys.

## Black Duck web application

Once the scan is completed, the Scan Client sends the signatures to Black Duck's web application. Black Duck's web application,
accessed via a browser, provides a central point for managing and viewing all the
information captured. User connections to Black Duck's
web application (from a browser or other supported client) are secured using HTTP/2
and TLS1.3 (or HTTP 1.1 and/or TLS 1.2 if the browser does not support HTTPS/2
and/or TLS 1.3).

The Black Duck application will send the signatures to the Black Duck KnowledgeBase (KB) web service to identify the
open-source software contained in the code which has been scanned and retrieve the
associated metadata for each component. It will then generate a BOM, which details
the open-source components/versions and presents the associated risk factors –
security risk, license risk, and operational risk.

End users can review and edit the BOMs, filter results based on risk and other
factors, and drill down to get more detailed information on the vulnerabilities,
licenses, files, and other information associated with each of the components in the
BOM. The Black Duck application also includes features
such as policy management, search, vulnerability mitigation status and tracking,
reporting, and so on.

The Black Duck application is built on top of various open-source
components – such as Apache Tomcat web server, PostgreSQL database, and so on. The
Black Duck application is deployed and managed as a
set of Docker containers and supports a range of container orchestration platforms.
More information on these containers is included in the Black Duck
installation guide.

A few notes about the Black Duck web application:

1. The web application can make frequent calls to both the Black Duck KB and
   Black Duck registration services. To get full operability of the system,
   those services must be accessible by the server. The endpoint for the KB is
   kb.blackducksoftware.com and the registration service endpoint is
   updates.suite.blackducksoftware.com. For more information on making those
   services accessible, click this [link](https://community.blackduck.com/s/question/0D53400004WULuLCAX/what-are-the-ip-whitelisting-requirements-for-all-black-duck-products-to-communicate-with-hosted-black-duck-services) to view the relevant community article.
2. For additional information about communication between the Black Duck web
   application and the various services, see the *Communication with Black
   Duck services* section.

## Black Duck upload service

Customers can optionally decide to upload their source files to be used in reviewing
snippet matches or embedded licenses and copyrights in the Black Duck UI. If not
enabled, the system will still function, however users will not be able to view
match content in the UI.

If enabled, the customer system administrator uses a Docker secret to provide a key
that encrypts a Black Duck generated master key, which is used for encrypting and
decrypting the customer's source files. The master key is stored encrypted
(AES-GCM-256 with a key length of 32 bytes) via the customer-provided key.
Information on how to set this up is included in the Black Duck installation guide
for your particular container orchestration platform.

During a scan, the scan client sends the source file contents to the Black Duck
instance via SSL/TLS-secured endpoint(s) and with the proper authorization token. An
upload endpoint receives the source file contents via HTTPS. Access to the endpoint
is secured via the generated and verified Black Duck JSON Web Token (JWT). The
source files are stored via their associated file signature – no files are stored
with their file name. Files are encrypted upon upload via the master key.

The web application requests the file contents via the given file signature. The
source file is transmitted via HTTPS over the network. The individual source file is
unencrypted for viewing in the Black Duck web application via the master encryption
key.

In addition to encryption, the uploaded files also are deleted according to the data
retention policy as defined by the customer. See the *Data retention policy*
section for more information.

## Web services hosted on customer's Black Duck servers

The Black Duck application works in conjunction with
services that are hosted in Black Duck data centers. These
services are:

- **Registration service**: Used to validate Black Duck
  software license and entitlements.

  This service is datacenter-managed by Black Duck in Massachusetts, USA.
- **Black Duck KnowledgeBase (KB)**: Contains meta-data (versions,
  signatures, licenses, vulnerability data, and so on) on all the open-source
  projects tracked by Black Duck. As a web service, the
  KB provides real-time updates, for example, new components or versions,
  vulnerabilities, and so on, which are immediately available to the Black Duck application.

  The KB resides on Google Cloud Platform (GCP) Services with a variety of
  locations. Currently the KB is running of an instance of GCP in North
  America, Europe, and Asia.

  It is possible to force the location of the KB onto one GCP geographical
  location. Failback mechanisms, in case one instance is down, can also be
  disabled.
