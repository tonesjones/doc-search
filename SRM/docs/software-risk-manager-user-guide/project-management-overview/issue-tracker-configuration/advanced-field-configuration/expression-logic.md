---
title: "Expression Logic"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/expression-logic.html"
content_id: "R831n1yprX_pR3L7odKX3A"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:03:16.615672+00:00"
content_hash: "096cf2e29e0f687ac46842189846e121e2808bc84d6dc977497fc44fa50dbf67"
---

# Expression Logic

Most Handlebars expressions can be used. Some basic examples are given here, but much
more information is available in the Handlebars documentation. Specific sections of
interest are [Expressions](https://handlebarsjs.com/guide/expressions.html), [Block Helpers](https://handlebarsjs.com/guide/block-helpers.html), and [Built-in Helpers](https://handlebarsjs.com/guide/builtin-helpers.html).

## Boolean Expressions

You can add basic boolean logic to your expressions by using the helpers
`if`, `ifeq`, and `ifneq`. Note
that `ifeq` and `ifneq` are custom helpers provided by
Software Risk Manager.

- **If**

  ```
  {{#if finding.detection.isDast}}
  		This finding is a DAST finding.
  	{{else}}
  		This finding is not a DAST finding.
  	{{/if}}
  ```

  will
  result

  ```
  This finding is a DAST finding.
  ```

  when

  ```
  This finding is not a DAST finding.
  ```
- **ifeq** 

  The `ifeq` helper allows you to test the
  equality between two string or number values for a boolean result.
  Comparing values of types other than strings or numbers is unsupported,
  and the block will always evaluate to false.

  Note that
  `else` can not be used with `ifeq`;
  you may use `ifneq` instead to simulate
  `else`.

  ```
  {{#ifeq finding.statusName "New"}}
  		This finding is new
  	{{/ifeq}}
  ```

  will result
  in

  ```
  This finding is new.
  ```

  when
  a finding's status is new.
- **ifneq**

  The `ifneq` helper behaves the same way as
  `ifeq` except it negates the boolean result of
  testing the equality between two `string` or
  `number` values.

  ```
  {{#ifeq finding.severity.name "Critical"}}
  		This finding is critical
  	{{/ifeq}}

  	{{#ifneq finding.severity.name "Critical"}}
  		This finding is not critical
  	{{/ifneq}}
  ```

  will result
  in

  ```
  This finding is not critical.
  ```

  when
  a finding's severity is `not Critical`.

## Iterating Lists

You can iterate over arrays by using the [each helper](https://handlebarsjs.com/guide/builtin-helpers.html#each).

For example, the
expression

```
{{#each allFindings}}
	{{id}},
{{/each}}
```

will result in

```
1, 2, 3, 4,
```

when evaluated on a group of findings with the IDs of 1, 2, 3, and 4.

In this example, all Results of relevant Findings are iterated through and all
formatted Host Info and Variant Request and Response data is
returned

```
{{#each allFindings}}
	{{#each results}}
		{{{hostInfo.formattedHostInfo}}}
		{{#each variants}}
			Request:
				{{{request-data}}}
			Response:
				{{{response-data}}}
		{{/each}}
	{{/each}}
{{/each}}
```

Understanding and utilizing `{{#each}}` is important, because as you
can see in the above summary of the properties of the finding objects, many of the
properties are arrays and therefore can't simply be accessed directly—you need to
iterate over them and access each property inside the loop.
