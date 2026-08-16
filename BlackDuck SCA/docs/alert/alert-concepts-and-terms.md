---
title: "Alert Concepts and Terms"
source_url: "https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/alert-concepts-and-terms.html"
content_id: "NKKmyZZYSrDzln_~5YU2fQ"
version: "8.4.0"
section: "Alert Concepts and Terms"
scraped_at: "2026-08-08T23:46:17.257530+00:00"
---

# Alert Concepts and Terms

This page describes the key concepts and terminology used in Alert.

## Key Concepts

| Concept | Description |
| --- | --- |
| Provider | A Provider is the source of the notifications that Alert manages. Black Duck is the current provider. |
| Channel | Channels are the means by which Alert sends notifications. These are applications such as Slack, JIRA, MS Teams etc. |
| Distribution Job | These determine which channel(s) are used, when to execute, the subject, recipients, notification types etc. for notifications. |
| Audit | Audit is the list of notifications sent for jobs that have run as well as the notifications that were not sent because they did not match any of the criteria for the configured jobs. |
| Authentication | SAML and LDAP can be used to authenticate users to the Alert application. |
| Scheduling | In Alert terms, this is when configurable tasks will run and how frequently. |
| Digest | This is the message information from the notification provider. |
| Task Management | The task management table is a read-only and lists data about tasks that are currently running. |
| User Management | You can create, delete users, or edit users and roles. Permissions to perform certain actions are then assigned to a role, which in turn can be assigned to a user. |
| Environment Variables | Alert processes environment variables at startup from which it derives various configuration values. |
| Error Messaging | Error messages that relate to authentication, which might be displayed in response to user actions. |
| Notification Types | These are the various reasons that an administrator may wish to send a notification. They include such reasons as rule violations, new project creation, vulnerabilities detected etc. |

## Terminology

| Term | Description |
| --- | --- |
| SAML | Security Assertion Markup Language (SAML) is a login standard that helps users access applications based on sessions in another context. It’s a single sign-on (SSO) login method. |
| LDAP | Lightweight Directory Access Protocol (LDAP), is a standards-based mechanism for interacting with directory servers. Used in this context for authentication and storing information about users, groups, and applications. |
| Encryption | This is the process of converting plaintext to ciphertext and is used to protect information. |
| Proxy | A gateway between the user or server/application and the internet. It is an intermediary server that separates local from remote. |
| Cron | A job scheduler on Unix-like operating systems. Used to schedule jobs,(commands or shell scripts), also known as cron jobs, to run periodically at fixed times, dates, or intervals. |
