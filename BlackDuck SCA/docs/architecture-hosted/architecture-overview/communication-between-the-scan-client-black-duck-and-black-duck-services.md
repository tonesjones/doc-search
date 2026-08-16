---
title: "Communication between the Scan Client, Black Duck, and Black Duck services"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/communication-between-the-scan-client-black-duck-and-black-duck-services.html"
content_id: "qZbfpC_HqhQG1igkhyysyw"
version: "2026.7"
section: "Hosted Architecture and Network Communications"
scraped_at: "2026-08-08T15:32:54.251863+00:00"
---

# Communication between the Scan Client, Black Duck, and Black Duck services

The Scan Client interacts purely as a client of the Black Duck application
running in the secure Black Duck hosted environments. Black Duck
interacts purely as a client of the servers hosted by Black Duck at secure data centers.
Black Duck understands that Black Duck is being used in conjunction with
our customer's valuable software intellectual property. All Internet-based
communications among the customer’s premises, the hosted environment where the Black Duck application is running and the Black Duck data center
servers is treated with due care. No source or binary code ever leaves the customer’s
premises, unless source files are uploaded, and no proprietary customer data ever leaves
the Black Duck hosted environment.

All proprietary information is treated as confidential information by Black Duck in accordance
with our customer agreements. By default, all communication between application layers
is done via HTTPS. More specifically, all session data is encrypted using TLS 1.2. The
Scan Client always initiates connections with Black Duck running in the
hosted environment, which in turn always initiates connections with Black Duck services.
The Black Duck application never calls out to the Scan Client, and the
hosted Black Duck services never call out to the Black Duck
application. The Black Duck servers contain the HTTPS certificate; the Black Duck application initiates all connection requests using the
certificate’s public key.

The information that is sent to the KB web services is for the purpose of retrieving
other information needed by the Black Duck application, for example,
open source metadata. Black Duck does not retain any sensitive customer application data
at the Black Duck data centers.

More details on the specific communications between a customer site installation of Black Duck and the Black Duck services is included below.

## Registration service

The registration service provides product activation and is used to authenticate the
customer’s license key and the associated entitlements. It also collects aggregate,
high-level operational metrics that are used to improve services delivered to the
customer.

To perform this function, information such as the registration code, and license
expiration date is exchanged between the installed product(s) at the customer's site
and the Black Duck registration server.

The list of metrics collected for each license key consist of: product serial number,
product version, last call home data, last scan date, scan count, total number of
projects, managed code base size in GB, number of code locations, total user count,
hard limit of total projects authorized by the license, hard limit of total users
authorized by the license, hard limit of codebase size authorized by the license,
total memory being used by the Black Duck server, number of CPUs being used by the
Black Duck server, and the expiration date of the license.

## KnowledgeBase services

Via web services, the Black Duck KB provides the Black Duck application with the most up-to-date information about
open source software without requiring regular updates on your Black Duck server. New vulnerability data is added to the KB
hourly; new searchable open source components are added daily; and new signatures
for matching are added 2-3 times per week. Other big data services are updated
quarterly.

  
 [image: KnowledgeBase services]   

The signatures of your scanned code are used to match signatures of the open source
software in the KB to identify the open source software contained in your code.
These signatures consist of one-way, encrypted MD5 or SHA1 hashes of file system
meta-data and file content. The use of MD5/SHA-1 is purely for signature hashing and
is not used for any cryptographic purpose. These signatures (collections and hashes)
are sent by the Black Duck application to the KB service. The
signatures are formatted as a JSON document and transmitted over HTTPS connections.
The scan document can send file paths, file sizes, and some SHA-1 or clean SHA-1
signatures to the Black Duck server. Black Duck does post-processing on this data to
create additional proprietary signatures.

As mentioned previously, if file/path information is not desired to be uploaded from
the Black Duck server to the Black Duck KnowledgeBase, you can contact Black Duck
Support to disable this feature. Note that not sending the file and path names can
lead to inexact component matching and a poorer quality BOM; therefore, this feature
is on by default.

The matching service is described in more detail below.

### Match service overview

The client POSTs a JSON document representing a tree structure of scanned nodes,
with a set of signatures per node to the match endpoint. The endpoint determines
if there are any matches to those signatures. If there are, it returns a JSON
document with the same nodes that were sent to the match service, and adds to
the document the matches from the KB for each node.

### URL format

https://<server>/kbmatch/api/v1/matches/<end-point>

### Header

X-BDS-AuthToken:<>

### Request body data

[image: Request body data]

### Response

[image: Response]   

As can be seen from the example, matching open source components are returned to
the Black Duck application using GUIDs. These GUIDs are then
used to retrieve metadata on each of the open source components using KB
services for vulnerabilities, licenses, and other information.

### KB feedback service

In the same way that signatures and hashes are sent up to the match service,
occasionally these same pieces of information will be sent associated with a
specific component and version. This is done in cases where users have corrected
(“adjusted”) an identification. This “vote” is recorded absent any customer
context whatsoever, and is used simply to increase the accuracy of the matching
capability. However, if it is desired to not share this data, customers can work
with Black Duck support to disable this feature.

## Black Duck Hosted Customer Instances Monitors

In the Black Duck Black Duck Hosted environment, there are monitors and alerts enabled
for each instance.

For monitoring, we are gathering the data on this metric and store it for a period of
time. This data can be used for later analysis. There may be thresholds in which
informational messages are dispatched, but a response is not required or triggered
for these types of monitors.

Examples of scenarios we monitor are Daily Scans and Job Instances which provide
useful metrics when issue analysis is being investigate by CloudOps and/or
Support.

For alerting notifications, we are monitoring the metrics with thresholds. There are
low and high level thresholds which may be adjusted based on reviews of Black Duck
Performance Testing Lab or changes to Black Duck functionality. Low levels do not
require an immediate response. High levels require an immediate response. When a
certain threshold is crossed, the CloudOps team is paged via our paging system. A
technical support ticket MAY be opened depending on the alert, and how many times we
have notified technical support. The Technical Support team troubleshoots the issue
and informs the customer of the issue while it is being investigated.

Examples of types of alerts that trigger Support tickets are: Database CPU
utilization hitting the high threshold which usually indicates that the customer is
performing actions which are heavily impacting the database which could cause the
instance to require rebooting or resizing. Pod Readiness is monitored which
indicates that a pod has been running, but that it is not ready to process requests.
When it taken too long for it to come online an alert is triggered to check the
instance
