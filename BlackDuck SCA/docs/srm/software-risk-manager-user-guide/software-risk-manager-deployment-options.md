---
title: "Software Risk Manager Deployment Options"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/software-risk-manager-deployment-options.html"
content_id: "BxibpVzfLJhG8GwNymIvdQ"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:02:48.389510+00:00"
content_hash: "510ae715bbb9deffdc24ed15c6bbe1c7eb997a9f6bedc6d177277f43acd64f28"
---

# Software Risk Manager Deployment Options

Software Risk Manager has several deployment options, depending on your AppSec
environment and requirements. The most common SRM deployment options are as follows:

- Data aggregation
- Tool orchestration (requires the SRM Tool Orchestration module deployed on
  Kubernetes)
- SRM coupled with SAST (requires the SRM Scan Farm module deployed on
  Kubernetes)
- SRM coupled with SCA (requires the SRM Scan Farm module deployed on
  Kubernetes)
- SRM coupled with SAST and SCA (requires the SRM Scan Farm module deployed on
  Kubernetes)

## Data Aggregation from Multiple Sources

Software Risk Manager supports a large and growing list of tool connectors that can
be used to collect and aggregate data from multiple sources. In addition to
providing risk assessment detail for each finding, SRM provides policy violation
management, dashboards, and a host of other features. For this deployment option,
SRM is installed as a standalone product in a Windows or Linux environment.

## Data Aggregation with Tool Orchestration

SRM with tool orchestration enables AppSec teams to build their own custom pipeline
and orchestrate all scanning from a central location. If a required tool isn't
currently supported, SRM allows teams to configure any commercial or open source
tool to work with SRM. This option requires the SRM Tool Orchestration module and a
Kubernetes deployment.

## Software Risk Manager Coupled with SAST

This deployment option allows teams to run Coverity (SAST) scans seamlessly with SRM.
This option requires the SRM Scan Farm module deployed on Kubernetes.

## Software Risk Manager Coupled with SCA

This deployment option allows teams to run Black Duck (SCA) scans seamlessly with
SRM. This option requires the SRM Scan Farm module deployed on Kubernetes.

## Software Risk Manager Coupled with SAST and SCA

This deployment option allows teams to run Coverity (SAST) and Black Duck (SCA) scans
seamlessly with SRM. This option requires the SRM Scan Farm module deployed on
Kubernetes.
