---
title: "Introduction to analyses within a Kubernetes cluster in the Cloud"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/introduction-to-analyses-within-a-kubernetes-cluster-in-the-cloud.html"
content_id: "wR3auvwkpwJ9RFEnl4dMWw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:32:26.353535+00:00"
---

# Introduction to analyses within a Kubernetes cluster in the Cloud

With a Coverity cloud deployment, you can run your Coverity
analyses within a Kubernetes cluster in the Cloud. This allows you to offload
computationally expensive analyses to Cloud-based compute resources. If you use the Thin
Client, you also have the benefit of a reduced installation size and footprint. This is
because the Thin Client provides a subset of Coverity Analysis tools
that includes only tools needed to capture the source code to be analyzed. The Thin
Client is considerably smaller than a non-Cloud Coverity Analysis
installation, which makes it suitable for use in a CI/CD build pipeline, especially if
you are using temporary containers for your builds.

Note: When you use the Coverity CLI, there is no difference between the workflows
available with a Coverity cloud deployment as opposed to traditional
Coverity workflows.

Using the Thin Client has the following limitations:

- You must use a build command to capture projects that use built sources, such as Java or C#.
  If you do not use a build command, the Coverity CLI will attempt to infer a build
  command. If the inference fails, the capture will fail.
- Analyses are performed by only the Coverity Scan Service since the Thin Client does not have
  the tools needed to do a local analysis.

To perform an analysis in the Cloud:

1. Create the project and stream to use in Coverity Connect.
   This is typically a one-time step.
2. Decide how to configure the Coverity CLI. You can either generate a configuration file or use
   environment variables.
3. Capture and analyze the project.
