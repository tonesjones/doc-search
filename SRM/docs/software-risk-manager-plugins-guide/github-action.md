---
title: "GitHub Action"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/github-action.html"
content_id: "bqNsU96oR1F7SJvFhmKUaQ"
version: "latest"
section: "Software Risk Manager Plugins Guide"
scraped_at: "2026-09-08T20:06:09.608321+00:00"
content_hash: "664fb2c6077955585d037c988cb42a45e9be57f15d841c307e2dd486236d8f29"
---

# GitHub Action

The Software Risk Manager [GitHub Action](https://github.com/marketplace/actions/srm-analysis) enables an Action workflow to upload files and
initiate a scan with your Software Risk Manager server.

A Software Risk Manager project and an API key or
PAT are required. It must have the `create`
role for the project.

The Action can be used on any [Runner machine type](https://docs.github.com/en/actions/learn-github-actions/workflow-syntax-for-github-actions#jobsjob_idruns-on). The machine should have
access to your Software Risk Manager server. If Software Risk Manager is inaccessible to
public traffic, we recommend using a [Self-Hosted Runner](https://docs.github.com/en/actions/hosting-your-own-runners/about-self-hosted-runners) to run the action.

Instructions for installation and configuration can be found on the Marketplace listing
and the [GitHub repository](https://github.com/codedx/codedx-github-action). This plugin is open source and we welcome
community involvement.
