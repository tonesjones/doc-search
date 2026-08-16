---
title: "Introducing Sigma"
source_url: "https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/introducing-sigma.html"
content_id: "LazckaOTKq9k1AfQEhPtKw"
version: "2026.8.0"
section: "Sigma User Guide"
scraped_at: "2026-08-13T00:25:02.348192+00:00"
---

# Introducing Sigma

Sigma is a fast and easy-to-use static analysis scanner that fits seamlessly into modern
development systems. It is an ideal solution for rapidly evolving projects, for cloud
adopters, and for those who are just starting their application security journey and
need to assess their code without a major investment of time and resources.

Note: Sigma is the engine powering the
Rapid Scan Static feature. Throughout the documentation,
*(Black Duck) Rapid Scan Static*
refers to the Sigma tool.

*Static analysis* is a type of analysis that allows you to test code early and to
correct problems before they become entrenched and costly to fix. Static analysis tests
every possible path through your code, which would be impossible to do by means of
dynamic test coverage.

Sigma analyzes your code using small components called *checkers*, which are the
foot soldiers of analysis. Each checker looks for a specific type of issue, which can
range in severity from the informative to the critical. Each checker contains multiple
checks. For example, the `access_control_disable` checker contains
individual checks for AWS SDK, Postgres, and Open API. When the check finds an issue, it
displays remediation advice that you can use to resolve the problem. Remediation
information is included in a Sigma results file that can be displayed in any system that
consumes the results, such as Polaris or any system that consumes the SARIF format.

In addition, you can define policies that align the development process with security
concerns. Using these policies, when Sigma finds issues that violate policy rules, it
fails the build and allows you to resolve the issues before proceeding.

For best overall results, we recommend running Sigma as a Rapid Scan via Polaris, in
combination with a (typically less frequent) Full Scan. A Full Scan includes a Rapid
Scan, and additionally runs a Coverity scan. These scans complement each other and allow
you to check your code at various stages of development:

- The Rapid Scan offers broad but shallow coverage with fast updates. You can run
  ultra-light fast scans on every commit.
- The Full Scan offers a more in-depth but more time-consuming analysis.

Having uncovered the more straightforward issues with Rapid Scans, you can run a nightly
or weekly Full Scan to go deeper and identify more complex issues.

## Sigma CLI

Use the sigma command to scan code, to define policy, to get
information, and to configure your scans. Note though that most customization can be
done by setting environment variables.

You can use the sigma command from the command line or you can embed
it in your CI/CD pipeline to scan code or to act as a quality gate.

For example, to scan code:

```
sigma analyze
```

To list available checkers and associated checks, including information about
languages, CWEs, severity and enablement:

```
sigma checkers
```

## Sigma Checks

Sigma supports hundreds of checks that identify issues in your code and return
diagnostic and remediation advice.

To get more information about a particular check or checker, use this command.

```
sigma explain <check_name>|<checker_name>
```

Each check:

- is enabled or disabled
- supports one or more languages
- has an associated severity level

You can configure Sigma to change the enablement status and the severity level of
checks.

## Basic Use Cases

You can run Sigma in the following ways:

- From the command line on a Linux, Mac, or Windows platform.
- As a Rapid Scan on Polaris.
- In a CI/CD pipeline.
- As a quality gate in a continuous integration job.

  You can configure a policy to ensure that certain conditions are met for the
  build to succeed. These conditions might relate to the specific issues found
  or to their severity.

## Basic Workflows

**To run Sigma on the command line:**

1. Download Sigma.

   See Downloading Sigma.
2. Configure if needed.

   See Configuring Sigma.
3. Scan code.

   See the analyze subcommand and the sections on GitHub
   and GitLab integrations.
4. Look at scan results.

   See Configuring Sigma Output.
5. Remediate or dismiss issues.

**To run Sigma as a Rapid Scan on Polaris:**

1. Configure if needed.

   See Configuring Sigma.
2. Set a policy, if desired.

   See [The Policies page](https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/the-policies-page.html).
3. Scan code.

   See [How to test from the web UI](https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/how-to-test-from-the-web-ui.html).
   To use Bridge CLI, see [Using Bridge CLI with
   Polaris](https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/using-bridge-cli-with-polaris.html).
4. Look at results by navigating to the [dashboards](https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/the-dashboards-page.html) and [reports](https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/the-reporting-page.html) .
5. Remediate or dismiss issues.

**To run Sigma in a CI/CD pipeline:**

1. Download Sigma.

   See Downloading Sigma.
2. Upload Sigma to a location the CI/CD tool can access.
3. Configure if needed.

   See Configuring Sigma.
4. Create your CI/CD job templates to use the URL to the download the
   binary, or pull the docker image for Sigma and run it.
5. If you're planning to use Sigma as a quality gate, define the policy to
   use. For more information, see Using Policies to Define a Quality Gate.
6. Look at scan results.

   See Configuring Sigma Output.
7. Remediate or dismiss issues.
