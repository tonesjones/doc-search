# Black Duck Alert Documentation Index

> Auto-generated catalog for local RAG. Do not hand-edit topic rows — update `sources/alert-8.4.0/manifest.json` statuses and run `python scripts/build-index.py --product alert-8.4.0`.

## Corpus status

| Field | Value |
|-------|-------|
| Product | Black Duck Alert |
| Product key | `alert-8.4.0` |
| Version | **8.4.0** |
| Map ID | `QEB0e_qPG~BdIwQfv5eDZQ` |
| TOC nodes | **45** |
| Progress | **45/45 done** (100.0%) · 0 pending · 0 skipped · 0 error |
| Last index build | 2026-08-08T23:46:46.932894+00:00 |
| Manifest | [sources/alert-8.4.0/manifest.json](sources/alert-8.4.0/manifest.json) |
| Raw TOC | [sources/alert-8.4.0/toc.json](sources/alert-8.4.0/toc.json) |
| Docs root | `docs/alert/` |

### Status legend

| Mark | Status | Meaning |
|------|--------|---------|
| `[ ]` | pending | Not scraped yet |
| `[x]` | done | Markdown written under `docs/` |
| `[-]` | skipped | Intentionally not scraped |
| `[!]` | error | Last scrape failed; retry later |

## How to resume

1. Filter `manifest.json` for `status` `pending` (or `error` to retry).
2. `python scripts/scrape-pending.py --product alert-8.4.0 --all-pending`
3. `python scripts/build-index.py --product alert-8.4.0` to refresh this index.

**Content API template:**

```
https://docs.blackduck.com/api/khub/maps/QEB0e_qPG~BdIwQfv5eDZQ/topics/{contentId}/content
```

## Section overview

| Section | Topics | Pending | Done | Skipped | Error | Local root |
|---------|--------|---------|------|---------|-------|------------|
| Installing and Upgrading Alert | 14 | 0 | 14 | 0 | 0 | `docs/alert/installing-and-upgrading-alert/` |
| Installation References | 8 | 0 | 8 | 0 | 0 | `docs/alert/installation-references/` |
| Post Installation Configuration | 8 | 0 | 8 | 0 | 0 | `docs/alert/post-installation-configuration/` |
| System and Task Management | 4 | 0 | 4 | 0 | 0 | `docs/alert/system-and-task-management/` |
| Alert Release Notes | 3 | 0 | 3 | 0 | 0 | `docs/alert/alert-release-notes/` |
| User and Role Management | 3 | 0 | 3 | 0 | 0 | `docs/alert/user-and-role-management/` |
| Black Duck Alert Overview | 1 | 0 | 1 | 0 | 0 | `docs/alert/black-duck-alert-overview/` |
| Alert Concepts and Terms | 1 | 0 | 1 | 0 | 0 | `docs/alert/alert-concepts-and-terms/` |
| Troubleshooting Alert | 1 | 0 | 1 | 0 | 0 | `docs/alert/troubleshooting-alert/` |
| Proprietary Statement | 1 | 0 | 1 | 0 | 0 | `docs/alert/proprietary-statement/` |
| Black Duck Statement on Inclusivity and Diversity | 1 | 0 | 1 | 0 | 0 | `docs/alert/black-duck-statement-on-inclusivity-and-diversity/` |

## Table of contents

- [x] [Black Duck Alert Overview](docs/alert/black-duck-alert-overview.md) · [source](https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/black-duck-alert-overview.html)
- [x] [Alert Release Notes](docs/alert/alert-release-notes.md) _(+2)_ · [source](https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/alert-release-notes.html)
  - [x] [Current Alert Release Notes](docs/alert/alert-release-notes/current-alert-release-notes.md) · [source](https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/current-alert-release-notes.html)
  - [x] [Previous Alert Release Notes](docs/alert/alert-release-notes/previous-alert-release-notes.md) · [source](https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/previous-alert-release-notes.html)
