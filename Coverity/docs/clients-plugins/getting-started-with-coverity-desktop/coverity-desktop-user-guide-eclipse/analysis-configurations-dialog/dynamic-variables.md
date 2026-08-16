---
title: "Dynamic variables"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/dynamic-variables.html"
content_id: "yEshmAP97BTumHd6Z4cCLg"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:48:19.302702+00:00"
---

# Dynamic variables

The following variables are supported in the Coverity Desktop UI:

- ${env_var:ANY_ENVIRONMENT_VARIABLE_NAME}
  - Substitutes corresponding environment variables.
- ${workspace_loc} - Substitutes the location of the IDE workspace.
- ${cov-inter-dir} - The full path to intermediate directory.
  For example:

  /home/me/workspace/.metadata/coverity/idir
- ${cov-im-user} - The Coverity Connect
  username.
- ${cov-im-password} - The Coverity Connect
  password.
- ${cov-im-host} - The Coverity Connect host
  name.
- ${cov-im-port} - The Coverity Connect data
  port.
- ${cov-im-auth-key} - The full path to the Coverity Connect authentication key file.
- ${cov-sa-bin} - The full path of the Coverity Static
  analysis /bin directory. For example:

  <install_dir>/bin
