---
title: "Hosting location for Black Duck Detect"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/hosting-location-for-black-duck-detect.html"
content_id: "dtg6_gLPuXWyRZM5tFPBgg"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:32:08.981961+00:00"
---

# Hosting location for Black Duck Detect

Managing and updating the versions of Detect across various pipeline jobs in Black Duck
can be a challenge. When incompatible versions of Detect and Black Duck are used, it can
take a lot of time and effort to update all jobs. Additionally, it's not always clear
which version of Detect is being used or which versions are available for a given Black
Duck version.

Black Duck offers two means to connect with Black Duck Detect to better suit your
needs; Internally Hosted and Black Duck Hosted.

## How does it work?

When Detect is invoked to scan source files, it first determines the configuration set in
Black Duck (see below) and then validates the version set in Black Duck. This
information is then communicated with Detect on client side.

If there is a difference between the client Detect version and the configuration set in Black Duck, Detect will pull the proper Detect version as
configured in Black Duck and scan the source with the newly pulled archive
instead.

- Enabling the **Internally Hosted** setting provides the option to host the Detect Binary
  JAR file directly on your own Artifactory to be pulled with the specific
  version specified for all users. If set to Internally Hosted, Detect will
  pull and use the version dictated in the Detect URL field.

  Using this option allows integration with Code Sight and Detect, but internally hosting the
  Detect JAR file does not provide a complete Detect installation; it will not
  include any inspector scripts or inspector tools like in a full [air-gap mode](https://docs.blackduck.com/access?ft:originId=9c0814dc6c47bd8e1b015657cf47a869/922ab7c0cde7d0b0a2f9245babfbbf23.topic) installation and is
  not meant as an alternative to deploying Detect via air-gap mode.

  Additionally, scan host machines still require access to the Internet for
  full functionality.

  Warning: Black Duck does not validate the JAR file obtained from the provided
  internally hosted URL. Ensure that a valid version of the Detect JAR is
  available for downloaded in the hosting location.
- Using the **Black Duck Hosted** setting allows the option to use
  our Black Duck repository to download the Detect
  version set based on the system setting configured.. If set to Black Duck Hosted, it will pull from our repository
  directly from client side.
- Code Sight users can find Detect configuration instructions at **[Setting Up Black Duck® SCA for Code
  Sight](https://docs.blackduck.com/access?ft:originId=e5be419b9a362d8c0118eeab3a8ee157/09dd801d1e9346ca6aae58b3b1046249.topic)**.

## Internally hosted Black Duck Detect

Users with limited external connectivity can define the internal hosting location of Black Duck Detect. Using this information, these users can leverage Code
Sight for deployment across their developer base to run on-demand Software
Composition Analysis (SCA) scans.

To specify the hosting location of Black Duck Detect:

1. Log in to Black Duck with the System Administrator role.
2. Click [image: Administration icon] .
3. Select **System Settings.**
4. Click **Black Duck Detect** in the left-hand menu.
5. Click the **Internally Hosted** box.
6. In the **Hosting location for Black Duck Detect** section, enter the valid
   URI for your internal instance of Black Duck Detect.
7. Click **Save**.

## Black Duck hosted Detect

Non-airgapped users who want Black Duck to manage the version of Detect to use can select the
Black Duck Hosted option:

1. Log in to Black Duck with the System Administrator role.
2. Click [image: Administration icon] .
3. Select **System Settings.**
4. Click **Black Duck Detect** in the left-hand menu.
5. Click the **Black Duck Hosted** box.
6. Select the desired version of Black Duck Detect from the **Black Duck Detect Version** dropdown
   menu.
7. Optionally, check the **Force newer versions of Detect to downgrade** box if you want
   to ensure users cannot perform scans with newer versions of Detect. If
   enabled, Black Duck Detect will downgrade to the selected
   version.

   Note: Black Duck Detect does not support downgrading itself to
   versions prior to 8.9.0 because such a downgrade will lose the ability to
   self-update again.
8. Click **Save**.
