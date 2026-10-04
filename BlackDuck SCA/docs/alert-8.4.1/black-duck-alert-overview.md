---
title: "Black Duck Alert Overview"
source_url: "https://docs.blackduck.com/r/alert/8.4.1/black-duck-alert-user-guide/black-duck-alert-overview.html"
content_id: "D5jJkGFn8zSJUw2hhpKhAA"
version: "8.4.1"
section: "Black Duck Alert Overview"
scraped_at: "2026-10-04T23:29:43.637672+00:00"
content_hash: "43a104cf58d73c38f567538fcf63afdb72ad0b08de6f610e0fc623d8bd04f45d"
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
