---
title: "Getting started with Black Duck SCA"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/getting-started-with-black-duck-sca.html"
content_id: "D6r3a27Y0z8CjJsouKglew"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T14:53:25.455213+00:00"
---

# Getting started with Black Duck SCA

Black Duck offers a comprehensive suite of services and tools that
support customers on their security journey. From customers just starting with security,
to customers strengthening an established program, Black Duck has
the expertise, skills, and products necessary for success.

Black Duck, a Software Composition Analysis (SCA) tool, helps with managing the supply
chain of software, understanding the third-party components in use and minimizing risks
from known vulnerabilities and licensing. Black Duck is a comprehensive solution for
supply chain management, based primarily on source analysis.

Using Black Duck, you can:

- Scan your code and identify open source software that exists in your code
  base.
- View the generated Bill of Materials (BOM) for your software projects.
- View vulnerabilities that have been identified in open source components.
- Assess your security, license, and operational risk.

Protex users can use Black Duck to view and manage
security vulnerabilities in their existing BOMs.

## Logging in to Black Duck

Note: You must have a username and password to access Black Duck. Contact your
system administrator if you do not have a username. If Black Duck
is configured to use LDAP, you may be able to log in to Black Duck
using those credentials.

To log in to Black Duck:

1. Using a browser, navigate to the Black Duck URL supplied by
   your system administrator. Typically, the URL is in the format
   https://<server hostname>.
2. Enter the username and password provided by your Black Duck
   administrator. Your password is case sensitive.

   Note: If your administrator has enabled password requirements and your password does not meet the
   requirements, a dialog box appears notifying you that you must change your
   password. When updating your password, make sure that it meets the
   requirements, as listed in the dialog box. You will not be able to log in to
   Black Duck unless the password meets *all* requirements.
3. Click **Login**.

   When you log in, Black Duck displays your dashboard
   page.

   - For new installations of Black Duck, when you first
     log in after installing Black Duck, an empty
     Dashboard appears.

       
      [image: image]   

     For information to appear in Black Duck, you need
     to:

     - Scan your code and map it to a project.

       and/or
     - Import and map a Protex BOM.

     Once these tasks are complete, you can view the
     discovered components in the BOM and manage your security
     vulnerabilities.
   - For existing installations of Black Duck, if this is
     not the first time you are logging in to Black Duck, the dashboard page that appears depends on the last main
     dashboard (specific Dashboard page or Summary) you
     viewed previously.

     The Dashboard page has two default dashboards: the **Watching**
     and **My Projects** dashboards. You can also create
     custom dashboards so that you can quickly view the project versions,
     component versions, or security vulnerabilities that are important
     to you: search for projects, components, and/or security vulnerabilities then save the searches. Your saved searches appear on the
     Dashboard page.

Note: You will be locked out of your account for 10 minutes if you fail to enter the correct
password after 10 attempts. After the 10th failed attempt, a message appears on the
login page notifying you that your account is locked. Note that there is no defined
time period in which the 10 failed attempts must occur – any failed attempt will be
included in the count of failed password attempts. The count resets to 0 after you
successfully log in to Black Duck.

The permissions assigned to your Black Duck user account
by your system administrator determine which:

- navigation elements are visible to you on each page
- projects and project data you can view on each page
- actions you can perform inBlack Duck

## Seeing What's New in Black Duck

Discover the latest features and enhancements introduced in the current Black Duck
release with the new What's New window.

The What's New window will appear automatically after login, highlighting the most
impactful updates in this version. Users can choose to disable this window for
future logins, but it will reappear with the next Black Duck server
upgrade. Even after being dismissed, the What's New content can be accessed under
the Help menu.

From the What's New window, you can also select the desired Black Duck
version to see its highlights.

[image: What's New]

## Scanning your code and mapping scans to projects

Use these methods to scan your code:

- Detect Desktop which you can
  download from Black Duck's Tools page
- [Plugins](https://github.com/blackducksoftware).
- Black Duck Detect. Use Black Duck Detect for package management level
  analysis combined with signature scanning

After running a scan, browse the
available component scan results in Black Duck to view
the results of a component scan and the status of a scan that is in progress.

## Mapping scans to projects

After scanning your code, use Black Duck's UI to map your component scan if
you did not map the scan while scanning. Mapping connects your scan results to a
Black Duck project.

A *project* is the base unit in Black Duck. A project can
be both a stand-alone development project and part of another project. For
example, Apache Tomcat is a project in its own right but it may also be part of
other, larger projects. Projects can have multiple versions.

## Administrative tasks

Other tasks for administrators include:

- Managing users. Administrators need to create and manage users
  in Black Duck and assign roles.
- Managing
  groups. In addition to managing role assignments and project team
  membership at the individual user account level, administrators can manage
  these for multiple Black Duck users at the same time by
  creating a user group.

## Importing a Protex BOM

Use the Protex BOM tool to import a Protex BOM. Click
here for an overview of the process and here
for more information on using the Protex BOM tool.

## Scanning C and C++ projects

C and C++ projects lack a standardized package manager or method for handling dependencies. As
a result, generating an accurate bill of materials (or BOM) for these projects is more
challenging. Use the [C/CPP Tool](https://docs.blackduck.com/access?ft:originId=d7a4b1f5a86f212be27e594dc02681c4473766e2b2ad3db9123e8a92e34e44e2) to generate a BOM report for
projects written in C/C++ by building the project, capturing the source and binary
files involved, and then delivering a BDIO and signatures to Black Duck.
