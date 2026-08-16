---
title: "Coverity glossary"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-glossary.html"
content_id: "r5O4YKem5xIzd7lC8saFZQ"
version: "2026.6"
section: "Coverity glossary"
scraped_at: "2026-08-12T03:20:26.256964+00:00"
---

# Coverity glossary

## A

### Abstract Syntax Tree (AST)

A tree-shaped data structure that represents the structure of concrete input syntax (from
source code).

### action

In Coverity Connect, a customizable attribute used to triage a CID. Default values are Undecided, Fix
Required, Fix Submitted, Modeling Required, and Ignore. Alternative custom values are
possible.

### Acyclic Path Count

The number of execution paths in a function, with loops counted one time at most. The
following assumptions are also made:

- `continue` breaks out of a loop.
- `while` and `for`  loops are executed exactly 0 or 1
  time.
- `do…while` loops are executed exactly once.
- `goto` statements which go to an earlier source location are treated
  as an exit.

Acyclic (Statement-only) Path Count adds the following assumptions:

- Paths within expressions are not counted.
- Multiple case labels at the same statement are counted as a single case.

### advanced triage

In Coverity Connect, streams that are associated with the same triage store always share the same triage data and
history. For example, if Stream A and Stream B are associated with Triage Store 1, and both
streams contain CID 123, the streams will share the triage values (such as a shared
Bug classification or a Fix Required action)
for that CID, regardless of whether the streams belong to the same project.

Advanced triage allows you to select one or more triage stores to update when triaging a CID in
a Coverity Connect project. Triage store selection is possible only if the following conditions
are true:

- Some streams in the project are associated with one triage store (for example, TS1), and
  other streams in the project are associated with another triage store (for example, TS2). In
  this case, some streams that are associated with TS1 must contain the CID that you are
  triaging, and some streams that are associated with TS2 must contain that CID.
- You have permission to triage issues in more than one of these triage stores.

In some cases, advanced triage can result in CIDs with issue attributes that are in the Various state in Coverity Connect.

See also triage.

### analysis annotation

A marker in the source code. An analysis annotation is not executable, but modifies
the behavior of Coverity Analysis in some way.

Analysis annotations can suppress false positives, indicate sensitive data, and enhance
function models.

Each language has its own analysis annotation syntax and set of capabilities. These are not the
same as the syntax or capabilities available to the other languages that support annotations.

- For C/C++, an analysis annotation is a comment with special formatting. See code-line annotation and function annotation.
- For C# and Visual Basic, an analysis annotation uses the native C# attribute syntax.
- For Java, an analysis annotation uses the native Java annotation syntax.

Other languages do not support annotations.

### annotation

See analysis annotation.

### Audit

A security level reported by certain Coverity checkers and by Rapid Scan Static scans.
The Audit level reports data-source or code patterns that might indicate an exploit, but where the evidence of a vulnerability is incomplete.

### AWS

Amazon Web Services (AWS) is an Amazon cloud hosting platform. Coverity can be
deployed within a customer VPC within AWS. Additionally, a Connect PostgreSQL database can be
implemented in AWS.

## C

### call graph

A graph in which functions are nodes, and the edges are the calls between the
functions.

### category

See issue category.

### checker

A program that traverses paths in your source code to find specific issues in it. Examples of
checkers include `RACE_CONDITION`, `RESOURCE_LEAK`,
and `INFINITE_LOOP`. For details about checkers, see Coverity 2026.6.0 Checker Reference.

### checker category

See issue category.

### churn

A measure of change in defect reporting between two Coverity Analysis releases that
are separated by one minor release, for example, 6.5.0 and 6.6.0.

### CID (Coverity identifier)

See Coverity identifier (CID).

### classification

A category that is assigned to a software issue in the database. Built-in
classification values are Unclassified, Pending, False Positive, Intentional, and Bug. For
Test Advisor issues, classifications include Untested, No Test Needed, and Tested Elsewhere.
Issues that are classified as Unclassified, Pending, and Bug are regarded as software issues
for the purpose of defect density calculations.

### code-line annotation

For C/C++, an analysis
annotation that applies to a particular line of code. When it encounters a
code-line annotation, the analysis engine skips the defect report that the following
line of code would otherwise trigger.

By default, an ignored defect is classified as `Intentional`. See "Annotations in C/C++" in Customizing Coverity.

See also function annotation.

### code base

A set of related source files.

### code coverage

The amount of code that is tested as a percentage of the total amount of code. Code
coverage is measured different ways: line coverage, path coverage, statement coverage,
decision coverage, condition coverage, and others.

### component

