---
title: "About Black Duck repositories"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/about-black-duck-repositories.html"
content_id: "tj_MDSEiQz2i1Sx0gka1EA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:40:32.471193+00:00"
---

# About Black Duck repositories

The Black Duck Docker registry contains repositories for the
various files needed for a Coverity cloud deployment. The following table identifies the
repositories and the files they contain.

Table 1. Black Duck repositories

| Repository | About |
| --- | --- |
| `repo.blackduck.com/containers/` | - Contains:   - Coverity cloud container images. - Private repository. Requires login credentials. - Access using `docker`   `pull` | `tag` |   `push` commands.  Note: In `docker`   commands, do not include `https://`. |
| `https://repo.blackduck.com/​coverity-releases/​2026.6.0/` | - Contains:   - Coverity toolkit (Thin Client) installer files.   - Full Coverity Analysis installer files.   - Host ID generate files   - Platform files   - Documentation files - Private repository. Requires login credentials. - Access using `curl` commands. |
| `https://repo.blackduck.com/cloudnative` | - Contains:   - Coverity cloud Helm chart. - Public repository. Does not require login credentials. - Access using a Web browser or `curl`   commands.   For information on Coverity installer files and documentation files, see Coverity client installer and documentation files. |
| `https://repo.blackduck.com/coverity-cloud/` | - Contains:   - Manifest file. - Public repository. Does not require login credentials. - Use curl commands. |

## Black Duck repository IP

All repository data has been migrated to the new Black Duck repository, `repo.blackduck.com`,
at 34.149.5.115. Make sure that you point to and use data from the public and
private repository folders within this new repository. See also .

## IP whitelist

If you use IP Whitelist to access `repo.blackduck.com`, add the
following IP address to the IP whitelist: 34.149.5.115. See also .
