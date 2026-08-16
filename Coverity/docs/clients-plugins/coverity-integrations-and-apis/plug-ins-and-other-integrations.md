---
title: "Plug-ins and other integrations"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/plug-ins-and-other-integrations.html"
content_id: "uS5t53b0WJpv4TvM5UCZfA"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:45:41.399247+00:00"
---

# Plug-ins and other integrations

Plug-ins are the easiest way to integrate testing into your CI/CD pipeline. We recommend
using the CI/CD plug-in integrations derived from the Bridge CLI. Support for Coverity-based plug-ins has been
deprecated and will be removed in a future release. Please see the following sections
for details about all available CI/CD plug-ins.

## Bridge-based CI/CD plug-ins

Our newest plug-ins have the Bridge CLI client
under the hood, so you get the same benefits without writing the code.

You can use the Bridge CI/CD plug-ins with any of
the following products or with a combination of them: Black Duck® SCA, Coverity, Polaris, or Software Risk Manager.

Capabilities include:

- SAST and SCA scanning;
- Scan in synchronous or asynchronous (non-blocking) mode;
- Scan whenever new code is merged to a branch;
- Scan whenever a pull request is created or updated;
- Decorate pull requests with comments;
- Create automatic pull requests for new fixes ("Fix PRs") - Black Duck® SCA only;
- Generate a SARIF file;
- Post results to SCM (GitHub advanced security);
- Post results to any supported server (see the list of products above);

- Make issues available in your instance of Black Duck® SCA, Coverity, Polaris, or
  Software Risk Manager;
- Fail the build in your CI system when a high-severity issue is found.

Bridge plug-ins are available on the following
platforms: Azure, GitHub, GitLab, Jenkins. They can be used with Coverity Connect,
as well with Coverity deployed in the cloud. On push events, a full Coverity scan
will be run and results are committed to the Coverity server database. On pull
request events, comments are added to pull requests for new issues found by the scan
if a certain property or environment variable (depending on the plug-in) is set to
`true`. Note that scan results are not committed to Coverity
server database in this case.

Note: We recommend automating
with the Bridge-based plug-ins, because they are the best way to get access to
newer features and they provide a common interface for all our products.

Some
customers rely on the product-specific integrations, and If you happen to be
looking for information about those, they can be found at these
links.

**Azure**

See [Using the Black Duck Security Scan Plugin with Coverity](https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/quickstart-azure-with-coverity.html)
on the documentation portal.

**GitHub**

See [Using the Black Duck Security Scan Plugin with Coverity](https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/using-the-github-app-with-coverity.html) on the documentation portal.

**GitLab**

See [Using the Black Duck Security Scan Plugin with Coverity](https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/quickstart-gitlab-template-with-coverity.html) on the documentation portal.

**Jenkins**

See [Using the Black Duck Security Scan Plugin with Coverity](https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/using-black-duck-security-scan-pipe-for-coverity.html) on the documentation portal.
