---
title: "Configure JSON scan settings and authentication profiles"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/configure-json-scan-settings-and-authentication-profiles.html"
content_id: "OUf_Ip9d8tnLTfeTRlVkhA"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:57:43.010281+00:00"
content_hash: "1df025fe7b690cb26a0b1ca048dd8b77ef918c766e76e8e98c427adaf8ed3967"
---

# Configure JSON scan settings and authentication profiles

The default DAST profile is suitable for most use cases. If necessary, you can fine-tune your DAST profile in a `scan-settings.json` file and upload it to the Polaris web UI. Configuration options are available for the scan engine (for example, excluded URLs, attack depth, and crawl settings) and the supported authentication methods (AI-Assisted, Forms, SAML, and Selenium). The settings you specify in the file will be applied to the default scan settings.

After you create a DAST project (see [Create DAST projects for web applications and APIs](create-dast-projects-for-web-applications-and-apis.md)), follow these steps to customize the project's DAST profile:

1. After you open the DAST project, go to DAST Profiles and select the project's profile.
2. Select Download Scan Settings to download a template `scan-settings.json` file.

   The template file contains all available configuration options and their default values.
3. Open the scan settings file in a text editor.
4. Edit the default settings, removing those you do not want to modify, and then save the file.

   Note: See Advanced DAST settings for descriptions of the most common scan settings and Authentication profiles and Authentication profiles for MFA for examples of the supported authentication methods. We recommend that you remove the configuration options that you don't want to modify before uploading the scan settings file.
5. Select Load Scan Settings File, then select the JSON file on your local machine to upload it to Polaris.
6. Click Save.

## Advanced DAST settings

Table 1. Advanced DAST configuration reference

| Setting | Description |
| --- | --- |
| `useSmartSetting` | When Smart Settings is enabled, fAST Dynamic crawls a limited section of the target web application to automatically detect several characteristics important to dynamic application security testing. These include (but are not limited to):  - The framework used in the web application, such as Angular, React, or Ember.js - Whether the site is a Single Page Application (SPA) or a traditional, non-JavaScript website - Whether pages must be fully loaded in the browser in order to navigate the site - Whether the page structure is duplicated across the site, to determine the extent of page de-duplication the scan engine can perform   Based on this data, the scan engine defines a set of optimal scan settings and applies them to the `scan-settings.json` file.  **Default:** `true`  Note: Be aware that enabling Smart Settings will override some pre-existing scan settings, if you have modified these in the `scan-settings.json` file. |
| `pageReadyConfig` | Configuration for "page readiness" heuristics; that is, how the scan engine determines if a page has finished loading in a browser and is ready for interaction. `pageReadyConfig` supports a single `mode` of `SPA` (Single Page Application). This mode is designed to help the scanner recognize when pages have loaded in JavaScript intensive web apps.  **Default:** `"mode": "SPA"`  The `pages` and `regexes` options are not supported in the initial release of fAST Dynamic. |
| `authSettings` | Configuration for authentication. **Default:** `"loginType": "none"`  Note: See Authentication profiles for more information. |
| `scanTimeout` | Maximum length of time before an incomplete scan times out. At the end of this period, the scanner will publish the partial results of the scan. **Default:** `72h` |
| `includedPaths` | Configuration for URL paths to include in scans of the target web application. If set, only URL paths matching the specified values are included in scans. Enter an array of regular expressions, for example:   ``` "includedUrls": ["app", "about", "contact", "reports"], ```   **Default:** N/A |
| `excludedUrls` | Configuration for URL paths to exclude from scans of the target web application. If found on a URL path, the given URLs will be excluded from scans, including active attacks. Enter an array of regular expressions, for example:   ``` "excludedUrls": ["logout", "signout"], ```   **Default:** `"logout", "signout", "log-out", "sign-out"` |
| `excludedAttackUrls` | Configuration for URL paths to exclude from active attacks of the target web application. Only applies if Perform Active Attacks is selected on the DAST project page.  **Default:** `null` |
| `excludedParameters` | An array of values where any matching parameter names (for example, query parameters, form fields, or headers) will not be attacked. Only applies if Perform Active Attacks is selected on the DAST project page.  **Default:** `"jsessionid", "__EVENTARGUMENT", "__EVENTTARGET", "__EVENTVALIDATION", "__VIEWSTATE", "X-WHS"` |
| `excludedStatusCodes` | A response with a matching status code will not be attacked. Only applies if Perform Active Attacks is selected on the DAST project page.  **Default:** `401, 404` |
| `excludedHosts` | List of hosts to exclude from crawling and attacking. The scan engine will never send a request to any URL on these hosts, even through the browser. A list of regular expressions.  Note: You might want to add internal services to the default list of excluded hosts, for example, application performance monitoring (APM) tools, ad servers, etc.  **Default:** See `scan-settings.json` |
| `customHeaders` | Extra headers to add to all requests from the scan engine. **Default:** `Cache-Control, Accept-Language` |
| `customCookies` | Extra cookies to add to all requests from the scan engine. **Default:** `null` |
| `activeCheckers` | List of active checkers to enable in scans of the target web application. Active checkers change the values of parameters in requests to detect vulnerabilities. Reducing the amount of active checkers will speed up scans but reduce the depth and breadth of intrusive testing.  See [fAST Dynamic checkers](fast-dynamic-checkers.md) for a complete list of active checker codes.  Only applies if Perform Active Attacks is selected on the DAST project page.  **Default:** See `scan-settings.json` |
| `passiveCheckers` | List of passive checkers to enable in scans of the target web application. Passive checkers are non-intrusive. They detect vulnerabilities by passively observing web traffic. See [fAST Dynamic checkers](fast-dynamic-checkers.md) for a complete list of passive checker codes.  **Default:** See `scan-settings.json` |
| `crawler.formValues` | Default values used by the scan engine when crawling pages that contain forms. You can customize these form values with specific names and types of form fields used in the target web application. **Default:** See `scan-settings.json` |

