---
title: "Designating a stream for auto-deletion of expired streams"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/designating-a-stream-for-auto-deletion-of-expired-streams.html"
content_id: "BBzHxXc6efOqnTRLDuPlyQ"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:50:07.079978+00:00"
---

# Designating a stream for auto-deletion of expired streams

Coverity Connect can automatically delete streams after a period of inactivity. Only
streams that are specifically configured for this feature are eligible for automatic
deletion. Streams can opt in to automatic deletion in one of two ways:

1. The Coverity Desktop plug-ins for Eclipse and Visual Studio create private
   streams, and these private streams are configured for automatic
   deletion.
2. Other streams can be configured for automatic deletion using Web Services
   API.

The configuration parameter which enables automatic deletion is only visible via Web
Services. Every night, Coverity Connect deletes streams which meet all of the following
criteria:

- The stream must be configured for automatic deletion, with the Web Services API
  setting `autoDeleteOnExpiry=true`.
- The stream must have at least one snapshot in it (it must have commit
  data).
- The stream must not have any snapshots (commits) within the last 28
  days.

Streams meeting all three criteria will be deleted automatically. The Coverity Connect
log will record each stream deleted.

To configure a stream for automatic deletion, the value
`autoDeleteOnExpiry` must be set to true in the
`StreamSpecDataObj` passed to the
`ConfigurationService` operation `createStream`,
`createStreamInProject`, or `updateStream`. See the
Coverity Platform 2026.6.0 SOAP Web Services API Reference for details on how to access the
SOAP web services.

The inactivity threshold is also configurable, by adding a line to
`cim.properties`. The property name is
`stream.expiration.inactivity.days`, and the value is specified in
days. For example, to set the inactivity threshold to 60 days, add the following
line:

`stream.expiration.inactivity.days=60`

The default value of 28 days is used if the property is not specified. The Stream Expiry
feature can be turned off entirely by setting the inactivity threshold to 0; with this
setting Coverity Connect will never delete streams automatically, even if they meet all
3 criteria for automatic deletion.

When copying a stream, either through Web Services or through the
Duplicate button in the UI, the hidden stream setting that
controls whether the stream should be deleted automatically is not preserved. The copied
stream will have this setting turned off.