- [x] [Alert Concepts and Terms](docs/alert/alert-concepts-and-terms.md) · [source](https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/alert-concepts-and-terms.html)
- [x] [Installing and Upgrading Alert](docs/alert/installing-and-upgrading-alert.md) _(+5)_ · [source](https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/installing-and-upgrading-alert.html)
  - [x] [Alert System Requirements](docs/alert/installing-and-upgrading-alert/alert-system-requirements.md) · [source](https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/alert-system-requirements.html)
  - [x] [Docker Swarm Install](docs/alert/installing-and-upgrading-alert/docker-swarm-install.md) · [source](https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/docker-swarm-install.html)
  - [x] [Helm Install](docs/alert/installing-and-upgrading-alert/helm-install.md) · [source](https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/helm-install.html)
  - [x] [Upgrading Black Duck Alert](docs/alert/installing-and-upgrading-alert/upgrading-black-duck-alert.md) · [source](https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/upgrading-black-duck-alert.html)
  - [x] [Alert Installation Quickstart Guides](docs/alert/installing-and-upgrading-alert/alert-installation-quickstart-guides.md) _(+2)_ · [source](https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/alert-installation-quickstart-guides.html)
    - [x] [Alert Quickstart: Docker Deployment](docs/alert/installing-and-upgrading-alert/alert-installation-quickstart-guides/alert-quickstart-docker-deployment.md) _(+3)_ · [source](https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/alert-quickstart-docker-deployment.html)
      - [x] [Black Duck Alert Quickstart (Docker Swarm)](docs/alert/installing-and-upgrading-alert/alert-installation-quickstart-guides/alert-quickstart-docker-deployment/black-duck-alert-quickstart-docker-swarm.md) · [source](https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/black-duck-alert-quickstart-docker-swarm-.html)
      - [x] [Black Duck Alert Quickstart (Docker Swarm - standalone)](docs/alert/installing-and-upgrading-alert/alert-installation-quickstart-guides/alert-quickstart-docker-deployment/black-duck-alert-quickstart-docker-swarm-standalone.md) · [source](https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/black-duck-alert-quickstart-docker-swarm-standalone-.html)
      - [x] [Black Duck Alert Quickstart (Docker Swarm - External Database)](docs/alert/installing-and-upgrading-alert/alert-installation-quickstart-guides/alert-quickstart-docker-deployment/black-duck-alert-quickstart-docker-swarm-external-database.md) · [source](https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/black-duck-alert-quickstart-docker-swarm-external-database-.html)
    - [x] [Alert Quickstart: Helm Deployment](docs/alert/installing-and-upgrading-alert/alert-installation-quickstart-guides/alert-quickstart-helm-deployment.md) _(+3)_ · [source](https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/alert-quickstart-helm-deployment.html)
      - [x] [Black Duck Alert Quickstart (Helm)](docs/alert/installing-and-upgrading-alert/alert-installation-quickstart-guides/alert-quickstart-helm-deployment/black-duck-alert-quickstart-helm.md) · [source](https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/black-duck-alert-quickstart-helm-.html)
      - [x] [Black Duck Alert Quickstart (Helm - Standalone)](docs/alert/installing-and-upgrading-alert/alert-installation-quickstart-guides/alert-quickstart-helm-deployment/black-duck-alert-quickstart-helm-standalone.md) · [source](https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/black-duck-alert-quickstart-helm-standalone-.html)
      - [x] [Black Duck Alert Quickstart (Helm - External Database)](docs/alert/installing-and-upgrading-alert/alert-installation-quickstart-guides/alert-quickstart-helm-deployment/black-duck-alert-quickstart-helm-external-database.md) · [source](https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/black-duck-alert-quickstart-helm-external-database-.html)
