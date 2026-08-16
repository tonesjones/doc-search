---
title: "Authentication key mode"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/authentication-key-mode.html"
content_id: "aSzpv1tkOQnypcAO14VfZA"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:51:37.276268+00:00"
---

# Authentication key mode

Create or revoke an authentication key for secure communication with the Coverity Connect
server.

## Synopsis

```
--mode auth-key --create --output-file <filename> [<SET>]

--mode auth-key --revoke <auth-key-ID>
```

## Authentication key mode options

In general, you can specify options in any order.

SET options
:   The SET options apply certain attributes to the authentication key created.

    --set description:description
    :   Sets the description of the authentication key. If not provided, the description is an empty string.

    --set expiration:dateTime
    :   Sets the expiration date for the authentication key.
        There are four accepted syntaxes for
        dateTime:

        - `YYYY-MM-DD`

          The authentication key will expire on the date
          specified.
        - `YYYY-MM-DD[T]hh:mm(:ss)`

          The authentication key will expire on the date and
          time specified. Date and time must be separated by
          "`T`". Seconds are optional.

          CAUTION:

          Separating the date and time by a space instead of "`T`"
          will cause an error.
        - `"after_N_days"`

          The authentication key will expire N days in the future.
        - `"after_N.M_days"`

          The authentication key will expire
          N.M days in
          the future.

Note:
See the Coverity Platform 2026.6.0 User and Administrator Guide for important information about
authentication key restrictions.

## Using the properties file to set key expiration

You can also specify the expiration time for an authentication key in the cim.proprties file,
using the `cim.authkey.expiration.duration` property.
For example:

```
cim.authkey.expiration.duration=1Y
```

## Authentication key mode examples

**Create example**

This example creates an authentication file named "myFile" with the description,
"test user authentication file." This authentication file will expire in 90 days.

```
> cov-manage-im --host cim.company.com --port 8080 --user test \
    --password secret --mode auth-key --create --output-file myFile \
    --set description:"test user authentication file" \
    --set expiration:"after_90_days"
```

**Revoke example**

This example revokes the authentication key with ID `12345`.

```
> cov-manage-im --mode auth-key --revoke 12345
```
