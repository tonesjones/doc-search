---
title: "Terms and definitions for Polaris"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/terms-and-definitions-for-polaris.html"
content_id: "0GNiohnboRyuAGt7qtfaMA"
product_key: "polaris-platform-latest"
section: "Reference"
scraped_at: "2026-08-12T19:57:57.240324+00:00"
content_hash: "d49f62f7b9861f6af4d50fc4a110e2cbda1fab298877b49778c3c33aa34bacb3"
---

# Terms and definitions for Polaris

Application
:   A collection of up to five projects (depending on the subscription purchased) and up to 1 million lines of code. The application is the organizing principal in Polaris. Code projects have to be part of an application, and users are associated with one or more applications, where they're allowed to test and view results.

Application Admin
:   Manages access and settings for one or several application. The Application Admin lack access to some of an organization's applications. (Not to be confused with the Organization Application Manager, who can access all Applications and Projects.)

Audit Log
:   Tracks system changes from the user interface and APIs.

BDSA
:   Black Duck® Security Advisory. A feed of vulnerability reference numbers maintained by the Black Duck Cybersecurity Research Center (CyRC).

BOLA
:   Broken Object Level Authorization. An API security vulnerability in which an API fails to verify that a requesting user is authorized to access a specific object. This allows an attacker to access or manipulate data belonging to other users by substituting a different object ID in an API request.

Component origin
:   Where an open-source software component comes from, such as a repository or package manager.

Contributor
:   An application-level role that frequently scans code and triages issues.

CVE®
:   Common vulnerabilities and exposures. A system that provides reference numbers to publicly known information security vulnerabilities. Maintained by the National Cybersecurity FFRDC.

CWE™/SANS
:   Common weakness enumeration. A list of frequently occurring defects in software and hardware security, maintained by the National Cybersecurity FFRDC.

DAST
:   Dynamic application security testing. DAST describes solutions that test a target application for vulnerabilities while it's running, without knowledge of the application's architecture or source code.

Direct dependency
:   A direct dependency is a package your project requires to run and compile (typically, managed with package managers like pip, npm, ... etc.). It is possible for a package to be both a direct and transitive dependency.

Entitlement
:   The ability to use a specific type of test or set of tests with a particular subscription. The entitlements in a subscription control the types and quantities of tests a subscription can run.

Fix-by date
:   A date by which an issue must be fixed to comply with an organization's security policies.

Issue
:   Any defect or vulnerability in software. Usually used to describe issues detected by a test.

Issue Policy
:   A policy that automates actions when issues with specific properties are detected in a test, and can apply fix-by dates to issues detected in a test.

Match Score
:   Each component captured in a signature analysis test is compared with a copy of the component in the Black Duck KnowledgeBase™ to generate a (percentage) match score. A higher match score indicates a closer match, and a lower match score indicates a component was modified. Precise match scores only appear for components identified in signature analysis tests; the match score for a component identified in a package manager test will always be 100%.

Member
:   An application-level role that frequently scans code and triages issues. Contributors and members have similar permissions in Polaris, but members cannot create, update, or delete projects.

Observer
:   An application-level role able to review and monitor ongoing tests, test results, and issues in all projects belonging to the application, as well as view dashboards showing the status of the application and its projects.

Organization Admin
:   The user in your organization who has access to all the functions of Polaris and can access all the applications and projects. An Org Admin sets up your organization and invites other users to begin using Polaris. An organization must have at least one Org Admin.

Organization Application Manager
:   A user in your organization who can create, delete, and modify applications. The Organization Application manager has access to *all* applications and projects in an organization. (Not to be confused with the Application Admin, who owns one or several applications but might lack access to others.)

OWASP®
:   Open Web Application Security Project. A non-profit foundation that focuses on application security.

Portfolio
:   A portfolio contains all the applications owned by an organization. Every organization has exactly one portfolio.

Portfolio item
:   At present, the same as an *application*. In the future this could change, if portfolios begin to contain items other than applications (e.g. web apps, networks, etc.)

Portfolio subitem
:   At present, the same as a *project*. In the future this term could apply to other test targets, if portfolios begin to contain items other than applications, enclosing subitems other than projects.

Project
:   A project is a discrete body of code associated with a parent application. A project can contain the entire application or can be one submodule in a larger application. It might correspond to one repository, but doesn't have to. Each project includes a default branch, and may include more (non-default) branches. A test always runs on a single branch of a project (and issues captured in tests are linked to the branch and project).

SAST
:   Static application security testing. A solution that analyzes source code without executing it and finds security vulnerabilities. Coverity is one example a SAST tool.

SCA
:   Software composition analysis. SCA describes solutions that scan code and detect the presence of known software libraries written either by open-source projects or vendors. After scanning code, an SCA application helps to manage any security, quality, and license compliance risks associated with the libraries it discovered.

Subscription
:   A subscription is a license that allows an organization to run tests in Polaris. The entitlements in a subscription control the types and quantities of tests a subscription can run.

Test
:   Execution of a tool or the attempt to execute a tool in Polaris.

Test Scheduling Policy
:   A policy that automates tests of SCM-integrated projects or branches on a weekly or daily basis.

Transitive dependency
:   Transitive dependencies are packages that aren't directly referenced in your project, but rather, are packages that are referenced by your project's direct dependencies. It is possible for a package to be both a direct and transitive dependency.

Triage
:   Involves the decision to dismiss an issue, or not. When issues are dismissed by a member of your team, the potential reasons are False Positive, Intentional, and Other (requires an explanatory comment). You can use triage to manually set, change, or clear fix-by dates.