- [x] [Installation References](docs/alert/installation-references.md) _(+7)_ · [source](https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/installation-references.html)
  - [x] [Configuring Persistent Storage](docs/alert/installation-references/configuring-persistent-storage.md) · [source](https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/configuring-persistent-storage.html)
  - [x] [External Postgres Database Requirements](docs/alert/installation-references/external-postgres-database-requirements.md) · [source](https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/external-postgres-database-requirements.html)
  - [x] [Black Duck Alert Environment Variables](docs/alert/installation-references/black-duck-alert-environment-variables.md) · [source](https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/black-duck-alert-environment-variables.html)
  - [x] [Changing the default server port](docs/alert/installation-references/changing-the-default-server-port.md) · [source](https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/changing-the-default-server-port.html)
  - [x] [Cloud Vendor Specific Database Considerations](docs/alert/installation-references/cloud-vendor-specific-database-considerations.md) · [source](https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/cloud-vendor-specific-database-considerations.html)
  - [x] [Using Custom SSL Certificates](docs/alert/installation-references/using-custom-ssl-certificates.md) · [source](https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/using-custom-ssl-certificates.html)
  - [x] [Black Duck Alert Helm Chart Configuration](docs/alert/installation-references/black-duck-alert-helm-chart-configuration.md) · [source](https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/black-duck-alert-helm-chart-configuration.html)
- [x] [Post Installation Configuration](docs/alert/post-installation-configuration.md) _(+7)_ · [source](https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/post-installation-configuration.html)
  - [x] [Configuring Black Duck Alert](docs/alert/post-installation-configuration/configuring-black-duck-alert.md) · [source](https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/configuring-black-duck-alert.html)
  - [x] [Configuring Black Duck Providers](docs/alert/post-installation-configuration/configuring-black-duck-providers.md) · [source](https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/configuring-black-duck-providers.html)
  - [x] [Configuring Channels in Alert](docs/alert/post-installation-configuration/configuring-channels-in-alert.md) · [source](https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/configuring-channels-in-alert.html)
  - [x] [Configuring Distribution Jobs](docs/alert/post-installation-configuration/configuring-distribution-jobs.md) · [source](https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/configuring-distribution-jobs.html)
  - [x] [Scheduling Notifications](docs/alert/post-installation-configuration/scheduling-notifications.md) · [source](https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/scheduling-notifications.html)
  - [x] [Auditing Notification Failures](docs/alert/post-installation-configuration/auditing-notification-failures.md) · [source](https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/auditing-notification-failures.html)
  - [x] [Encryption and Proxy Configuration](docs/alert/post-installation-configuration/encryption-and-proxy-configuration.md) · [source](https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/encryption-and-proxy-configuration.html)
- [x] [System and Task Management](docs/alert/system-and-task-management.md) _(+3)_ · [source](https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/system-and-task-management.html)
  - [x] [Managing Certificates in Alert](docs/alert/system-and-task-management/managing-certificates-in-alert.md) · [source](https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/managing-certificates-in-alert.html)
  - [x] [Alert Task Management](docs/alert/system-and-task-management/alert-task-management.md) · [source](https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/alert-task-management.html)
  - [x] [Authentication - Configuring LDAP or SAML](docs/alert/system-and-task-management/authentication-configuring-ldap-or-saml.md) · [source](https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/authentication-configuring-ldap-or-saml.html)
- [x] [User and Role Management](docs/alert/user-and-role-management.md) _(+2)_ · [source](https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/user-and-role-management.html)
  - [x] [Alert Users and Roles](docs/alert/user-and-role-management/alert-users-and-roles.md) · [source](https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/alert-users-and-roles.html)
  - [x] [Alert User Management](docs/alert/user-and-role-management/alert-user-management.md) · [source](https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/alert-user-management.html)
- [x] [Troubleshooting Alert](docs/alert/troubleshooting-alert.md) · [source](https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/troubleshooting-alert.html)
- [x] [Proprietary Statement](docs/alert/proprietary-statement.md) · [source](https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/proprietary-statement.html)
- [x] [Black Duck Statement on Inclusivity and Diversity](docs/alert/black-duck-statement-on-inclusivity-and-diversity.md) · [source](https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/black-duck-statement-on-inclusivity-and-diversity.html)

---

*Generated from Fluid Topics map `QEB0e_qPG~BdIwQfv5eDZQ` (8.4.0). Official docs: [Black Duck Alert](https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/).*
