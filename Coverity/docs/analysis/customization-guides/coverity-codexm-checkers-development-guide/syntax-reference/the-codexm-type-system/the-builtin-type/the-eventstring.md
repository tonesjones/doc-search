---
title: "The eventstring"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-eventstring.html"
content_id: "u2y05GXyUEnDIy4aMcWxqQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:28:00.252253+00:00"
---

# The eventstring

A string that has been formatted for output is known as an `eventstring`.

The following operations create an eventstring:

- Using the `+` operator to concatenate two or more string literals, or a combination of strings and eventstrings.
- Specifying a format property for a string value.

  These are the properties you can use to format a string:

  - `formattedAsBold`
  - `formattedAsCode`
  - `formattedAsEmphasized`
  - `formattedAsPre`
  - `formattedAsQuoted`

Concatenation is the only operation allowed on an eventstring object.
You cannot compare eventstrings in a Boolean expression.

To format a string, simply append the attribute to the string value. Here is an example:

[image: CXM code follows]

```
    let s = "Possible issue".formatedAsBold
```

CodeXM creates the eventstring by adding Markdown to the original string.

Typically you will use formatting properties with the `expression`
value output by a checker. For example, if your checker includes the following code:

[image: CXM code follows]

```
    // ...
        events = [
            {
                description = "found " + "error ".formattedAsBold;
                // ...
            }
        ];
    // ...
```

... then Coverity sends the following string to the output stream:

[image: Command output follows]

```
found *error*
```

... which in turn, on many systems will appear in the following form:

found **error**

CAUTION:

The formatting properties belong to objects of the type `string` and
*not* to objects of the type `eventstring`.
So if you assign `x`, for example, the result of concatenating two strings, the code
`let y = x.formattedAsEmphasized` generates an error because `x`, the result of a concatenation,
is an `eventstring`.