## Authentication profiles

Authentication profiles are the components of a DAST profile that handle authentication to web apps and APIs. DAST scans use authentication profiles to represent different types of users, such as unauthenticated, authenticated, or administrator.

Authentication profiles are defined in the `authProfiles` section of a scan settings JSON file. They support the same authentication settings as the Polaris web UI, plus advanced settings for each authentication method and settings for multi-factor authentication (MFA).

Note: You can also configure authentication profiles in the UI when adjusting scan settings.

Note: Some API checkers, such as those for BOLA issues, require you to add more than one authentication profile (`authProfiles`). Web application scans only use the first-added `authProfiles`, regardless of how many you add.

**authProfiles structure**

The `authProfiles` JSON object consists of the following fields:

- `name`: The name of the authentication profile (must be unique).
- `authenticators`: A group of authentication settings for the enabled `loginType`.
- `loginType`: The authentication method.
  - For Web App scans, the supported `loginTypes` are: `none`, `ai`, `simple`, `SAML`, `header`, `selenium`, and `chromeRecording`.
  - For API scans, the supported `loginTypes` are: `none`, `header`, `queryParams`, `OAuth2Password`, `OAuth2ClientCredentials`, `AWSSigV4`, and mTLS `ClientCertificate`.

The structure of the `authenticators` object depends on the selected `loginType`. By default, no authentication method is set, so the `loginType` is `none`:

```
"authProfiles": [
    {
      "name": "Primary",
      "authenticators": [
        {
          "timeoutMultiplier": 1,
          "fingerprintSimilarityThreshold": 0.97,
          "loginType": "none",
          "retryLimit": 3,
          "logoutLimit": -1,
          "onStateError": "reacquire",
          "settings": null
        }
      ],
      "accessTags": null
    }
  ],
```

The following sections describe the individual settings for each authentication method (`loginType`), and provide example authentication profiles that you can customize for your own web app or API. Methods for use with API targets only are labeled with "API scans" in parentheses.

