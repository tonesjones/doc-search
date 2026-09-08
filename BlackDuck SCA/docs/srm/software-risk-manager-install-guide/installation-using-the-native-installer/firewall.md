---
title: "Firewall"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/firewall.html"
content_id: "3OE3peTLSZ8nvcE~jVQvpw"
version: "latest"
section: "Software Risk Manager Install Guide"
scraped_at: "2026-09-08T20:04:56.357362+00:00"
content_hash: "17731a6fd847d1ddb6fda99fae766f36554bbad362a4850d99da33c9b148b0eb"
---

# Firewall

Software Risk Manager is a web application that requires a web server to house it. The
Apache web server is provided and configured automatically with the installer. However,
for most systems, this means that a firewall exception is necessary to allow incoming
connections over the network so that users (including you) can access the installation
from other machines. By default, the firewall ports that need to be opened up are 80 and
443, for HTTP and HTTPS respectively.

On Windows, you will be prompted with the following alert in order to grant the firewall
exception.

[image: image]

Note: The first time you use Software Risk Manager, you must log in using the
installer admin credentials. After that, you can change the admin's password within
Software Risk Manager; however, changing the password in Software Risk Manager does
**not** change the admin's password for the installer.