A named grouping of source code files. Components allow developers to view only issues in the
source files for which they are responsible, for example. In Coverity Connect, these files are specified by a Posix regular expression.
See also  component map.

### component map

Describes how to map source code files, and the issues contained in the source files,
into components.

### control flow graph

A graph in which blocks of code without any jumps or jump targets are nodes, and the
directed edges are the jumps in the control flow between the blocks. The entry block is where
control enters the graph, and the exit block is where the control flow leaves.

### Coverity Analysis

Coverity Analysis is a Coverity tool that analyzes customer software
for vulnerabilities, standards adherence, and other style or design constraints.

### Coverity Connect

A web application that allows developers and managers to identify, manage, and fix issues found
by Coverity Analysis and third-party tools. The analyses are
stored within the PostgreSQL database.

Coverity Connect for cloud deployment is nearly identical to Coverity Connect installed on-premises, with some extra commands to enable
operation within the cloud environment.

### Coverity Connect Administration Tools

A set of tools used to administer a Coverity instance. These consist of
"`cov-manage-im`", "`cov-archive`", and "`cov-admin-db`". Refer to
"Coverity tools in a Coverity
cloud deployment" in the Coverity 2026.6.0 Cloud Deployment Administrator and User Guide and to "Coverity Connect
commands" in the Coverity 2026.6.0 Command Reference.

### Coverity Connect Database

A PostgreSQL database that is used by Coverity Connect to store Coverity Analysis data. This PostgreSQL database must be DBaaS. Each cloud provider provides database
management tools. Coverity Connect must be configured to access the database.

### Coverity identifier (CID)

An identification number assigned to a software issue. A snapshot contains issue *instances*
(or occurrences), which take place on a specific code path in a specific version of a
file.

Issue instances, both within a snapshot and across snapshots
(even in different streams), are grouped together according to
similarity, with the intent that two issues are "similar" if the same source code change
would fix them both. These groups of similar issues are given a numeric identifier, the
CID.

Coverity Connect associates triage data, such as classification, action,
and severity, with the CID (rather than with an individual issue).

### CWE (Common Weakness Enumeration)

