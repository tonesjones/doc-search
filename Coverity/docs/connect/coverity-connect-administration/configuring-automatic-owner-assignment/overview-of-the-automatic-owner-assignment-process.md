---
title: "Overview of the automatic owner assignment process"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/overview-of-the-automatic-owner-assignment-process.html"
content_id: "N2KXwtqDm_SoLxr54tZDyA"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:50:29.091425+00:00"
---

# Overview of the automatic owner assignment process

The following steps provide an overview of the automatic owner assignment configuration
process, as well as pointers to specific configuration/implementation details:

1. Determine the method in which you want Coverity Connect to automatically assign
   owners:

   - **By retrieving SCM (Source Code Management) history
     to determine the assigned owner.**

     The SCM history consists of when, where, and by whom the code was changed and the
     assignment rules derive the owner of an issue based on the SCM history.
     Determining the owner using SCM data is accomplished by a combination of
     configuring Coverity Connect UI properties and Coverity Analysis command
     utilities. For a list of supported SCM tools, see "Coverity SCM
     support" in theCoverity 2026.6.0 Installation and Upgrade Guide. Test
     Advisor is no longer supported as of the 2021.9.0 release.

     There are two types of users that are referred to in this section:
     - SCM user - A user identity that modified or checked the code
       into the SCM system.
     - Coverity Connect user - A user identity that exists in the
       Coverity Connect database.
   - **By defining the default owner in a
     component.**

     This method uses the functionality associated with Coverity Connect
     components. If you choose this method, skip to Step 4.
   - **Alternatively, you can choose not to enable
     automatic owner assignment at all.**

   This allows organizations with multiple code bases to gradually transition to
   automatic owner assignment, one code base at a time and according to a schedule
   convenient to each development team.
2. If you are planning to use SCM data for owner assignment, define the global SCM
   derivations rule under the system configurations. See Setting global SCM rules and the SCM user map.
3. Configure the SCM to Coverity Connect user map file. See Configuring the SCM to Coverity Connect user map.
4. At the stream level, define the owner assignment rule. See Setting stream-level rules.

   If you configure owner assignment with SCM data, continue to the next step in
   this workflow.

   If you are using the component mechanism, or choose not to enable owner
   assignment, the remaining steps are not applicable.
5. Update your Coverity Analysis scripts(s)/commit process to include the SCM
   options to `cov-commit-defects`.

   If you are not already using the `cov-import-scm` command to
   retrieve SCM data, then you will need to add the `--scm` option
   (and other optional SCM-related options) for
   `cov-commit-defects`. For more information, see
   `cov-commit-defects`
   in the Coverity 2026.6.0 Command Reference.
6. Optionally test the results of different derivation rules without having to
   commit them to Coverity Connect by using the `cov-blame`
   command. For more information, see the `cov-blame`
   in the Coverity 2026.6.0 Command Reference.
