---
title: "Configuring AI-Assisted Documentation Service"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/configuring-ai-assisted-documentation-service.html"
content_id: "dm~cgpRnxvmQW2k9T72UkQ"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:32:21.386748+00:00"
---

# Configuring AI-Assisted Documentation Service

The AI-Assisted Documentation Service provides in-application access to Black Duck SCA documentation through an AI-powered search experience.
Users can search documentation content and view relevant results without leaving the
application.

When the AI-Assisted Documentation Service is disabled, Black Duck SCA
uses the legacy documentation experience instead. Air-gapped deployments always use the
legacy documentation experience.

Note: AI-Assisted Documentation Service is enabled by default.

## Requirements

To configure the AI-Assisted Documentation Service, you must have the **System
Administrator** role.

## Enable or Disable the AI-Assisted Documentation Service

1. Log into Black Duck SCA with the **System Administrator**
   role.
2. Click **Admin** → **System Settings**.
3. Under **System**, click **Help**.
4. Enable or disable the **AI Assisted Documentation Service** setting.

## Service Behavior

The behavior of the documentation experience depends on the selected setting.

| Setting | Behaviour |
| --- | --- |
| Enabled | Users can access AI-assisted documentation search from the Help menu. |
| Disabled | Users are directed to the legacy documentation experience. |
| Air-gapped deployment | The legacy documentation experience is always used. |

## Data Collection and Privacy

When the AI-Assisted Documentation Service is enabled, documentation search requests
are processed by an external cloud-based service to provide AI-assisted search
functionality.

Organizations that do not want documentation search requests processed externally can
disable the AI-Assisted Documentation Service. When disabled, Black Duck SCA uses the legacy documentation experience instead.

The AI-Assisted Documentation Service does not place cookies in the user's
browser.

Note: Air-gapped deployments cannot use the AI-Assisted Documentation Service and
continue to use the legacy documentation experience.

## Access AI-Assisted Documentation

When the AI-Assisted Documentation Service is enabled:

1. Click the **Help** menu in the top navigation bar.
2. Select **Documentation Search**.

The documentation search panel opens, allowing you to search Black Duck SCA documentation directly from within the
application.
