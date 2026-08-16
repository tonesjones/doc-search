---
title: "Downloading a Coverity toolkit artifact from the Black Duck repository"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/downloading-a-coverity-toolkit-artifact-from-the-black-duck-repository.html"
content_id: "e8iyb3S1ybhPDDCY~72PyQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:40:34.529061+00:00"
---

# Downloading a Coverity toolkit artifact from the Black Duck repository

If you are deploying Scan Service, you must download a
`coverity-all-platforms...` artifact. Each of these artifacts
contains:

- Thin Client installers to be able to run scans in Scan Service within the
  Kubernetes container environment,
- full Coverity Analysis client installers to run analyses locally,
- and tools to setup and run scans.

## Downloading using a Web browser

You can download artifacts using a Web browser as follows:

1. Open <http://repo.blackduck.com>.
2. Log into the [community.blackduck.com](http://community.blackduck.com) website and open the
   Licenses and Downloads page.
3. Click Log In and enter your credentials which you can find on the Licenses and
   Downloads page in the Cmmunity website.
4. Open the page for the Coverity version. All files for the selected version are
   listed.
5. Click each needed file to download to your local system. Note that many files
   take time to download.

## Downloading using curl

This section describes how to download a `coverity-all-platforms-2026.6.0.tar.gz` file from the Black Duck repository using the `curl`
command. Download the file to a computer from which you can later upload to Coverity
Connect.

The `curl` command syntax to download a Coverity toolkit artifact (tar
file) from the Black Duck repository is:

```
curl https://repo.blackduck.com/​coverity-releases/{release}/{filename} -o {filename} -u {user:password}
```

where `user` and `password` are the credentials
available on your Software Licenses page of the Black Duck Community
website by clicking View/Request Docker Registry
Credentials.

Important: Do not change the
`coverity-all-platforms-<version>.tar.gz` file names.

For example, to download the Coverity toolkit artifact (tar file) for 2026.6.0:

```
curl https://repo.blackduck.com/coverity-releases/2026.6.0/coverity-all-platforms-2026.6.0.tar.gz
   -o coverity-all-platforms-2026.6.0.tar.gz -u <user:password>
```
