---
title: "Configuring Email notification and delivery"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/configuring-email-notification-and-delivery.html"
content_id: "hOPK0ACnMikByaooK0fOSA"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:48:57.116395+00:00"
---

# Configuring Email notification and delivery

You can enable Coverity Connect to send email from Configuration > System > Email Configuration. You can now change the default email listed in the From
Address field of your email configuration settings to send view-specific
notification emails. Once enabled, users can schedule periodic notifications to help
track issue data in their specific views. See View-specific Email notifications for more information.

The administrator account can also be configured to use email, but a valid email address
must be used. You can view or change the default configuration settings for your account
by navigating to Configuration > Users & Groups.

Email configuration consists of the following options:

Allow Coverity Connect to send email
:   Select to enable email. This can include name-password information when
    creating new users. If this is not enabled, all Coverity Connect email
    functionality is disabled. Selecting this option is required for
    self-service user password recovery.

Suspend email delivery
:   Select to hold all email notification until this attribute is unselected. All
    email notifications are queued and then sent after the attribute is
    unselected. This feature is useful, for example, if there is a problem
    connecting to your mail server, or if your are in the process of changing or
    updating your users' email addresses.

Host Name
:   Specify the SMTP or server name.

Port
:   Type a port number for the mail server.

No encryption
:   Email is sent without encryption. This typically uses port 25.

SMTP over SSL
:   Email is sent by means of SMTP using SSL. This typically uses port
    465.

Require STARTTLS
:   Email is sent using the STARTTLS protocol. This typically uses port 587 or
    port 25.

Username
:   Specify a username to authorize name/password on the mail server.

Password
:   Specify a password to authorize name/password on the mail server.

From Address
:   Specify the email address of the sender.

    View notification emails use the email address of the View owner as the
    sender address.

Plain-Text only
:   If On is selected, Coverity Connect will send emails of Content-Type:
    text/plain. If Off is selected, Coverity Connect will send emails of Content-Type: text/html.
    The default is Off.

Send Test Email
:   (Optional) Send an email to test these settings. Provide a destination email
    address, and click Send. If there is a failure, you
    can find more information about it in the cim.log
    file.

Click Done to finalize your changes and exit the screen.

Note: Before you click Done, ensure that the browser's auto-fill function
has not entered spurious values in the Username or
Password fields.
