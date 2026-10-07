---
title: "Additional port information"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/additional-port-information.html"
content_id: "mrN_~q2P8g9FkcVt2bgmow"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-10-04T23:32:24.042461+00:00"
content_hash: "b1ea701c8263a0d2d25897439b8c11a22280f4e95c7c287c3d91609ce0d7b0e5"
---

# Additional port information

The following list of ports cannot be blocked by firewall rules or by your Docker configuration. Examples of how these ports may be blocked include:

- The `iptable`s configuration on the host machine.
- A `firewalld` configuration on the host machine.
- External firewall configurations on another router/server on the network.
- Special Docker networking rules applied above and beyond what Docker creates by default, and also what Black Duck creates by default.

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
