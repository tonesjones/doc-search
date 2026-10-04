---
title: "Creating a checker policy"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/creating-a-checker-policy.html"
content_id: "0FIW4lExzgmHBW5BIgGZOg"
version: "2026.9"
section: "Coverity Connect"
scraped_at: "2026-10-04T23:33:14.758965+00:00"
---

# Creating a checker policy

Create a checker policy by writing a YAML or JSON file that defines the analysis
settings a scan must satisfy.

A checker policy is a plain text file. You create it in any text editor and then
upload it to Coverity Connect. Before writing the file, decide whether the policy
applies to the entire Coverity Connect instance (global) or to a specific
project.

For the full list of supported policy keys and examples, see Checker policy file reference.

1. Decide the policy scope.
   - **Global** — applies to all projects in the Coverity Connect
     instance. Use this for organization-wide baseline requirements.
   - **Project** — applies to one specific project. Use this for
     project-specific requirements that extend or override the global
     baseline.
2. Create a new file with a .yaml,
   .yml, or .json extension.
3. Define at least one of the following top-level elements:

   - `versions` — to restrict which analysis versions are
     allowed
   - `require` — to specify the analysis settings the scan
     must include

   Both elements can appear in the same file.
4. Under `require.analyze`, define the requirements using one or
   more of the following approaches:

   - Predefined checker sets (for example,
     `cwe-top-25-2023`)
   - Coding standards (for example, `misrac20212`)
   - Individual checker enablement
   - `cov-analyze` argument sequences
   - Analysis settings
5. Verify that the file uses supported settings only and that the YAML or JSON
   syntax is valid.

   Coverity Connect validates the file at upload time and rejects files with
   unsupported settings or syntax errors.

After creating the policy file, upload it to Coverity Connect. See Setting the global checker policy or Assigning a checker policy to a project.
