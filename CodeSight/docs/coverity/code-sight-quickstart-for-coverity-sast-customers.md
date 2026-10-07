---
title: "Code Sight QuickStart for Coverity (SAST) customers"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/code-sight-quickstart-for-coverity-sast-customers.html"
content_id: "OwQeK2syECV25dBfhL5Jig"
version: "2026.9.0"
section: "Coverity with Code Sight"
scraped_at: "2026-10-06T23:39:52.368603+00:00"
---

# Code Sight QuickStart for Coverity (SAST) customers

Here is information to help you quickly get started using Code Sight, if you are a Coverity (SAST) customer.

All supported development environments can run Coverity (SAST): Eclipse, IntelliJ IDEA and other JetBrains IDEs,
Microsoft Visual Studio, and Microsoft Visual Studio Code.

## 1. If necessary, prepare the configuration

You might need to specify custom configuration settings if your development environment:

- Uses Coverity Connect
- Has a nonstandard compiler setup
- Requires customizing the behavior of Coverity Analysis or of Code Sight itself

For more information, see Setting up Coverity for Code Sight.

## 2. Install Code Sight on your own system

Black Duck Code Sight is available on the Marketplace site for the IDE that you use.

If you need more detailed information, see the installation instructions for that particular IDE:

- Installing Code Sight in IntelliJ
- Installing Code Sight in Eclipse
- Installing Code Sight in Visual Studio
- Installing Code Sight in Visual Studio Code

## 3. Authenticate Coverity

In the Coverity tile of the Products and Licenses panel,
click Enable Coverity.

[image: Products and Licenses panel displayed on startup]

Enable Coverity displays the authentication controls for Coverity.
For full details, see To authenticate Coverity within Code Sight.

## 4. Set up your server

You can run Coverity locally. If you do so and you configure a server, Code Sight
can download scan summaries, which optimize scan performance.
For more information, see Configuring a local scan engine.

Once you configure a server, scan summaries become available.
For more information, see Enhancing Single-File Scans with Central Scan Results.

You can also run Coverity remotely, and use Team View to view the issues Coverity has found.
For more information, see Configuring Code Sight to view remote Coverity issues.

If Coverity is already installed on your system, you are ready to run it.

If Coverity was not already installed, then click Install in the Coverity tile.

Figure 1. Authentication: Prompts to install Coverity and Rapid Scan Static
  
 [image: Authentication: Coverity and Rapid Scan Static installation]

You can also install Rapid Scan Static at this time.

Note:
Installing Rapid Scan Static runs fairly quickly.
Installing Coverity Analysis can take quite some time.

## 5. Start using Code Sight

For information about how Code Sight displays and manages Rapid Scan Static and Coverity results, see
Static Application Security Testing (SAST) overview.