### Simple

Simple authentication is most appropriate for simple username/password login forms where both username and password fields are on a single page.

Note: If your application uses multiple pages for authentication (like Polaris), use Selenium.

Table 2. `scan-settings.json`, simple authentication reference

| Setting | Optional/Required | Description |
| --- | --- | --- |
| `loginURL` | Required | URL of the target login page. |
| `steps` | Required | Specifies one or more login steps for the target web application. |
| `inputs` | Required | Specifies the input identifiers and values for a specified login step. For example:  ``` "inputs": [               {                 "identifier": "username",                 "value": "admin"               },               {                 "identifier": "password",                 "value": "password123"               } ``` |
| `formCSSSelector` | Optional | A CSS selector for the login form if there is more than one form on the login page. A CSS selector can be generated using your browser's developer tools by highlighting the `<form>` HTML element and choosing Copy Selector from the context menu. For example: ``` #my-page-form, body > div:nth-child(5) > form ``` |
| `formValues` | Optional | Specifies the input field names and values for interacting with the target login form. You can specify one or more of the following:  - `nameValues`: select for exact matches on the `name` attribute of an `<input>` HTML element. Note: The rendered label used to identify an `<input>` element may not match its `name` attribute.  For example:  ```   <form>     <input name="username">     <input name="password" type="password">   </form>   ```  ```   "formValues": {       "nameValues": {           "username": "myuser",           "password": "mypassword"       }   }   ``` - `typeValues`: select for an exact match on the `type` attribute of an `<input>` HTML element. For example: ```   <form>     <input name="email-1234" type="email">     <input name="username-5678" type="text">     <input name="password-9999" type="password">   </form>   ```  ```   "formValues": {       "typeValues": {           "text": "myuser",           "password": "mypassword",           "email": "myuser@example.com"       }   }   ``` - `nameRegexValues`: select for a regular expression match using the `name` attribute of an `<input>` HTML element. For example: ```   <form>     <input name="email-1234" type="email">     <input name="username-5678" type="text">     <input name="password-9999" type="password">   </form>   ```  ```   "formValues": {       "nameRegexValues": {           "username-\d+": "myuser",           "password-\d+": "mypassword"       }   }   ``` |
| `headers` | Optional | An array of `Name,Value` pairs (note the capitalization). For example: ``` "headers": [     {"Name": "foo", "Value": "bar"} ] ``` |
| `cookies` | Optional | An array of Cookie objects as `Name,Value` pairs. Other cookie properties, such as `Path` or `Expires`, are supported too. For example: ``` "cookies": [     {"Name": "session", "Value": "123"} ] ``` |

For example:

```
{
  "version": "0.25",
  
  "authProfiles": [{
    "name": "<PROFILE_NAME>",
    "authenticators": [{
      "loginType": "simple",
      "settings": {
        "loginURL": "https://example.com/login",
        "steps": [
           {
            "formCSSSelector": "#login-form",
            "inputs": [
              {
                "identifier": "username",
                "value": "admin"
              },
              {
                "identifier": "password",
                "value": "password123"
              }
            ]
          }  
        ]
      }
    }]
  }]
}
```

### SAML

Authenticate via a SAML Identity Provider (IdP) to access the target application through single-sign on (SSO).

Table 3. `scan-settings.json`, SAML authentication reference

