# Sigma Documentation Documentation Index

> Auto-generated catalog for local RAG. Do not hand-edit topic rows — update `sources/sigma-2026.8.0/manifest.json` statuses and run `python scripts/build-index.py --product sigma-2026.8.0`.

## Corpus status

| Field | Value |
|-------|-------|
| Product | Sigma Documentation |
| Product key | `sigma-2026.8.0` |
| Version | **2026.8.0** |
| Map ID | `S_R7XSLfKPN3q6kGpp1eHQ` |
| TOC nodes | **59** |
| Progress | **59/59 done** (100.0%) · 0 pending · 0 skipped · 0 error |
| Last index build | 2026-08-13T00:25:46.970146+00:00 |
| Manifest | [sources/sigma-2026.8.0/manifest.json](sources/sigma-2026.8.0/manifest.json) |
| Raw TOC | [sources/sigma-2026.8.0/toc.json](sources/sigma-2026.8.0/toc.json) |

### Status legend

| Mark | Status | Meaning |
|------|--------|---------|
| `[ ]` | pending | Not scraped yet |
| `[x]` | done | Markdown written under `docs/` |
| `[-]` | skipped | Intentionally not scraped |
| `[!]` | error | Last scrape failed; retry later |

## How to resume

1. Filter `manifest.json` for `status` `pending` (or `error` to retry).
2. `python scripts/scrape-pending.py --product sigma-2026.8.0 --all-pending`
3. `python scripts/build-index.py --product sigma-2026.8.0` to refresh this index.

**Content API template:**

```
https://docs.blackduck.com/api/khub/maps/S_R7XSLfKPN3q6kGpp1eHQ/topics/{contentId}/content
```

## Section overview

| Section | Topics | Pending | Done | Skipped | Error | Local root |
|---------|--------|---------|------|---------|-------|------------|
| Sigma User Guide | 59 | 0 | 59 | 0 | 0 | `docs/user-guide/` |

## Table of contents

