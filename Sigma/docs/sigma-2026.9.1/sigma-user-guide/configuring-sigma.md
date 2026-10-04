---
title: "Configuring Sigma"
source_url: "https://docs.blackduck.com/r/sigma/2026.9.1/sigma-documentation/configuring-sigma.html"
content_id: "Xl8iDJakrSeDOXugDFeR8Q"
version: "2026.9.1"
section: "Sigma User Guide"
scraped_at: "2026-10-04T23:29:34.192913+00:00"
---

# Configuring Sigma

Sigma is configured to run out of the box, without alteration.

Sigma configuration
specifies information such as the following:

- The number of threads to use in running Sigma.
- The name and location of the policy file (if any).
- The location of the directory where you want to store temporary files.
- Which checks to disable.

Configuration options are either global or particular to the `sigma
analyze` command:

- Use a configuration file to change both global and `analyze`
  options.
- Use the `sigma analyze` command to change `analyze`
  options.
- Use environment variables to set both global and `analyze`
  options.