| Setting | Optional/Required | Description |
| --- | --- | --- |
| `ssoLoginURL` | Required | The URL of SAML SSO login page. |
| `formValues` | Optional | Specifies the input field names and values for interacting with the target login form. You can specify one or more of the following:  - `nameValues`: select for exact matches on the `name` attribute of an `<input>` HTML element. Note: The rendered label used to identify an `<input>` element may not match its `name` attribute.  For example:  ```   <form>     <input name="username">     <input name="password" type="password">   </form>   ```  ```   "formValues": {       "nameValues": {           "username": "myuser",           "password": "mypassword"       }   }   ``` - `typeValues`: select for an exact match on the `type` attribute of an `<input>` HTML element. For example: ```   <form>     <input name="email-1234" type="email">     <input name="username-5678" type="text">     <input name="password-9999" type="password">   </form>   ```  ```   "formValues": {       "typeValues": {           "text": "myuser",           "password": "mypassword",           "email": "myuser@example.com"       }   }   ``` - `nameRegexValues`: select for a regular expression match using the `name` attribute of an `<input>` HTML element. For example: ```   <form>     <input name="email-1234" type="email">     <input name="username-5678" type="text">     <input name="password-9999" type="password">   </form>   ```  ```   "formValues": {       "nameRegexValues": {           "username-\d+": "myuser",           "password-\d+": "mypassword"       }   }   ``` |
| `headers` | Optional | An array of `Name,Value` pairs (note the capitalization). For example: ``` "headers": [     {"Name": "foo", "Value": "bar"} ] ``` |
| `cookies` | Optional | An array of Cookie objects as `Name,Value` pairs. Other cookie properties, such as `Path` or `Expires`, are supported too. For example: ``` "cookies": [     {"Name": "session", "Value": "123"} ] ``` |

For example:

```
{
  "version": "0.25",
  
  "authProfiles": [{
    "name": "<PROFILE_NAME>",
    "authenticators": [{
      "authSettings": {
        "loginType": "SAML",
        "settings": {
          "ssoLoginURL": "https://mycompany.okta.com/app/12345",
          "steps": [{
            "inputs": [
              {
                "identifer": "username",
                "value": "admin"
              },
              {
                "identifier": "password",
                "value": "password123"
              }
            ]
          }]
        }
      }
    }]
  }]
}
```

### Selenium

Authenticate using a Selenium .cfg or .side file, generated from the Selenium IDE browser extension.

Table 4. `scan-settings.json`, Selenium authentication reference

| Setting | Optional/Required | Description |
| --- | --- | --- |
| `sideFileContents` | Optional | The ID of the Selenium .cfg file. Alternatively, use the `sideFilePath` parameter to point to a .side file saved on your machine, e.g. `"sideFilePath": "C:\\Users\\user-name\\site-login.side"` |

For example:

```
{
  "version": "0.25",
  
  "authProfiles": [{
    "name": "<PROFILE_NAME>",
    "authenticators": [{
      "loginType": "selenium",
      "settings": {
        "sideFileContents": {
          "id": "f2d3d670-62f4-476d-bec8-6ffdb4508725",
          ... 
        }
      }
    }]
  }]
}
```

### Chrome Recording

Authenticate using a Chrome recording JSON file, generated with the Chrome DevTools Recorder. Chrome recordings can handle complex, multi-step authentication flows, including those with dynamic elements.

Chrome recording authentication is configured in the scan-settings.json file only.

Table 5. `scan-settings.json`, Chrome Recording authentication reference

| Setting | Optional/Required | Description |
| --- | --- | --- |
| `chromeRecordingContents` | Required | The contents of the Chrome recording file, in JSON format. |

For example:

```
{
  "version": "0.25",
  "authProfiles": [
    {
      "name": "<PROFILE_NAME>",
      "authenticators": [
        {
          "loginType": "chromeRecording",
          "settings": {
            "chromeRecordingContents": {
              "title": "Recording 8/22/2025 at 1:04:54 PM",
              "steps": [...]
            }
          }
        }
      ]
    }
  ]
}
```

### AI-Assisted

Automatically detect the login process using AI-Assisted authentication. See [Use AI-Assisted Authentication](use-ai-assisted-authentication.md) for more information about this fAST Dynamic feature.

Table 6. `scan-settings.json`, AI-Assisted Authentication reference

| Setting | Optional / Required | Description |
| --- | --- | --- |
| `loginURL` | Required | The URL of the login page of the target web application to scan. This must be accessible to the fAST Dynamic DAST scanner. |
| `username` | Required | The username used to log in. |
| `password` | Required | The password used to log in. |
| `otpEmail` | Optional | The Black Duck MFA email address associated with the DAST project, in the format `<project-ID>@mfa.dast.blackduck.com`. |
| `otpTimeSecret` | Optional | The TOTP Secret Key that is configured in your MFA provider. |

