---
title: "Encryption and Proxy Configuration"
source_url: "https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/encryption-and-proxy-configuration.html"
content_id: "vH0em7NPxUcUK1SAexDsCA"
version: "8.4.0"
section: "Post Installation Configuration"
scraped_at: "2026-08-08T23:46:38.752687+00:00"
---

# Encryption and Proxy Configuration

Use the Settings page in Alert to configure encryption and proxies.

- The encryption fields are required in Alert, and your password and salt are required when encrypting sensitive fields, such as the Black Duck SCA API token and proxy password, which must be securely stored in the database.
- Proxy configuration is only required if you want to use a proxy in your setup.

## Encryption configuration

Configure your encryption credentials by navigating to **Settings > Encryption**.

Figure 1. Encryption Configuration. [image: Encryption Configuration]

It is recommended to use environment variables to configure encryption when deploying Alert. The environment variables are:

- `ALERT_ENCRYPTION_PASSWORD`
- `ALERT_ENCRYPTION_GLOBAL_SALT`

If you have not set the environment variables, then you must configure encryption with the GUI.

If the encryption password and salt are not set, the setup page displays before you log in, and requires you to set the required values.

To set up your encryption configuration, complete the following fields under **Encryption Configuration** and then click Save.

You can use the special characters `!,@,%,#` in the Encryption Password and Encryption Global Salt fields.

The fields must contain values between 8 and 24 characters in length.

| Encryption configuration fields | Description |
| --- | --- |
| Encryption Password | Used to encrypt the data. It can be any alphanumeric string between 8 and 24 characters. |
| Encryption Global Salt | The salt appended to the sensitive information before it is encrypted. |

Environment variables are inserted at startup if there is nothing in the database for that configuration.

## Providing encryption configuration in a file

Using Docker secrets, you can supply a file for the encryption password and a file for the encryption salt. The files must contain the text that is the password and salt to be used for encryption on the first line of the file. The files must have the following names so that Alert can find them.

- `ALERT_ENCRYPTION_PASSWORD`
- `ALERT_ENCRYPTION_GLOBAL_SALT`

To create secrets, follow the normal docker commands - We recommend storing the values in a file which can be kept safe

```
docker secret create <STACK_NAME>_ALERT_ENCRYPTION_PASSWORD <FILE_CONTAINING_VALUE>
```

for example:

```
docker secret create blackduck_ALERT_ENCRYPTION_PASSWORD alert_encryption_password.txt
```

where the alert_encryption_password.txt file contains the password.

## Using multiple configuration methods

If you use multiple methods to configure encryption, they are evaluated and used in the following order:

1. Environment variables for encryption.
2. The files in the docker secrets directory.
3. The database volume if the encryption data was written to the volume.

## Encryption considerations when upgrading

When upgrading Alert, if the encryption password and salt were configured using environment variables in the previous version, then the encryption password and encryption salt values must be specified using environment variables for the new version of Alert. The environment variables must contain the same values as the corresponding password and salt variables in the previous version.

**Note:**

Do not change the environment variable values when upgrading Alert. Additionally, changing the encryption password or salt requires all sensitive fields to be updated, as Alert is no longer able to decrypt them with the new values.

## Proxy configuration

To configure your proxy environment, navigate to **Settings > Proxy**.

Figure 2. Proxy Configuration. [image: Proxy Configuration]

Complete the following fields:

1. Proxy Host: Type your proxy server hostname.
2. Proxy Port: Type the port number to be used on your proxy server.
3. Proxy Username: If the proxy server requires authentication, type your proxy user name.
4. Proxy Password: If the proxy server requires authentication, type your proxy password.
5. Non-proxy hosts can be specified, and Alert will not send network traffic to those hosts through the proxy. This field supports the wildcard character '*' (e.g. specifying **.example.com* will match https://org.example.com and server.example.com, but not http://my-example.com ).
6. Click **Save.**

For more information on User Management and Roles, see User Management
