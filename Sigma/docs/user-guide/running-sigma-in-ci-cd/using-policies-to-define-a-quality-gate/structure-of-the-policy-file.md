---
title: "Structure of the Policy File"
source_url: "https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/structure-of-the-policy-file.html"
content_id: "pPF0MtUZLXluZNKX~eX8JA"
version: "2026.8.0"
section: "Sigma User Guide"
scraped_at: "2026-08-13T00:25:27.315749+00:00"
---

# Structure of the Policy File

The basic structure of the file looks like this:

```
version: <VERSION_NUMBER>
policies:
	- <POLICY_RULE>
		...
	- <POLICY_RULE>
		...
	- <POLICY_RULE>
```

- The `VERSION_NUMBER` is the version of the policy file format.
- The `policies` field is a collection of policy rules.

A policy rule has the following structure:

```
- <POLICY_RULE>
	-> id: <UNIQUE_IDENTIFIER>
	|
	-> when: 
		|
		-> <WHEN_NODE>
	|
	-> result: 
		|
		-> <RESULT_NODE>
```

The `id` field identifies the policy rule. You can use whatever value you
prefer; it is treated as a string.
