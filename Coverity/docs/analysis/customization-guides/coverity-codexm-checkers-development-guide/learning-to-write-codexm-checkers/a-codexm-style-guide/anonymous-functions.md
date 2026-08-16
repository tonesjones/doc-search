---
title: "Anonymous functions"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/anonymous-functions.html"
content_id: "DxQsQl8J1aYf5OtvLh3PHA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:26:54.944469+00:00"
---

# Anonymous functions

Try to keep anonymous, or lambda, functions to a single line.

The following code shows an example:

[image: CXM code follows]

```
let noNegatives = filter(function (a: int) -> a > 0, listType) in // ...
```

If the lambda function has to use several lines, use the following indentation style:

[image: CXM code follows]

```
let hasAcceptableValue =
    filter(
        function (a: int) ->
            switch (a) {
                | 1       -> true
                | 10      -> true
                | default -> false
            },
        listType
    )
in
    // ...
```
