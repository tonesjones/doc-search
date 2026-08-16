---
title: "Dynamic variables"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/dynamic-variables.html"
content_id: "pUfA3KnAEAoJz4SeGFfLtA"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:49:50.654178+00:00"
---

# Dynamic variables

The following variables are supported in the Coverity Desktop UI:

- ${env_var:ANY_ENVIRONMENT_VARIABLE_NAME}
  - Substitutes corresponding environment variables.
- ${Solution} - Substitutes the solution folder names (where
  the solution is located) and the .cov subdirectory. This
  includes the trailing backslash. For example:

  c:\MySolution\.cov\
- ${SolutionRoot} - The full path to the solution folder,
  where the solution (.sln) file is located. This includes
  the trailing backslash '\'.
- ${cov-inter-dir} - The full path to intermediate directory.
  This includes the trailing backslash. For example:

  c:\Users\me\workspace\.metadata\coverity\server8080mycode\
- ${cov-im-user} - The Coverity Connect
  username.
- ${cov-im-password} - The Coverity Connect
  password.
- ${cov-im-host} - The Coverity Connect host
  name.
- ${cov-im-port} - The Coverity Connect data
  port. The default is 9090.
- ${cov-im-auth-key} - The full path to the Coverity Connect authentication key file.
- ${cov-sa-bin} - The full path of the Coverity Static
  analysis \bin directory. This includes the trailing
  backslash. For example:

  c:\<install_dir>\bin\
- ${active-build-configuration} - Expands to the selected
  Visual Studio configuration. Strips all whitespace and special characters, and
  all characters will be made lowercase. For example, `Debug`
  becomes `debug`.
- ${active-build-platform} - Expands to the selected Visual
  Studio platform. Strips all whitespace and special characters, and all
  characters will be made lowercase. For example, `Any CPU` becomes
  `anycpu`.
