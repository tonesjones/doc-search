---
title: "Black Duck Alert Overview"
source_url: "https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/black-duck-alert-overview.html"
content_id: "37F7MAlUmA9EJ4RshMEPew"
version: "8.4.0"
section: "Black Duck Alert Overview"
scraped_at: "2026-08-08T23:46:14.417533+00:00"
---

# Black Duck Alert Overview

Alert enables you to receive Black Duck SCA notifications via a number of commonly used
distribution channels, such as email, Slack, Azure Boards, and Jira.

Alert is a web application with a user interface that runs in a browser. It can be
orchestrated as part of, and runs in parallel with, your Black Duck SCA deployment. Alert
runs as its own application, so logging into Black Duck SCA is not required to use it.

After configuring your Black Duck SCA provider and notification channels in Alert, users with
the administrator or job manager role can create distribution jobs that determine how
the notifications are sent from Black Duck to the various Alert channels.

## How Alert works

After Alert is configured, it runs continuously in the background receiving
notifications from Black Duck SCA and delivering those notifications to configured
recipients using the configured channels. Administrators can verify the successful
sending of notifications through the Alert Audit screen.

Figure 1. High Level Architecture
[image: High Level Architecture]

## About Alert

Figure 2. About Alert
[image: About Alert]