- [x] [Sigma User Guide](docs/user-guide/sigma-user-guide.md) _(+8)_ · [source](https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/sigma-user-guide.html)
  - [x] [Introducing Sigma](docs/user-guide/introducing-sigma.md) · [source](https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/introducing-sigma.html)
  - [x] [Downloading Sigma](docs/user-guide/downloading-sigma.md) _(+2)_ · [source](https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/downloading-sigma.html)
    - [x] [Getting the Binary](docs/user-guide/downloading-sigma/getting-the-binary.md) · [source](https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/getting-the-binary.html)
    - [x] [Getting the Docker Image](docs/user-guide/downloading-sigma/getting-the-docker-image.md) · [source](https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/getting-the-docker-image.html)
  - [x] [Configuring Sigma](docs/user-guide/configuring-sigma.md) _(+9)_ · [source](https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/configuring-sigma.html)
    - [x] [Configuring the AI-augmented SAST checker plug-in](docs/user-guide/configuring-sigma/configuring-the-ai-augmented-sast-checker-plug-in.md) · [source](https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/configuring-the-ai-augmented-sast-checker-plug-in.html)
    - [x] [Security considerations for the AI-augmented SAST checker plug-in](docs/user-guide/configuring-sigma/security-considerations-for-the-ai-augmented-sast-checker-plug-in.md) · [source](https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/security-considerations-for-the-ai-augmented-sast-checker-plug-in.html)
    - [x] [Configuration Methods and Precedence](docs/user-guide/configuring-sigma/configuration-methods-and-precedence.md) · [source](https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/configuration-methods-and-precedence.html)
    - [x] [Configuration Options](docs/user-guide/configuring-sigma/configuration-options.md) · [source](https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/configuration-options.html)
    - [x] [Configuring Sigma Output](docs/user-guide/configuring-sigma/configuring-sigma-output.md) · [source](https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/configuring-sigma-output.html)
    - [x] [Configuring Sigma with coverity.yml](docs/user-guide/configuring-sigma/configuring-sigma-with-coverity-yml.md) · [source](https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/configuring-sigma-with-coverity.yml.html)
    - [x] [Configuring Sigma with .sigma-config.yml](docs/user-guide/configuring-sigma/configuring-sigma-with-sigma-config-yml.md) _(+2)_ · [source](https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/configuring-sigma-with-.sigma-config.yml.html)
      - [x] [Creating a Default Configuration](docs/user-guide/configuring-sigma/configuring-sigma-with-sigma-config-yml/creating-a-default-configuration.md) · [source](https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/creating-a-default-configuration.html)
      - [x] [Customizing Check Attributes](docs/user-guide/configuring-sigma/configuring-sigma-with-sigma-config-yml/customizing-check-attributes.md) _(+2)_ · [source](https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/customizing-check-attributes.html)
        - [x] [Overriding Severity Levels](docs/user-guide/configuring-sigma/configuring-sigma-with-sigma-config-yml/customizing-check-attributes/overriding-severity-levels.md) · [source](https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/overriding-severity-levels.html)
        - [x] [Using the Configuration File to Specify Overrides](docs/user-guide/configuring-sigma/configuring-sigma-with-sigma-config-yml/customizing-check-attributes/using-the-configuration-file-to-specify-overrides.md) · [source](https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/using-the-configuration-file-to-specify-overrides.html)
    - [x] [Environment Variables](docs/user-guide/configuring-sigma/environment-variables.md) · [source](https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/environment-variables.html)
    - [x] [Using a Configuration File in a CI/CD Pipeline](docs/user-guide/configuring-sigma/using-a-configuration-file-in-a-ci-cd-pipeline.md) · [source](https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/using-a-configuration-file-in-a-ci/cd-pipeline.html)
  - [x] [Running Sigma in CI/CD](docs/user-guide/running-sigma-in-ci-cd.md) _(+2)_ · [source](https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/running-sigma-in-ci/cd.html)
    - [x] [Using the Black Duck Rapid Scan Static Jenkins Plugin](docs/user-guide/running-sigma-in-ci-cd/using-the-black-duck-rapid-scan-static-jenkins-plugin.md) _(+5)_ · [source](https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/using-the-black-duck-rapid-scan-static-jenkins-plugin.html)
      - [x] [Installing the Black Duck Rapid Scan Static Jenkins Plugin for Sigma](docs/user-guide/running-sigma-in-ci-cd/using-the-black-duck-rapid-scan-static-jenkins-plugin/installing-the-black-duck-rapid-scan-static-jenkins-plugin-for-sigma.md) · [source](https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/installing-the-black-duck-rapid-scan-static-jenkins-plugin-for-sigma.html)
      - [x] [Configuring Sigma as a Jenkins Tool](docs/user-guide/running-sigma-in-ci-cd/using-the-black-duck-rapid-scan-static-jenkins-plugin/configuring-sigma-as-a-jenkins-tool.md) _(+2)_ · [source](https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/configuring-sigma-as-a-jenkins-tool.html)
        - [x] [Installing and Updating Sigma Automatically](docs/user-guide/running-sigma-in-ci-cd/using-the-black-duck-rapid-scan-static-jenkins-plugin/configuring-sigma-as-a-jenkins-tool/installing-and-updating-sigma-automatically.md) · [source](https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/installing-and-updating-sigma-automatically.html)
        - [x] [Installing Sigma Manually](docs/user-guide/running-sigma-in-ci-cd/using-the-black-duck-rapid-scan-static-jenkins-plugin/configuring-sigma-as-a-jenkins-tool/installing-sigma-manually.md) · [source](https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/installing-sigma-manually.html)
      - [x] [Working with a Jenkins Freestyle Project](docs/user-guide/running-sigma-in-ci-cd/using-the-black-duck-rapid-scan-static-jenkins-plugin/working-with-a-jenkins-freestyle-project.md) _(+7)_ · [source](https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/working-with-a-jenkins-freestyle-project.html)
        - [x] [Defining a Freestyle Project for Using Sigma as a Quality Gate](docs/user-guide/running-sigma-in-ci-cd/using-the-black-duck-rapid-scan-static-jenkins-plugin/working-with-a-jenkins-freestyle-project/defining-a-freestyle-project-for-using-sigma-as-a-quality-gate.md) · [source](https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/defining-a-freestyle-project-for-using-sigma-as-a-quality-gate.html)
        - [x] [Defining a Freestyle Project for Using Sigma to Report Issues](docs/user-guide/running-sigma-in-ci-cd/using-the-black-duck-rapid-scan-static-jenkins-plugin/working-with-a-jenkins-freestyle-project/defining-a-freestyle-project-for-using-sigma-to-report-issues.md) · [source](https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/defining-a-freestyle-project-for-using-sigma-to-report-issues.html)
        - [x] [Controlling How Sigma Executes](docs/user-guide/running-sigma-in-ci-cd/using-the-black-duck-rapid-scan-static-jenkins-plugin/working-with-a-jenkins-freestyle-project/controlling-how-sigma-executes.md) · [source](https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/controlling-how-sigma-executes.html)
        - [x] [Adding Sigma Configuration Files](docs/user-guide/running-sigma-in-ci-cd/using-the-black-duck-rapid-scan-static-jenkins-plugin/working-with-a-jenkins-freestyle-project/adding-sigma-configuration-files.md) · [source](https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/adding-sigma-configuration-files.html)
        - [x] [Setting Sigma Policy Files](docs/user-guide/running-sigma-in-ci-cd/using-the-black-duck-rapid-scan-static-jenkins-plugin/working-with-a-jenkins-freestyle-project/setting-sigma-policy-files.md) · [source](https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/setting-sigma-policy-files.html)
        - [x] [Recording Issues](docs/user-guide/running-sigma-in-ci-cd/using-the-black-duck-rapid-scan-static-jenkins-plugin/working-with-a-jenkins-freestyle-project/recording-issues.md) · [source](https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/recording-issues.html)
        - [x] [Executing Other Sigma Commands](docs/user-guide/running-sigma-in-ci-cd/using-the-black-duck-rapid-scan-static-jenkins-plugin/working-with-a-jenkins-freestyle-project/executing-other-sigma-commands.md) · [source](https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/executing-other-sigma-commands.html)
      - [x] [Working with a Jenkins Pipeline](docs/user-guide/running-sigma-in-ci-cd/using-the-black-duck-rapid-scan-static-jenkins-plugin/working-with-a-jenkins-pipeline.md) _(+3)_ · [source](https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/working-with-a-jenkins-pipeline.html)
        - [x] [Defining a Jenkins Pipeline](docs/user-guide/running-sigma-in-ci-cd/using-the-black-duck-rapid-scan-static-jenkins-plugin/working-with-a-jenkins-pipeline/defining-a-jenkins-pipeline.md) · [source](https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/defining-a-jenkins-pipeline.html)
        - [x] [Configuring a Scripted Pipeline](docs/user-guide/running-sigma-in-ci-cd/using-the-black-duck-rapid-scan-static-jenkins-plugin/working-with-a-jenkins-pipeline/configuring-a-scripted-pipeline.md) · [source](https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/configuring-a-scripted-pipeline.html)
        - [x] [Configuring a Declarative Pipeline](docs/user-guide/running-sigma-in-ci-cd/using-the-black-duck-rapid-scan-static-jenkins-plugin/working-with-a-jenkins-pipeline/configuring-a-declarative-pipeline.md) · [source](https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/configuring-a-declarative-pipeline.html)
      - [x] [Viewing Sigma Issues Reports](docs/user-guide/running-sigma-in-ci-cd/using-the-black-duck-rapid-scan-static-jenkins-plugin/viewing-sigma-issues-reports.md) · [source](https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/viewing-sigma-issues-reports.html)
    - [x] [Using Policies to Define a Quality Gate](docs/user-guide/running-sigma-in-ci-cd/using-policies-to-define-a-quality-gate.md) _(+3)_ · [source](https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/using-policies-to-define-a-quality-gate.html)
      - [x] [Structure of the Policy File](docs/user-guide/running-sigma-in-ci-cd/using-policies-to-define-a-quality-gate/structure-of-the-policy-file.md) _(+2)_ · [source](https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/structure-of-the-policy-file.html)
        - [x] [The when Node](docs/user-guide/running-sigma-in-ci-cd/using-policies-to-define-a-quality-gate/structure-of-the-policy-file/the-when-node.md) · [source](https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/the-when-node.html)
        - [x] [The result Node](docs/user-guide/running-sigma-in-ci-cd/using-policies-to-define-a-quality-gate/structure-of-the-policy-file/the-result-node.md) · [source](https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/the-result-node.html)
      - [x] [Policy Examples](docs/user-guide/running-sigma-in-ci-cd/using-policies-to-define-a-quality-gate/policy-examples.md) · [source](https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/policy-examples.html)
      - [x] [Policy Violations Output](docs/user-guide/running-sigma-in-ci-cd/using-policies-to-define-a-quality-gate/policy-violations-output.md) · [source](https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/policy-violations-output.html)
  - [x] [Command Reference](docs/user-guide/command-reference.md) _(+7)_ · [source](https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/command-reference.html)
    - [x] [The sigma Command](docs/user-guide/command-reference/the-sigma-command.md) · [source](https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/the-sigma-command.html)
    - [x] [The analyze Subcommand](docs/user-guide/command-reference/the-analyze-subcommand.md) · [source](https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/the-analyze-subcommand.html)
    - [x] [The checkers Subcommand](docs/user-guide/command-reference/the-checkers-subcommand.md) · [source](https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/the-checkers-subcommand.html)
    - [x] [The config Subcommand](docs/user-guide/command-reference/the-config-subcommand.md) · [source](https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/the-config-subcommand.html)
    - [x] [The docs Subcommand](docs/user-guide/command-reference/the-docs-subcommand.md) · [source](https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/the-docs-subcommand.html)
    - [x] [The explain Subcommand](docs/user-guide/command-reference/the-explain-subcommand.md) · [source](https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/the-explain-subcommand.html)
    - [x] [The metadata Subcommand](docs/user-guide/command-reference/the-metadata-subcommand.md) · [source](https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/the-metadata-subcommand.html)
  - [x] [Sigma Support Matrix](docs/user-guide/sigma-support-matrix.md) _(+4)_ · [source](https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/sigma-support-matrix.html)
    - [x] [Language and Framework Support](docs/user-guide/sigma-support-matrix/language-and-framework-support.md) · [source](https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/language-and-framework-support.html)
    - [x] [OS Support](docs/user-guide/sigma-support-matrix/os-support.md) · [source](https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/os-support.html)
    - [x] [CI/CD System Support](docs/user-guide/sigma-support-matrix/ci-cd-system-support.md) · [source](https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/ci/cd-system-support.html)
    - [x] [Minimal Hardware Requirements](docs/user-guide/sigma-support-matrix/minimal-hardware-requirements.md) · [source](https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/minimal-hardware-requirements.html)
  - [x] [Release Notes](docs/user-guide/release-notes.md) · [source](https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/release-notes.html)
  - [x] [Sigma Checkers](docs/user-guide/sigma-checkers.md) · [source](https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/sigma-checkers.html)

---

*Generated from Fluid Topics map `S_R7XSLfKPN3q6kGpp1eHQ` (2026.8.0). Official docs: [Sigma Documentation](https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/).*
