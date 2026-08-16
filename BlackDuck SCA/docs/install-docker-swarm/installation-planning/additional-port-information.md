---
title: "Additional port information"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/additional-port-information.html"
content_id: "VKuyaSx58GJREU_E6HAA8w"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:33:34.009427+00:00"
---

# Additional port information

The following list of ports cannot be blocked by firewall rules or by your Docker
configuration. Examples of how these ports may be blocked include:

- The `iptable`s configuration on the host machine.
- A `firewalld` configuration on the host machine.
- External firewall configurations on another router/server on the network.
- Special Docker networking rules applied above and beyond what Docker creates by
  default, and also what Black Duck creates by default.

The complete list of ports that must remain unblocked is:

- 443
- 8443
- 8000
- 8888
- 8983
- 16543
- 17543
- 16545
- 16544
- 55436