For example:

```
{
  "version": "0.25",
  
  "authProfiles": [{
    "name": "<PROFILE_NAME>",
    "authenticators": [{
        "loginType": "ai",
        "settings": {
          "loginURL": "https://myapp.blackduck.com",
          "username": "user",
          "password": "pass"
          "otpEmail": "<project_id>@mfa.dast.blackduck.com",
          "otpTimeSecret": "PJ4N90FWMDMSOQEMNC8FDK"
        }
      }]
  }]
}
```

### Header (API scans)

Authenticate by passing an auth header containing a bearer token, for example.

Table 7. `scan-settings.json`, Header authentication reference

| Setting | Optional / Required | Description |
| --- | --- | --- |
| `headers` | Required | An array of authentication headers. |
| `name` | Required | Header name (string). |
| `value` | Required | Header value (string). |

For example:

```
{
  "version": "0.25",
  
  "authProfiles": [{
    "name": "<PROFILE_NAME>",
    "authenticators": [{
      "loginType": "header",
      "settings": {
        "headers": [
          {
            "name": "Authorization",
            "value": "Bearer 1234"
          }
        ]
      }
    }]
  }]
}
```

### Query Parameters (API scans)

Authenticate by providing credentials as query parameters.

Table 8. `scan-settings.json`, Query Parameters authentication reference

| Setting | Optional/Required | Description |
| --- | --- | --- |
| `queryParams` | Required | An array of query parameters. |
| `name` | Required | Query parameter name (string). |
| `value` | Required | Query parameter value (string). |

For example:

```
{
  "version": "0.25",

  "authProfiles": [{
    "name": "<PROFILE_NAME>",
    "authenticators": [{
      "loginType": "queryParams",
      "settings": {
        "queryParams": [
          {
            "name": "token",
            "value": "12345"
          }
        ]
      }
    }]
  }]
}
```

### OAuth 2.0 Password (API scans)