A community-developed list of software weaknesses, each of which is assigned a number
(for example, see CWE-476 at <http://cwe.mitre.org/data/definitions/476.html>).
Coverity associates many categories of defects (such as "Null pointer
dereferences") with a CWE number.

## D

### data directory

The directory that contains the Coverity Connect database. After
analysis, the `cov-commit-defects` command stores defects in this directory. You
can use Coverity Connect to view the defects in this directory. See also intermediate directory.

### deadcode

Code that cannot possibly be executed regardless of what input values are provided to
the program. The DEADCODE checker can find this code.

### defect

See issue.

### deterministic

A characteristic of a function or algorithm that, when given the same input, will
always give the same output.

### dismissed issue

Issue marked by developers as Intentional or False
Positive in the Triage pane. When such issues are no longer present in the
latest snapshot of the code base, they are identified as absent
dismissed.

### domain

A combination of the language that is being analyzed and the type of analysis, either
static or dynamic.

### dynamic analysis

Analysis of software code by executing the compiled program. See also static analysis.

## E

### event

In Coverity Connect, a software issue is composed of one or more events
found by the analysis. Events are useful in illuminating the context of the issue. See also
issue.

## F

### false negative

A defect in the source code that is not found by Coverity Analysis.

### false path pruning (FPP)

A technique to ensure that defects are only detected on feasible paths. For example,
if a particular path through a method ensures that a given condition is known to be true, then
the `else` branch of an `if` statement which tests that condition
cannot be reached on that path. Any defects found in the `else` branch would be
impossible because they are "on a false path". Such defects are suppressed by a false path
pruner.

### false positive

A potential defect that is identified by Coverity Analysis, but that
you decide is not a defect. In Coverity Connect, you can dismiss such issues as
false positives. In C or C++ source, you might also use  code-line annotations to identify such
issues as intentional during the source code analysis phase, prior to sending analysis results
to Coverity Connect.

### fixed issue

Issue from the previous snapshot that is
not in the latest snapshot.

### fixpoint

The Extend SDK engine notices that the second and subsequent paths through the loop
are not significantly different from the first iteration, and stops analyzing the loop. This
condition is called a fixpoint of the loop.

### flow-insensitive analysis

A checker that is stateless. The abstract syntax trees are not visited in any
particular order.

### function annotation

For C/C++, an  analysis annotation that
applies to the definition of a particular function. The annotation either suppresses or
enhances the effect of that function's model. See "Annotations in C/C++" in Customizing Coverity.

See also code-line annotation.

### function model

A model of a function that is not in the code base that enhances the intermediate
representation of the code base that Coverity Analysis uses to more
accurately analyze defects.

## G

### GCP

Google Cloud Platform (GCP) is a Google cloud hosting platform. Coverity can be deployed within a customer VPC within GCP. Additionally,
a Connect PostgreSQL database can be implemented in
GCP.

## H

### Helm

Helm is a package manager for Kubernetes. Helm deploys a Helm chart
which contains the equivalent of many Kubernetes YAML manifests. Helm simplifies the
deployment and management of Kubernetes applications. You can easily create and deploy
versions of a Helm chart, each containing a different set of configurations.

The Coverity cloud deployment configuration options which are used in a Helm
chart are listed in "Helm keys for
a Coverity Cloud deployment" in the Coverity 2026.6.0 Cloud Deployment Administrator and User Guide.

## I

### impact

Term that is intended to indicate the likely urgency of fixing the issue, primarily
considering its consequences for software quality and security, but also taking into account
the accuracy of the checker. Impact is necessarily probabilistic and subjective, so one should
not rely exclusively on it for prioritization.

### inspected issue

Issue that has been triaged or fixed by
developers.

### intermediate directory

A directory that is specified with the --dir option to many commands. The main
function of this directory is to write build and analysis results before they are committed to
the Coverity Connect database as a snapshot. Other more specialized commands that support the --dir
option also write data to or read data from this directory.

The intermediate representation of the build is stored in
<intermediate_directory>/emit directory, while the analysis results
are stored in <intermediate_directory>/output. This directory can
contain builds and analysis results for multiple languages.

See also data directory.

### intermediate representation

The output of the Coverity compiler, which Coverity Analysis uses to run its analysis and check for defects. The
intermediate representation of the code is in the intermediate directory.

### interprocedural analysis

An analysis for defects based on the interaction between functions. Coverity Analysis uses call graphs to perform this type of analysis. See also
intraprocedural analysis.

### intraprocedural analysis

An analysis for defects within a single procedure or function, as opposed to interprocedural analysis.

### issue

Coverity Connect displays three types of software issues: quality
defects, potential security vulnerabilities, and test policy violations. Some  checkers find both quality defects and potential security
vulnerabilities, while others focus primarily on one type of issue or another. The Quality,
Security, and Test Advisor dashboards in Coverity Connect provide high-level
metrics on each type of issue.

Note that this glossary includes additional entries for the various types of issues, for
example, an inspected issue, issue category, and so on.

### issue category

A string used to describe the nature of a software issue; sometimes called a "checker
category" or simply a "category." The issue pertains to a subcategory of software issue that a
checker can report within the context of a given domain.

Examples:

- `Memory - corruptions`
- `Incorrect expression`
- `Integer overflow Insecure data handling`

The "Software issues and impacts by
checker" and "Checker enablement and option defaults
by language dynamic tables in the
Coverity 2026.6.0 Checker Reference list issues found by checkers according to
their category and other associated checker properties.

## K

### killpath

For Coverity Analysis for C/C++, a path in a function that aborts
program execution. See
<install_dir>/library/generic/common/killpath.c for the functions
that are modeled in the system.

For Coverity Analysis for Java, and similarly for C# and Visual Basic, a
modeling primitive used to indicate that execution terminates at this point, which prevents the
analysis from continuing down this execution path. It can be used to model a native method that
kills the process, like `System.exit`, or to specifically identify an execution
path as invalid.

### kind

A string that indicates whether software issues found by a given checker pertain to
SECURITY (for security issues), QUALITY (for quality issues), TEST (for issues with developer
tests, which are found by Test Advisor), or QUALITY/SECURITY. Some checkers can report quality
and security issues. The Coverity Connect UI can use this property to filter and
display CIDs.

### Kubernetes

Kubernetes is a container orchestration system that automates the deployment, scaling,
and management of containerized software and the subsequent workloads and services.
Containers are automatically created and scaled to meet production needs.

## L

### latest state

A CID's state in the latest snapshot merged with its state from previous snapshots
starting with the snapshot in which its state was 'New'.

### local analysis

Interprocedural analysis on a subset of the code base with Coverity Desktop plugins, in contrast to one with Coverity Analysis, which usually takes place on a remote server.

### local effect

A string serving as a generic event message that explains why the checker reported a
defect. The message is based on a subcategory of software issues that the checker can detect.
Such strings appear in the Coverity Connect triage pane for a given CID.

Examples:

- `May result in a security violation.`
- `There may be a null pointer exception, or else the comparison against null is
  unnecessary.`

### long description

A string that provides an extended description of a software issue (compare with type). The long description appears in the Coverity Connect triage pane for a given CID. In Coverity Connect,
this description is followed by a link to a corresponding CWE, if available.

Examples:

- `The called function is unsafe for security related code.`
- `All paths that lead to this null pointer comparison already dereference the
  pointer earlier (CWE-476).`

## M

### model

In Coverity Analysis of the code for a compiled language - such as
C, C++, C#, Java, or Visual Basic - a model represents a function in the application source.
Models are used for interprocedural analysis.

Each model is created as each function is analyzed. The model is an abstraction of the
function’s behavior at execution time; for example, a model can show which arguments the
function dereferences, and whether the function returns a null value.

It is possible to write custom models for a code base. Custom models can help improve
Coverity's ability to detect certain kinds of bugs. Custom models can also
help reduce the incidence of false positives.

### modeling primitive

A modeling primitive is used when writing custom models. Each modeling primitive is a
function stub: It does not specify any executable code, but when it is used in a custom model it
instructs Coverity Analysis how to analyze (or refrain from analyzing) the
function being modeled.

For example, the C/C++ checker CHECKED_RETURN is associated with the modeling primitive `_coverity_always_check_return_()`. This primitive tells
CHECKED_RETURN to verify that the function being analyzed really does return a value.

Some modeling primitives are generic, but most are specific to a particular checker or group of
checkers. The set of available modeling primitives varies from language to language.

## N

### namespace

A namespace is needed to isolate the handling of resources specific to the Coverity
cloud deployment. Namespaces offer an additional layer of security and isolation from other
resources that the customer might want to run on the same cluster.

### native build

The normal build process in a software development environment that does not involve
Coverity products.

## O

### outstanding issue

Issues that are uninspected and
unresolved.

### outstanding defects count

The sum of security and non-security defects count.

### outstanding non-security defects count

The sum of non-security defects count.

### outstanding security defects count.

The sum of security defects count.

### owner

User name of the user to whom an issue has been assigned in Coverity Connect. Coverity Connect identifies the owner of issues
not yet assigned to a user as Unassigned.

## P

### PostgreSQL

The PostgreSQL database is used by Coverity Connect to store
Coverity Analysis data. The PostgreSQL database must be DBaaS.
Each cloud provider provides database management tools. Coverity Connect must
be configured to access the PostgreSQL database.

### postorder traversal

The recursive visiting of children of a given node in order, and then the visit to
the node itself. Left sides of assignments are evaluated after the assignment because the left
side becomes the value of the entire assignment expression.

### primitive

In the Java language, elemental data types such as strings and integers are known as
*primitive types*. (In the C-language family, such types are typically known as
*basic types)*.

For the function stubs that can be used when constructing custom models, see modeling primitive.

### project

In Coverity Connect, a specified set of related streams that provide a comprehensive view of issues in a code base.

## R

### resolved issues

Issues that have been fixed or marked by developers as
Intentional or False Positive through the Coverity Connect Triage pane.

### run

In Coverity releases 4.5.x or lower, a grouping of defects committed to
the Coverity Connect. Each time defects are inserted into the Coverity Connect using the `cov-commit-defects` command, a new run is
created, and the run ID is reported. See also snapshot.

## S

### sanitize

To clean or validate tainted data to ensure that the data is valid. Sanitizing
tainted data is an important aspect of secure coding practices to eliminate system crashes,
corruption, escalation of privileges, or denial of service. See also tainted data.

### severity

In Coverity Connect, a customizable property that can be assigned to
CIDs. Default values are Unspecified, Major, Moderate, and Minor. Severities are generally
used to specify how critical a defect is.

### sink

Coverity Analysis for C/C++: Any operation or function that must be
protected from tainted data. Examples are array subscripting, `system()`,
`malloc()`.

Coverity Analysis for Java: Any operation or function that must be protected
from tainted data. Examples are array subscripting and the JDBC API
`Connection.execute`.

### snapshot

A copy of the state of a code base at a certain point during development. Snapshots
help to isolate defects that developers introduce during development.

Snapshots contain the results of an analysis. A snapshot includes both the issue information
and the source code in which the issues were found. Coverity Connect allows you
to delete a snapshot in case you committed faulty data, or if you committed data for testing
purposes.

### snapshot scope

Determines the snapshots from which the CID are listed using the
Show and the optional Compared To fields. The show
and compare scope is only configurable in the Settings menu in
Issues:By Snapshot views and the snapshot information pane in the
Snapshots view.

### source

An entry point of untrusted data. Examples include environment variables, command
line arguments, incoming network data, and source code.

### static analysis

Analysis of software code without executing the compiled program. See also dynamic analysis.

### status

Describes the state of an issue. Takes one of the following values: `New`, `Triaged`, `Dismissed`, `Absent
Dismissed`, or `Fixed`.

### store

A map from abstract syntax trees to integer values and a sequence of events. This map
can be used to implement an abstract interpreter, used in flow-sensitive analysis.

### stream

A sequential collection of snapshots.
Streams can thereby provide information about software issues over time and at a particular
points in development process.

Attention:
Stream names are case sensitive. Coverity would treat `stream1` and `Stream1` as two distinct streams.

## T

### tainted data

Any data that comes to a program as input from a user. The program does not have
control over the values of the input, and so before using this data, the program must sanitize
the data to eliminate system crashes, corruption, escalation of privileges, or denial of
service. See also sanitize.

### translation unit

A translation unit is the smallest unit of code that can be compiled separately. What
this unit is, depends primarily on the language: For example, a Java translation unit is a
single source file, while a C or C++ translation unit is a source file plus all the other
files (such as headers) that the source file includes.

When Coverity tools capture code to analyze, the resulting intermediate
directory contains a collection of translation units. This collection includes source files
along with other files and information that form the context of the compilation. For example,
in Java this context includes bytecode files in the class path; in C or C++ this context
includes both preprocessor definitions and platform information about the compiler.

### triage

The process of setting the states of an issue in a particular stream, or of issues
that occur in multiple streams. These user-defined states reflect items such as how severe the
issue is, if it is an expected result (false positive), the action that should be taken for the
issue, to whom the issue is assigned, and so forth. These details provide tracking information
for your product. Coverity Connect provides a mechanism for you to update this
information for individual and multiple issues that exist across one or more streams.

See also advanced triage.

### triage store

A repository for the current and historical triage values of CIDs. In Coverity Connect, each stream must be associated with a single triage store so that
users can triage issues (instances of CIDs) found in the streams. Advanced triage allows you to
select one or more triage stores to update when triaging a CID in a Coverity Connect project.

See also advanced triage.

### type

A string that typically provides a short description of the root cause or potential effect of a
software issue. The description pertains to a subcategory of software issues that the
checker can find within the scope of a given domain. Such strings appear at the top of the Coverity Connect
triage pane, next to the CID that is associated with the issue. Compare with long description.

Examples:

```
The called function is unsafe for security related code
```

```
Dereference before null check
```

```
Out-of-bounds access
```

```
Evaluation order violation
```

The "Software issues and impacts by
checker" and "Checker enablement and option defaults
by language dynamic tables in the
Coverity 2026.6.0 Checker Reference list issues found by checkers according to
their category and other associated checker properties.

## U

### unified issue

An issue that is identical and present in multiple streams. Each instance of an
identical, unified issue shares the same CID.

### uninspected issues

Issues that are as yet unclassified in Coverity Connect because they
have not been triaged by developers.

### unresolved issues

Defects are marked by developers as Pending or
Bug through the Coverity Connect Triage pane. Coverity Connect sometimes refers to these issues as *Outstanding* issues.

## V

### various

Coverity Connect uses the term Various  in two
cases:

- When a checker is categorized as both a quality and a security checker. For example,
  USE_AFTER_FREE and UNINIT are listed
  as such in the Issue Kind  column of the View pane. For
  details, see the Coverity 2026.6.0 Checker Reference.
- When different instances of the same CID are triaged differently. Within the scope of a
  project, instances of a given CID that occur in separate streams can have different values for
  a given triage attribute if the streams are associated with different triage stores. For example, you might use advanced triage to classify a CID as a
  Bug in one triage store but retain the default
  Unclassified setting for the CID in another store. In such a case, the
  View pane of Coverity Connect identifies the project-wide classification of the
  CID as Various.

  Note: If all streams share a single triage store, you will never encounter a CID in this triage
  state.

### view

Saved searches for Coverity Connect data in a given project. Typically,
these searches are filtered. Coverity Connect displays this output in data
tables (located in the Coverity Connect View pane). The columns in these tables
can include CIDs, files, snapshots, checker names, dates, and many other types of data.

### VPC

A virtual private cloud (VPC) is a secure private cloud space that hosts company
specific or agency specific software, including the Kubernetes
cluster and the Coverity cloud deployment.

## C

## D

## E

## F

## K

## L

## M

## N

## O

### outstanding defects count

### outstanding non-security defects count

### outstanding security defects count.

## P

## R

### run

## S

## T

## U

## V
