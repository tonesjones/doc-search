---
title: "token"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/token.html"
content_id: "wAt2xAQVxTCyUHRIMBh23g"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:30:10.545762+00:00"
---

# token

A single lexical unit in a tokenizedSourceFile.

## Properties

Every `token` has the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `text` | `string?` | The text of the token This property is `null` if the token has no text. |
| `location` | `sourceloc` | The location of the token in the tokenized source |
| `regex` | `regex` declaration | Specifies a regular expression (regex) that iterates over the text of the token and captures the matches that it finds. |

## **`regex` declaration**

The `regex` property takes the following form:

```
function(value : string) -> list<record> {
    fullMatch : string;
    location : sourceloc;
    captures : list<string>
}
```

Where ...

`value`
:   Is the regex to compare with matches in the token's content.

`fullMatch`
:   `fullmatch` is the fully matched text.

`sourceloc`
:   The location, in the token source, of the matched text.

`captures`
:   A list of the captures that were made.

    CAUTION:

    This list might be empty.

## Example

The following use of the `regex` property finds occurences of the string `"BUG"` inside of comments:

```
include `C/C++`;
                
checker {
    name = "BUG_IN_COMMENT";

    reports = for f in globalset allTokenizedSourceFiles :
        for token in f.tokens % commentToken:
            for bug in token.regex("\\<BUG\\>"): {
                events = [{
                    description = "Seen a BUG.";
                    location = bug.location;
                }]};
};
```
