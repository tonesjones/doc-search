---
title: "Deployment checklist"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/deployment-checklist.html"
content_id: "CpnYDOAkJVEtM2Gpt5Z3xw"
version: "2026.6"
section: "Coverity overview"
scraped_at: "2026-08-12T03:18:34.880471+00:00"
---

# Deployment checklist

The deployment checklist is a list of questions that helps you make decisions about how
you will deploy Coverity products (for example, which deployment models you will choose)
and what hardware you will choose.

When you are thinking about how you will deploy the tools, it is important to recognize
that one of the largest contributing factors to the performance of your system is based
on system load. System load consists of the following:

- Number of concurrent commits from Coverity Analysis to Coverity Connect - Commits
  represent the act of sending and processing the Coverity Analysis results and defect
  data from the intermediate directory to Coverity Connect. The number of and size of
  your commits can require a lot of hardware resources. The number of commits also
  increases the size of the database that Coverity Connect uses to store this
  information.

  The basic criteria for commit load is the number of issue
  instances that are committed per unit of time. This is determined by a number of
  factors, including the number of code bases, the size of each code base, the
  number of branches and configurations per code base, and how many of the code
  bases will be analyzed and how frequently.
- Number of concurrent users of Coverity Connect - The number of concurrent users on a
  Coverity Connect system can affect the performance of the user interface.
- Number of concurrent Coverity Connect Web Services API calls - The Web Services API
  allows you to write web applications that communicate with Coverity Connect. The
  number of concurrent Web Service calls on a Coverity Connect system can affect the
  performance of the user interface.
- Number of concurrent desktop users - Desktop users fit into the desktop deployment model
  and as such use both concurrent web services API calls and concurrent commits
  (although the size of the commits tends to be much smaller than in a central
  build).

Table 1. Deployment checklist

| Deployment considerations | Results/notes | More information |
| --- | --- | --- |
| **Questions regarding your organization's products** | | |
| What platforms do you develop and build on? |  | Consult the Supported platforms section of this guide to determine operating systems, versions, and required patches for Coverity products. |
| How many products do you have in your organization? |  | The number of products can determine the number of streams you that you commit, thereby impacting the commit load. |
| How many targets are typically built for each product? |  | Targets are for a given product can determine the number of streams you that you commit, thereby impacting the commit load. |
| How many lines of code are in your product? |  |  |
| **Questions regarding your organization's build process** | | |
| When will a build be generated |  | Are builds made on demand or integrated as part of an automated process? |
| How frequently are builds initiated? |  | The frequency of the builds in relation to the analysis integration contributes to commit load, and thus affects the way you plan for your hardware deployment. For more information, see . |
| What is the number of concurrent Coverity Analysis commits? |  | See Changing the number of concurrent commits. |
| How is the build command invoked? |  | Is it through a CI tool (such as Jenkins)? See Integration with Jenkins automated builds. |
| Do your developers develop on IDEs? |  | See the deployment descriptions for the desktop option. |
| **Questions regarding your organization's development process** | | |
| How many organizations or business units are using Coverity products? |  |  |
| How many developers are there in each organization or business unit? |  | The number of concurrent users will impact the performance of your system, particularly the Coverity Connect UI. Because of this, it is important to have an accurate number of users. Coverity has a list of maximum limits to help ensure optimum performance. If the number of users for your organization exceeds the limits, you could consider implementing one Coverity Connect deployment type over another. |
| How are your developers distributed geographically? |  | How developers in your organization distributed geographically? Do you want developers in other organizations to access a given Coverity Connect instance? You could consider implementing a Coverity Connect clustered environment. |
| Do you have a "clean before check-in" policy? |  | See the clean before check-in model. |
| Do you use a bug-tracking system? |  | See Export issues. |
| Do you have established standard back-up procedures? |  | See Backing up the database" in Coverity Platform 2026.6.0 User and Administrator Guide. |
| Do you have a system validation and monitoring plan? |  | See Monitoring and diagnosing Coverity Connect performance. |
| Do you plan on using the Coverity deployment maturity model? |  | See The Coverity deployment maturity model. |
