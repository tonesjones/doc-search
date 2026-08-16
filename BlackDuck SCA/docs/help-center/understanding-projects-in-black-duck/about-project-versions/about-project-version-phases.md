---
title: "About project version phases"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/about-project-version-phases.html"
content_id: "xP0nbYmxe3Spv9srqUQygA"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:14:17.583998+00:00"
---

# About project version phases

Projects versions include a phase which you can use to manage your development projects
in Black Duck. Possible phase values are:

- In Planning: The *In Planning* phase is where the project solution is
  further developed in as much detail as possible and the steps necessary to meet
  the project’s objective are planned.
- In Development: The *In Development* phase is when the project plan is put
  into motion and the work of the project is performed.
- Pre-release: The *Pre-release* phase is when the project development has
  been completed and testing is underway.
- Released: The *Released* phase is when the project has officially progressed
  to general availability and the software product is ready to be delivered or has
  been delivered.
- Deprecated: The *Deprecated* phase is when the software has reached
  end-of-life and is no longer sold or supported. In this phase, the software
  might still be used by customers.
- Archived: The *Archived* phase is similar to the Deprecated phase, however
  the software is no longer available and customers are no longer utilizing it,
  having moved on to more recent releases.

Note: The definitions above serve only as examples. You can use the phases in any way to suit your
organization's software development life cycle steps.

You can select the phase when creating or editing a project version. By default, a project version is in the "In
Planning" phase.

Black Duck treats In Planning, In Development, Pre-release, Released, and Deprecated
project versions the same. Black Duck does not differentiate between these phases: these
phases are to help you manage your projects. Project versions with these phases are
included in project risk calculations.

Archived project versions are treated differently than the other project version
phases.

Note: You can "lock" a project version BOM against any component and license changes from Black Duck KnowledgeBase by select the archived phase, as described below.

## About archived project versions

You can modify archived project versions, as you would a project version in any other phase,
for example, modifying component usage and licenses.

However, archived project versions are treated differently than all other project
version phases.

- Archived project versions are excluded from project risk calculations.

  Project versions with any other phase are included in project risk
  calculations.
- If you enabled persistent edits:
  - Your edits made to a project version *are not* propagated to
    archived project versions.
  - Your edits made to an archived project version *are* propagated
    to all other non-archived project versions.

    Those edits *are
    not* applied to any other archived project version.
- Updates from Black Duck KnowledgeBase regarding security vulnerabilities
  *are* applied to archived project versions.

  Other updates from Black Duck KB, such as updates to license
  information, *are not* applied to archived project versions.
- New policy rules and updated expressions are not evaluated in archived project versions.
- Disabled and deleted policy rules violations will be removed from archived project
  versions.
