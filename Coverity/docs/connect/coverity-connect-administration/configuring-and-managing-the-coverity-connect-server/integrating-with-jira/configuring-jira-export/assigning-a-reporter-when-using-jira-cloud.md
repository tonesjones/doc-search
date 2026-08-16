---
title: "Assigning a Reporter when using Jira Cloud"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/assigning-a-reporter-when-using-jira-cloud.html"
content_id: "Tixo4gDtGVRI75U8XJwqsQ"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:48:17.689041+00:00"
---

# Assigning a Reporter when using Jira Cloud

When you assign the Reporter field while using Jira Cloud, the
behavior is as follows:

- If the choice is Coverity Connect Field, then if the user
  exists, the issue is created successfully. If the user *does not* exist,
  the issue is created but the Reporter is set to the value
  of Default Assignee (the Default
  Assignee is specified in the Jira Cloud project
  settings).
- If the choice is Constant, then if the user exists, the
  issue is created successfully.

  CAUTION:

  If the choice is Constant but the user
  does not exist, the issue *is not created,* and Coverity Connect reports an
  error.