Authenticate by using an OAuth 2.0 password flow (see the [OAuth 2.0 specification](https://oauth.net/2/)).

Table 9. `scan-settings.json`, **OAuth 2.0 Password** authentication reference

| Setting | Optional/Required | Description |
| --- | --- | --- |
| `username` | Required | Username used to log in (string). |
| `password` | Required | Password used to log in (string). |
| `clientID` | Required | ID of the OAuth Client. |
| `clientSecret` | Required | The client secret of the application. |
| `site` | Required | URL of the API that fAST Dynamic will authenticate to. |
| `tokenPath` | Required | Path to the access token from the Authorization server. |
| `queryParams` | Required | Array of query parameters. |
| `bodyParams` | Required | Array of body parameters. |
| `headerParams` | Required | Array of header parameters. |

For example:

```
{
  "version": "0.25",
  
  "authProfiles": [{
    "name": "<PROFILE_NAME>",
    "authenticators": [{
      "loginType": "OAuth2Password",
      "settings": {
        "username": "user1",
        "password": "pass1234",
        "clientID": "mRkZGFjM",
        "clientSecret": "DFsdafz",
        "site": "https://api.example.com",
        "tokenPath": "/oauth/token",
        "queryParams": [{"key": "query1", "value": "example"}],
        "bodyParams": [{"key": "body1", "value": "example"}],
        "headerParams": [{"key": "header1", "value": "example"}]
      }
    }]
  }]
}
```

### OAuth 2.0 Client Credentials (API scans)

Authenticate using an OAuth 2.0 Client Credentials flow (see the [OAuth 2.0 specification](https://oauth.net/2/)).

Table 10. `scan-settings.json`, OAuth 2.0 Client Credentials authentication reference

| Setting | Optional/Required | Description |
| --- | --- | --- |
| `clientID` | Required | ID of the OAuth Client (string). |
| `clientSecret` | Required | The OAuth Client secret, e.g. password. |
| `site` | Required | URL of the API that fAST Dynamic will authenticate to. |
| `tokenPath` | Required | Path to the access token from the Authorization Server. |
| `queryParams` | Required | Array of query parameters. |
| `bodyParams` | Required | Array of body parameters. |
| `headerParams` | Required | Array of header parameters. |

For example:

```
{
  "version": "0.25",
  
  "authProfiles": [{
    "name": "<PROFILE_NAME>",
    "authenticators": [{
      "loginType": "OAuth2ClientCredentials",
      "settings": {
        "clientID": "mRkZGFjM",
        "clientSecret" : "DFsdafz",
        "site" : "https://example.com",
        "tokenPath" : "/oauth/token",
        "queryParams" : [{"key": "query1", "value": "example"}],
        "bodyParams" : [{"key": "body1", "value": "example"}],
        "headerParams" : [{"key": "header1", "value": "example"}]
      }
    }]
  }]

}
```

### AWS Signature v4 (API scans)

Authenticate using AWS Sig v4 (see [AWS Signature Version 4 for API requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv.html)).

Table 11. `scan-settings.json`, AWS Signature v4 authentication reference

| Setting | Optional/Required | Description |
| --- | --- | --- |
| `accessKey` | Required | Access key ID. |
| `serviceKey` | Required | Service key ID. |
| `region` | Required | AWS region, e.g. us-east-1. |
| `service` | Required | AWS service, e.g. s3, iam. |

For example:

```
{
  "version": "0.25",
  
  "authProfiles": [{
    "name": "<PROFILE_NAME>",
    "authenticators": [{
      "loginType": "AWSSigV4",
      "settings": {
        "accessKey": "AKIDEXAMPLE",
        "serviceKey": "mRkZGFjMASdsfOFKmkls",
        "region": "us-east-1",
        "service": "s3"
      }
    }]
  }]
  
}
```

### mTLS (Client Certificate) (API scans)

Authenticate using mutual TLS (mTLS) Client Certificate.

Table 12. `scan-settings.json`, MTLS (Client Certificate) authentication reference

| Setting | Optional/Required | Description |
| --- | --- | --- |
| `certificate` | Required | TLS certificate from the server. |

For example:

```
{
  "version": "0.25",
  
  "authProfiles": [{
    "name": "<PROFILE_NAME>",
    "authenticators": [{  
        "loginType": "ClientCertificate",
        "settings": {
          "certificate": "-----BEGIN CERTIFICATE-----\nMIIBvDCCAWOgAwIBAgIQAmlgHhAhCL5+jJeTakHVHTAKBggqhkjOPQQDAjAzMTEw\nLwYDVQQDEyhDYWRkeSBMb2NhbCBBdXRob3JpdHkgLSBFQ0MgSW50ZXJtZWRpYXRl\nMB4XDTI1MDEwODAxMDEwM1oXDTI1MDEwODEzMDEwM1owADBZMBMGByqGSM49AgEG\nCCqGSM49AwEHA0IABI/V1KHWk3+fFdiq5ke/lAh2QMuoNnCcMWx6Tkga0oLwKBR+\nyn2JI0kg2gtc8gdmtC9/aY5pLgo5cU/Tl9Y28SijgYswgYgwDgYEVR0PAQH/BAQD\nAgeAMB0GA1UdJQQWMBQGCCsGAQUFBwMBBggrBgEFBQcDAjAdBgNVHQ4EFgQUqwzL\nnbPig1zy6ytRVIJ4kK7gAiEwHwYDVR0jBBgwFoAUd1CbI6wESNJ+XhY3UjlXpmNh\nkDowFwYDVR0RAQH/BA0wC4IJbG9jYWxob3N0MAoGCCqGSM49BAMCD0cAMEQCIDoT\n2X1yLe+QYt4aZ2TbqAIQ+K1NmfQJaXm8gyZT9skhAiACnmOKlqb0klHoAuJ4f/sL\nxdveQuVr4d4QEDe0eebt2w==\n-----END CERTIFICATE-----",      "privateKey": "-----BEGIN EC PRIVATE KEY-----\nMHcCAQEEIPZRJKfTWNYJNWvX9iXoQ0PnjEdBhPDXHHjb6ZrrYfGmoAoGCCqGSM49\nAwEHoUQDQgAEj9XUodaTf58V2KrmR7+UCHZAy6g2cJwxbHpOSBrSgvAoFH7KfYkj\nSSDaC1zA52a0L39pjmkuCjlxT9OX1jbxKA==\n-----END EC PRIVATE KEY-----"    
        }  
      }] 
  }]

}
```

## Authentication profiles for MFA

fAST Dynamic can authenticate to web application targets that implement multi-factor authentication (MFA) security measures. Two types of MFA are supported:

- **Email MFA**: Where a one-time code is sent to a preconfigured email address on attempted login and then entered into an input field on the login page.
- **Time-based One-Time Password (TOTP) MFA**: Where a time-based code is generated using a pre-shared secret key and entered into an input field on the login page.

  Note: The TOTP implementation supports standard TOTP parameters (SHA-1 hash algorithm, 6-digit codes, 30-second time step).

The AI-Assisted Authentication feature includes support for both types of MFA. Email MFA can only be configured by uploading a customized scan settings JSON file within the "Simple Forms" or the "Selenium/Chrome recordings" authentication types (examples of these methods are shown below).

TOTP-based MFA can be configured either through the Polaris web UI or through the JSON upload method.

Note: The AI-Assisted Authentication example, above, also includes configuration for MFA.

**Email and TOTP MFA with Simple Authentication**

Table 13. `scan-settings.json`, Email MFA - simple authentication reference

| Setting | Optional/Required | Description |
| --- | --- | --- |
| `loginURL` | Required | URL of the target application's login page. |
| `steps.inputs` | Required | A series of steps that must be performed to access the application (with required inputs at each stage). In the example JSON below this table, two steps are used. The first step in the example below includes identifiers for username and password fields in the target application, along with the username and password used to access the application.  You can identify input fields (username, password, and MFA input fields) using HTML IDs, names, or type attributes.  The second step in the example below includes the identifier for the MFA code input field that appears after the initial login, along with a project-specific email address that receives MFA codes.  Each DAST project is assigned a unique Black Duck MFA email address to receive one-time codes from MFA providers. You must configure the target web application to send emails to the correct email address for the DAST project. This is in the following format:   ``` <dast-project-id>@mfa.dast.blackduck.com (America, Production and POC) <dast-project-id>@mfa.eu.dast.blackduck.com (European Union) <dast-project-id>@mfa.ksa.dast.blackduck.com (Kingdom of Saudi Arabia) ```   Note: The `<dast-project-id>` is visible in the browser address bar when viewing the project in Polaris (after `/project/` in the URL).  `valueType` must be set to `email-totp` to indicate this is an email-based MFA field. |

For example:

```
{
  "version": "0.25",
  "authProfiles": [{
    "name": "<PROFILE_NAME>",
    "accessTags": [],
    "authenticators": [{
      "loginType": "simple",
      "settings": {
      "loginURL": "https://example.com/login",
          "steps": [
            {
              "inputs": [
                {
                  "identifier": "username",
                  "value": "admin"
                },
                {
                  "identifier": "password",
                  "value": "password123"
                }
              ]
            },
            {
              "inputs": [{
                "identifier": "email-mfa-field",
                "value": "dast-project-id@mfa.dast.blackduck.com",
                "valueType": "email-totp"
              }]
            }   
          ]
      }
    }]
  }],
```

Table 14. `scan-settings.json`, TOTP MFA - simple authentication reference

| Setting | Optional/Required | Description |
| --- | --- | --- |
| `loginURL` | Required | URL of the target application's login page. |
| `steps.inputs` | Required | A series of steps that must be performed to access the application (with required inputs at each stage). In the example JSON below this table, two steps are used. The first step in the example below includes identifiers for username and password fields in the target application, along with the username and password used to access the application.  You can identify input fields (username, password, and MFA input fields) using HTML IDs, names, or type attributes.  The second step in the example below includes the identifier for the TOTP MFA code input field that appears after the initial login, along with the secret key used to generate TOTP codes.  The `value` field must contain the TOTP secret key, typically a base32-encoded string that was provided when setting up TOTP for the account.  `valueType` must be set to `totp` to indicate this is a time-based one-time password field. |

For example:

```
{
  "version": "0.25",
  "authProfiles": [{
    "name": "<PROFILE_NAME>",
    "accessTags": [],
    "authenticators": [{
      "loginType": "simple",
      "settings": {
      "loginURL": "https://example.com/login",
          "steps": [
            {
              "formCSSSelector": "#login-form",
              "inputs": [
                {
                  "identifier": "username",
                  "value": "admin"
                },
                {
                  "identifier": "password",
                  "value": "password123"
                }
              ]
            },
            {
              "inputs": [{
                "identifier": "otp-id",
                "value": "DCXPW31KDM1ISCX",
                "valueType": "totp"
              }]
            }   
          ]
      }
    }]
  }],
```

### TOTP MFA with Selenium authentication

This example configuration shows Selenium authentication, including a step for MFA using a time-based one-time password (TOTP). To use this method, you must manually replace the `value` field with the string `*BD-TOTP*` and add the TOTP secret to the `comment` field.

```
{
      "id": "6c185925-9fe5-499a-bb77-6e48e94f1a30",
      "comment": "ISJSXMU4PRB6EGK5OL7V44J4OT4D2BJK",
      "command": "type",
      "target": "id=foo",
      "targets": [],
      "value": "*BD-TOTP*"
}
```

### TOTP MFA with Chrome Recording authentication

This example configuration shows Chrome Recording authentication, including a step for MFA using a TOTP. To use this method, you must manually replace the `type` field with `*BD-TOTP*` and add a new field named `secret` containing the TOTP secret.

```
  {
      "type": "*BD-TOTP*",
      "secret": "JBSWY3DPEHPK3PXP",
      "selectors": [
          "#totp-code"
      ],
      "target": "main"
  }
```

### Email MFA with Selenium authentication

This example configuration shows Selenium authentication, including a step for email MFA. To use this method, you must manually replace the `value` field with `*BD-EMAIL-MFA*`. In the `comment` field, add the email address that the one-time code will be sent to, e.g. `dast-project-id@mfa.dast.blackduck.com`.

```
{
  "command": "type",
  "comment": "dast-project-id@mfa.dast.blackduck.com",
  "id": "ec9e5a83-bfc4-4ead-9078-105ebb8d17da",
  "target": "id=code",
  "targets": [
    [
      "id=code",
      "id"
    ],
    [
      "name=code",
      "name"
    ],
    [
      "css=#code",
      "css:finder"
    ],
    [
      "xpath=//input[@id='code']",
      "xpath:attributes"
    ],
    [
      "xpath=//form[@id='mfaForm']/div/input",
      "xpath:idRelative"
    ],
    [
      "xpath=//input",
      "xpath:position"
    ]
  ],
  "value": "*BD-EMAIL-MFA*"
},
```

### Email MFA with Chrome Recording authentication

This example configuration shows Chrome Recording authentication, including a step for email MFA. To use this method, you must manually replace the `type` field from `change` to `*BD-EMAIL-MFA*`. Add an `address` field and enter the email address that the one-time code will be sent to.

```
#...
{
    "type": "*BD-EMAIL-MFA*",
    "address": "test-user-2@mfa.dast.blackduck.com",
    "selectors": [
        [
            "aria/Verification Code:"
        ],
        [
            "#code"
        ],
        [
            "xpath///*[@id=\"code\"]"
        ],
        [
            "pierce/#code"
        ]
    ],
    "target": "main"
},
```
