---
title: "Configuring a Build Agent"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/configuring-a-build-agent.html"
content_id: "UaGVhgvXVneNs3kcraJu5g"
version: "11.5.1"
section: "Detect Integrations"
scraped_at: "2026-08-08T23:46:10.161950+00:00"
---

# Configuring a Build Agent

To configure a build agent in your pipeline do the following under the **Tasks** tab on your pipeline page.

The default option for the build agent is the Microsoft hosted agent. To be able to select a self-hosted agent, you must have installed the agent and ensure that it's available to your project before you can use it in your pipeline. Click the ellipsis (**…**) next to Pipeline to Add an agent job.

- Click the ellipsis (**…**) next to Pipeline to Add an agent job.

  Figure 1. Configuring an Agent
  [image: Configuring an Agent]

- On the Agent job configuration screen, do the following:

  - Select a self-hosted agent from your Agent pool or select Azure Pipelines for an Azure-hosted agent.
  - If you select a hosted agent, then you must select an operating system such as macOS, Windows, or a version of Linux for the hosted agent VM.

Tip: This is not an air gap option as internet connections are still required for downloading other tools and the script will still download new content if needed.

Note: If the agent is behind a proxy, Detect Azure plug-in will utilize the agent proxy by default.

## Configuring with a proxy

You can configure the build agent for Detect Azure Plugin to use a proxy when running jobs.

### Proxy configuration scenarios

- If both an agent proxy and Black Duck SCA Poxy Service Endpoint are set through ADO Plugin parameter, the Black Duck SCA proxy url endpoint takes precedence.
- If agent proxy is configured, and the Black Duck SCA Poxy Service Endpoint is not set through ADO Plugin parameter, the Detect Azure Plugin utilizes the agent proxy.
