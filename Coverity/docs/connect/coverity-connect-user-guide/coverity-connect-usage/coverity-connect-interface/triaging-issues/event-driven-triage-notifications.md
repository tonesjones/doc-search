---
title: "Event-driven triage notifications"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/event-driven-triage-notifications.html"
content_id: "IVnivNfe0WCIar83orwivQ"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:47:00.129671+00:00"
---

# Event-driven triage notifications

The administrator can use event-driven triage notifications to send notifications to
issue owners about all triage event changes as they happen. These notifications are
filterable and configurable. Even driven notifications do not replace existing
notification systems.

This feature is not enabled by default. Once enabled, notifications are sent to Apache
Kafka servers provided and configured by the user to consume these events. The user can
then subscribe to these notifications using technology provided by Kafka. Users can
decide what to do with the notifications they consume: for example, they can use them to
send email or instant messenger notifications, or process them in any other way.

Triage events can originate from the following operations:

- Updating triage in the Coverity Connect UI.
- Updating triage using Web Services requests.
- Triage updates at commit time.

Triage events do not originate from importing or exporting a triage store, or from associating
triage stores with streams or de-associating triage stores from streams.

For each triaged issue, the triage event is sent to the consumer in the following JSON
format:

```
{   
    version: 1,    
    cid: 10001,    
    owner: "Mike",    
    email: "mike@example.com",    
    urls: ["issue-url-1", "issue-url-2"],
    timestamp: "2019-10-10T17:01:28.111+0000",    
    triage-attribute-changes: [
    {
        "triage-attribute-name": "classification",
        "triage-attribute-value": "Pending"
    },
    ...] 
}
```

The fields are described in the following table.

| Field | Meaning |
| --- | --- |
| cid | CID of the triaged issue |
| owner | Owner of the issue |
| email | Email of the issue owner |
| urls | List of links with all stream-defects affected by the triage event. The same CID may be present in different streams in different projects; the links will point to all occurrences of such a CID. |
| timestamp | The time when triage happened |
| triage-attribute changes | A list of the changed triage attributes and their new values. |

The basic workflow for setting up event-driven triage notifications is the following:

1. Set up an Apache Kafka server and set up a triage-events topic
   to receive triage event notifications.

   If this topic is missing triage event notifications will fail.
2. Enable triage event notifications using the
   eventstriage.enabled property in the
   cim.properties file:

   ```
   events.triage.enabled=true
   ```
3. Specify the Kafka servers that have been configured to receive triage events. Use
   the following syntax:

   ```
   events.triage.kafka.bootstrapServers=<server1>, <server2>, ...
   ```

   Notifications can be lost if the consumer is unavailable to Coverity Connect.
   Events are delivered on an *at least once* basis. This means that duplicate
   events might sometimes be delivered by Kafka. The user is responsible for
   filtering or tolerating duplicate messages.

Note: In a Coverity Connect cluster, only the nodes with properly configured triage events
notifications will send the notifications to Kafka. The notification is sent by the node
where the triage event happens.
