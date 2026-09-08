---
title: "Manage Software Risk Manager Services"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/manage-software-risk-manager-services.html"
content_id: "iNeOtXPRbzfOr_~KnJhhaQ"
version: "latest"
section: "Software Risk Manager Install Guide"
scraped_at: "2026-09-08T20:04:59.563870+00:00"
content_hash: "19a1832f08133216e4748384c4e52e308ffaa1d48aa3a99e27d20afa88071fec"
---

# Manage Software Risk Manager Services

The Software Risk Manager installer includes a graphical tool to manage services, which
can be found in the Software Risk Manager installation folder. For Windows, the tool is
called *manager-windows*; for Linux, it's *manager-linux-x64.run*.

Open the appropriate tool and go to the *Manage Servers* tab to view and change the
status of the services. To start, stop, or restart individual services, highlight the
service, then click the desired action (see the screenshot below). Use the buttons on
the bottom to change the status of all the services.

Alternatively, you can use the Windows Service Manager or the ctlscript shell files for
Linux to change the status of Software Risk Manager services. To start, stop, or restart
any Software Risk Manager services using ctlscript, navigate to the Software Risk
Manager installation folder and follow the examples below:

- Start individual services (you can replace "start" with "stop" or "restart"):
  - `./ctlscript.sh start tomcat`
  - `./ctlscript.sh start apache`
  - `./ctlscript.sh start mysql`
- Start, stop, or restart all services:
  - `./ctlscript.sh start`
  - `./ctlscript.sh stop`
  - `./ctlscript.sh restart`
- Obtain the current status of all services:

  - `./ctlscript.sh status`
