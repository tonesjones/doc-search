---
title: "Configuring Black Duck Alert"
source_url: "https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/configuring-black-duck-alert.html"
content_id: "~fvO4ZtZPQyC4CpTAs0MbA"
version: "8.4.0"
section: "Post Installation Configuration"
scraped_at: "2026-08-08T23:46:33.498500+00:00"
---

# Configuring Black Duck Alert

After installation, you can log in using the administrator account (sysadmin) to complete
Alert configuration.

As part of the Alert installation, you may have used environment
variables to configure settings such as encryption password and global salt,
authentication, or providers. The order in which you perform configuration tasks may
vary depending on how much pre-configuration has been completed using environment
variable settings.

Alert has the following default users with the default password *blackduck*:

- `sysadmin` - full system configuration access.
- `jobmanager` - full access to distribution jobs and read permissions for other operational functions.
- `alertuser` - read access for distribution jobs only.

The following configuration steps assume that you have not fully configured your
installation via environment variables. If you have completed any configuration via
environment variables, the requirement and order of completion will vary
accordingly.

**Note:** Only the **sysadmin** user has the appropriate permission to configure
Alert system settings such as Settings, Authentication, User Management, or
Scheduling.

## Configuration Method Precedence

Most Alert configuration can be set by using environment variables that get loaded at
startup. Environment variables are inserted at startup if there is nothing in the
Alert database for that configuration setting.

Alert processes the default setting of environment variables at startup in situations
where there are neither environment variables nor configuration values set in the
database.

- The environment variable is written into the Alert database if the value for
  the corresponding configuration property isn't already in the database. This
  means that the environment variables take precedence over the default values
  shown in the user interface.
- If there is an existing configuration related to environment variables stored
  in the Alert database, the environment variables will have no
  effect.

## Configuration Workflow

Navigate to the following pages from the navigation panel in Alert to configure your
Alert application. Click on the links below to read the documentation specific for
each section.

## 1. Encryption Configuration

Configure the encryption password and global salt on the Settings page if you have
not configured the encryption details using environment variables during
installation.

Configure proxy settings if required for your environment.

See Encryption and Proxy Configuration

## 2. User Management

Configuration of users and roles is performed via the User Management page. The
default users in Alert may satisfy your requirements, but you can configure new users
and manage users and roles as required.

See User
Management

## 3. Authentication

Configure LDAP and SAML user authentication on the Authentication page if you want to
add/manage users via these authentication methods.

See Authentication

## 4. Configure Sending Notifications in Alert

To enable Alert to send notifications you must configure the Black Duck Provider
(provides the notifications), Channel (means for sending), and the Distribution job
that defines all the elements required for sending notifications.

- Configure the Black Duck provider instance that sends the Black Duck
  notification to Alert via the Providers page.
- Configure channels such as Email or Jira that you want to use in your
  distribution jobs to enable the sending of notifications from the Black Duck
  provider via the Channels page.
- Configure distribution jobs by configuring an Alert channel and Black Duck
  provider. Distribution jobs are used to process Black Duck provider
  notifications that are sent through channels such as Email or Slack via the
  Distributions page.

## 5. Scheduling

On the Scheduling page, you can modify the configuration of system tasks or
leave the default settings.

See Scheduling Notifications

CAUTION:

If you are upgrading Alert and the encryption password and global
salt were configured using environment variables in the previous version, then
the encryption password and encryption salt values must be specified using
environment variables for the new version of Alert and match those previously
used.
